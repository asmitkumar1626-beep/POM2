from selenium.webdriver import ActionChains

from utilites.base_page import Basepage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
class add(Basepage):
    add1_image=(By.XPATH,"//body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/img[1]")
    ADD1=(By.XPATH,"//div[@class='features_items']//div[2]//div[1]//div[1]//div[2]//div[1]//a[1]")
    add2_image=(By.XPATH,"//body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/img[1]")
    ADD2=(By.XPATH,"//body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/a[1]")
    add3_image=(By.XPATH,"//body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[10]/div[1]/div[1]/div[1]/img[1]")
    ADD3=(By.XPATH,"//body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[10]/div[1]/div[1]/div[1]/a[1]")
    continue_shopping=(By.XPATH,"//button[normalize-space()='Continue Shopping']")
    view_cart=(By.XPATH,"//u[normalize-space()='View Cart']")
    def add_items(self):
        prod1=self.wait.until(EC.presence_of_element_located(self.add1_image))
        prodd1 = self.wait.until(EC.presence_of_element_located(self.ADD1))
        self.driver.execute_script("arguments[0].scrollIntoView()",prodd1)
        actions=ActionChains(self.driver)
        actions.move_to_element(prod1).perform()
        self.click(self.ADD1)
        self.click(self.continue_shopping)
        prod2 = self.wait.until(EC.presence_of_element_located(self.add2_image))
        actions.move_to_element(prod2).perform()
        self.jsclick(self.ADD2)
        self.click(self.continue_shopping)
        prod3=self.wait.until(EC.presence_of_element_located(self.add3_image))
        self.driver.execute_script("arguments[0].scrollIntoView();",prod3)
        actions.move_to_element(prod3)
        self.click(self.ADD3)
        self.click(self.view_cart)
