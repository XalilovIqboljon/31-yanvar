import requests
import json
from pprint import pprint

token = 'https://api.telegram.org/bot1687972442:AAFTgtZXybvpDqsTddplgtzO9GHUuenLwKs/getme'
r=requests.get(token)
user=r.json()
pprint(user)