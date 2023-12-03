import telebot
import random
from telebot import types
from sites import sites_dict
token = ''
bot = telebot.TeleBot(token)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
@bot.message_handler(commands=['button'])
def welcome(message):
    sti = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')
    # Создание и отправка клавиатуры при старте бота
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Написать мне в личку")
    item2 = types.KeyboardButton("Дай ссылку на какой-нибудь сайт")
    item3 = types.KeyboardButton("Моё резюме")
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Выбери действие:", reply_markup=markup)

# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def buttons(message):
    if message.chat.type == 'private':
        if message.text == 'Написать мне в личку':
            bot.send_message(message.chat.id, 'https://t.me/wirtusok')
        elif message.text == 'Дай ссылку на какой-нибудь сайт':
            link_name, link_url = random.choice(list(sites_dict.items()))
            bot.send_message(message.chat.id, f"Держи {link_url}")
        elif message.text == 'Моё резюме':
            bot.send_message(message.chat.id, 'Здесь пока ничего нет 😥, но скоро будет!')    
        else:
            bot.send_message(message.chat.id, 'Повтори, плз')

# Запуск бота
bot.polling(none_stop=True)
