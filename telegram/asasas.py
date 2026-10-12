import telebot
import v2ray_tunnel
from telebot import apihelper
import appapi



def main () :
    BOT_TOKEN = "..."



    
    bot = telebot.TeleBot(BOT_TOKEN)

    @bot.message_handler(commands = ["start"])
    def send_message(message):
        bot.send_message(message.chat.id, text = "slam")
 


    @bot.message_handler(commands = ["help" , "support"])
    def reply_message(message):
        bot.reply_to(message ,"slam")




    @bot.message_handler(commands = ["news"])
    def show_menu(message):
        markup = telebot.types.InlineKeyboardMarkup(row_width=1)
        b1 = telebot.types.InlineKeyboardButton(text = "choise1" , url = "https://varzesh3.com")
        b2 = telebot.types.InlineKeyboardButton(text = "choise2" , url = "https://entekhab.ir")
        b3 = telebot.types.InlineKeyboardButton(text = "choise3" , url = "https://github.com")
        markup.add(b1,b2,b3)

        bot.send_message(message.chat.id, text = "lkankjcnkcajn" , reply_markup=markup)



    @bot.message_handler(commands =  ["menu"])
    def show_news(message):
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
        b1 = telebot.types.InlineKeyboardButton(text = "we" )
        b2 = telebot.types.InlineKeyboardButton(text = "call" )
        b3 = telebot.types.InlineKeyboardButton(text = "back" )
        markup.add(b1 , b2 , b3)

        bot.send_message(message.chat.id, text = "lkankjcnkcajn" , reply_markup=markup)

    @bot.message_handler(commands= ["movie"])
    def show_ms(message):
        msg = bot.send_message(message.chat.id ,"name")
        bot.register_next_step_handler_by_chat_id(msg , show_movie_id)

    def show_movie_id(message):
        movie_name = message.text

        result = appapi.get_movie_info_by_name(movie_name)


    @bot.message_handler(func=lambda message:True)
    def salam (message):

        if message.text == "we":
            DES = "HCC"
            bot.send_message(message.chat.id, text = DES)

        elif message.text == "call" :
            email = "assasss@gmail.com"
            mobile = "9009323989"
            office = "ahvaz"
            info = f" \n{email } \n { mobile} \n { office}"
            bot.reply_to(message , text = info)
        elif message.text == "back":
            markup = telebot.types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id , text = "i dont know" , reply_markup=markup)



        else :
            bot.send_message(message.chat.id , text = "lidhifhkeuh.kufhk.ufh")

        


    bot.infinity_polling()
        


if __name__ == "__main__" :
    main()