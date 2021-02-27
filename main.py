import telebot
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('./config/secret.ini')
cfg.read('./config/config.ini')
bot = telebot.TeleBot(cfg.get('secret', 'token'))


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Ты идешь прогат?')


if __name__ == '__main__':
    bot.polling()