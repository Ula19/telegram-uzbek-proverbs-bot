"""CRUD операции с базой данных"""
import random as _random
from datetime import date as date_t, datetime, timezone

from sqlalchemy import delete, func as sa_func, select
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.ext.asyncio import AsyncSession

from bot.database.models import Channel, Favorite, Proverb, ProverbOfDay, User
from bot.utils.tz import TASHKENT_TZ


# === User ===

async def get_or_create_user(
    session: AsyncSession,
    telegram_id: int,
    username: str | None,
    full_name: str,
    language: str | None = None,
) -> User:
    """Получить юзера или создать нового"""
    result = await session.execute(
        select(User).where(User.telegram_id == telegram_id)
    )
    user = result.scalar_one_or_none()

    if user is None:
        user = User(
            telegram_id=telegram_id,
            username=username,
            full_name=full_name,
            language=language or "ru",
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)

    return user


async def get_user_language(session: AsyncSession, telegram_id: int) -> str:
    """Получить язык юзера (по умолчанию ru)"""
    result = await session.execute(
        select(User.language).where(User.telegram_id == telegram_id)
    )
    lang = result.scalar_one_or_none()
    return lang or "ru"


async def update_user_language(
    session: AsyncSession, telegram_id: int, language: str
) -> None:
    """Обновить язык юзера"""
    result = await session.execute(
        select(User).where(User.telegram_id == telegram_id)
    )
    user = result.scalar_one_or_none()
    if user:
        user.language = language
        await session.commit()


# === Channel ===

async def get_active_channels(session: AsyncSession) -> list[Channel]:
    """Получить все каналы для обязательной подписки"""
    result = await session.execute(select(Channel))
    return list(result.scalars().all())


async def add_channel(
    session: AsyncSession,
    channel_id: int,
    title: str,
    invite_link: str,
) -> Channel:
    """Добавить канал для обязательной подписки"""
    result = await session.execute(
        select(Channel).where(Channel.channel_id == channel_id)
    )
    existing = result.scalar_one_or_none()
    if existing:
        raise ValueError(f"Канал {channel_id} уже добавлен")

    channel = Channel(
        channel_id=channel_id,
        title=title,
        invite_link=invite_link,
    )
    session.add(channel)
    await session.commit()
    await session.refresh(channel)
    return channel


async def remove_channel(session: AsyncSession, channel_id: int) -> bool:
    """Удалить канал. Возвращает True если удалён"""
    result = await session.execute(
        select(Channel).where(Channel.channel_id == channel_id)
    )
    channel = result.scalar_one_or_none()
    if not channel:
        return False

    await session.delete(channel)
    await session.commit()
    return True


# === Статистика ===

async def get_user_stats(session: AsyncSession) -> dict:
    """Статистика бота"""
    total = await session.execute(select(sa_func.count(User.id)))
    total_users = total.scalar() or 0

    today = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    today_result = await session.execute(
        select(sa_func.count(User.id)).where(User.created_at >= today)
    )
    today_users = today_result.scalar() or 0

    channels = await session.execute(select(sa_func.count(Channel.id)))
    total_channels = channels.scalar() or 0

    proverbs = await session.execute(select(sa_func.count(Proverb.id)))
    total_proverbs = proverbs.scalar() or 0

    return {
        "total_users": total_users,
        "today_users": today_users,
        "total_proverbs": total_proverbs,
        "total_channels": total_channels,
    }


async def get_all_user_ids(session: AsyncSession) -> list[int]:
    """Получить все telegram_id юзеров для рассылки"""
    result = await session.execute(select(User.telegram_id))
    return [row[0] for row in result.all()]


# === Proverb ===

async def get_proverb_by_id(session: AsyncSession, proverb_id: int) -> Proverb | None:
    """Получить мақол по ID"""
    result = await session.execute(select(Proverb).where(Proverb.id == proverb_id))
    return result.scalar_one_or_none()


async def get_random_proverb(session: AsyncSession) -> Proverb | None:
    """Случайный мақол через COUNT + OFFSET (быстрее ORDER BY RANDOM() на больших таблицах)."""
    count = await session.scalar(select(sa_func.count(Proverb.id)))
    if not count:
        return None
    offset = _random.randint(0, count - 1)
    result = await session.execute(
        select(Proverb).offset(offset).limit(1)
    )
    return result.scalar_one_or_none()


