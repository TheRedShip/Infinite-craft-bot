import requests
import time
from threading import Thread

PROXY_OUTPUT = "proxies.txt"
PROXY_TIMEOUT = 800

def get_proxy():
    response = requests.get(f"https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=http&timeout={PROXY_TIMEOUT}&proxy_format=protocolipport&format=text")
    return [resp.replace("http://","") for resp in response.content.decode("utf-8").split("\r\n")[0:-1]]

liste = []

def try_proxy(proxy):
    global liste
    proxy_ip = proxy.split(":")[0]
    proxy_port = proxy.split(":")[1]

    proxies = {
        "http": f"http://{proxy_ip}:{proxy_port}/",
    }

    url = 'http://api.ipify.org'

    for i in range(3):
        try:
            response = requests.get(url, proxies=proxies, timeout=2)
            assert response.text==proxy_ip
        except:
            return
        time.sleep(1)
    liste.append(proxy)
    print(proxy)

threads = []
for proxy in get_proxy():
    time.sleep(0.01)
    print("trying", proxy)
    x = Thread(target=try_proxy, args=(proxy, ))
    x.start()
    threads.append(x)

for thread in threads:
    thread.join()
    
with open(PROXY_OUTPUT, "w") as f:
    f.write("\n".join(liste))
