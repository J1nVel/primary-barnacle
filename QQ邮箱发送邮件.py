# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 20:20:05 2019

@author: 97286
"""

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

#sender_qq为发件人的qq号码
sender_qq = '972866441'
#pwd为qq邮箱的授权码
pwd = 'frzeqlqdfjyqbcde'
#收件人邮箱receiver
receiver='1962243670@qq.com'
#邮件的正文内容
mail_content = '你好，我是来自赛博坦星球的[J1nVel] ，现在在进行一项用python登录qq邮箱发邮件的测试'
#邮件标题
mail_title = 'J1nVel 的邮件'

def send_mail(sender_qq='',pwd='',\
    receiver='',mail_title='',mail_content=''):
    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    sender_qq_mail = sender_qq+'@qq.com'

    #ssl登录
    smtp = SMTP_SSL(host_server)
    #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)
    #MIMEText函数中的第二个参数为“plain”时，发送的是text文本。如果为“html”，则能发送网页格式文本邮件。
    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()


for i in range(10):
     send_mail(sender_qq=sender_qq,pwd=pwd,\
     receiver=receiver,mail_title=mail_title,\
     mail_content=mail_content)