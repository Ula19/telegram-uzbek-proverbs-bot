"""Доменный хэндлер — мақолы (узбекские пословицы)"""
import logging

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from bot.database import async_session
from bot.database.crud import (
    add_to_favorites,
    get_favorites,
    get_favorites_count,
    get_or_set_proverb_of_day,
    get_proverb_by_id,
    get_random_proverb,
    get_user_language,
    is_favorite,
    remove_from_favorites,
)
from bot.i18n import t
from bot.keyboards.inline import (
    get_back_keyboard,
    get_favorites_keyboard,
    get_proverb_keyboard,
)
from bot.services.proverbs import format_proverb, promo_footer

logger = logging.getLogger(__name__)
router = Router()


# === Случайный мақол ===

@router.callback_query(F.data == "random_proverb")
async def cb_random_proverb(callback: CallbackQuery) -> None:
    async with async_session() as session:
        lang = await get_user_language(session, callback.from_user.id)
        proverb = await get_random_proverb(session)
        if not proverb:
            await callback.answer(t("proverb.empty_db", lang), show_alert=True)
            return
        fav = await is_favorite(session, callback.from_user.id, proverb.id)

    header = t("proverb.random_title", lang)
    body = format_proverb(proverb, lang)
    text = f"{header}\n\n{body}{promo_footer(lang)}"
    try:
        await callback.message.edit_text(
            text,
            reply_markup=get_proverb_keyboard(proverb.id, fav, lang, show_more=True),
            parse_mode="HTML",
            disable_web_page_preview=True,
        )
    except Exception as e:
        # если редактировать не получилось (например, content тот же) — отправляем новое
        logger.warning("Не удалось отредактировать сообщение случайного мақола: %s", e)
        await callback.message.answer(
            text,
            reply_markup=get_proverb_keyboard(proverb.id, fav, lang, show_more=True),
            parse_mode="HTML",
            disable_web_page_preview=True,
        )
    await callback.answer()


# === Мақол дня ===

@router.callback_query(F.data == "proverb_of_day")
async def cb_proverb_of_day(callback: CallbackQuery) -> None:
    async with async_session() as session:
        lang = await get_user_language(session, callback.from_user.id)
        proverb = await get_or_set_proverb_of_day(session)
        if not proverb:
            await callback.answer(t("proverb.empty_db", lang), show_alert=True)
            return
        fav = await is_favorite(session, callback.from_user.id, proverb.id)

    header = t("proverb.day_title", lang)
    body = format_proverb(proverb, lang)
    text = f"{header}\n\n{body}{promo_footer(lang)}"
    try:
        await callback.message.edit_text(
            text,
            reply_markup=get_proverb_keyboard(proverb.id, fav, lang, show_more=False),
            parse_mode="HTML",
            disable_web_page_preview=True,
        )
    except Exception as e:
        logger.warning("Не удалось отредактировать сообщение мақола дня: %s", e)
        await callback.message.answer(
            text,
            reply_markup=get_proverb_keyboard(proverb.id, fav, lang, show_more=False),
            parse_mode="HTML",
            disable_web_page_preview=True,
        )
    await callback.answer()


# === Избранное: добавление/удаление ===

# Карточка мақола: контекст явно зашит в callback_data — fav_{add|del}_{random|day}_{id}
@router.callback_query(F.data.regexp(r"^fav_add_(random|day)_\d+$"))
async def cb_fav_add_ctx(callback: CallbackQuery) -> None:
    ctx, proverb_id = _parse_ctx_id(callback.data, "fav_add_")
    if proverb_id is None:
        await callback.answer()
        return
    async with async_session() as session:
        lang = await get_user_language(session, callback.from_user.id)
        added = await add_to_favorites(session, callback.from_user.id, proverb_id)
    await callback.answer(
        t("proverb.added_to_fav" if added else "proverb.already_in_fav", lang),
        show_alert=False,
    )
    await _refresh_proverb_keyboard(callback, proverb_id, in_fav=True, ctx=ctx)


@router.callback_query(F.data.regexp(r"^fav_del_(random|day)_\d+$"))
async def cb_fav_del_ctx(callback: CallbackQuery) -> None:
    ctx, proverb_id = _parse_ctx_id(callback.data, "fav_del_")
    if proverb_id is None:
        await callback.answer()
        return
    async with async_session() as session:
        lang = await get_user_language(session, callback.from_user.id)
        removed = await remove_from_favorites(session, callback.from_user.id, proverb_id)
    await callback.answer(
        t("proverb.removed_from_fav" if removed else "proverb.not_in_fav", lang),
        show_alert=False,
    )
    await _refresh_proverb_keyboard(callback, proverb_id, in_fav=False, ctx=ctx)


# Удаление из списка избранного (без контекста — перерисовывает страницу)
@router.callback_query(F.data.regexp(r"^fav_del_\d+$"))
async def cb_fav_del_from_list(callback: CallbackQuery) -> None:
    proverb_id = _parse_id(callback.data, "fav_del_")
    if proverb_id is None:
        await callback.answer()
        return
    async with async_session() as session:
        lang = await get_user_language(session, callback.from_user.id)
        removed = await remove_from_favorites(session, callback.from_user.id, proverb_id)
    await callback.answer(
        t("proverb.removed_from_fav" if removed else "proverb.not_in_fav", lang),
        show_alert=False,
    )
    # перерисовываем текущую страницу списка избранного
    await _show_favorites_page(callback, page=0)


