from selenium.webdriver import ActionChains

from utilites.base_page import Basepage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
class Checkout2(Basepage):
    message=(By.XPATH,"//textarea[@name='message']")
    place_order=(By.XPATH,"//a[normalize-space()='Place Order']")
    def checkout_2(self):
        self.type(self.message,"veryyy good")
        self.click(self.place_order)