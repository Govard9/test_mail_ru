#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://mail.ru/'

        super().__init__(web_driver, url)

    # вставить логин
    login = WebElement(name='login')
    # нажать кнопку входа
    run_button_login = WebElement(xpath='//*[@id="mailbox"]/form[1]/button[1]')
    # вставить пароль
    passwd = WebElement(name='password')
    # нажать кнопку входа
    run_button_password = WebElement(xpath='//*[@id="mailbox"]/form[1]/button[2]')

    # нажать кнопку "Написать письмо"
    write_letter = WebElement(class_name='compose-button__txt')

    # поле "Кому"
    to_whom = WebElement(xpath='/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/label/div/div/input')
    # поле "Тема"
    theme = WebElement(name='Subject')
    # поле "Сообщение"
    message = WebElement(xpath='/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[5]/div/div/div[2]/div[1]/div[2]')
    # нажать кнопку "Отправить"
    send_button = WebElement(class_name='button2.button2_base.button2_primary.button2_hover-support.js-shortcut')
