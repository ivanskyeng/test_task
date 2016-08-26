import time
from selenium import webdriver
from support.Vimbox_Login_Page import Vimbox_Login_Page
from selenium.webdriver.common.keys import Keys

lg = Vimbox_Login_Page()

class Vimbox_Login:
    def Login(self, context, email, password):
        lg.username(context).send_keys(email)
        lg.password(context).send_keys(password)
        lg.loginbutton(context)
        time.sleep(5)