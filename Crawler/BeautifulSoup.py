from bs4 import BeautifulSoup
import requests
news_url = "http://news.qq.com/"
res = requests.get(news_url)

soup = BeautifulSoup(res.text,'html.parser')
news_result = []
for news in soup.select('.Q-tpWrap .text'):
    news_result.append({'title':news.select('.linkto')[0].text, 'url':news.select('.linkto')[0]['href']})
print(news_result)

import pandas

news_df = pandas.DataFrame(news_result)

print(news_df)
news_df.to_excel('news.xlsx')