from selenium.webdriver import ActionChains

from utilites.base_page import Basepage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
class Checkout(Basepage):
    checkout=(By.XPATH,"//a[normalize-space()='Proceed To Checkout']")

    def checkout_click(self):
        self.click(self.checkout)