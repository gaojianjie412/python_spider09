from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
from lxml import etree

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 5)


def get_page():
    url = 'https://www.zhipin.com'
    browser.get(url)
    input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ipt-search')))
    input.clear()
    input.send_keys('python')
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-search"]')))
    button.click()
    button_city1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//i[@class="icon-arrow-down"]')))
    button_city1.click()
    button_city = wait.until(EC.element_to_be_clickable((By.XPATH, '//ul[@class="dorpdown-province"]/li[1]')))
    button_city.click()
    button_search = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-search"]')))
    button_search.click()
    time.sleep(2)

    return browser.page_source


def parse_page(html):
    etree_html = etree.HTML(html)
    job_lists = etree_html.xpath('//div[@class="job-list"]')
    infomation_dic = {}
    for job_list in job_lists:
        # 工作详情页面
        job_detail = job_list.xpath('//li//div[@class="info-primary"]/h3[@class="name"]/a/@href')
        infomation_dic['job_detail'] = job_detail
        # 工作名称
        job_title = job_list.xpath('//li//div[@class="job-title"]/text()')
        # 薪资
        salary = job_list.xpath('//li//span[@class="red"]/text()')
        # 城市
        citys = job_list.xpath('//li//div[@class="info-primary"]/p/text()[1]')
        city = [city.strip() for city in citys]
        # 经验要求
        experience = job_list.xpath('//li//div[@class="info-primary"]/p/text()[2]')
        # 学历要求
        education = job_list.xpath('//li//div[@class="info-primary"]/p/text()[3]')
        # 公司名称
        company_title = job_list.xpath('//li//div[@class="company-text"]/h3[@class="name"]/a/text()')
        # 公司类型
        company_type = job_list.xpath('//li//div[@class="company-text"]/p/text()[1]')
        # 公司资本
        company_capital = job_list.xpath('//li//div[@class="company-text"]/p/text()[2]')
        # 公司规模
        company_scale = job_list.xpath('//li//div[@class="company-text"]/p/text()[3]')



def main():
    html = get_page()
    parse_page(html)


if __name__ == '__main__':
    main()
