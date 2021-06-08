import requests
import json

cache = {}
r = requests.get(f'http://www.floatrates.com/daily/{input()}.json'.lower())
currencies = json.loads(r.text)
cache['usd'] = currencies['usd']['rate'] if 'usd' in currencies else 1
cache['eur'] = currencies['eur']['rate'] if 'eur' in currencies else 1

while True:
    cur = input().lower()
    if cur == '':
        break
    num = float(input())
    print('Checking the cache...')
    if cur in cache:
        print('Oh! It is in the cache!')
    else:
        print('Sorry, but it is not in the cache!')
        cache[cur] = currencies[cur]['rate']
    print(f'You received {round(cache[cur] * num, 2)} {cur.upper()}.')
