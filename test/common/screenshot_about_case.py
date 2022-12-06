# -*-coding:utf-8 -*-
import os
import inspect
from datetime import datetime
from functools import wraps

"""
此模块用于屏幕截图  
https://www.cnblogs.com/jhhh/p/16763981.html
"""
# 获取截截图保存的路径
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
img_base_path = os.path.join(base_path, 'img')
print(img_base_path)


# 截图
def screenshot(driver, case_name, img_base_path):
    screenshotPath = os.path.join(img_base_path, case_name)
    time_now = datetime.now().strftime('%Y%m%d%H%M%S')
    screen_shot_name = "CheckPoint_NG.png"
    screen_img = screenshotPath + '_' + time_now + '_' + screen_shot_name
    # screen_img = os.path.join(screenshotPath, screenshotName)
    driver.get_screenshot_as_file(screen_img)
    return screen_img


# 得到当前类的实例方法名
# 也就是获得用例的名称
def get_current_function_name():
    # temp = inspect.stack()
    return inspect.stack()[1][3]


# case 断言失败截图装饰器
def screenshot_about_case(func):
    # 保持传入的case的名称不被装饰器所改变
    @wraps(func)
    # t = func
    def get_screenshot_about_case(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except Exception as e:
            # 获取case_name的名称
            # case_name = '{}_{} invoked'.format(self.__class__.__name__, get_current_function_name())
            case_name = '{}_{} invoked'.format(self.__class__.__name__, func.__name__)

            # 截屏的路径
            screenshotPath = os.path.join(img_base_path, case_name)
            # 获得现在的时间戳
            time_now = datetime.now().strftime('%Y%m%d%H%M%S')
            # 名字的一部分
            screen_shot_name = "CheckPoint_NG.png"
            # 组装图片需要传入的路径和推片名称
            screen_img = screenshotPath + '_' + time_now + '_' + screen_shot_name
            # 截图并保存到相应的名称的路径
            self.driver.get_screenshot_as_file(screen_img)
            raise e

    return get_screenshot_about_case
