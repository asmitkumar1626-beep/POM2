from pages.checkout import Checkout
from pages.checkout2 import Checkout2
from pages.dasboard import add
from pages.dashpage1 import dashpage
from pages.payment import Payment
from pages.signup2_success import Success
from pages.signup_page import Signup
from pages.signuppage2 import Signuppage
from utilites import driver_setup
from utilites.driver_setup import get_driver
from pages.signup_page import Signup

driver=get_driver()
driver.get("https://automationexercise.com")
#dashpage1
dashpage=dashpage(driver)
dashpage.daspage()
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

assert "Congratulations! Your order has been confirmed" in driver.page_source
print("congratulations !! i just made my 1st industry based automation testcase")
























































#Congratulations! Your order has been confirmed!