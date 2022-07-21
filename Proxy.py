import requests

proxies = {
  'http':  'http://128.199.202.122:3128',
  'http':  'http://185.61.152.137:8080',
  'http':  'http://5.58.37.254:8080',
  'http':  'http://51.250.80.131:80',
  'http':  'http://107.179.33.13:80',
  'http':  'http://005.252.161.48:8080',
  'http':  'http://5.252.161.48  3128',
  'http':  'http://139.162.78.109:3128',
  'http':  'http://154.16.63.16:8080',
  'http':  'http://202.6.233.133:80',
}


result = requests.get('https://httpbin.org/ip', proxies=proxies)

setup = print(result.json())


if setup == proxies:
  print("[!] Using Proxy")
else:
  print("\n [!] Using Original IP")