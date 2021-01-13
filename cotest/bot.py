import telebot
import requests
import json
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
bot = telebot.TeleBot("1410134344:AAGhcCE9QssZi7VALCxnKQqi7v4J5MRJ0SM")


def Button(message):
    r = requests.get('http://127.0.0.1:8000/api/button')
    data = json.loads(r.text)
    key = ReplyKeyboardMarkup(True, False)
    text = 'Hello {}'.format(message.from_user.first_name)
    for i in range(len(data['list'])):
        button = KeyboardButton(data['list'][i]['name'])
        key.add(button)
    bot.send_message(message.from_user.id, text)


@bot.message_handler(commands=['start', 'help', 'wow'])
def start(message):
    # text = 'Hello {}'.format(message.from_user.first_name)
    # bot.send_message(message.from_user.id,text)
    Button(message)


@bot.message_handler(commands=['letBegin'])
def sendId(message):
    text = 'Your Telegram Code is #{}'.format(message.from_user.id)
    bot.send_message(message.from_user.id, text)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    receivedMsg = message.text
    if receivedMsg == 'Hello':
        replyText = 'Hello {}'.format(message.from_user.first_name)
    else:
        replyText = 'We ulisikia wp !'

    bot.reply_to(message,replyText)


@bot.message_handler(content_types='text')
def Send_Message(message):
    pass


bot.polling()
