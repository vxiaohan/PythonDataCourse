
with open('../Data/jd.json', 'r') as f:
    jd = f.read()

import json
dic = json.loads(jd)
print(dic)

for info in dic:
    print(info.get("shop_logo"))

import pandas

table = pandas.read_json(jd)
print(table)