# -*- coding: UTF-8 -*-
import smtplib
from email.header import Header

from email.mime.text import MIMEText
from email.utils import formataddr


def sendemils(emil_adress,yzm):
    msg_from = '948014059@qq.com'  # 发送方邮箱
    passwd = 'xdiwkutxybembfcg'  # 填入发送方邮箱的授权码
    msg_to = emil_adress  # 收件人邮箱

    subject = "PdfRead 注册账号"  # 主题
    content = '这是您的验证码：' + str(yzm)+ '<br>千万不要给别人看见哦'
    msg = MIMEText(content, 'html', 'utf-8')
    msg["From"] = formataddr(['dada',msg_from])
    msg['Subject'] = subject
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
    except Exception as e:
        print(e)
    finally:
        s.quit()




