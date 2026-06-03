"""Утилита для установки персонального меню команд юзеру"""
import logging

from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat

from bot.i18n import t

logger = logging.getLogger(__name__)

# список команд в нужном порядке
MENU_COMMANDS = ["start", "menu", "random", "today", "favorites", "profile", "help", "language"]


async def set_user_commands(bot: Bot, user_id: int, lang: str) -> None:
    """Устанавливает персональное меню команд для конкретного юзера на его языке"""
    commands = [
        BotCommand(command=cmd, description=t(f"cmd.{cmd}", lang))
        for cmd in MENU_COMMANDS
    ]
    try:
        await bot.set_my_commands(
            commands=commands,
            scope=BotCommandScopeChat(chat_id=user_id),
        )
    except Exception as e:
        # не критично — просто логируем
        logger.warning("Не удалось установить команды для %s: %s", user_id, e)


async def set_default_commands(bot: Bot) -> None:
    """Устанавливает глобальные команды для каждого языка.
    Telegram сам покажет их юзеру, основываясь на языке его приложения,
    ЕЩЁ ДО ТОГО как юзер нажмёт /start.

    Для uz_latn и uz_cyrl используем uz — Telegram не поддерживает суффиксы.
    """
    # Стандартные коды языков Telegram → наши коды
    lang_map = {
        "ru": "ru",
        "en": "en",
        "uz": "uz_latn",  # узбекский в Telegram → показываем латиницу
    }
    for tg_lang, our_lang in lang_map.items():
        commands = [
            BotCommand(command=cmd, description=t(f"cmd.{cmd}", our_lang))
            for cmd in MENU_COMMANDS
        ]
        await bot.set_my_commands(commands=commands, language_code=tg_lang)

    # Резервный дефолт (например, для немецкого → английский)
    fallback = [
        BotCommand(command=cmd, description=t(f"cmd.{cmd}", "en"))
        for cmd in MENU_COMMANDS
    ]
    await bot.set_my_commands(commands=fallback)
