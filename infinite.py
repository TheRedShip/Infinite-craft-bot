import requests
import time

s = requests.session()

proxies = []
with open("proxies", "r") as f:
	proxies = f.read().split("\n")

def send(first,second):
	global s
	url = "https://neal.fun/api/infinite-craft/pair"
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
		# "Cookie": "_ga_L7MJCSDHKV=GS1.1.1708698160.2.0.1708698160.0.0.0; _ga=GA1.1.307133597.1708695621; FCCDCF=%5Bnull%2Cnull%2Cnull%2C%5B%22CP6bsAAP6bsAAEsACBENAoEoAP_gAEPgACiQINJD7D7FbSFCwHpzaLsAMAhHRsCAQoQAAASBAmABQAKQIAQCgkAQFASgBAACAAAAICZBIQAECAAACUAAQAAAAAAEAAAAAAAIIAAAgAEAAAAIAAACAAAAEAAIAAAAEAAAmAgAAIIACAAAhAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAQOhQD2F2K2kKFkPCmQWYAQBCijYEAhQAAAAkCBIAAgAUgQAgFIIAgAIFAAAAAAAAAQEgCQAAQABAAAIACgAAAAAAIAAAAAAAQQAAAAAIAAAAAAAAEAAAAAAAQAAAAIAABEhCAAQQAEAAAAAAAQAAAAAAAAAAABAAA%22%2C%222~2072.70.89.93.108.122.149.196.2253.2299.259.2357.311.313.323.2373.338.358.2415.415.449.2506.2526.486.494.495.2568.2571.2575.540.574.2624.609.2677.864.981.1029.1048.1051.1095.1097.1126.1201.1205.1211.1276.1301.1344.1365.1415.1423.1449.1451.1570.1577.1598.1651.1716.1735.1753.1765.1870.1878.1889.1958~dv.%22%2C%22BEB542CE-E2B7-4C81-B4EB-49EAF4407D01%22%5D%5D; __gads=ID=f0d02e5d9ef535ee:T=1708695622:RT=1708695622:S=ALNI_MaqUPkeIWZzxOUS86dnrUXMxOUxrQ; __gpi=UID=00000d2e912e1caf:T=1708695622:RT=1708695622:S=ALNI_MYsToQlb4vjrtc8afgmi45HR4AZRg; __eoi=ID=68c594d2f756f355:T=1708695622:RT=1708695622:S=AA-Afjb44eds-3wzzOSfMW1ANwV9; FCNEC=%5B%5B%22AKsRol-oSgZ7ky4OeoCjCh99ap5RT9ZEXZ6-W5Dl8O38w9JPorSEKhCDiASsuAjzQ8_XioT40lkuAjEiBhGDo16G2f90WsI7ASlZkL9i5LTN-WjQU_otrudSp6YVCmtE_x2MKyCInRSDGKLZTN5-BXlaQxzfGw7FBg%3D%3D%22%5D%5D",
		"Sec-Fetch-Dest": "empty",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Site": "same-origin",
		"If-Modified-Since": "Wed, 21 Feb 2024 14:52:50 GMT"
	}
	proxies = {
		'http': f'{proxies.random()}:80',
	}

	response = s.get(url, params=params, headers=headers, proxies=proxies)
	return response.json()

items = ["Fire", "Earth", "Wind", "Water"]

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
		time.sleep(0.25)
		response = send(i, item)
		if (response["isNew"]):
			print(f"FIRST DISCOVERY {response['result']}")
		if (response["result"] not in items):
			items.append(response["result"])
			recipes[response["result"]] = [i, item]

			print(f"found {response['result']} :")
			get_recipe(response["result"])

			recursive(i)

# for i in ["Fire", "Earth", "Wind", "Water"]:
# 	recursive(i)