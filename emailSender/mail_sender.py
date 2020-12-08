import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os import listdir
from os.path import isfile, join


class Mail:
    def __init__(self, sender_mail, sender_pass, to_mail, subject):
        #  User data part
        self.sender_mail = sender_mail
        self.to_mail = to_mail
        self.sender_pass = sender_pass

        #  Create message objects with MIMEMultipart
        self.message = MIMEMultipart()

        #  Setup message settings
        self.message["From"] = self.sender_mail
        self.message["To"] = self.to_mail
        self.message["Subject"] = subject

        #  Server login part
        try:
            self.server = smtplib.SMTP("smtp.gmail.com", 587)
            self.server.ehlo()
            self.server.starttls()
            self.server.login(sender_mail, sender_pass)
            print("Login Success.")
        except smtplib.SMTPAuthenticationError:
            print("Couldn't Login")

    def attach_text(self, body):
        #  Setup body of message
        body_text = MIMEText(body, "plain")
        self.message.attach(body_text)

    def attach_file(self, file_path, file_name):
        #  Setup image
        try:
            with open(file_path, "rb") as file:

                #  Find file format
                file_format = file_name.split(".")[len(file_name.split("."))-1]

                #  Set file data
                file_data = MIMEBase("document", file_format, filename=file_name)

                #  Set image headers
                file_data.add_header("Content-Disposition", "attachment", filename=file_name)
                file_data.add_header("Content-ID", "<0>")
                file_data.set_payload(file.read())

                #  Encode image
                encoders.encode_base64(file_data)
                self.message.attach(file_data)
        except FileNotFoundError:
            print("File couldn't found.")

    """İn this part of my code, ı made a loop for file names. This files must be in the same directory. Then i search 
    every loop i can reach files which the user needs."""

    def attach_files(self, directory_path, files_name):
        #  Make a loop for list of files
        for element_name in files_name:
            Mail.attach_file(self, directory_path + element_name, element_name)

    def attach_directory(self, directory_path):
        directory_files = [f for f in listdir(directory_path) if isfile(join(directory_path, f))]
        for element_name in directory_files:
            Mail.attach_file(self, directory_path + element_name, element_name)
        print("Files Attached.")

    def send_mail(self):
        try:
            #  Sending mail.
            self.server.sendmail(self.message["From"], self.message["To"], self.message.as_string())

            #  Logout from mail.
            self.server.quit()
            print("Mail sent.")
        except smtplib.SMTPSenderRefused:
            print("Access Denied")
