import requests

#https://api.telegram.org/bot5854500338:AAGczdwfWccKkd1SQlASs50KBK0SD0F85iw/getMe
#여기서 id값 찾아오기

token = '5854500338:AAGczdwfWccKkd1SQlASs50KBK0SD0F85iw'
url = f'https://api.telegram.org/bot{token}/getMe'

data = requests.get(url).json()
bot_id = data.get('result').get('id')

#getUpdates : 봇과 주고받은 메세지 업데이트