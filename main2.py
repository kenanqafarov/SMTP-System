import smtplib
import time
import itertools
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

# Zoho və digər e-poçt hesabları
SMTP_ACCOUNTS = [
    {"email": "notifer@zohomail.eu", "password": "5HKD19M6xSQr"},  # Zoho hesabı
]

# SMTP parametrləri (Zoho üçün)
SMTP_SERVER = "smtp.zoho.eu"
SMTP_PORT = 465  # SSL portu

# Alıcılar
recipients = [
    "qafarovkenan2006@gmail.com",
    "aliyevaleyla6277@gmail.com",
    "ferdiish1974@gmail.com",
    "j.gooldberg2006@gmail.com",
    "e.mailkq1239@gmail.com",
    "qafarovkenan06@gmail.com",
    "560slide@gmail.com",
    "konul.mirzammadova@gmail.com"
]

# Mövzu başlıqları
subjects = [
    "Salam, sizə bir mesajımız var",
    "Yeniliklər haqqında qısa məlumat",
    "Xəbərdar olmaq üçün bu maili yoxlayın",
    "Bizi izləyin – yeni yeniliklər buradadır!",
    "Sadəcə məlumatlandırmaq istədik :)"
]

account_cycle = itertools.cycle(SMTP_ACCOUNTS)

def send_email(to_email):
    account = next(account_cycle)
    email = account["email"]
    password = account["password"]

    try:
        msg = MIMEMultipart("alternative")
        
        msg["From"] = formataddr((str(Header("Yahya Camalzadə", "utf-8")), email))
        
        msg["To"] = to_email
        msg["Subject"] = random.choice(subjects)
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
        msg.attach(MIMEText(body_html, "html"))

        body_plain = """
Salam!

Bu mesaj sizə yeni məlumat vermək üçündür.
Əlavə suallar üçün cavab yazmaqdan çəkinməyin.

Hörmətlə,
Komanda
"""
        msg.attach(MIMEText(body_plain, "plain"))

        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(email, password)
        server.sendmail(email, to_email, msg.as_string())
        server.quit()

        print(f"✅ Göndərildi: {to_email}")
        time.sleep(random.randint(15, 30))  

    except Exception as e:
        print(f"❌ Xəta: {to_email} -> {e}")

start_time = time.time()

for recipient in recipients:
    send_email(recipient)

end_time = time.time()
print(f"🕣 Göndəriş tamamlandı!\nÜmumi vaxt: {end_time - start_time:.2f} saniyə")
