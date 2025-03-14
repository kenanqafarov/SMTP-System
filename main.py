import smtplib
import time
import concurrent.futures
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = "camalzadeyahya8@gmail.com"
PASSWORD = "rgwb xcxn levz dxwv"


def send_email(to_email):
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL
        msg["To"] = to_email
        msg["Subject"] = "Test E-poçtu"
        with open("message.html", "r", encoding="utf-8") as file:
            body = file.read()
            msg.attach(MIMEText(body, "html"))
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, to_email, msg.as_string())
        server.quit()

        print(f"✅ Göndərildi: {to_email}")
    except Exception as e:
        print(f"❌ Xəta: {to_email} -> {e}")

start_time = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(send_email, recipients)

end_time = time.time()
print(f"🕣Göndəriş tamamlandı!\nÜmumi vaxt: {end_time - start_time} saniyə")
