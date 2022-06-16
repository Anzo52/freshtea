# used by monitor.py to send email when the website is changed or updated.


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os


def send_email(url):
    """
    Function to send email.
    :param url: url of the website
    :return: None
    """
    fromaddr = "example@example.com"
    toaddr = "example@example.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr 
    msg['To'] = toaddr
    msg['Subject'] = "Website changed"
    body = "The website " + url + " has changed."
    msg.attach(MIMEText(body, 'plain'))
    filename = "screenshot.png"
    attachment = open(filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "password")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    os.remove(filename)


if __name__ == "__main__":
    send_email("https://www.example.com")