import smtplib
import time
import itertools
import random
import concurrent.futures
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP accounts

SMTP_ACCOUNTS = [
    {"email": "camalzadeyahya8@gmail.com", "password": "rgwb xcxn levz dxwv"},
    {"email": "camalzadeyahya8@gmail.com", "password": "rgwb xcxn levz dxwv"},
    {"email": "camalzadeyahya8@gmail.com", "password": "rgwb xcxn levz dxwv"}
]

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

recipients = [
    "qafarovkenan2006@gmail.com",
    "alibaku2002@gmail.com",
    "betabankoffice@gmail.com",
    "backtestbeta64@gmail.com"
]

account_cycle = itertools.cycle(SMTP_ACCOUNTS)

subjects = [
    "Salam! Yeni bir xəbər var ✅",
    "Diqqət: Bu fürsəti qaçırmayın!",
    "Sizin üçün vacib bir mesaj 💬",
    "Sürpriz xəbərlər sizi gözləyir!",
    "Test mesajı – Gözlənilən e-poçt!"
]

def send_email(to_email):
    account = next(account_cycle)
    email = account["email"]
    password = account["password"]
    
    try:
        msg = MIMEMultipart("alternative")  
        msg["From"] = email
        msg["To"] = to_email
        msg["Subject"] = random.choice(subjects)
        msg["Reply-To"] = email  

        with open("message.html", "r", encoding="utf-8") as file:
            body_html = file.read()
            msg.attach(MIMEText(body_html, "html"))
        body_plain = "Bu, HTML e-poçtun 'plain text' versiyasıdır."
        msg.attach(MIMEText(body_plain, "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, to_email, msg.as_string())
        server.quit()
        print(f"✅ Göndərildi: {to_email} ({email} ilə)")

        time.sleep(random.uniform(5, 10))  

    except Exception as e:
        print(f"❌ Xəta: {to_email} -> {e}")

start_time = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(send_email, recipients)

end_time = time.time()
print(f"🕣 Göndəriş tamamlandı!\nÜmumi vaxt: {end_time - start_time:.2f} saniyə")
