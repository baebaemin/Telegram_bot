import requests

token = '5854500338:AAGczdwfWccKkd1SQlASs50KBK0SD0F85iw' 
url = f'https://api.telegram.org/bot{token}/getUpdates'

data = requests.get(url).json()
chat_id = data.get('result')[3].get('message').get('chat').get('id')
msg = '배불러'

url_sendMessage = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}'

requests.get(url_sendMessage)