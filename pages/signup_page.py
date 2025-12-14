from utilites.base_page import Basepage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class Signup(Basepage):
    Name=(By.XPATH,"//input[@placeholder='Name']")
    Email=(By.XPATH,"//input[@data-qa='signup-email']")
    Sign_up=(By.XPATH,"//button[normalize-space()='Signup']")

    def signup(self):
        self.type(self.Name,"asmit")
        self.type(self.Email,"andugandugjakg@gmail.com")
        self.click(self.Sign_up)