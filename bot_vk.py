import requests
import vk_api 
from vk_api.longpoll import VKLongPoll, VKEventType

vk_session = vk_api.VkApi( token = '#73368e27072c28a4d71c929e39f182bb88ef8a459cb187d605041505fb7813b74db61427a6d3886a5b634')

longpoll = VKLongPoll(vk_sesssion)
vk = vk.session.get_api()
for event in longpoll.listen():
    if event.type == VKEventType.MESSAGE_new and event.to_me and event.text:
        if event.text == 'Первый вариант фразы' or event.text == 'Второй вариант фразы':
            if event.from_user:
                vk.message.send(
                    user_id=event.user_id,
                    message='Ваш текст1'
                    )
            elif event.from_chat:
                vk.messages.send(
                    chat_id=event.chat_id,
                    message='Ваш текст2'
                    )