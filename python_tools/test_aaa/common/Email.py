import smtplib
from email.mime.text import MIMEText
from email.header import Header

def E_mail(mes):
    # 邮件服务器配置
    smtp_server = 'smtp.163.com'
    # smtp_port = 465
    smtp_username = 'guanlin4924@163.com'
    smtp_password = 'NBWOVYJPSKAYQJXO'

    # 发件人和收件人信息
    sender = 'guanlin4924@163.com'
    receiver = 'mayakun@biyingniao.com'

    # 邮件内容
    subject = '店铺列表信息'
    message = mes

    # 创建邮件对象
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['From'] = Header(sender)
    msg['To'] = Header(receiver)
    msg['Subject'] = Header(subject)

    server = None  # 初始化server变量

    try:
        # 连接SMTP服务器
        server = smtplib.SMTP(smtp_server)
        server.starttls()  # 如果使用TLS加密连接，请取消此行注释
        server.login(smtp_username, smtp_password)

        # 发送邮件
        server.sendmail(sender, receiver, msg.as_string())
        print('邮件发送成功！')

    except Exception as e:
        print('邮件发送失败:', str(e))

    finally:
        # 关闭连接
        if server is not None:
            server.quit()

if __name__ == '__main__':
    E_mail('123')