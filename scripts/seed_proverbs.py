"""Seed-скрипт: загружает мақоллар из scripts/seed_proverbs.json в БД.

Использование:
    python -m scripts.seed_proverbs

Скрипт идемпотентный: если запись с таким text_latn уже есть — пропускает.
"""
import asyncio
import json
import logging
import sys
from pathlib import Path

from sqlalchemy import func, select

# Позволяет запускать через `python scripts/seed_proverbs.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from bot.database import async_session, engine  # noqa: E402
from bot.database.models import Base, Proverb  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

SEED_FILE = Path(__file__).parent / "seed_proverbs.json"


async def seed_if_empty() -> int:
    """Если таблица proverbs пуста — заливает мақоллар из seed_proverbs.json.

    Вызывается при старте бота. Возвращает кол-во добавленных записей (0 если БД не пуста).
    """
    async with async_session() as session:
        count = await session.scalar(select(func.count()).select_from(Proverb))
    if count and count > 0:
        logger.info("Таблица proverbs не пуста (%d записей) — seed пропущен", count)
        return 0
    added, _ = await _seed()
    return added


async def main() -> None:
    added, skipped = await _seed()
    logger.info("Готово. Добавлено: %d, пропущено: %d", added, skipped)


async def _seed() -> tuple[int, int]:
    if not SEED_FILE.exists():
        logger.error("Файл %s не найден", SEED_FILE)
        return 0, 0

    with open(SEED_FILE, encoding="utf-8") as f:
        items = json.load(f)
    logger.info("Загружено %d записей из JSON", len(items))

    # на всякий случай — создаём таблицы
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    added = 0
    skipped = 0
    async with async_session() as session:
        # один SELECT всех существующих text_latn
        res = await session.execute(select(Proverb.text_latn))
        existing = {row[0].strip().lower() for row in res.all() if row[0]}

        for item in items:
            text_latn = (item.get("text_latn") or "").strip()
            text_cyrl = (item.get("text_cyrl") or "").strip()
            source = (item.get("source") or "").strip()
            if not text_latn or not text_cyrl or not source:
                skipped += 1
                continue
            key = text_latn.lower()
            if key in existing:
                skipped += 1
                continue
            existing.add(key)

            session.add(Proverb(
                text_latn=text_latn,
                text_cyrl=text_cyrl,
                meaning_uz=item.get("meaning_uz"),
                translation_ru=item.get("translation_ru"),
                translation_en=item.get("translation_en"),
                equivalent_ru=item.get("equivalent_ru"),
                equivalent_en=item.get("equivalent_en"),
                source=source,
            ))
            added += 1
            # коммитим пачками по 200
            if added % 200 == 0:
                await session.commit()
                logger.info("  ... добавлено %d", added)

        await session.commit()

    return added, skipped


if __name__ == "__main__":
    asyncio.run(main())
