# import telebot
# from admins import admin_id
# import config
#
# bot = telebot.TeleBot(config.token)
#
#
# @bot.message_handler(commands=['start'])
# def welcome(message):
#     markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#     if message.from_user.id in admin_id:
#         check_messages = telebot.types.KeyboardButton("Проверить новые сообщения")
#         add_checker = telebot.types.KeyboardButton("Добавить администратора")
#         markup.add(check_messages, add_checker)
#     else:
#         send_message_button = telebot.types.KeyboardButton("Написать сообщение")
#         check_id = telebot.types.KeyboardButton("Узнать свой ID")
#         markup.add(send_message_button, check_id)
#
#     bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)
#
#
# # @bot.message_handler(commands=['add_admin'])
# # def add_admin
# @bot.message_handler(content_types=['text'])
# def text(message):
#     if message.chat.type == "private":
#         match message.text:
#             case "Написать сообщение":
#                 bot.send_message(message.chat.id, "Напишите ваше сообщение")
#
#             case "Узнать свой ID":
#                 bot.send_message(message.chat.id, f"Ваш ID: {message.from_user.id}")
#             case _:
#                 bot.send_message(message.chat.id, "Неизвестная команда")
#
#
# bot.polling(none_stop=True)
