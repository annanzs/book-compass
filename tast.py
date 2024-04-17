import telebot
from telebot import types
import requests

bot = telebot.TeleBot('6895711735:AAHTvZOLjT1i9TqE1P93JYZu9s9PltS2CgE')

name = ''
surname = ''
age = 0
but = 0


def searching(message):
    url = f'https://openlibrary.org/search.json?q={message}&fields=title,author_name'
    data = requests.get(url).json()
    print(1)
    return data


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Привет! Я бот 'Book Compass'! Здесь ты можешь подобрать себе книгу на лю"
                                           "бой вкус :)")


@bot.message_handler(content_types=['text'])
def searching(message):
    url = f'https://openlibrary.org/search.json?q={message}&fields=title,author_name'
    data = requests.get(url).json()
    return data


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "search":
        bot.send_message(call.message.chat.id,
                         "Напиши название книги:")

        while call.message.text == "Привет! Я бот 'Book Compass'! Здесь ты можешь подобрать себе книгу на любой вкус :)":
            pass
        name = call.message.text

        result = searching(name)
        bot.send_message(call.message.chat.id, name)
        bot.send_message(call.message.chat.id, result)

    elif call.data == "genre":
        but = 2


bot.polling(none_stop=True, interval=0)
