import smtplib
from email.mime.text import MIMEText
from email.header import Header


class MailSender(object):
    def __init__(self):
        self.smtp_obj = None
        self.from_mail = ''
        self.from_nick = ''
        self.password = ''
        self.to_mail = ''
        self.to_nick = ''

    def set_server(self, __server__, __port__):
        self.smtp_obj = smtplib.SMTP_SSL(__server__, __port__)

    def set_from_info(self, __mail__, __nickname__, __password__):
        self.from_mail = __mail__
        self.from_nick = __nickname__
        self.password = __password__

    def set_to_info(self, __mail__, __nickname__):
        self.to_mail = __mail__
        self.to_nick = __nickname__

    def login(self):
        self.smtp_obj.login(self.from_mail, self.password)

    async def send(self, __title__, __content__, __content_type__):
        message = MIMEText(__content__, __content_type__, 'UTF-8')
        from_header = Header(self.from_nick, 'utf-8')
        from_header.append('<' + self.from_mail + '>', 'ascii')
        to_header = Header(self.to_nick, 'utf-8')
        to_header.append('<' + self.to_mail + '>', 'ascii')
        message['From'] = from_header
        message['To'] = to_header
        message['Subject'] = Header(__title__, 'UTF-8')
        self.smtp_obj.sendmail(self.from_mail, self.to_mail, message.as_string())
