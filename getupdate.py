import requests
from pprint import pprint

# token= '1687972442:AAFTgtZXybvpDqsTddplgtzO9GHUuenLwKs'
url='htpps://api.telegram.org/bot1687972442:AAFTgtZXybvpDqsTddplgtzO9GHUuenLwKs/getUpdates'
print(url)
r=requests.get(url)
data=r.json()
pprint(data)
