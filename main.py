import telebot
import vk_api

from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('./config/secret.ini')
cfg.read('./config/config.ini')

vk_session = vk_api.VkApi(cfg.get('secret', 'vkToken'))


bot = telebot.TeleBot(cfg.get('secret', 'token'))


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я прогаю')


if __name__ == '__main__':
    bot.polling()