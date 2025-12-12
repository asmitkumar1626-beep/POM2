from selenium.webdriver import ActionChains

from utilites.base_page import Basepage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
class Payment(Basepage):
    name_card=(By.XPATH,"//input[@name='name_on_card']")
    card_num=(By.XPATH,"//input[@name='card_number']")
    cvc=(By.XPATH,"//input[@placeholder='ex. 311']")
    mm=(By.XPATH,"//input[@placeholder='MM']")
    year=(By.XPATH,"//input[@placeholder='YYYY']")
    pay=(By.XPATH,"//button[@id='submit']")

    def payment(self):
        self.type(self.name_card,"asmit")
        self.type(self.card_num,"123112214545")
        self.type(self.cvc,"123")
        self.type(self.mm,"11")
        self.type(self.year,"2003")
        self.click(self.pay)