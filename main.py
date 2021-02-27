import telebot
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from threading import Thread
import asyncio


from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('./config/secret.ini')
cfg.read('./config/config.ini')

vk_session = vk_api.VkApi(token=cfg.get('secret', 'vkToken'))
longpoll = VkBotLongPoll(vk_session, 202915868)
vk = vk_session.get_api()

Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()

bot = telebot.TeleBot(cfg.get('secret', 'token'))


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я прогаю')


@bot.message_handler(func=lambda message: True, content_types=['audio', 'video', 'document', 'text', 'location', 'contact', 'sticker'])
def default_command(message):
    print(message.text)
    Lsvk.messages.send(
        user_id=248749105,
        message=message.text,
        random_id=get_random_id()
    )


def vk_polling():
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event.message['text'])
            bot.send_message(-1001411811056, event.message['text'])


def tg_polling():
    bot.polling()


if __name__ == '__main__':
    Thread(target=vk_polling).start()
    Thread(target=tg_polling).start()
    # loop = asyncio.get_event_loop()
    # cors = asyncio.wait([vk_polling(), tg_polling()])
    # loop.run_until_complete(cors)
    # bot.polling()
    # for event in longpoll.listen():
    #     if event.type == VkBotEventType.MESSAGE_NEW:
    #         print(event.message['text'])
    #         bot.send_message(-1001411811056, event.message['text'])