async def count_proverbs(session: AsyncSession) -> int:
    """Количество мақолов в БД"""
    result = await session.execute(select(sa_func.count(Proverb.id)))
    return result.scalar() or 0


# === ProverbOfDay ===

def _today_tashkent() -> date_t:
    """Текущая дата по Ташкенту (UTC+5)"""
    return datetime.now(TASHKENT_TZ).date()


async def get_or_set_proverb_of_day(session: AsyncSession) -> Proverb | None:
    """Получить мақол дня. Если на сегодня нет — выбрать случайный и сохранить.

    Реализовано через PostgreSQL INSERT ... ON CONFLICT DO NOTHING RETURNING,
    что исключает гонку между параллельными воркерами.
    """
    today = _today_tashkent()
    # 1. Уже есть запись на сегодня?
    res = await session.execute(
        select(ProverbOfDay).where(ProverbOfDay.day == today)
    )
    pod = res.scalar_one_or_none()
    if pod:
        return await get_proverb_by_id(session, pod.proverb_id)

    # 2. Нет — выбираем случайный
    proverb = await get_random_proverb(session)
    if not proverb:
        return None

    # 3. Атомарная попытка вставки. Если другой воркер уже вставил — RETURNING пуст.
    stmt = (
        pg_insert(ProverbOfDay)
        .values(day=today, proverb_id=proverb.id)
        .on_conflict_do_nothing(index_elements=["day"])
        .returning(ProverbOfDay.proverb_id)
    )
    res = await session.execute(stmt)
    inserted_id = res.scalar_one_or_none()
    await session.commit()

    if inserted_id is not None:
        return proverb

    # 4. Кто-то успел раньше — читаем чужой выбор
    res = await session.execute(
        select(ProverbOfDay).where(ProverbOfDay.day == today)
    )
    pod = res.scalar_one_or_none()
    if pod:
        return await get_proverb_by_id(session, pod.proverb_id)
    return None


# === Favorite ===

async def add_to_favorites(
    session: AsyncSession, telegram_id: int, proverb_id: int
) -> bool:
    """Добавить в избранное. True — добавлено, False — уже было"""
    res = await session.execute(
        select(Favorite).where(
            Favorite.telegram_id == telegram_id,
            Favorite.proverb_id == proverb_id,
        )
    )
    if res.scalar_one_or_none():
        return False
    fav = Favorite(telegram_id=telegram_id, proverb_id=proverb_id)
    session.add(fav)
    try:
        await session.commit()
        return True
    except Exception:
        await session.rollback()
        return False


async def remove_from_favorites(
    session: AsyncSession, telegram_id: int, proverb_id: int
) -> bool:
    """Убрать из избранного. True — удалено"""
    res = await session.execute(
        delete(Favorite).where(
            Favorite.telegram_id == telegram_id,
            Favorite.proverb_id == proverb_id,
        )
    )
    await session.commit()
    return (res.rowcount or 0) > 0


async def is_favorite(
    session: AsyncSession, telegram_id: int, proverb_id: int
) -> bool:
    """Проверка: мақол уже в избранном у юзера?"""
    res = await session.execute(
        select(Favorite.id).where(
            Favorite.telegram_id == telegram_id,
            Favorite.proverb_id == proverb_id,
        )
    )
    return res.scalar_one_or_none() is not None


async def get_favorites(
    session: AsyncSession, telegram_id: int, limit: int = 10, offset: int = 0
) -> list[Proverb]:
    """Список избранных мақолов юзера (пагинация)"""
    res = await session.execute(
        select(Proverb)
        .join(Favorite, Favorite.proverb_id == Proverb.id)
        .where(Favorite.telegram_id == telegram_id)
        .order_by(Favorite.created_at.desc())
        .limit(limit)
        .offset(offset)
    )
    return list(res.scalars().all())


async def get_favorites_count(session: AsyncSession, telegram_id: int) -> int:
    """Количество избранных мақолов у юзера"""
    res = await session.execute(
        select(sa_func.count(Favorite.id)).where(Favorite.telegram_id == telegram_id)
    )
    return res.scalar() or 0
