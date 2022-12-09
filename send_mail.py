import smtplib


def sendMail(login, password, text, mailto, subject, service):
    title = f'From: {login}\nTo: {mailto}\nSubject: {subject}\nContent-Type: text/plain; charset="UTF-8";'

    letter = f"{title}\n\n{text}"
    letter = letter.encode("UTF-8")

    server = smtplib.SMTP_SSL(f'smtp.{service}.ru:465')
    server.login(login, password)
    server.sendmail(login, mailto, letter)
    server.quit()
