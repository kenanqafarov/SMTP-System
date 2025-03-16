import smtplib
import time
import itertools
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

SMTP_SERVER = "mail.rkt.org.az"  
SMTP_PORT = 465  

SMTP_ACCOUNTS = [
    {"email": "noreply@rkt.org.az", "password": "s64R$y0v5"},  
]

recipients = [
    "qafarovkenan2006@gmail.com",
    "aliyevaleyla6277@gmail.com",
    "ferdiish1974@gmail.com",
    "camalzadeyahya8@gmail.com",
    "betabankoffice@gmail.com",
    "backtestbeta64@gmail.com",
    "yahyavj@code.edu.az",
    "alibaku2002@gmail.com"
]

subjects = [
    "Salam, sizə bir mesajımız var",
    "Yeniliklər haqqında qısa məlumat",
]

account_cycle = itertools.cycle(SMTP_ACCOUNTS)

def send_email(to_email):
    account = next(account_cycle)
    email = account["email"]
    password = account["password"]

    try:
        msg = MIMEMultipart("alternative")

        msg["From"] = formataddr((Header("Sirket Adı", "utf-8").encode(), email))
        msg["To"] = to_email
        msg["Subject"] = str(Header(random.choice(subjects), "utf-8"))
        msg["Reply-To"] = email

        body_html = """
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6;">
                <h3>Salam!</h3>
                <p>Bu mesaj sizə yeni məlumat vermək üçündür.</p>
                <p>Əlavə suallar üçün cavab yazmaqdan çəkinməyin.</p>
                <p>Hörmətlə,<br>Komanda</p>
            </body>
        </html>
        """

        body_plain = """
        Salam!

        Bu mesaj sizə yeni məlumat vermək üçündür.
        Əlavə suallar üçün cavab yazmaqdan çəkinməyin.

        Hörmətlə,
        Komanda
        """

        msg.attach(MIMEText(body_html, "html", "utf-8"))
        msg.attach(MIMEText(body_plain, "plain", "utf-8"))

        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(email, password)
        server.sendmail(email, to_email, msg.as_string())
        server.quit()

        print(f"✅ Göndərildi: {to_email}")
        time.sleep(random.randint(15, 30))

    except Exception as e:
        print(f"❌ SMTP xətası: {to_email} -> {e}")

for recipient in recipients:
    send_email(recipient)
