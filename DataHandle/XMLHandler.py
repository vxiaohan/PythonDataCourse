import xml.etree.cElementTree as ET

tree = ET.parse("../Data/weather.xml")

root = tree.getroot()

print(root)

for city in root.iter('city'):
    print(city.get('cityname'),city.get('tem1'))