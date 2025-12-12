from utilites.base_page import Basepage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class dashpage(Basepage):
    Login_btt=(By.XPATH,"//a[normalize-space()='Signup / Login']")

    def daspage(self):
        self.click(self.Login_btt)

