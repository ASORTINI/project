import telebot;
import schedule
import threading
import time
import sqlite3
from config import *
from telebot import types


bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['start'])
def get_text_messages(message):
    conn = sqlite3.connect("shedule.db")
    conn = sqlite3.connect("admin.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS shedule (ID, date)")
    cur.execute("CREATE TABLE IF NOT EXISTS admin (id, Name)")
    for i in cur.execute("SELECT id FROM admin"):
        user_id = message.from_user.id
        if message.from_user.id == id.admin:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("schedule")
            btn2 = types.KeyboardButton("new.schedule")
            markup.add(btn1, btn2)

            bot.send_message(message.from_user.id, "Привет Админ, чем я могу тебе помочь?", reply_markup=markup)

            @bot.message_handler(content_types=['schedule'])
            def get_text_messages(message):
                bot.send_message(message.from_user.id, "Расписание:")
                with open("schedule/schedule","rb") as file:
                    f=file.read()
            @bot.message_handler(content_types=['new.schedule'])
            def get_text_messages(message):
                bot.send_message(message.from_user.id, "Укажите дату:")
                bot.send_message(message.from_user.id, "И отправьте расписание(в формате .dox):")
            def handle_docs_photo(message):
                try:
                    chat_id = message.chat.id

                    file_info = bot.get_file(message.text)
                    downloaded_file = bot.download_file(file_info.file_path)

                    src = 'schedule' + message
                    with open(src, 'wb') as new_file:
                        new_file.write(message.text)

                    bot.reply_to(message, "Пожалуй, я сохраню")
                except Exception as e:
                    bot.reply_to(message, e)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("schedule")
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?", reply_markup=markup)

        @bot.message_handler(content_types=['start'])
        def get_text_messages(message):
            bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")

        @bot.message_handler(content_types=['schedule'])
        def get_text_messages(message):
            bot.send_message(message.from_user.id, "Расписание:")
            with open("schedule/schedule","rb") as file:
                f=file.read()
            bot.send_document(message.chat.id,f,"schedule")


    conn.commit()
    conn.close()
bot.polling(none_stop=True, interval=0)
