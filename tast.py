import telebot
import requests

bot = telebot.TeleBot('6895711735:AAHTvZOLjT1i9TqE1P93JYZu9s9PltS2CgE')


@bot.message_handler(content_types=['text'])
def searching(message):
    url = f'https://openlibrary.org/search.json?q={message.text}&fields=title,author_name,first_publish_year'
    data = str(requests.get(url).json())[:200]
    bot.send_message(message.from_user.id, data)


bot.polling(none_stop=True, interval=0)
