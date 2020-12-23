import os
import requests
import time


from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()

token = os.getenv('TOKEN')
sid_user = os.getenv('SID_USER')
id_app = os.getenv('ID_APP')
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

API_STATUS = 'https://api.vk.com/method/users.get'


def get_status(user_id):
    params = {
        'user_ids': user_id,
        'v': '5.92',
        'access_token': token,
        'fields': 'online',
    }
    user_status = requests.post(
        API_STATUS,
        params=params
    )
    return user_status.json()['response'][0]['online']


def sms_sender(sms_text):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=sms_text,
        from_='+19388882750',
        to='+79990387162'
    )
    return message.sid


if __name__ == '__main__':
    # тут происходит инициализация Client
    vk_id = input('Введите id ')
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
