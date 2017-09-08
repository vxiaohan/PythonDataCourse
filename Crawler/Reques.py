import requests

news_url = "http://news.qq.com/"

res = requests.get(news_url)

print(res.text)