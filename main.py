import telebot
from telebot import types

# Токен Telegram-бота
bot = telebot.TeleBot('6895711735:AAHTvZOLjT1i9TqE1P93JYZu9s9PltS2CgE')

# API ключ от ЛитРес
LITRES_API_KEY = 'LITRES_API_KEY'

# Список возрастных рейтингов
age_ratings = {
    '0+': '0',
    '6+': '6',
    '12+': '12',
    '16+': '16',
    '18+': '18'
}

# Список жанров
genres = {
    'детектив': '1',
    'фантастика': '2',
    'фэнтези': '3',
    'приключения': '4',
    'романтика': '5'
}
# Список изданий
edition = {
    'бумажное': '1',
    'электронное': '2'
}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Приветик! Тебе стало скучно просто ходить по магазинам в поисках хорошей книги? Тогда тебе к нам!")
    send_search_menu(message)


def send_search_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    items = [
        types.KeyboardButton('Жанр'),
        types.KeyboardButton('Возрастной рейтинг'),
        types.KeyboardButton('Издание'),
    ]
    markup.add(*items)
    bot.send_message(message.chat.id, "Выбери критерий поиска:", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def search_books(message):
    if message.text.lower() == 'жанр':
        send_genre_menu(message)
    elif message.text.lower() == 'возрастной рейтинг':
        send_age_rating_menu(message)
    elif message.text.lower() == 'издание':
        send_edition_menu(message)


def send_genre_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    items = [types.KeyboardButton(genre) for genre in genres.keys()]
    markup.add(*items)
    bot.send_message(message.chat.id, "Выбери жанр:", reply_markup=markup)


def send_age_rating_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    items = [types.KeyboardButton(rating) for rating in age_ratings.keys()]
    markup.add(*items)
    bot.send_message(message.chat.id, "Выбери возрастной рейтинг:", reply_markup=markup)

def send_edition_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    items = [types.KeyboardButton(rating) for rating in age_ratings.keys()]
    markup.add(*items)
    bot.send_message(message.chat.id, "Выбери издание:", reply_markup=markup)