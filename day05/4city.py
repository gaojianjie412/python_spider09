from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PIL import Image
from io import BytesIO
from chaojiying import main1
from sms_helper import *
from captcha_helper import get_captcha

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

screen_width = 1400
screen_height = 700

browser.set_window_size(screen_width, screen_height)
# 显式等待 针对某个节点的等待
wait = WebDriverWait(browser, 5)


def get_page():
    url = 'https://passport.4c.cn/signup'
    browser.get(url)
    input_mobile = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mobile')))
    mobile = get_mobile()
    print(mobile)
    input_mobile.clear()
    input_mobile.send_keys(mobile)

    show_captcha_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#show-captcha')))
    show_captcha_button.click()

    time.sleep(2)
    # 取图形验证码
    catcha_str = get_captcha(browser, '.captcha-img')
    print(catcha_str)

    # 输入图形验证码
    input_captcha = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#captcha')))
    input_captcha.clear()
    input_captcha.send_keys(catcha_str)

    # 点击获取短信验证码
    send_sms_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#sendsms')))
    send_sms_button.click()

    time.sleep(2)
    # 获取短信接口
    message = get_sms_message(mobile)

    # 输入短信验证码
    input_code = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#code')))
    input_code.clear()
    input_code.send_keys(message)

    # 输入密码
    input_password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password')))
    input_password.clear()
    input_password.send_keys('Vff123456')

    # 点击注册按钮
    register_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#nextstep')))
    register_button.click()

    # 修改昵称
    modify_nick_name_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, '修改')))
    modify_nick_name_link.click()

    input_nick_name = wait.until(EC.presence_of_element_located((By.NAME, 'nickname')))
    input_nick_name.clear()
    input_nick_name.send_keys('小甜甜11111')

    # 点击修改
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-primary')))
    submit_button.click()


def main():
    get_page()


if __name__ == '__main__':
    main()
