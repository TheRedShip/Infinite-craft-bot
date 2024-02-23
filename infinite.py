import requests
import time
import random
import json

s = requests.session()

def get_proxy():
	with open("proxies.txt", "r") as f:
		return f.read().split("\n")

proxies = get_proxy()
proxy_index = -1

def send(first,second):
	global s
	global proxy_index
	global proxies

	url = "http://neal.fun/api/infinite-craft/pair"
	params = {
		"first": first,
		"second": second
	}
	headers = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
		"Accept": "*/*",
		"Accept-Language": "en-US,en;q=0.5",
		"Accept-Encoding": "gzip, deflate, br",
		"Referer": "https://neal.fun/infinite-craft/",
		"Alt-Used": "neal.fun",
		"Connection": "keep-alive",
		"Sec-Fetch-Dest": "empty",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Site": "same-origin",
		"If-Modified-Since": "Wed, 21 Feb 2024 14:52:50 GMT"
	}
	
	proxy_index += 1
	if (proxy_index > len(proxies) - 1):
		proxy_index = 0

	if (len(proxies) == 0):
		proxies = get_proxy()
	random_proxy = proxies[proxy_index]

	prox = {
		'http': f'http://{random_proxy}'
	}

	try:
		response = s.get(url, params=params, headers=headers, proxies=prox, timeout=1)
		return response.json()
	except Exception as e:
		proxies.remove(random_proxy)
		return send(first,second)

items = ["Fire", "Earth", "Wind", "Water"]
tried = []
recipes = {}

def get_recipe(item, tab=4):
	if (item not in recipes.keys()):
		print((tab-4)*' '+item)
	else:
		item1 = recipes[item][0]
		item2 = recipes[item][1]
		if (item1 not in ["Fire", "Earth", "Wind", "Water"]):
			print(f"{tab*' '}{item1} : ")
		get_recipe(item1, tab+4)
		if (item2 not in ["Fire", "Earth", "Wind", "Water"]):
			print(f"{tab*' '}{item2} : ")
		get_recipe(item2, tab+4)

def recursive(item):
	for i in items:
		if([item,i] in tried or [i,item] in tried):
			continue
		time.sleep(0.25 / len(proxies))
		
		print(f"TESTING {item} + {i} {' ' * 100}", end="\r")
		
		response = send(item,i)
		result_item = response["result"]

		tried.append([item,i])
		
		if (result_item not in items):
			items.append(result_item)
			recipes[result_item] = [i,item]

			print(' ' * 100, end='\r')
			print(f"found {response['result']} :")
			get_recipe(result_item)

			recursive(i)

for item in ["Fire", "Earth", "Wind", "Water"]:
	try:
		recursive(item)
	except KeyboardInterrupt as e:
		with open("result.txt", "w") as f:
			f.write(json.dumps(recipes))
		exit()