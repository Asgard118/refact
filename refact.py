import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from typing import List

class EmailClient:
    def __init__(self, login: str, password: str, smtp_server: str = "smtp.gmail.com", imap_server: str = "imap.gmail.com"):
        self.login = login
        self.password = password
        self.smtp_server = smtp_server
        self.imap_server = imap_server

    def send_email(self, subject: str, recipients: List[str], message: str) -> None:
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        with smtplib.SMTP(self.smtp_server, 587) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.login, self.password)
            server.sendmail(self.login, recipients, msg.as_string())

    def receive_emails(self, header: str = None) -> email.message.Message:
        with imaplib.IMAP4_SSL(self.imap_server) as mail:
            mail.login(self.login, self.password)
            mail.list()
            mail.select("inbox")
            criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
            result, data = mail.uid('search', None, criterion)
            assert data[0], 'There are no letters with the current header'
            latest_email_uid = data[0].split()[-1]
            result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_string(raw_email)
        return email_message


if __name__ == "__main__":
    
    email_client = EmailClient(login='your_email@gmail.com', password='your_password')

    email_client.send_email(subject='Test Subject', recipients=['recipient_email@gmail.com'], message='Test Message')

    received_email = email_client.receive_emails(header='Test Subject')
    print(received_email)
