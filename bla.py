import requests
import random

proxies = []
with open("proxies", "r") as f:
	proxies = f.read().split("\n")

proxies = [[proxy.split("\t")[0],proxy.split("\t")[1]] for proxy in proxies]
import time
while True:
	myproxy = proxies[random.randint(0, len(proxies)-1)]
	proxy = {
		'https': f'https://{myproxy[0]}:{myproxy[1]}'
	}
	print("using proxy", proxy)
	time.sleep(1)
	response = requests.get('https://api64.ipify.org?format=json', proxies=proxy)
	print(response.content)