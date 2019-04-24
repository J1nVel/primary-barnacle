# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:45:16 2019

@author: 97286
"""

import urllib.request as r
from lxml.etree import HTML
url='http://pic.haibao.com/hotimage/?tdsourcetag=s_pcqq_aiomsg'
req=r.Request(url)
rst=r.urlopen(req).read().decode('utf-8')
html=HTML(rst)
img=html.xpath('//@data-original')
img1=[]
for i in range (0,len(img)):
    img1.append(str(img[i]))
    with open('D:\\972866441\\Documents\\Python\\海报时尚网图片url.txt','a',encoding='utf-8') as f:
        f.write(img[i]+'\n')