from utilites.base_page import Basepage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
class Success(Basepage):
    Continue=(By.XPATH,"//a[normalize-space()='Continue']")
    def continue_butt(self):
        self.click(self.Continue)