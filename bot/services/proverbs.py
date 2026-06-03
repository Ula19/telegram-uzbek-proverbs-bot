"""Доменный сервис — работа с мақолами: выбор и форматирование"""
from bot.config import settings
from bot.database.models import Proverb
from bot.emojis import E
from bot.i18n import t


def promo_footer(lang: str) -> str:
    """Рекламная подпись (самопромо) под одиночным мақолом.

    Возвращает пустую строку, если BOT_USERNAME не задан в .env —
    чтобы не показывать «@» без юзернейма.
    """
    username = (settings.bot_username or "").strip().lstrip("@")
    if not username:
        return ""
    return t("proverb.promo", lang, bot_username=username)


def format_proverb(proverb: Proverb, lang: str) -> str:
    """Отформатировать мақол для отображения юзеру.

    Всегда показываем оба варианта узбекского (латиница + кириллица).
    Затем, в зависимости от языка интерфейса:
      uz_latn / uz_cyrl → meaning_uz (если есть)
      ru                → translation_ru + equivalent_ru (если есть)
      en                → translation_en + equivalent_en (если есть)
    Источник — всегда внизу маленькими буквами.
    """
    parts: list[str] = []

    # 1. Узбекские варианты — всегда оба
    parts.append(f"<b>{_safe(proverb.text_latn)}</b>")
    parts.append(f"<i>{_safe(proverb.text_cyrl)}</i>")

    # 2. Толкование/переводы в зависимости от языка
    extras: list[tuple[str, str]] = []  # (label_key, value)

    if lang in ("uz_latn", "uz_cyrl"):
        if proverb.meaning_uz:
            extras.append(("proverb.label_meaning", proverb.meaning_uz))
    elif lang == "ru":
        if proverb.meaning_uz:
            extras.append(("proverb.label_meaning", proverb.meaning_uz))
        if proverb.translation_ru:
            extras.append(("proverb.label_translation", proverb.translation_ru))
        if proverb.equivalent_ru:
            extras.append(("proverb.label_equivalent", proverb.equivalent_ru))
    elif lang == "en":
        if proverb.meaning_uz:
            extras.append(("proverb.label_meaning", proverb.meaning_uz))
        if proverb.translation_en:
            extras.append(("proverb.label_translation", proverb.translation_en))
        if proverb.equivalent_en:
            extras.append(("proverb.label_equivalent", proverb.equivalent_en))

    if extras:
        parts.append("")  # пустая строка
    for label_key, value in extras:
        label = t(label_key, lang)
        parts.append(f"{E['pin']} <b>{label}:</b> {_safe(value)}")

    # 3. Источник снизу маленькими
    parts.append("")
    raw_src = (proverb.source or "").strip()
    src_label = t("proverb.label_source", lang)
    # ссылку рендерим только для безопасных http(s) схем
    if raw_src.startswith(("http://", "https://")):
        href = _safe_attr(raw_src)
        parts.append(f"<i><a href=\"{href}\">{src_label}</a></i>")
    elif raw_src:
        parts.append(f"<i>{src_label}: {_safe(raw_src)}</i>")
    else:
        parts.append(f"<i>{src_label}</i>")

    return "\n".join(parts)


def _safe(s: str | None) -> str:
    """Экранирование HTML-спецсимволов"""
    if not s:
        return ""
    return (
        s.replace("&", "&amp;")
         .replace("<", "&lt;")
         .replace(">", "&gt;")
    )


def _safe_attr(s: str | None) -> str:
    """Экранирование для использования внутри HTML-атрибута (href="...")."""
    return (
        _safe(s)
        .replace("\"", "&quot;")
        .replace("'", "&#39;")
    )
