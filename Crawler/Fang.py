import requests
from bs4 import BeautifulSoup
import pandas
domain = "http://esf.sh.fang.com"
res = requests.get('http://esf.sh.fang.com/')

soup = BeautifulSoup(res.text, 'html.parser')
house_info = []
for house in soup.select('.houseList dl'):
    if len(house.select('.title'))>=1:
        url = domain+house.select('.title a')[0]['href']
        house_soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        info = {}
        info['标题'] = house_soup.select('#lpname')[0].text.strip()
        info['总价'] = house_soup.select('div[class="trl-item sty1"] i')[0].text.strip()
        detail_list = house_soup.select('div[class="tr-line clearfix"] div[class="trl-item1"]')
        for detail in detail_list:
            info[detail.select('div')[1].text.strip()] = detail.select('div')[0].text.strip()
        print(info)
        house_info.append(info)
    else:
        pass

df = pandas.DataFrame(house_info)

df.to_excel('fang.xlsx')