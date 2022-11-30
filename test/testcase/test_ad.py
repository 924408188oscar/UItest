import configparser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from data.config import Config
from utils.logger import Logger

logger = Logger(logger="Testcc").getlog()


class Testad:
    ip = None
    drivers = None

    def setup_class(self):
        print('--setup_class 执行--')
        c = Config()
        browser = c.get("browserType", "browserName")
        logger.info("选择的浏览器为: %s 浏览器" % browser)
        url = c.get('ptahUrl', "URL")
        # logger.info("打开的URL为: %s" % url)
        if browser == "Firefox":
            self.drivers = webdriver.Firefox()
            logger.info("启动火狐浏览器")
        else:
            chrome_options = Options()
            chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
            chrome_options.add_argument('--start-maximized')  # 指定浏览器分辨率
            chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
            # chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
            # chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('lang=zh_CN.UTF-8')
            self.drivers = webdriver.Chrome(options=chrome_options)
            self.drivers.get(url)
            aa = type(self.drivers)
            logger.info("打开URL: %s" % url)
            self.drivers.maximize_window()
            logger.info("全屏当前窗口")
            self.drivers.implicitly_wait(5)
            logger.info("设置5秒隐式等待时间")

    def teardown_class(self):
        print('\r--teardown_class 执行--')

    def test_cc(self):
        driver = self.drivers
        driver.get("https://www.baidu.com")
        driver.find_element(By.ID, "kw").send_keys("selenium")
        # driver.execute_script('alert("To Bottom")')
