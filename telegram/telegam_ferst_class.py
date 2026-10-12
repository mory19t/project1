import telegram.appapi
import telebot




BOT_TOKEN = "..."

bot = telebot.TeleBot( BOT_TOKEN)


@bot.message_handler(commands = ["start"])
def send_message(message):
    bot.send_message(message.chat.id, text = 
    '''🎬 **به ربات دانلود فیلم و موسیقی خوش اومدی!** 🎵

اینجا می‌تونی اسم **فیلم، سریال یا آهنگ** موردنظرت رو جستجو کنی و فایلش رو دریافت کنی. 📥

✨ **دستورات بات:**

🎬 `/film`
جستجو و دریافت فیلم و سریال

🎵 `/music`
جستجو و دریافت آهنگ

📋 `/menu`
نمایش منوی اصلی

❓ `/help`
راهنمای استفاده از ربات

🔙 `/back`
بازگشت به منوی قبلی

👑 `/admin`
ارتباط با مدیریت

━━━━━━━━━━━━━━

🔎 فقط کافیه دستور موردنظرت رو انتخاب کنی و اسم چیزی که می‌خوای رو جستجو کنی.

⚡ **سریع، ساده، یک‌جا.**
''')

@bot.message_handler(commands=["film"])
def film(message):
    bot.send_message(
        message.chat.id,
        "اسم فیلمت رو بفرست 🎬"
    )

    bot.register_next_step_handler(message, search_film)


def search_film(message):

    movie_name = message.text

    bot.send_message(
        message.chat.id,
        "دارم فیلم رو پیدا می‌کنم... 🔎"
    )

    results = appapi.search_movie(movie_name)

    if not results:
        bot.send_message(
            message.chat.id,
            "فیلمی پیدا نشد ❌"
        )
        return

    movie = results[0]

    identifier = movie.get("identifier")
    title = movie.get("title", "بدون عنوان")

    movie_file = appapi.get_movie_files(identifier)

    if movie_file is None:
        bot.send_message(
            message.chat.id,
            "فایل قابل دانلود برای این مورد پیدا نشد ❌"
        )
        return

    markup = telebot.types.InlineKeyboardMarkup()

    button = telebot.types.InlineKeyboardButton(
        text="🎬 دانلود فیلم",
        url=movie_file["url"]
    )

    markup.add(button)

    bot.send_message(
        message.chat.id,
        f"🎬 {title}\n\n"
        "فیلم پیدا شد. برای دانلود روی دکمه زیر بزن:",
        reply_markup=markup
    )

@bot.message_handler(commands = ["menu"])
def menu(menu):
    markup = telebot.types.InlineKeyboardMarkup(row_width= 2)
    b1 = telebot.types.InlineKeyboardButton(text = "راهنمای دریافت موزیک ", callback_data="test")
    b2 = telebot.types.InlineKeyboardButton(text = "راهنمای دریافت فیلم " , callback_data="test")
    b3 = telebot.types.InlineKeyboardButton(text = "راهنمای تغییر مشخصات خود", callback_data="test")
    b3 = telebot.types.InlineKeyboardButton(text = "راهنمای خرید توکن ", callback_data="test")
    b4 = telebot.types.InlineKeyboardButton(text = "زیر مجموعه گیری", callback_data="test")
    b5 = telebot.types.InlineKeyboardButton(text = "دریافت توکن روزانه", callback_data="test")
    b6 = telebot.types.InlineKeyboardButton(text = "game", callback_data="test")
    markup.add(b1,b2,b3,b4,b5 ,b6)
    bot.send_message(menu.chat.id ,text =  "از منوی زیر انتخاب کن:", reply_markup=markup )

@bot.message_handler(fanc=lambda message:True)
def menu_text(message):

    if message.text == "راهنمای دریافت موزیک " :
       with open("music.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo)

    elif message.text == "راهنمای دریافت فیلم " :
        pass

    elif message.text == "راهنمای تغییر مشخصات خود" :
        pass

    elif message.text == "راهنمای خرید توکن " :
        pass

    elif message.text == "زیر مجموعه گیری" :
        pass

    elif message.text == "دریافت توکن روزانه" :
        pass

    elif message.text == "game" :
        pass
    



bot.infinity_polling()