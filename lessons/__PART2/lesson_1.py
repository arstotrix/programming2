import urllib.request
import json
token = 'a7fe1623a7fe1623a7fe162351a797aadeaa7fea7fe1623fb5959690245101b2b598172'

import urllib.request  # импортируем модуль
req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=1&count=20&v=5.74&access_token=a7fe1623a7fe1623a7fe162351a797aadeaa7fea7fe1623fb5959690245101b2b598172')
response = urllib.request.urlopen(req) # да, так тоже можно, не обязательно делать это с with, как в примере выше
result = response.read().decode('utf-8')
data = json.loads(result)
print(data['response']['items'][18]['copy_history'][0]['text'])