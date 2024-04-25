import urllib
import telebot
import requests

bot = telebot.TeleBot('6895711735:AAHTvZOLjT1i9TqE1P93JYZu9s9PltS2CgE')

@bot.message_handler(commands=["start", "help"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет! Это телеграмм бот по поиcку книг "Book Compass". Все что надо чтобы'
                                ' пользоваться ботом это просто ввести название автора или книги. НО УЧТИТЕ, ЧТО ВСЕ '
                                'НАЗВАНИЯ КНИГ ДОЛЖНЫ ВВОДИТЬСЯ ПО АНГЛИЙСКИ!!!')
@bot.message_handler(content_types=['text'])
def searching(message):
    try:
        url = f'https://openlibrary.org/search.json?q={message.text}&fields=title,author_name,first_publish_year,cover_i'
        data = str(requests.get(url).json())
        data = data[:data.find('}')]
        id_cover = data[data.find("'cover_i': ") + 11:data.find(", 'first_publish_year'")]
        cover = f'https://covers.openlibrary.org/b/id/{id_cover}-L.jpg?default=false'
        urllib.request.urlretrieve(cover, "geeksforgeeks.png")
        start_a = data.find("author_name': ['") + 16
        end_a = data.find("'], '")
        start_n = data.find("'title': ") + 10
        end_n = data.find("'}")
        start_y = data.find("year': ") + 7
        end_y = data.find(", 'ti")
        year = data[start_y:end_y]
        author = data[start_a:end_a]
        name_of_book = data[start_n:end_n]
        text = f'Название: {name_of_book}\n\nАвтор: {author}\n\nГод публикации: {year}'
        with open('geeksforgeeks.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML")
    except:
        bot.send_message(message.chat.id, 'Извините, книга не была найдена так как API OpenLibrary ее не существует')


bot.polling(none_stop=True, interval=0)
