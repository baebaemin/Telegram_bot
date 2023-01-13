import requests

#https://api.telegram.org/bot5854500338:AAGczdwfWccKkd1SQlASs50KBK0SD0F85iw/getUpdates

token = '5854500338:AAGczdwfWccKkd1SQlASs50KBK0SD0F85iw'
url = f'https://api.telegram.org/bot{token}/getUpdates'

data = requests.get(url).json()

chat_id = data.get('result')[2].get('message').get('chat').get('id')

msg = '비오네...'
send_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}'
#parameter표기시 '?' 뒤에 붙임. 추가로 붙일땐 '&'을 붙임


requests.get(send_url)