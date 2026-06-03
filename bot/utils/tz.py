"""Единый источник правды для таймзоны проекта."""
from datetime import timedelta, timezone

# Ташкент — UTC+5 (без перехода на летнее время)
TASHKENT_TZ = timezone(timedelta(hours=5))
