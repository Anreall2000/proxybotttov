import telebot
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('./config/secret.ini')
cfg.read('./config/config.ini')

vk_session = vk_api.VkApi(token=cfg.get('secret', 'vkToken'))
longpoll = VkBotLongPoll(vk_session, 202915868)
vk = vk_session.get_api()

bot = telebot.TeleBot(cfg.get('secret', 'token'))


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я прогаю')


if __name__ == '__main__':
    bot.polling()