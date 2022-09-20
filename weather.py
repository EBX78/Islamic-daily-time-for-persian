import requests
import json
import pprint
from datetime import datetime
import khayyam

r = requests.get('https://api.keybit.ir/owghat', params={'city':'مشهد'})

# keys for params & values for new params name
parat = {'azan_sobh':'Morning call', 'tolu_aftab':'Sunrise', 'azan_zohr':'Noon call', 'ghorub_aftab':'Sunset', 'azan_maghreb':'Night call', 'nimeshab':'Islamic midnight', 'day':'Day'}
# translate month (number) from json file
months = ['farvardin', 'ordibehesht', 'khordad', 'tir', 'mordad', 'shahrivar', 'mehr', 'aban', 'azar', 'dey', 'bahman', 'esfand']
saal = khayyam.JalaliDate.today().strftime('%Y')

[print("{:20}".format(parat[i]), json.loads(r.text)["result"][i]) for i in parat]
print("{:20}".format("Month"), months[int(json.loads(r.text)["result"]["month"]) - 1])
print("{:21}{}".format("Year", saal))

# pprint.pprint(json.loads(r.text))

