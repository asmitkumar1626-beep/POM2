from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Basepage:

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
    def click(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self,locator,text):
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(text)
    def get_text(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    def scrollto(self,locator):
        element=self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();",element)
    def jsclick(self,locator):
        element=self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();",element)
