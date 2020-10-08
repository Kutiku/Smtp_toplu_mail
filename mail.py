import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tqdm import tqdm

dosya = open("mailler.txt","r")
mailler = []
mailler=dosya.readlines()
print(mailler)

def mail_gonder(gonderen,gonderen_sifre,alici,konu,icerik):

    message = MIMEMultipart()
    message["From"] = gonderen
    message["To"] = alici
    message["Subject"] = konu

    text = icerik
    stem = MIMEText(text,"plain")
    message.attach(stem)

    try:
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login(gonderen,gonderen_sifre)
        mail.sendmail(message["From"],message["To"],message.as_string())
        mail.close()

    except:
        sys.stderr.write("Mail gönderilemedi")
        sys.stderr.flush()


gonderen = ""
gonderen_sifre = ""
konu = "Toplu mail denemesi"
icerik = """
Toplu mail denemesidir.Pyhon kodu ile gönderilmiştir.

Enes Mutlu
"""

for alici in tqdm(mailler):
    alici=alici.replace("\n","")
    mail_gonder(gonderen, gonderen_sifre, alici, konu, icerik)


