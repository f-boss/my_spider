import smtplib
from email import (header)
from email.mime import text
from email.mime import multipart
import time


def sender_mail():
    smt_p = smtplib.SMTP()
    smt_p.connect(host='smtp.qq.com', port=25)
    sender, password = '2362315840@qq.com', 'cwypxaetaqruecff'
    smt_p.login(sender, password)
    receiver_addresses = ['邮箱地址']
    count_num = 1
    for email_address in receiver_addresses:
        try:
            msg = multipart.MIMEMultipart()
            msg['From'] = 'Boss'
            msg['To'] = email_address
            msg['subject'] = header.Header('这个是标题', 'utf-8')
            msg.attach(text.MIMEText('这是内容', 'plain', 'utf-8'))
            smt_p.sendmail(sender, email_address, msg.as_string())
            print('第%d次发送给%s' % (count_num, email_address))
            time.sleep(10)
            count_num = count_num + 1
        except Exception:
            print('第%d次发给%s异常' % (count_num, email_address))
    smt_p.quit()


sender_mail()

