from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
from lxml import etree

# 设置浏览器参数
chrome_options = webdriver.ChromeOptions()
# 设置成无头浏览器
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(browser, 5)


def get_page():
    browser.get('https://passport.hupu.com/register?project=bbs&display=&from=https%3A%2F%2Fbbs.hupu.com%2Fgear&jumpurl=https%3A%2F%2Fbbs.hupu.com%2Fgear')

    # 获取手机号
    mobile = '13393738627'

    # 获取手机号输入框
    mobile_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.mobile')))
    mobile_input.clear()
    mobile_input.send_keys(mobile)

    time.sleep(1)
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#rectMask')))
    button.click()


def main():
    get_page()


if __name__ == '__main__':
    main()
