import time
from cv2 import VideoCapture, imwrite
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

kamera_port = 0
kamera = VideoCapture(kamera_port)
time.sleep(0.2)
_, image = kamera.read()
imwrite(r"kayit konumu", image) #  27.satıra da bu yazılacak. Tek değişkene neden aktarmadım bilmiyorum.
del kamera
time.sleep(2)

fromaddr = "gönderen email adresi"
toaddr = "alıcı email adresi"

msg = MIMEMultipart()
msg["From"] = fromaddr
msg["To"] = toaddr
msg["Subject"] = "Your PC Opened !!!"
body = "Your PC has opened by a person. Photo in adds."

msg.attach(MIMEText(body, "plain"))
filename = r"kayit konumu"
attachment = open(filename, "rb")
attachment_file = MIMEBase("application", "octet-stream")
attachment_file.set_payload(attachment.read())
encoders.encode_base64(attachment_file)
attachment_file.add_header("Content-Disposition", "attachment; filename= %s" % filename)
msg.attach(attachment_file)
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login(fromaddr, "fromaddr şifresi")
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()
