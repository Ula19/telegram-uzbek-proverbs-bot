"""Мультиязычность — русский, узбекский (латиница), узбекский (кириллица), английский
Использование: from bot.i18n import t
  t("start.welcome", lang="uz_latn", name="Alisher")

Коды языков:
  "ru"      — русский
  "uz_latn" — узбекский латиница
  "uz_cyrl" — узбекский кириллица
  "en"      — английский
"""

from bot.emojis import E

TRANSLATIONS = {
    # === /start ===
    "start.welcome": {
        "ru": (
            f"{E['bot']} <b>Привет, {{name}}!</b>\n\n"
            f"{E['book']} Я — бот узбекских пословиц (мақоллар).\n\n"
            f"{E['pin']} Здесь ты найдёшь мудрость народа,\n"
            "переведённую и объяснённую на трёх языках.\n\n"
            "Выбери действие ниже:"
        ),
        "uz_latn": (
            f"{E['bot']} <b>Salom, {{name}}!</b>\n\n"
            f"{E['book']} Men — o'zbek maqollar botiman.\n\n"
            f"{E['pin']} Bu yerda xalq donishmandligini\n"
            "uch tilda tarjima va izoh bilan topasiz.\n\n"
            "Quyidagi tugmalardan birini tanlang:"
        ),
        "uz_cyrl": (
            f"{E['bot']} <b>Салом, {{name}}!</b>\n\n"
            f"{E['book']} Мен — ўзбек мақоллар ботиман.\n\n"
            f"{E['pin']} Бу ерда халқ донишмандлигини\n"
            "уч тилда таржима ва изоҳ билан топасиз.\n\n"
            "Қуйидаги тугмалардан бирини танланг:"
        ),
        "en": (
            f"{E['bot']} <b>Hello, {{name}}!</b>\n\n"
            f"{E['book']} I am a bot for Uzbek proverbs (maqollar).\n\n"
            f"{E['pin']} Here you'll find the wisdom of the people,\n"
            "translated and explained in three languages.\n\n"
            "Choose an action below:"
        ),
    },

    # === Кнопки главного меню ===
    "btn.random_proverb": {
        "ru": "Случайный мақол",
        "uz_latn": "Tasodifiy maqol",
        "uz_cyrl": "Тасодифий мақол",
        "en": "Random proverb",
    },
    "btn.proverb_of_day": {
        "ru": "Мақол дня",
        "uz_latn": "Kunning maqoli",
        "uz_cyrl": "Куннинг мақоли",
        "en": "Proverb of the day",
    },
    "btn.favorites": {
        "ru": "Избранное",
        "uz_latn": "Sevimlilar",
        "uz_cyrl": "Севимлилар",
        "en": "Favorites",
    },
    "btn.profile": {
        "ru": "Мой профиль",
        "uz_latn": "Mening profilim",
        "uz_cyrl": "Менинг профилим",
        "en": "My profile",
    },
    "btn.help": {
        "ru": "Помощь",
        "uz_latn": "Yordam",
        "uz_cyrl": "Ёрдам",
        "en": "Help",
    },
    "btn.back": {
        "ru": "Назад",
        "uz_latn": "Orqaga",
        "uz_cyrl": "Орқага",
        "en": "Back",
    },
    "btn.language": {
        "ru": "Сменить язык",
        "uz_latn": "Tilni o'zgartirish",
        "uz_cyrl": "Тилни ўзгартириш",
        "en": "Change language",
    },
    "btn.check_sub": {
        "ru": "Проверить подписку",
        "uz_latn": "Obunani tekshirish",
        "uz_cyrl": "Обунани текшириш",
        "en": "Check subscription",
    },

    # === Профиль ===
    "profile.title": {
        "ru": (
            f"{E['profile']} <b>Твой профиль</b>\n\n"
            f"{E['edit']} Имя: {{full_name}}\n"
            f"{E['info']} ID: <code>{{user_id}}</code>\n"
            f"{E['star']} Избранных мақолов: {{favorites_count}}\n"
        ),
        "uz_latn": (
            f"{E['profile']} <b>Sizning profilingiz</b>\n\n"
            f"{E['edit']} Ism: {{full_name}}\n"
            f"{E['info']} ID: <code>{{user_id}}</code>\n"
            f"{E['star']} Sevimli maqollar: {{favorites_count}}\n"
        ),
        "uz_cyrl": (
            f"{E['profile']} <b>Сизнинг профилингиз</b>\n\n"
            f"{E['edit']} Исм: {{full_name}}\n"
            f"{E['info']} ID: <code>{{user_id}}</code>\n"
            f"{E['star']} Севимли мақоллар: {{favorites_count}}\n"
        ),
        "en": (
            f"{E['profile']} <b>Your profile</b>\n\n"
            f"{E['edit']} Name: {{full_name}}\n"
            f"{E['info']} ID: <code>{{user_id}}</code>\n"
            f"{E['star']} Favorite proverbs: {{favorites_count}}\n"
        ),
    },

    # === Помощь ===
    "help.text": {
        "ru": (
            f"{E['book']} <b>Помощь</b>\n\n"
            f"{E['star']} Получай случайный мақол нажатием кнопки\n"
            f"{E['star']} Мақол дня меняется каждые сутки\n"
            f"{E['star']} Сохраняй понравившиеся мақолы в избранное\n"
            f"{E['star']} Интерфейс доступен на 4 языках\n\n"
            f"{E['plane']} По вопросам: @{{admin_username}}"
        ),
        "uz_latn": (
            f"{E['book']} <b>Yordam</b>\n\n"
            f"{E['star']} Tugma orqali tasodifiy maqol oling\n"
            f"{E['star']} Kunning maqoli har 24 soatda yangilanadi\n"
            f"{E['star']} Yoqqan maqollarni sevimlilarga saqlang\n"
            f"{E['star']} Interfeys 4 tilda mavjud\n\n"
            f"{E['plane']} Savollar uchun: @{{admin_username}}"
        ),
        "uz_cyrl": (
            f"{E['book']} <b>Ёрдам</b>\n\n"
            f"{E['star']} Тугма орқали тасодифий мақол олинг\n"
            f"{E['star']} Куннинг мақоли ҳар 24 соатда янгиланади\n"
            f"{E['star']} Ёққан мақолларни севимлиларга сақланг\n"
            f"{E['star']} Интерфейс 4 тилда мавжуд\n\n"
            f"{E['plane']} Саволлар учун: @{{admin_username}}"
        ),
        "en": (
            f"{E['book']} <b>Help</b>\n\n"
            f"{E['star']} Get a random proverb by pressing the button\n"
            f"{E['star']} Proverb of the day changes every 24 hours\n"
            f"{E['star']} Save favorite proverbs to your collection\n"
            f"{E['star']} Interface available in 4 languages\n\n"
            f"{E['plane']} Contact: @{{admin_username}}"
        ),
    },

    # === Подписка ===
    "sub.welcome": {
        "ru": (
            f"{E['bot']} <b>Привет!</b>\n\n"
            f"{E['book']} Этот бот — каталог узбекских пословиц "
            "с переводом и объяснением!\n\n"
            f"{E['lock']} <b>Для начала подпишись на каналы ниже:</b>\n\n"
            f"После подписки нажми «{E['check']} Проверить подписку»"
        ),
        "uz_latn": (
            f"{E['bot']} <b>Salom!</b>\n\n"
            f"{E['book']} Bu bot — tarjima va izohlari bilan "
            "o'zbek maqollar katalogi!\n\n"
            f"{E['lock']} <b>Boshlash uchun quyidagi kanallarga obuna bo'ling:</b>\n\n"
            f"Obuna bo'lgandan keyin «{E['check']} Obunani tekshirish» tugmasini bosing"
        ),
        "uz_cyrl": (
            f"{E['bot']} <b>Салом!</b>\n\n"
            f"{E['book']} Бу бот — таржима ва изоҳлари билан "
            "ўзбек мақоллар каталоги!\n\n"
            f"{E['lock']} <b>Бошлаш учун қуйидаги каналларга обуна бўлинг:</b>\n\n"
            f"Обуна бўлгандан кейин «{E['check']} Обунани текшириш» тугмасини босинг"
        ),
        "en": (
            f"{E['bot']} <b>Hello!</b>\n\n"
            f"{E['book']} This bot is a catalog of Uzbek proverbs "
            "with translations and explanations!\n\n"
            f"{E['lock']} <b>To start, subscribe to the channels below:</b>\n\n"
            f"After subscribing, tap «{E['check']} Check subscription»"
        ),
    },
    "sub.not_subscribed": {
        "ru": (
            f"{E['cross']} <b>Ты ещё не подписался на все каналы:</b>\n\n"
            f"Подпишись и нажми «{E['check']} Проверить подписку» ещё раз."
        ),
        "uz_latn": (
            f"{E['cross']} <b>Siz hali barcha kanallarga obuna bo'lmadingiz:</b>\n\n"
            f"Obuna bo'ling va «{E['check']} Obunani tekshirish» tugmasini qayta bosing."
        ),
        "uz_cyrl": (
            f"{E['cross']} <b>Сиз ҳали барча каналларга обуна бўлмадингиз:</b>\n\n"
            f"Обуна бўлинг ва «{E['check']} Обунани текшириш» тугмасини қайта босинг."
        ),
        "en": (
            f"{E['cross']} <b>You haven't subscribed to all channels yet:</b>\n\n"
            f"Subscribe and tap «{E['check']} Check subscription» again."
        ),
    },
    "sub.success": {
        "ru": (
            f"{E['check']} <b>Отлично, {{name}}!</b>\n\n"
            f"Теперь ты можешь пользоваться ботом! {E['book']}\n\n"
            "Выбери действие ниже:"
        ),
        "uz_latn": (
            f"{E['check']} <b>Ajoyib, {{name}}!</b>\n\n"
            f"Endi siz botdan foydalanishingiz mumkin! {E['book']}\n\n"
            "Quyidagi tugmalardan birini tanlang:"
        ),
        "uz_cyrl": (
            f"{E['check']} <b>Ажойиб, {{name}}!</b>\n\n"
            f"Энди сиз ботдан фойдаланишингиз мумкин! {E['book']}\n\n"
            "Қуйидаги тугмалардан бирини танланг:"
        ),
        "en": (
            f"{E['check']} <b>Great, {{name}}!</b>\n\n"
            f"You can now use the bot! {E['book']}\n\n"
            "Choose an action below:"
        ),
    },
    "sub.check_alert_fail": {
        "ru": f"{E['cross']} Подпишись на все каналы!",
        "uz_latn": f"{E['cross']} Barcha kanallarga obuna bo'ling!",
        "uz_cyrl": f"{E['cross']} Барча каналларга обуна бўлинг!",
        "en": f"{E['cross']} Subscribe to all channels!",
    },
    "sub.check_alert_ok": {
        "ru": f"{E['check']} Подписка подтверждена!",
        "uz_latn": f"{E['check']} Obuna tasdiqlandi!",
        "uz_cyrl": f"{E['check']} Обуна тасдиқланди!",
        "en": f"{E['check']} Subscription confirmed!",
    },
    "sub.not_required": {
        "ru": f"{E['check']} Подписка не требуется!",
        "uz_latn": f"{E['check']} Obuna talab qilinmaydi!",
        "uz_cyrl": f"{E['check']} Обуна талаб қилинмайди!",
        "en": f"{E['check']} No subscription required!",
    },

    # === Ошибки ===
    "error.generic": {
        "ru": f"{E['cross']} <b>Что-то пошло не так</b>\n\nПопробуй позже.",
        "uz_latn": f"{E['cross']} <b>Nimadir noto'g'ri ketdi</b>\n\nKeyinroq urinib ko'ring.",
        "uz_cyrl": f"{E['cross']} <b>Нимадир нотўғри кетди</b>\n\nКейинроқ уриниб кўринг.",
        "en": f"{E['cross']} <b>Something went wrong</b>\n\nPlease try again later.",
    },
    "error.rate_limit": {
        "ru": f"{E['clock']} <b>Слишком много запросов!</b>\n\nПодожди {{seconds}} секунд и попробуй снова.",
        "uz_latn": f"{E['clock']} <b>Juda ko'p so'rovlar!</b>\n\n{{seconds}} soniya kuting va qayta urinib ko'ring.",
        "uz_cyrl": f"{E['clock']} <b>Жуда кўп сўровлар!</b>\n\n{{seconds}} сония кутинг ва қайта уриниб кўринг.",
        "en": f"{E['clock']} <b>Too many requests!</b>\n\nWait {{seconds}} seconds and try again.",
    },
    "error.not_found": {
        "ru": f"{E['cross']} <b>Не найдено</b>\n\nПопробуй ещё раз.",
        "uz_latn": f"{E['cross']} <b>Topilmadi</b>\n\nQayta urinib ko'ring.",
        "uz_cyrl": f"{E['cross']} <b>Топилмади</b>\n\nҚайта уриниб кўринг.",
        "en": f"{E['cross']} <b>Not found</b>\n\nPlease try again.",
    },

    # === Выбор языка ===
    "lang.choose": {
        "ru": f"{E['gear']} <b>Выберите язык интерфейса:</b>",
        "uz_latn": f"{E['gear']} <b>Interfeys tilini tanlang:</b>",
        "uz_cyrl": f"{E['gear']} <b>Интерфейс тилини танланг:</b>",
        "en": f"{E['gear']} <b>Choose interface language:</b>",
    },
    "lang.changed": {
        "ru": f"{E['check']} Язык изменён на русский",
        "uz_latn": f"{E['check']} Til o'zbek tiliga (lotin) o'zgartirildi",
        "uz_cyrl": f"{E['check']} Тил ўзбек тилига (кирилл) ўзгартирилди",
        "en": f"{E['check']} Language changed to English",
    },

    # === Мақоллар ===
    "proverb.random_title": {
        "ru": f"{E['refresh']} <b>Случайный мақол</b>",
        "uz_latn": f"{E['refresh']} <b>Tasodifiy maqol</b>",
        "uz_cyrl": f"{E['refresh']} <b>Тасодифий мақол</b>",
        "en": f"{E['refresh']} <b>Random proverb</b>",
    },
    "proverb.day_title": {
        "ru": f"{E['star']} <b>Мақол дня</b>",
        "uz_latn": f"{E['star']} <b>Kunning maqoli</b>",
        "uz_cyrl": f"{E['star']} <b>Куннинг мақоли</b>",
        "en": f"{E['star']} <b>Proverb of the day</b>",
    },
    # Рекламная подпись под одиночным мақолом (самопромо бота)
    "proverb.promo": {
        "ru": f"\n\n{E['book']} Мақоллар каждый день — @{{bot_username}}",
        "uz_latn": f"\n\n{E['book']} Har kuni yangi maqollar — @{{bot_username}}",
        "uz_cyrl": f"\n\n{E['book']} Ҳар куни янги мақоллар — @{{bot_username}}",
        "en": f"\n\n{E['book']} Daily proverbs — @{{bot_username}}",
    },
    "proverb.label_meaning": {
        "ru": "Толкование",
        "uz_latn": "Ma'nosi",
        "uz_cyrl": "Маъноси",
        "en": "Meaning",
    },
    "proverb.label_translation": {
        "ru": "Перевод",
        "uz_latn": "Tarjima",
        "uz_cyrl": "Таржима",
        "en": "Translation",
    },
    "proverb.label_equivalent": {
        "ru": "Аналог",
        "uz_latn": "Muqobil",
        "uz_cyrl": "Муқобил",
        "en": "Equivalent",
    },
    "proverb.label_source": {
        "ru": "Источник",
        "uz_latn": "Manba",
        "uz_cyrl": "Манба",
        "en": "Source",
    },
    "proverb.added_to_fav": {
        "ru": f"{E['check']} Добавлено в избранное",
        "uz_latn": f"{E['check']} Sevimlilarga qo'shildi",
        "uz_cyrl": f"{E['check']} Севимлиларга қўшилди",
        "en": f"{E['check']} Added to favorites",
    },
    "proverb.already_in_fav": {
        "ru": f"{E['info']} Уже в избранном",
        "uz_latn": f"{E['info']} Allaqachon sevimlilarda",
        "uz_cyrl": f"{E['info']} Аллақачон севимлиларда",
        "en": f"{E['info']} Already in favorites",
    },
    "proverb.removed_from_fav": {
        "ru": f"{E['check']} Удалено из избранного",
        "uz_latn": f"{E['check']} Sevimlilardan olindi",
        "uz_cyrl": f"{E['check']} Севимлилардан олинди",
        "en": f"{E['check']} Removed from favorites",
    },
    "proverb.not_in_fav": {
        "ru": f"{E['info']} Этого мақола нет в избранном",
        "uz_latn": f"{E['info']} Bu maqol sevimlilarda yo'q",
        "uz_cyrl": f"{E['info']} Бу мақол севимлиларда йўқ",
        "en": f"{E['info']} This proverb is not in favorites",
    },
    "proverb.favorites_empty": {
        "ru": (
            f"{E['star']} <b>Избранное пусто</b>\n\n"
            f"Открой случайный мақол и нажми «{E['star']} В избранное», "
            "чтобы сохранить понравившиеся."
        ),
        "uz_latn": (
            f"{E['star']} <b>Sevimlilar bo'sh</b>\n\n"
            f"Tasodifiy maqolni oching va yoqqanlarini saqlash uchun "
            f"«{E['star']} Sevimlilarga» tugmasini bosing."
        ),
        "uz_cyrl": (
            f"{E['star']} <b>Севимлилар бўш</b>\n\n"
            f"Тасодифий мақолни очинг ва ёққанларини сақлаш учун "
            f"«{E['star']} Севимлиларга» тугмасини босинг."
        ),
        "en": (
            f"{E['star']} <b>Favorites are empty</b>\n\n"
            f"Open a random proverb and tap «{E['star']} Add to favorites» "
            "to save the ones you like."
        ),
    },
    "proverb.favorites_title": {
        "ru": f"{E['star']} <b>Ваше избранное</b> ({{count}})",
        "uz_latn": f"{E['star']} <b>Sevimlilaringiz</b> ({{count}})",
        "uz_cyrl": f"{E['star']} <b>Севимлиларингиз</b> ({{count}})",
        "en": f"{E['star']} <b>Your favorites</b> ({{count}})",
    },
    "proverb.empty_db": {
        "ru": f"{E['cross']} В базе пока нет мақолов. Запустите seed-скрипт.",
        "uz_latn": f"{E['cross']} Bazada hali maqollar yo'q. Seed-skriptni ishga tushiring.",
        "uz_cyrl": f"{E['cross']} Базада ҳали мақоллар йўқ. Seed-скриптни ишга туширинг.",
        "en": f"{E['cross']} No proverbs in the database yet. Run the seed script.",
    },

    # === Кнопки доменные ===
    "btn.more_proverb": {
        "ru": "Ещё один мақол",
        "uz_latn": "Yana bir maqol",
        "uz_cyrl": "Яна бир мақол",
        "en": "Another proverb",
    },
    "btn.add_fav": {
        "ru": "В избранное",
        "uz_latn": "Sevimlilarga",
        "uz_cyrl": "Севимлиларга",
        "en": "Add to favorites",
    },
    "btn.remove_fav": {
        "ru": "Убрать из избранного",
        "uz_latn": "Sevimlilardan olish",
        "uz_cyrl": "Севимлилардан олиш",
        "en": "Remove from favorites",
    },
    "btn.remove_short": {
        "ru": "Убрать",
        "uz_latn": "Olish",
        "uz_cyrl": "Олиш",
        "en": "Remove",
    },
    "btn.prev_page": {
        "ru": "Назад",
        "uz_latn": "Oldingi",
        "uz_cyrl": "Олдинги",
        "en": "Previous",
    },
    "btn.next_page": {
        "ru": "Вперёд",
        "uz_latn": "Keyingi",
        "uz_cyrl": "Кейинги",
        "en": "Next",
    },

    # === Команды доменные ===
    "cmd.random": {
        "ru": "Случайный мақол",
        "uz_latn": "Tasodifiy maqol",
        "uz_cyrl": "Тасодифий мақол",
        "en": "Random proverb",
    },
    "cmd.today": {
        "ru": "Мақол дня",
        "uz_latn": "Kunning maqoli",
        "uz_cyrl": "Куннинг мақоли",
        "en": "Proverb of the day",
    },
    "cmd.favorites": {
        "ru": "Избранное",
        "uz_latn": "Sevimlilar",
        "uz_cyrl": "Севимлилар",
        "en": "Favorites",
    },

    # === Админ-панель ===
    "admin.title": {
        "ru": f"{E['gear']} <b>Админ-панель</b>\n\nВыбери действие:",
        "uz_latn": f"{E['gear']} <b>Admin panel</b>\n\nAmalni tanlang:",
        "uz_cyrl": f"{E['gear']} <b>Админ панель</b>\n\nАмални танланг:",
        "en": f"{E['gear']} <b>Admin panel</b>\n\nChoose an action:",
    },
    "admin.no_access": {
        "ru": f"{E['lock']} У тебя нет доступа к админке.",
        "uz_latn": f"{E['lock']} Sizda admin panelga kirish huquqi yo'q.",
        "uz_cyrl": f"{E['lock']} Сизда админ панелга кириш ҳуқуқи йўқ.",
        "en": f"{E['lock']} You don't have access to admin panel.",
    },
    "admin.stats": {
        "ru": (
            f"{E['chart']} <b>Статистика бота</b>\n\n"
            f"{E['users']} Всего юзеров: <b>{{total_users}}</b>\n"
            f"{E['star']} Новых юзеров сегодня: <b>{{today_users}}</b>\n"
            f"{E['book']} Всего мақолов в БД: <b>{{total_proverbs}}</b>\n"
            f"{E['megaphone']} Каналов: <b>{{total_channels}}</b>"
        ),
        "uz_latn": (
            f"{E['chart']} <b>Bot statistikasi</b>\n\n"
            f"{E['users']} Jami foydalanuvchilar: <b>{{total_users}}</b>\n"
            f"{E['star']} Bugungi yangi foydalanuvchilar: <b>{{today_users}}</b>\n"
            f"{E['book']} Bazadagi maqollar: <b>{{total_proverbs}}</b>\n"
            f"{E['megaphone']} Kanallar: <b>{{total_channels}}</b>"
        ),
        "uz_cyrl": (
            f"{E['chart']} <b>Бот статистикаси</b>\n\n"
            f"{E['users']} Жами фойдаланувчилар: <b>{{total_users}}</b>\n"
            f"{E['star']} Бугунги янги фойдаланувчилар: <b>{{today_users}}</b>\n"
            f"{E['book']} Базадаги мақоллар: <b>{{total_proverbs}}</b>\n"
            f"{E['megaphone']} Каналлар: <b>{{total_channels}}</b>"
        ),
        "en": (
            f"{E['chart']} <b>Bot statistics</b>\n\n"
            f"{E['users']} Total users: <b>{{total_users}}</b>\n"
            f"{E['star']} New users today: <b>{{today_users}}</b>\n"
            f"{E['book']} Proverbs in DB: <b>{{total_proverbs}}</b>\n"
            f"{E['megaphone']} Channels: <b>{{total_channels}}</b>"
        ),
    },
    "admin.channels_empty": {
        "ru": f"{E['megaphone']} <b>Каналы</b>\n\nСписок пуст. Добавь канал кнопкой ниже.",
        "uz_latn": f"{E['megaphone']} <b>Kanallar</b>\n\nRo'yxat bo'sh. Quyidagi tugma orqali kanal qo'shing.",
        "uz_cyrl": f"{E['megaphone']} <b>Каналлар</b>\n\nРўйхат бўш. Қуйидаги тугма орқали канал қўшинг.",
        "en": f"{E['megaphone']} <b>Channels</b>\n\nList is empty. Add a channel using the button below.",
    },
    "admin.channels_title": {
        "ru": f"{E['megaphone']} <b>Каналы для подписки:</b>\n",
        "uz_latn": f"{E['megaphone']} <b>Obuna kanallari:</b>\n",
        "uz_cyrl": f"{E['megaphone']} <b>Обуна каналлари:</b>\n",
        "en": f"{E['megaphone']} <b>Subscription channels:</b>\n",
    },
    "admin.add_channel_id": {
        "ru": (
            f"{E['megaphone']} <b>Добавление канала</b>\n\n"
            "Отправь <b>ID канала</b> (например <code>-1001234567890</code>)\n\n"
            f"{E['bulb']} Узнать ID: добавь бота @getmyid_bot в канал"
        ),
        "uz_latn": (
            f"{E['megaphone']} <b>Kanal qo'shish</b>\n\n"
            "<b>Kanal ID</b> raqamini yuboring (masalan <code>-1001234567890</code>)\n\n"
            f"{E['bulb']} ID bilish: @getmyid_bot ni kanalga qo'shing"
        ),
        "uz_cyrl": (
            f"{E['megaphone']} <b>Канал қўшиш</b>\n\n"
            "<b>Канал ID</b> рақамини юборинг (масалан <code>-1001234567890</code>)\n\n"
            f"{E['bulb']} ID билиш: @getmyid_bot ни каналга қўшинг"
        ),
        "en": (
            f"{E['megaphone']} <b>Add channel</b>\n\n"
            "Send the <b>channel ID</b> (e.g. <code>-1001234567890</code>)\n\n"
            f"{E['bulb']} Get ID: add @getmyid_bot to the channel"
        ),
    },
    "admin.add_channel_title": {
        "ru": f"{E['edit']} Теперь отправь <b>название канала</b>:",
        "uz_latn": f"{E['edit']} Endi <b>kanal nomini</b> yuboring:",
        "uz_cyrl": f"{E['edit']} Энди <b>канал номини</b> юборинг:",
        "en": f"{E['edit']} Now send the <b>channel name</b>:",
    },
    "admin.add_channel_link": {
        "ru": (
            f"{E['link']} Теперь отправь <b>ссылку или юзернейм канала</b>\n\n"
            "Принимаю любой формат:\n"
            "• <code>https://t.me/your_channel</code>\n"
            "• <code>@your_channel</code>\n"
            "• <code>your_channel</code>"
        ),
        "uz_latn": (
            f"{E['link']} Endi <b>kanal havolasi yoki username</b> yuboring\n\n"
            "Istalgan formatda:\n"
            "• <code>https://t.me/your_channel</code>\n"
            "• <code>@your_channel</code>\n"
            "• <code>your_channel</code>"
        ),
        "uz_cyrl": (
            f"{E['link']} Энди <b>канал ҳаволаси ёки username</b> юборинг\n\n"
            "Истаган форматда:\n"
            "• <code>https://t.me/your_channel</code>\n"
            "• <code>@your_channel</code>\n"
            "• <code>your_channel</code>"
        ),
        "en": (
            f"{E['link']} Now send the <b>channel link or username</b>\n\n"
            "Any format accepted:\n"
            "• <code>https://t.me/your_channel</code>\n"
            "• <code>@your_channel</code>\n"
            "• <code>your_channel</code>"
        ),
    },
    "admin.channel_added": {
        "ru": f"{E['check']} <b>Канал добавлен!</b>",
        "uz_latn": f"{E['check']} <b>Kanal qo'shildi!</b>",
        "uz_cyrl": f"{E['check']} <b>Канал қўшилди!</b>",
        "en": f"{E['check']} <b>Channel added!</b>",
    },
    "admin.confirm_delete": {
        "ru": f"{E['warning']} <b>Удалить канал?</b>\n\nID: <code>{{channel_id}}</code>\n\nЭто действие нельзя отменить.",
        "uz_latn": f"{E['warning']} <b>Kanalni o'chirishni xohlaysizmi?</b>\n\nID: <code>{{channel_id}}</code>\n\nBu amalni qaytarib bo'lmaydi.",
        "uz_cyrl": f"{E['warning']} <b>Канални ўчиришни хоҳлайсизми?</b>\n\nID: <code>{{channel_id}}</code>\n\nБу амални қайтариб бўлмайди.",
        "en": f"{E['warning']} <b>Delete channel?</b>\n\nID: <code>{{channel_id}}</code>\n\nThis action cannot be undone.",
    },
    "admin.id_not_number": {
        "ru": f"{E['cross']} ID должен быть числом. Попробуй ещё раз:",
        "uz_latn": f"{E['cross']} ID raqam bo'lishi kerak. Qayta urinib ko'ring:",
        "uz_cyrl": f"{E['cross']} ID рақам бўлиши керак. Қайта уриниб кўринг:",
        "en": f"{E['cross']} ID must be a number. Try again:",
    },
    "admin.title_too_long": {
        "ru": f"{E['cross']} Название слишком длинное (макс 200 символов)",
        "uz_latn": f"{E['cross']} Nom juda uzun (maks 200 belgi)",
        "uz_cyrl": f"{E['cross']} Ном жуда узун (макс 200 белги)",
        "en": f"{E['cross']} Name is too long (max 200 characters)",
    },
    "admin.link_invalid": {
        "ru": f"{E['cross']} Не удалось распознать ссылку.\nПопробуй ещё:",
        "uz_latn": f"{E['cross']} Havolani aniqlab bo'lmadi.\nQayta urinib ko'ring:",
        "uz_cyrl": f"{E['cross']} Ҳаволани аниқлаб бўлмади.\nҚайта уриниб кўринг:",
        "en": f"{E['cross']} Could not parse the link.\nTry again:",
    },

    # === Кнопки админки ===
    "btn.admin_stats": {
        "ru": "Статистика",
        "uz_latn": "Statistika",
        "uz_cyrl": "Статистика",
        "en": "Statistics",
    },
    "btn.admin_channels": {
        "ru": "Каналы",
        "uz_latn": "Kanallar",
        "uz_cyrl": "Каналлар",
        "en": "Channels",
    },
    "btn.admin_home": {
        "ru": "Главное меню",
        "uz_latn": "Bosh menyu",
        "uz_cyrl": "Бош меню",
        "en": "Main menu",
    },
    "btn.admin_add": {
        "ru": "Добавить канал",
        "uz_latn": "Kanal qo'shish",
        "uz_cyrl": "Канал қўшиш",
        "en": "Add channel",
    },
    "btn.admin_back": {
        "ru": "Назад",
        "uz_latn": "Orqaga",
        "uz_cyrl": "Орқага",
        "en": "Back",
    },
    "btn.admin_cancel": {
        "ru": "Отмена",
        "uz_latn": "Bekor qilish",
        "uz_cyrl": "Бекор қилиш",
        "en": "Cancel",
    },
    "btn.admin_confirm_del": {
        "ru": "Да, удалить",
        "uz_latn": "Ha, o'chirish",
        "uz_cyrl": "Ҳа, ўчириш",
        "en": "Yes, delete",
    },
    "btn.admin_cancel_del": {
        "ru": "Отмена",
        "uz_latn": "Bekor qilish",
        "uz_cyrl": "Бекор қилиш",
        "en": "Cancel",
    },
    "btn.admin_panel": {
        "ru": "Админ-панель",
        "uz_latn": "Admin panel",
        "uz_cyrl": "Админ панель",
        "en": "Admin panel",
    },
    "btn.admin_broadcast": {
        "ru": "Рассылка",
        "uz_latn": "Xabar yuborish",
        "uz_cyrl": "Хабар юбориш",
        "en": "Broadcast",
    },

    # === Рассылка ===
    "admin.broadcast_prompt": {
        "ru": f"{E['plane']} <b>Массовая рассылка</b>\n\nОтправь текст/фото/видео для рассылки.\nПоддерживается HTML.",
        "uz_latn": f"{E['plane']} <b>Ommaviy xabar</b>\n\nYuborish uchun matn/rasm/video yuboring.\nHTML qo'llab-quvvatlanadi.",
        "uz_cyrl": f"{E['plane']} <b>Оммавий хабар</b>\n\nЮбориш учун матн/расм/видео юборинг.\nHTML қўллаб-қувватланади.",
        "en": f"{E['plane']} <b>Mass broadcast</b>\n\nSend text/photo/video to broadcast.\nHTML supported.",
    },
    "admin.broadcast_preview": {
        "ru": f"{E['eye']} <b>Предпросмотр</b>\n\nОтправить это сообщение всем юзерам?",
        "uz_latn": f"{E['eye']} <b>Oldindan ko'rish</b>\n\nBu xabarni barcha foydalanuvchilarga yuborishni xohlaysizmi?",
        "uz_cyrl": f"{E['eye']} <b>Олдиндан кўриш</b>\n\nБу хабарни барча фойдаланувчиларга юборишни хоҳлайсизми?",
        "en": f"{E['eye']} <b>Preview</b>\n\nSend this message to all users?",
    },
    "admin.broadcast_confirm": {
        "ru": "Да, отправить",
        "uz_latn": "Ha, yuborish",
        "uz_cyrl": "Ҳа, юбориш",
        "en": "Yes, send",
    },
    "admin.broadcast_cancel": {
        "ru": "Отмена",
        "uz_latn": "Bekor qilish",
        "uz_cyrl": "Бекор қилиш",
        "en": "Cancel",
    },
    "admin.broadcast_started": {
        "ru": f"{E['plane']} Рассылка запущена... Ожидай отчёт.",
        "uz_latn": f"{E['plane']} Xabar yuborilmoqda... Hisobotni kuting.",
        "uz_cyrl": f"{E['plane']} Хабар юборилмоқда... Ҳисоботни кутинг.",
        "en": f"{E['plane']} Broadcast started... Wait for report.",
    },
    "admin.broadcast_done": {
        "ru": f"{E['chart']} <b>Рассылка завершена!</b>\n\n{E['check']} Доставлено: <b>{{success}}</b>\n{E['cross']} Ошибок: <b>{{failed}}</b>\n{E['users']} Всего: <b>{{total}}</b>",
        "uz_latn": f"{E['chart']} <b>Xabar yuborish tugadi!</b>\n\n{E['check']} Yetkazildi: <b>{{success}}</b>\n{E['cross']} Xatolar: <b>{{failed}}</b>\n{E['users']} Jami: <b>{{total}}</b>",
        "uz_cyrl": f"{E['chart']} <b>Хабар юбориш тугади!</b>\n\n{E['check']} Етказилди: <b>{{success}}</b>\n{E['cross']} Хатолар: <b>{{failed}}</b>\n{E['users']} Жами: <b>{{total}}</b>",
        "en": f"{E['chart']} <b>Broadcast complete!</b>\n\n{E['check']} Delivered: <b>{{success}}</b>\n{E['cross']} Failed: <b>{{failed}}</b>\n{E['users']} Total: <b>{{total}}</b>",
    },

    # === Описания команд бота (для меню Telegram) ===
    "cmd.start": {
        "ru": "Запустить бота",
        "uz_latn": "Botni boshlash",
        "uz_cyrl": "Ботни бошлаш",
        "en": "Start the bot",
    },
    "cmd.menu": {
        "ru": "Главное меню",
        "uz_latn": "Asosiy menyu",
        "uz_cyrl": "Асосий меню",
        "en": "Main menu",
    },
    "cmd.profile": {
        "ru": "Мой профиль",
        "uz_latn": "Mening profilim",
        "uz_cyrl": "Менинг профилим",
        "en": "My profile",
    },
    "cmd.help": {
        "ru": "Помощь",
        "uz_latn": "Yordam",
        "uz_cyrl": "Ёрдам",
        "en": "Help",
    },
    "cmd.language": {
        "ru": "Сменить язык",
        "uz_latn": "Tilni o'zgartirish",
        "uz_cyrl": "Тилни ўзгартириш",
        "en": "Change language",
    },
}

# Допустимые коды языков
VALID_LANGS = ("ru", "uz_latn", "uz_cyrl", "en")


def t(key: str, lang: str = "ru", **kwargs) -> str:
    """Получить перевод по ключу и языку.

    Порядок fallback: lang → ru → ключ как есть.
    """
    translations = TRANSLATIONS.get(key, {})
    text = translations.get(lang, translations.get("ru", f"[{key}]"))
    if kwargs:
        text = text.format(**kwargs)
    return text


def detect_language(language_code: str | None) -> str:
    """Определяет язык по коду Telegram.

    uz → uz_latn (латиница — дефолт для узбекского)
    ru → ru
    остальное → en
    """
    if not language_code:
        return "ru"
    if language_code.startswith("ru"):
        return "ru"
    if language_code.startswith("uz"):
        return "uz_latn"
    return "en"
