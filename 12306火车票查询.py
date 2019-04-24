# -*- coding: utf-8 -*-
"""
Created on Fri 4月5日 07:21:26 2019 @author: 97286
""" def CN(city): with open('火车站三字码.csv') as f: ls=f.readlines() for i in ls: if city==i.split(',')[0]: EN=i.split(',')[1].replace('\n','') return EN
#CN('北京')
#CN('天津') import urllib.request as r
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'
train_date=input('请输入出发时间(示例格式:2019-04-17):')
fs=input('请输入始发站:')
ts=input('请输入终点站:')
from_station=CN(fs)
to_station=CN(ts)
url1=url.format(train_date,from_station,to_station)
rst=r.urlopen(url1).read().decode('utf-8') import json
data=json.loads(rst) train_data=data['data']['result']
train_data_map=data['data']['map']
train_num=len(train_data)
print(str(train_date)+'共有'+str(train_num)+'列车从<'+str(fs)+'>到<'+str(ts)+'>') from prettytable import PrettyTable
a=['车次','始发站/出发站','出发时间/到达时间','历时','商务座/特等座','一等座','二等座','高级软卧','软卧/一等卧','动卧','硬卧/二等卧','软座','硬座','无座','其他','备注']
x=PrettyTable(a)
line='------'
for i in range(0,len(train_data)): m=str(train_data[i]) n=m.split('|') try: train_data_map[n[6]] train_data_map[n[7]] except Exception: continue x.add_row([n[3],train_data_map[n[6]]+'\n'+train_data_map[n[7]],n[8]+'\n'+n[9],n[10],n[32],n[31],n[30],n[29],n[28],n[27],n[26],n[25],n[24],n[23],n[22],n[1]]) x.add_row([line,line,line,line,line,line,line,line,line,line,line,line,line,line,line,line])
print(x)
input('请按Enter键退出')
