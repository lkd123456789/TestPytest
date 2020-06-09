from appium import webdriver

class BaseDriver:
    def base_driver(self):
        desired_caps = {}
        # 当前系统平台名称
        desired_caps["platformName"]="android"
        # 当前连接设备的android版本号
        desired_caps["platformVersion"] = "5.1.1"
        # 当前已经连接设备的名称
        desired_caps["deviceName"] = "emulator-5554"
        # 被测试App的包名
        desired_caps["appPackage"] = "com.android.settings"
        # 被测App的启动名
        desired_caps["appActivity"] = ".Settings"
        # 解决允许输入中文
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        # 获取对应的连接
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return self.driver