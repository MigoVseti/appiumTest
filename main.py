import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = {
    'appium:automationName': 'uiautomator2',
    'platformName': 'Android',
    'appium:deviceName': 'Pixel 7',
    'appium:language': 'en',
    'appium:locale': 'US'
}

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def click_element(self, xpath):
        el = self.driver.find_element(by=AppiumBy.ID, value=xpath)
        el.click()


    def test_min(self) -> None:
        el5 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btn9")
        el5.click()
        el6 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btnAdd")
        el6.click()
        el7 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btn8")
        el7.click()
        el8 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btnEqual")
        el8.click()
        el9 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btnC")
        el9.click()
    def test_plus(self) -> None :
        el10 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btn3")
        el10.click()
        el11 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btnSub")
        el11.click()
        el12 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btn2")
        el12.click()
        el13 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btnEqual")
        el13.click()
        el14 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btnC")
        el14.click()
    def test_mul(self) -> None :
        el15 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btn8")
        el15.click()
        el16 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btnMul")
        el16.click()
        el17 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btn4")
        el17.click()
        el18 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btnEqual")
        el18.click()
        el19 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btnC")
        el19.click()
    def test_div(self) -> None :
        el20 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btn9")
        el20.click()
        el21 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btnDiv")
        el21.click()
        el22 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btn3")
        el22.click()
        el23 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btnEqual")
        el23.click()
        el24 = self.driver.find_element(by=AppiumBy.ID, value="mobi.appplus.calculator.plus:id/btnC")
        el24.click()


if __name__ == '__main__':
    unittest.main()
