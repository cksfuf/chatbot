import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

URL = f'https://api.telegram.org/bot{TOKEN}'

method = 'getUpdates'

# print(f'{URL}/{method}')

res = requests.get(f'{URL}/{method}')
print(res) # 200 이라는 숫자는 좋은결과라는 뜻

res_dict = res.json()
# print(res_dict['result'][-1]['message']['text'])# 브라우저로 본 딕셔너리 구조를 코드로 바꿔준거임.
user_input = res_dict['result'][-1]['message']['text']
user_id = res_dict['result'][-1]['message']['from']['id']

print(user_id, user_input)



# 답장하기
# print(f'{URL}/sendMessage?caht_id={user_id}&text={user_input}')
SEND_MSG_URL = f'{URL}/sendMessage?chat_id={user_id}&text={user_input}'
requests.get(SEND_MSG_URL)