async def _refresh_proverb_keyboard(
    callback: CallbackQuery, proverb_id: int, in_fav: bool, ctx: str
) -> None:
    """Обновить только клавиатуру под текущим сообщением (текст не трогаем).

    ctx — "random" (показывать «Ещё») или "day" (без кнопки «Ещё»).
    """
    async with async_session() as session:
        lang = await get_user_language(session, callback.from_user.id)
    show_more = ctx == "random"
    try:
        await callback.message.edit_reply_markup(
            reply_markup=get_proverb_keyboard(proverb_id, in_fav, lang, show_more=show_more)
        )
    except Exception as e:
        logger.warning("Не удалось обновить клавиатуру мақола: %s", e)


def _parse_ctx_id(data: str, prefix: str) -> tuple[str, int | None]:
    """Парсит callback_data вида '{prefix}{ctx}_{id}' → (ctx, id)."""
    try:
        tail = data[len(prefix):]
        ctx, raw_id = tail.split("_", 1)
        return ctx, int(raw_id)
    except (ValueError, IndexError):
        return "random", None


# === Избранное: список ===

PAGE_SIZE = 5


@router.callback_query(F.data == "my_favorites")
async def cb_my_favorites(callback: CallbackQuery) -> None:
    await _show_favorites_page(callback, page=0)


@router.callback_query(F.data.startswith("fav_page_"))
async def cb_fav_page(callback: CallbackQuery) -> None:
    page = _parse_id(callback.data, "fav_page_") or 0
    await _show_favorites_page(callback, page=page)


async def _show_favorites_page(callback: CallbackQuery, page: int) -> None:
    async with async_session() as session:
        lang = await get_user_language(session, callback.from_user.id)
        total = await get_favorites_count(session, callback.from_user.id)
        items = await get_favorites(
            session,
            callback.from_user.id,
            limit=PAGE_SIZE,
            offset=page * PAGE_SIZE,
        )
        # Если страница пустая, но в избранном что-то есть (например, удалили
        # последний элемент на текущей странице) — редиректим на последнюю.
        if not items and total > 0:
            page = max(0, (total - 1) // PAGE_SIZE)
            items = await get_favorites(
                session,
                callback.from_user.id,
                limit=PAGE_SIZE,
                offset=page * PAGE_SIZE,
            )

    if not items:
        await callback.message.edit_text(
            t("proverb.favorites_empty", lang),
            reply_markup=get_back_keyboard(lang),
            parse_mode="HTML",
        )
        await callback.answer()
        return

    header = t("proverb.favorites_title", lang, count=total)
    bodies = [format_proverb(p, lang) for p in items]
    text = header + "\n\n" + ("\n\n———\n\n".join(bodies))
    # клавиатура: пагинация + кнопки «убрать из избранного» по каждому ID
    kb = get_favorites_keyboard(
        items=[(p.id, p.text_latn) for p in items],
        page=page,
        total=total,
        page_size=PAGE_SIZE,
        lang=lang,
    )
    try:
        await callback.message.edit_text(
            text,
            reply_markup=kb,
            parse_mode="HTML",
            disable_web_page_preview=True,
        )
    except Exception as e:
        logger.warning("Не удалось отредактировать страницу избранного: %s", e)
        await callback.message.answer(
            text,
            reply_markup=kb,
            parse_mode="HTML",
            disable_web_page_preview=True,
        )
    await callback.answer()


# === Команды ===

@router.message(Command("random"))
async def cmd_random(message: Message) -> None:
    async with async_session() as session:
        lang = await get_user_language(session, message.from_user.id)
        proverb = await get_random_proverb(session)
        if not proverb:
            await message.answer(t("proverb.empty_db", lang))
            return
        fav = await is_favorite(session, message.from_user.id, proverb.id)
    await message.answer(
        f"{t('proverb.random_title', lang)}\n\n{format_proverb(proverb, lang)}{promo_footer(lang)}",
        reply_markup=get_proverb_keyboard(proverb.id, fav, lang, show_more=True),
        parse_mode="HTML",
        disable_web_page_preview=True,
    )


@router.message(Command("today"))
async def cmd_today(message: Message) -> None:
    async with async_session() as session:
        lang = await get_user_language(session, message.from_user.id)
        proverb = await get_or_set_proverb_of_day(session)
        if not proverb:
            await message.answer(t("proverb.empty_db", lang))
            return
        fav = await is_favorite(session, message.from_user.id, proverb.id)
    await message.answer(
        f"{t('proverb.day_title', lang)}\n\n{format_proverb(proverb, lang)}{promo_footer(lang)}",
        reply_markup=get_proverb_keyboard(proverb.id, fav, lang, show_more=False),
        parse_mode="HTML",
        disable_web_page_preview=True,
    )


@router.message(Command("favorites"))
async def cmd_favorites(message: Message) -> None:
    async with async_session() as session:
        lang = await get_user_language(session, message.from_user.id)
        total = await get_favorites_count(session, message.from_user.id)
        items = await get_favorites(session, message.from_user.id, limit=PAGE_SIZE, offset=0)
    if not items:
        await message.answer(t("proverb.favorites_empty", lang), reply_markup=get_back_keyboard(lang), parse_mode="HTML")
        return
    header = t("proverb.favorites_title", lang, count=total)
    bodies = [format_proverb(p, lang) for p in items]
    await message.answer(
        header + "\n\n" + ("\n\n———\n\n".join(bodies)),
        reply_markup=get_favorites_keyboard(
            items=[(p.id, p.text_latn) for p in items],
            page=0,
            total=total,
            page_size=PAGE_SIZE,
            lang=lang,
        ),
        parse_mode="HTML",
        disable_web_page_preview=True,
    )


# === utils ===

def _parse_id(data: str, prefix: str) -> int | None:
    try:
        return int(data[len(prefix):])
    except (ValueError, IndexError):
        return None
