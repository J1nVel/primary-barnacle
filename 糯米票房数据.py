# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 16:19:19 2019

@author: 97286
"""


import requests
from prettytable import PrettyTable
import json
import time
url='http://dianying.nuomi.com/movie/boxrefresh'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36','X-Requested-With':'XMLHttpRequest'}
data='isAjax=true&date=2019-04-23'
req=requests.get(url,headers=headers,data=data.encoding())
req.decode='utf-8'
rst=req.text
#   import urllib.request as r
#   urls='http://dianying.nuomi.com/movie/boxoffice'
#   req1=r.Request(urls,headers=headers)
#   rst1=r.urlopen(req1).read().decode('utf-8')
nm_data=json.loads(rst)

y=PrettyTable(['糯','米','电','影'])
y.add_row([
    str(nm_data['real']['data']['total']['boxNum'])+'万'+'\n'+'截至至'+nm_data['real']['data']['total']['message'],
    str(nm_data['real']['data']['total']['ticketNum'])+'万'+'\n'+'人次',
    nm_data['real']['data']['total']['scheNum']+'万'+'\n'+'场次',
    str(nm_data['real']['data']['total']['avgPrice'])+'元'+'\n'+'平均票价'
    ])
x=PrettyTable(['影片','上映天数','累计票房','实时票房','票房占比','排片占比','上座率','排座占比','场次','人数','场均人次','场均收入','平均票价'])
x.align['影片']='1'
x.padding_width=1
for m in range(0,len(nm_data['real']['data']['detail'])):
    x.add_row([
        nm_data['real']['data']['detail'][m]['movieName'],
        nm_data['real']['data']['detail'][m]['attribute']['1']['attrValue'],
        nm_data['real']['data']['detail'][m]['attribute']['2']['attrValue'],
        nm_data['real']['data']['detail'][m]['attribute']['3']['attrValue'],
        nm_data['real']['data']['detail'][m]['attribute']['4']['attrValue'],
        nm_data['real']['data']['detail'][m]['attribute']['5']['attrValue'],
        nm_data['real']['data']['detail'][m]['attribute']['6']['attrValue'],
        nm_data['real']['data']['detail'][m]['attribute']['7']['attrValue'],
        nm_data['real']['data']['detail'][m]['attribute']['8']['attrValue'],
        nm_data['real']['data']['detail'][m]['attribute']['9']['attrValue'],
        nm_data['real']['data']['detail'][m]['attribute']['10']['attrValue'],
        nm_data['real']['data']['detail'][m]['attribute']['11']['attrValue'],
        str(nm_data['real']['data']['detail'][m]['attribute']['12']['attrValue'])+'\n'
        ])
print(y)
print(x)
time.sleep(3)
input('按Enter键退出')