from email.mime.text import MIMEText
import smtplib


def send_email(email, height, average_height, count):
    from_email = "chucksogwo@gmail.com"
    from_password = "Chidera001"
    to_email = email

    subject = "Height data"
    message = "Hey there, your height is <strong>%s</strong>. The average height of users in the area is <strong>%s</strong>, the number of users who have submitted their data till date is <strong>%s</strong>." % (height, average_height, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['from'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)