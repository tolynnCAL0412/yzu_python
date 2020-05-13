import json
import requests

news_list = []
url = 'http://oldpaper.g0v.ronny.tw/index/json?fbclid=IwAR1zip-1_wLBrsZ2p9RfiAjm-WeFaxb8UyI4nA-uXOhK6Q3Wkgn7D_Zukow'
data = json.loads(requests.get(url).text)
print(data)

for d in data.get('data'):
    dictNews = {'title': d.get('title'), 'headlines': d.get('headlines')}
    news_list.append(dictNews)

file = open('news.txt', 'a', encoding='UTF-8')
for news in news_list:
    for head in news['headlines']:
        if '紓困' in head[1]:
            print(head)
            # file.writelines(('%s' % head) + '\n')
            file.writelines(head)
            file.write('\n')


# print(news_list)
