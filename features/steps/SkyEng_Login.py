import os, time
from selenium import webdriver
from behave import given, then, when
from lib.Config import Config
from functions.SkyEng_Login import SkyEng_Login
from support.SkyEng_Login_Page import SkyEng_Login_Page
from selenium.common.exceptions import TimeoutException

cf = Config()
log = SkyEng_Login()
lg = SkyEng_Login_Page()

skyengprod = cf.get_config('config/config.ini', 'links', 'skyengprod')
skyengstaging = cf.get_config('config/config.ini', 'links', 'skyengstaging')


@given(u'I navigate to SkyEng')
def step_impl(context):
    if (os.environ['location'] == "staging"):
        context.browser.get(skyengstaging)
    elif (os.environ['location'] == "prod"):
        context.browser.get(skyengprod)
    time.sleep(3)
    print(lg.header_login_obj(context))
    assert (lg.header_login_obj(context)).is_displayed()

@when(u'I go to Login page')
def step_impl(context):
    lg.header_login_click(context)
    time.sleep(4)

@then(u'I log in with "{email}" and "{password}"')
def step_impl(context, email, password):
    try:
        log.Login(context, email=email, password=password)
    except TimeoutException:
        print ("Element not present TimeoutException")
        print  (context.browser.current_url)
        assert False
    time.sleep(4)

@then(u'I should see that Cabinet is loaded')
def step_impl(context):
    print(lg.username_dropdown(context))
    assert (lg.username_dropdown(context)).is_displayed()
