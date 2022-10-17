# @Project : pythonwork
# @File    : settings.py.py
# @Author  : zhangjing
# @Time    : 2022/9/13 11:52
# @Software : Pycharm
# @Description :

taobao_desired_caps = {
    # 被测平台
    "platformName": "Android",
    # 系统版本号，保留到整数位即可
    "platformVersion": "8",
    # 设备名，通过 adb devices 获取
    "devicesName": "85bde763",
    # 应用程序包名, 建议向移动端开发获取
    "appPackage": "com.taobao.taobao",
    # Activity 类名
    "appActivity": "com.taobao.tao.TBMainActivity",
    # 设置自动化后不重置app
    "noReset": True,
    # 设置一个超时时间, 单位是秒
    "newCommandTimeout": 60,
    # 设置底层驱动
    "automationName": "UiAutomator2"
}


jingdong_desired_caps = {
    # 被测平台
    "platformName": "Android",
    # 系统版本号，保留到整数位即可
    "platformVersion": "8",
    # 设备名，通过 adb devices 获取
    "devicesName": "85bde763",
    # 应用程序包名, 建议向移动端开发获取
    "appPackage": "com.jingdong.app.mall",
    # Activity 类名
    "appActivity": "com.jingdong.app.mall.main.MainActivity",
    # 设置自动化后不重置app
    "noReset": True,
    # 设置一个超时时间, 单位是秒
    "newCommandTimeout": 60,
    # 设置底层驱动
    "automationName": "UiAutomator2"
}