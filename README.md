# Мақоллар

Telegram-бот — каталог узбекских народных пословиц (мақоллар) на латинице и кириллице.
У каждой пословицы указан источник. Фичи: случайный мақол, мақол дня, избранное.

## Стек

- Python 3.12
- aiogram 3.26
- PostgreSQL 16 + SQLAlchemy 2 + asyncpg
- Alembic (миграции)
- Docker Compose

## Быстрый старт

```bash
cp .env.example .env
# заполни BOT_TOKEN, BOT_USERNAME, DB_PASSWORD, ADMIN_IDS в .env
docker compose up -d
```

При первом запуске база автоматически заполняется мақолами из `scripts/seed_proverbs.json`.

## Структура

```
bot/
  main.py              # entrypoint + планировщик мақола дня
  config.py            # настройки из .env
  i18n.py              # переводы интерфейса ru/uz_latn/uz_cyrl/en
  emojis.py            # кастомные эмодзи
  database/            # модели, crud, подключение
  handlers/            # start, admin, proverbs
  middlewares/         # subscription, rate_limit
  keyboards/           # inline, admin
  services/            # proverbs (форматирование, промо)
  utils/               # commands (меню Telegram), tz (таймзона)
scripts/
  seed_proverbs.json   # база мақолов
  seed_proverbs.py     # скрипт заполнения базы
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

Ручное заполнение базы (если нужно перезалить):

```bash
python -m scripts.seed_proverbs
```
