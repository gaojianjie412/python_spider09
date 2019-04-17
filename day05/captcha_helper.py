from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PIL import Image
from io import BytesIO
from chaojiying import main1

# 取浏览器窗口内全图
def get_big_image(browser):
    # browser.execute_script('window.scrollTo(0, 300)')
    screenshot = browser.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))
    return screenshot

def get_captha_position(browser, class_str):
    wait = WebDriverWait(browser, 5)
    captha = wait.until(EC.presence_of_element_located
                       ((By.CSS_SELECTOR, class_str)))
    location = captha.location
    size = captha.size
    x1 = location['x']
    y1 = location['y']
    width = size['width']
    height = size['height']
    x2 = x1 + width
    y2 = y1 + height
    print(x1, y1, x2, y2)
    print(width, height)
    return (x1, y1, x2, y2)

def get_captcha(browser, class_str):
    full_screen_img = get_big_image(browser)
    full_screen_img.save('mobile_login.png')

    # 获取验证码左上角和右下角坐标
    x1, y1, x2, y2 = get_captha_position(browser, class_str)

    captha_img = full_screen_img.crop((x1, y1, x2, y2))
    captha_img.save('mobile_captha.png')
    captha_str = main1('mobile_captha.png')
    return captha_str

