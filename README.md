# bot_4_proverbs — Мақоллар

Telegram-бот с каталогом узбекских пословиц (мақоллар).
Переводы и объяснения на русском, узбекском (латиница + кириллица) и английском.

## Стек

- Python 3.12
- aiogram 3.26
- PostgreSQL 16 + SQLAlchemy 2 + asyncpg
- Alembic (миграции)
- Docker Compose

## Быстрый старт

```bash
cp .env.example .env
# заполни BOT_TOKEN, DB_PASSWORD, ADMIN_IDS в .env
docker compose up -d
```

## Структура

```
bot/
  main.py              # entrypoint
  config.py            # настройки из .env
  i18n.py              # переводы ru/uz_latn/uz_cyrl/en
  emojis.py            # кастомные эмодзи
  database/            # модели, crud, подключение
  handlers/            # start, admin, __todo_proverbs
  middlewares/         # subscription, rate_limit
  keyboards/           # inline, admin
  services/            # __todo_proverbs (доменная логика)
  utils/               # commands (меню Telegram)
```

## Локальная разработка

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# заполни .env, запусти PostgreSQL
python -m bot.main
```
