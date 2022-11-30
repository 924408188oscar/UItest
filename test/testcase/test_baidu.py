from time import sleep

from selenium import webdriver

from test.common.BrowserDriver import BrowserDriver
from test.page.BaiduPage import BaiduPage
from utils.logger import Logger
import pytest

logger = Logger(logger="TestBaidu").getlog()


class TestBaidu:
    driver = None

    def setup_class(self):
        # self.driver = webdriver.Chrome()
        self.driver = BrowserDriver().openbrowser()
        # self.driver.get("https://www.baidu.com")

    def test_baidu_search_case(self):
        page = BaiduPage(self.driver)
        print(type(page))
        logger.info(' page.open("https: // www.baidu.com")')
        page.open("https://www.baidu.com")
        page.search_input("selenium ")
        page.search_button()
        sleep(2)
        logger.info(page.get_title())
        assert page.get_title() == "selenium_百度搜索ACS1"  # 使用pytest框架的断言

    def teardown_class(self):
        self.driver.quit()
