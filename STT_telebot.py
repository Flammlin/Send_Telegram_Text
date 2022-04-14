# install - pip3 install pytelegrambotapi

import telebot

token = 'TOKEN-TELEGRAM-BOT'
bot = telebot.TeleBot(token)
chat_id = 'CHAT-ID'
text = 'Hello python'
bot.send_message(chat_id, text)