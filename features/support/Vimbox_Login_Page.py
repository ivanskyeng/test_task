import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Vimbox_Login_Page:
    def username(self, context):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ng-pristine[title='Email']")))
        return context.browser.find_element_by_css_selector('.ng-pristine[title="Email"]')

    def password(self, context):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ng-pristine[title='Password']")))
        return context.browser.find_element_by_css_selector('.ng-pristine[title="Password"]')

    def loginbutton(self, context):
        context.browser.find_element_by_css_selector('.button_root_22nBk').click()

    def logo(self, context):
        return context.browser.find_element_by_id('skyeng')

    def validation_error(self, context):
        return context.browser.find_element_by_css_selector('.login_error_A3jo_').text

    def username_dropdown(self, context):
       return context.browser.find_element_by_css_selector('.b-gl-header__user-name')

    def menu_avatar_obj(self, context):
        return context.browser.find_element_by_css_selector('.menu_avatar-image_2aFIB')
