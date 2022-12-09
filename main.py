import send_mail
from dotenv import load_dotenv
import os
import argparse
import json


def main():
    if os.path.isfile('.env'):
        load_dotenv()
        login = os.getenv("LOGIN")
        password = os.getenv("PASSWORD")
    else:
        print("Такой файл не существует")
        exit()

    parser = argparse.ArgumentParser(
            description='Программа по отправке писем'
    )

    parser.add_argument('-m', help='путь до файла с почтами')
    parser.add_argument('-t', help='путь до файла с текстом')
    parser.add_argument('-s', help='тема письма')
    parser.add_argument('-v', help='почтовый домен')

    EmailsPath = parser.parse_args().m
    TextPath = parser.parse_args().t
    LetterSubject = parser.parse_args().s
    service = parser.parse_args().v

    try:
        with open(EmailsPath, 'r') as myFile:
            fileContents = myFile.read()
        EmailsList = json.loads(fileContents)
    except (ValueError, FileNotFoundError) as e:
        print(f"Не удалось открыть файл {EmailsPath}")
        exit()
    else:
        print(f"Файл открыть удалось {EmailsPath}")

    try:
        with open(TextPath, 'r', encoding='UTF-8') as myFile:
            LetterText = myFile.read()
    except (ValueError, FileNotFoundError) as e:
        print(f"Не удалось открыть файл {TextPath}")
        exit()
    else:
        print(f"Файл открыть удалось {TextPath}")

    for mailto in EmailsList:
        send_mail.sendMail(login, password, LetterText, mailto, LetterSubject, service)


if __name__ == "__main__":
    main()
