#!/usr/bin/python3
# -*- encoding=utf8 -*-

# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python -m pytest -v --driver Chrome --driver-path chromedriver tests/test_mail_ru.py
#   Remote:
#  export SELENIUM_HOST=<moon host>
#  export SELENIUM_PORT=4444
#  pytest -v --driver Remote --capability browserName chrome tests/*
#
import time

from pages.mail_ru import MainPage


def test_check_main_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser)

    # вставить логин
    page.login = 'test793853@bk.ru'
    # нажать кнопку входа логин
    page.run_button_login.click()

    time.sleep(2)

    # вставить пароль
    page.passwd = 'Docker228'
    # нажать кнопку ввода пароля
    page.run_button_password.click()

    # нажать кнопку "Написать письмо"
    page.write_letter.click()
    time.sleep(5)

    # вставить текст в поля - "Кому, тема и сообщение"
    page.to_whom = 'test793853@bk.ru'
    page.theme = 'Тема'
    page.message = 'Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне. ' \
                 'Lorem Ipsum является стандартной "рыбой" для текстов на латинице с начала XVI века. ' \
                 'В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов, ' \
                 'используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только успешно пережил без ' \
                 'заметных изменений пять веков, но и перешагнул в электронный дизайн. Его популяризации ' \
                 'в новое время послужили публикация листов Letraset с образцами Lorem Ipsum в 60-х годах и, ' \
                 'в более недавнее время, программы электронной вёрстки типа Aldus PageMaker, в шаблонах которых ' \
                 'используется Lorem Ipsum.'

    # нажать кнопку входа пароля
    page.send_button.click()
    time.sleep(10)