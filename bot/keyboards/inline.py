"""Inline-клавиатуры — главное меню, подписка, язык, мақоллар"""
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.config import settings
from bot.emojis import E_ID
from bot.i18n import t


def get_start_keyboard(user_id: int, lang: str = "ru") -> InlineKeyboardMarkup:
    """Главное меню бота"""
    buttons = [
        [InlineKeyboardButton(
            text=t("btn.proverb_of_day", lang),
            callback_data="proverb_of_day",
            style="primary",
            icon_custom_emoji_id=E_ID["star"],
        )],
        [InlineKeyboardButton(
            text=t("btn.random_proverb", lang),
            callback_data="random_proverb",
            style="primary",
            icon_custom_emoji_id=E_ID["refresh"],
        )],
        [InlineKeyboardButton(
            text=t("btn.favorites", lang),
            callback_data="my_favorites",
            style="success",
            icon_custom_emoji_id=E_ID["heart"],
        )],
        [
            InlineKeyboardButton(
                text=t("btn.profile", lang),
                callback_data="my_profile",
                style="success",
                icon_custom_emoji_id=E_ID["profile"],
            ),
            InlineKeyboardButton(
                text=t("btn.help", lang),
                callback_data="help",
                style="success",
                icon_custom_emoji_id=E_ID["info"],
            ),
        ],
        [InlineKeyboardButton(
            text=t("btn.language", lang),
            callback_data="change_language",
            style="success",
            icon_custom_emoji_id=E_ID["gear"],
        )],
    ]

    if user_id in settings.admin_id_list:
        buttons.append([InlineKeyboardButton(
            text=t("btn.admin_panel", lang),
            callback_data="admin_panel",
            style="danger",
            icon_custom_emoji_id=E_ID["lock"],
        )])

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_back_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    """Кнопка 'Назад' в главное меню"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text=t("btn.back", lang),
            callback_data="back_to_menu",
            style="success",
            icon_custom_emoji_id=E_ID["back"],
        )],
    ])


def get_subscription_keyboard(
    channels: list[dict], lang: str = "ru"
) -> InlineKeyboardMarkup:
    buttons = []
    for ch in channels:
        buttons.append([InlineKeyboardButton(
            text=f"{ch['title']}",
            url=ch["invite_link"],
            style="primary",
            icon_custom_emoji_id=E_ID["megaphone"],
        )])
    buttons.append([InlineKeyboardButton(
        text=t("btn.check_sub", lang),
        callback_data="check_subscription",
        style="success",
        icon_custom_emoji_id=E_ID["check"],
    )])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_language_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Русский",
                callback_data="set_lang_ru",
                style="primary",
                icon_custom_emoji_id=E_ID["flag_ru"],
            ),
            InlineKeyboardButton(
                text="English",
                callback_data="set_lang_en",
                style="primary",
                icon_custom_emoji_id=E_ID["flag_gb"],
            ),
        ],
        [
            InlineKeyboardButton(
                text="O'zbek (lotin)",
                callback_data="set_lang_uz_latn",
                style="primary",
                icon_custom_emoji_id=E_ID["flag_uz"],
            ),
            InlineKeyboardButton(
                text="Ўзбек (кирилл)",
                callback_data="set_lang_uz_cyrl",
                style="primary",
                icon_custom_emoji_id=E_ID["flag_uz"],
            ),
        ],
    ])


# === Клавиатуры мақолов ===

def get_proverb_keyboard(
    proverb_id: int, in_fav: bool, lang: str = "ru", show_more: bool = True,
) -> InlineKeyboardMarkup:
    """Клавиатура под мақолом: [Ещё/В/из избранного] [Назад].

    Контекст передаётся явно в callback_data:
      show_more=True  → контекст "random"
      show_more=False → контекст "day"
    Это нужно, чтобы при перерисовке клавиатуры после fav_add/fav_del
    мы знали, показывать ли кнопку «Ещё».
    """
    ctx = "random" if show_more else "day"
    buttons = []

    if show_more:
        buttons.append([InlineKeyboardButton(
            text=t("btn.more_proverb", lang),
            callback_data="random_proverb",
            style="primary",
            icon_custom_emoji_id=E_ID["refresh"],
        )])

    if in_fav:
        buttons.append([InlineKeyboardButton(
            text=t("btn.remove_fav", lang),
            callback_data=f"fav_del_{ctx}_{proverb_id}",
            style="danger",
            icon_custom_emoji_id=E_ID["trash"],
        )])
    else:
        buttons.append([InlineKeyboardButton(
            text=t("btn.add_fav", lang),
            callback_data=f"fav_add_{ctx}_{proverb_id}",
            style="success",
            icon_custom_emoji_id=E_ID["heart"],
        )])

    buttons.append([InlineKeyboardButton(
        text=t("btn.back", lang),
        callback_data="back_to_menu",
        style="success",
        icon_custom_emoji_id=E_ID["back"],
    )])

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_favorites_keyboard(
    items: list[tuple[int, str]],
    page: int,
    total: int,
    page_size: int,
    lang: str = "ru",
) -> InlineKeyboardMarkup:
    """Клавиатура списка избранного.

    items — список (proverb_id, text_latn) на текущей странице.
    Кнопки: для каждой записи «Убрать» + пагинация Назад/Вперёд + В меню.
    """
    buttons: list[list[InlineKeyboardButton]] = []

    # Кнопки удаления — короткая подпись с обрезанным текстом
    for proverb_id, preview in items:
        short = preview.strip().replace("\n", " ")
        if len(short) > 30:
            short = short[:27] + "..."
        buttons.append([InlineKeyboardButton(
            text=f"{t('btn.remove_short', lang)} «{short}»",
            callback_data=f"fav_del_{proverb_id}",
            style="danger",
            icon_custom_emoji_id=E_ID["trash"],
        )])

    # Пагинация
    nav_row: list[InlineKeyboardButton] = []
    if page > 0:
        nav_row.append(InlineKeyboardButton(
            text=t("btn.prev_page", lang),
            callback_data=f"fav_page_{page - 1}",
            style="success",
            icon_custom_emoji_id=E_ID["back"],
        ))
    if (page + 1) * page_size < total:
        nav_row.append(InlineKeyboardButton(
            text=t("btn.next_page", lang),
            callback_data=f"fav_page_{page + 1}",
            style="success",
            icon_custom_emoji_id=E_ID["refresh"],
        ))
    if nav_row:
        buttons.append(nav_row)

    buttons.append([InlineKeyboardButton(
        text=t("btn.back", lang),
        callback_data="back_to_menu",
        style="success",
        icon_custom_emoji_id=E_ID["back"],
    )])

    return InlineKeyboardMarkup(inline_keyboard=buttons)
