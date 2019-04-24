# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 07:11:29 2019

@author: 97286
"""
while True:
    import urllib.request as r
    a=input('请输入商品名>>>>>')
    if a == '0':
        break
    q=r.quote(a)
    url='https://s.taobao.com/search?q={}&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'.format(q)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','cookie':' t=d8671c9df3b3644aab34d681d22aaefd; cookie2=123d0b49f8bb658c6d65aa05b544524c; v=0; _tb_token_=563feeb5158ee; UM_distinctid=169e7baa7fbae-0026ea2928a05f-345c487f-100200-169e7baa7fd73c; cna=l78sFXqJG0ICAd5QrxGqhb6p; unb=2985441037; sg=%E7%8B%B875; _l_g_=Ug%3D%3D; skt=3d0c475446be0e86; cookie1=AHnX4if0nx%2BVSgHhNYUXc6bbibBGr%2FDd48fWLJy5G7Y%3D; csg=5b6b435d; uc3=vt3=F8dByEnV2TyrsZ8u1%2Fc%3D&id2=UUGq1F1RfIGf3Q%3D%3D&nk2=odeXCwmfaFEEtObS&lg2=UIHiLt3xD8xYTw%3D%3D; existShop=MTU1NDM3MTAwOA%3D%3D; tracknick=%5Cu9EBB%5Cu62C9%5Cu56FE%5Cu80E1%5Cu963F%5Cu72F8; lgc=%5Cu9EBB%5Cu62C9%5Cu56FE%5Cu80E1%5Cu963F%5Cu72F8; _cc_=Vq8l%2BKCLiw%3D%3D; dnk=%5Cu9EBB%5Cu62C9%5Cu56FE%5Cu80E1%5Cu963F%5Cu72F8; _nk_=%5Cu9EBB%5Cu62C9%5Cu56FE%5Cu80E1%5Cu963F%5Cu72F8; cookie17=UUGq1F1RfIGf3Q%3D%3D; tg=0; mt=ci=4_1; thw=cn; _m_h5_tk=49c8738d3db849f90238d4dbd059001a_1554380009705; _m_h5_tk_enc=07c1d16c974f965be183e86d0e3f0bac; enc=G6ITXdkluYfX%2Bnenm2YBAWwi7wGoGWITIwRpIkKyBRiO%2Bjqg85l1CHzCQJSkv24vR4ojKwgahssDV6MLaGvhrA%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; hng=CN%7Czh-CN%7CCNY%7C156; swfstore=308413; JSESSIONID=E8B16058279A9E7043A9FDCD0884EF2C; uc1=cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&cookie14=UoTZ4MzyshEWqg%3D%3D; whl=-1%260%260%260; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; isg=BKmpgzLh0X2lgu3JatuAnlrurVUJyoZWOBxLZ0ueqhDPEsokksRceNjA1PaBjDXg; l=bBLS1Rzrv-ik9KXkBOfNNZN-f47OnIJR1rVPhzEZRICPO4Cw5f-5WZs7rYTeC3GVZ6dkJ3PqyMaLBX8OfynV.'}
    request=r.Request(url,headers = headers)
    rst=r.urlopen(request).read().decode('utf-8')
    import json
    tb=json.loads(rst)
    
    from prettytable import PrettyTable
    x= PrettyTable(['','尚','天猫','就','购了'])
    x.align['尚']='1'
    t=tb["mods"]["itemlist"]["data"]["auctions"]
    def goods(g):
        price=t[g]['view_price']
        fee=t[g]['view_fee']
        sales=t[g]['view_sales']
        raw_title=t[g]['raw_title']
        nick=t[g]['nick']
        item_loc=t[g]['item_loc']
        
        if fee == '0.00':
            fee='包邮'      
        else:
            fee='邮费:' + fee
        fee2=t[g+1]['view_fee']
        if fee2 == '0.00':
            fee2='包邮'
        else:
            fee2='邮费:'+ fee2
        fee3=t[g+2]['view_fee']
        if fee3 == '0.00':
            fee3='包邮'
        else:
            fee3='邮费:'+ fee3
        fee4=t[g+3]['view_fee']
        if fee4 == '0.00':
            fee4='包邮'
        else:
            fee4='邮费:'+ fee4
        x.add_row([
                  '价格:'+'\n'+
                  '邮费:'+'\n'+
                  '销量:'+'\n'+
                  '商品名:'+'\n'+
                  '店铺名:'+'\n'+
                  '店铺地址:'+'\n'+'*************************',
                  price+'\n'+
                  fee+'\n'+
                  sales +'\n'+
                  raw_title[0:9]+'\n'+
                  nick+'\n'+
                  item_loc+'\n'+'*************************',
                  
                  t[g+1]['view_price']+'\n'+
                  fee2+'\n'+
                  t[g+1]['view_sales']+'\n'+
                  t[g+1]['raw_title'][0:15]+'\n'+
                  t[g+1]['nick']+'\n'+
                  t[g+1]['item_loc']+'\n'+'*************************',
                  
                  t[g+2]['view_price']+'\n'+
                  fee3+'\n'+
                  t[g+2]['view_sales']+ '\n'+
                  t[g+2]['raw_title'][0:15]+'\n'+
                  t[g+1]['nick']+'\n'+
                  t[g+2]['item_loc']+'\n'+'*************************',
                  
                  t[g+3]['view_price']+'\n'+
                  fee4+'\n'+
                  t[g+3]['view_sales']+'\n'+
                  t[g+3]['raw_title'][0:15]+'\n'+
                  t[g+3]['nick']+'\n'+
                  t[g+3]['item_loc']+'\n'+'*************************'
                  ])
    for n in range(0,12):
        goods(n)
    print(x)
input('请按Enter键退出')