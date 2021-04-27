########################
#name    send_mail.py  #
#author  Facker        #
#date    2021.4.27     #
#version 2.0           #
########################

import smtplib
from email import header
from email.mime import text
from email.mime import multipart


def sender_mail():

    msg = multipart.MIMEMultipart()
    msg['From'] = 'Facker'
    msg['To'] = '**********@**.com'
    msg['subject'] = header.Header('subject', 'utf-8')
    texts = "You text!"
    msg.attach(text.MIMEText(texts, 'plain', 'utf-8'))
    
    try:
        smt_p = smtplib.SMTP()
        smt_p.connect(host='smtp.***.com', port=25)
        sender, password = '*******@***.com','****************'
        smt_p.login(sender, password)
        smt_p.sendmail(sender, '2362315840@qq.com', msg.as_string())
    except Exception as e:
        print("发送失败！")
    smt_p.quit()
    print("发送成功！")
