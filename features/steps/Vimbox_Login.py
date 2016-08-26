import os, time
from selenium import webdriver
from behave import given, then, when
from lib.Config import Config
from functions.Vimbox_Login import Vimbox_Login
from support.Vimbox_Login_Page import Vimbox_Login_Page
from selenium.common.exceptions import TimeoutException

cf = Config()
log = Vimbox_Login()
lg = Vimbox_Login_Page()

vimboxstaging = cf.get_config('config/config.ini', 'links', 'vimboxstaging')
vimboxprod = cf.get_config('config/config.ini', 'links', 'vimboxprod')


@given(u'I navigate to Vimbox login page')
def step_impl(context):
    if (os.environ['location'] == "staging"):
        context.browser.get(vimboxstaging)
    elif (os.environ['location'] == "prod"):
        context.browser.get(vimboxprod)
    time.sleep(3)
    #print(lg.header_login(context))
    #assert (lg.header_login(context)).is_displayed()

#@when(u'I log in with "wr.warning2014@mail.ru" and "111111"')
@when(u'I log in with "{email}" and "{password}"')
def step_impl(context, email, password):
    try:
        log.Login(context, email=email, password=password)
    except TimeoutException:
        print ("Element not present TimeoutException")
        print  (context.browser.current_url)
        assert False
    time.sleep(4)

@then(u'I should see that Virtual Classroom is loaded')
def step_impl(context):
    print(lg.menu_avatar_obj(context))
    assert (lg.menu_avatar_obj(context)).is_displayed()