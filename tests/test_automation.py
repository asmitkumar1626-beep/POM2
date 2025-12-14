from pages.checkout import Checkout
from pages.checkout2 import Checkout2
from pages.dasboard import add
from pages.dashpage1 import dashpage
from pages.payment import Payment
from pages.signup2_success import Success
from pages.signuppage2 import Signuppage
from pages.signup_page import Signup

def test_automation(driver):
    driver.get("https://automationexercise.com")
    #dashpage1
    dash_page=dashpage(driver)
    dash_page.daspage()
    #signup_page
    signuppage=Signup(driver)
    signuppage.signup()
    #signuppage2
    signuppage2=Signuppage(driver)
    signuppage2.signup2()
    #signup2_success
    signupsuccess=Success(driver)
    signupsuccess.continue_butt()
    #dasboard
    dash=add(driver)
    dash.add_items()
    #checkout
    check=Checkout(driver)
    check.checkout_click()
    #checkout2
    check2=Checkout2(driver)
    check2.checkout_2()
    #payment
    pay=Payment(driver)
    pay.payment()
























































#Congratulations! Your order has been confirmed!