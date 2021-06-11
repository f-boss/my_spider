import smtplib
from email import header
from email.mime import text
from email.mime import multipart


def sender_mail(html):
    msg = multipart.MIMEMultipart()
    # TODO: make the data from json
    msg['From'] = 'Facker'
    msg['To'] = '**********@**.com'
    msg['subject'] = header.Header('subject', 'utf-8')
    texts = "You text!"
    msg.attach(text.MIMEText(texts, 'html', 'utf-8'))
    
    try:
        smt_p = smtplib.SMTP()
        smt_p.connect(host='smtp.163.com', port=25)
        sender, password = '*******@***.com','****************'
        smt_p.login(sender, password)
        smt_p.sendmail(sender, '2362315840@qq.com', msg.as_string())
    except Exception as e:
        print("发送失败！")
    smt_p.quit()
    print("发送成功！")
