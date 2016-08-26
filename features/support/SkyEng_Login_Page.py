import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SkyEng_Login_Page:
    def header_login_obj(self, context):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".b-gl-header__sign")))
        return context.browser.find_element_by_css_selector('.b-gl-header__sign')

    def header_login_click(self, context):
        context.browser.find_element_by_css_selector('.b-gl-header__sign').click()

    def username(self, context):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.NAME, "username")))
        return context.browser.find_element_by_name('username')

    def password(self, context):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.NAME, "password")))
        return context.browser.find_element_by_name('password')

    def loginbutton(self, context):
        context.browser.find_element_by_css_selector('.b-gui-v2-button.b-gui-v2-button_color_lime').click()

    def logo(self, context):
        return context.browser.find_element_by_css_selector('.l-motion__logo>img')

    def forgotpassord(self, context):
        return context.browser.find_element_by_css_selector('a[href="https://auth.skyeng.ru/resetPassword"]')

    def register(self, context):
        return context.browser.find_element_by_css_selector('a[href="http://skyeng.ru/order"]')

    def validation_error(self, context):
        return context.browser.find_element_by_css_selector('.b-auth-login__error.ng-binding').text

    def username_dropdown(self, context):
        return context.browser.find_element_by_css_selector('.b-gl-header__user-name')