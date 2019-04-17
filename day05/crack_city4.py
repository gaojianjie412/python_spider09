from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
from lxml import etree
from sms_helper import get_mobile, get_sms_message
from captcha_helper import *

# 设置浏览器参数
chrome_options = webdriver.ChromeOptions()
# 设置成无头浏览器
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(browser, 5)

def get_page():
    browser.get('https://passport.4c.cn/signup')

    # 获取手机号
    mobile = get_mobile()
    print(mobile)

    # 获取手机号输入框
    mobile_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mobile')))
    mobile_input.clear()
    mobile_input.send_keys(mobile)

    time.sleep(1)
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#show-captcha')))
    button.click()

    time.sleep(1)

    # 获取图形验证码
    captcha = get_captcha(browser, '.captcha-img')
    print(captcha)

    # 输入图形验证码
    captcha_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#captcha')))
    captcha_input.clear()
    captcha_input.send_keys(captcha)

    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#sendsms')))
    button.click()

    time.sleep(1)

    # 获取短信验证码
    sms_code = get_sms_message(mobile)
    print(sms_code)

    sms_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#code')))
    sms_input.clear()
    sms_input.send_keys(sms_code)

    # 输入密码
    pwd_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password')))
    pwd_input.clear()
    pwd_input.send_keys('Vff123456')

    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#nextstep')))
    button.click()


def main():
    get_page()

if __name__ == '__main__':
    main()