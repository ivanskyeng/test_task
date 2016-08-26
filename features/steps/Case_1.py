import os, time
import requests
from selenium import webdriver
from behave import given, then, when
from lib.Config import Config
from support.Case_1_Page import Case_1_Page
from support.SkyEng_Login_Page import SkyEng_Login_Page
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

cf = Config()
cs = Case_1_Page()
lg = SkyEng_Login_Page()

skyengprod = cf.get_config('config/config.ini', 'links', 'skyengprod')
skyengstaging = cf.get_config('config/config.ini', 'links', 'skyengstaging')


@then(u'I select New Student')
def step_impl(context):
    cs.new_student(context)
    time.sleep(3)
    print(cs.new_student_mode_title(context))
    assert cs.new_student_mode_title(context) == "New Student mode"

@then(u'I select options General English, Beginner, 1st lesson')
def step_impl(context):
    cs.mode_general(context)
    cs.mode_level_beginner(context)
    time.sleep(2)
    cs.mode_lesson_1(context)
    time.sleep(1)

@when(u'I click Start the lesson')
def step_impl(context):
    context.browser.execute_script("$('.lessons_lesson_3O0jy:nth-child(2) .lessons_buttons-block_3coUp').click();")
    time.sleep(3)

@then(u'I see that lesson started')
def step_impl(context):
    print(cs.lesson_link(context))
    assert (cs.lesson_link(context)).is_displayed()
    print(cs.listen_repeat_title(context))
    assert cs.listen_repeat_title(context) == "Listen and repeat"

@then(u'I navigate to the lesson as a student')
def step_impl(context):
    link = context.browser.current_url
    print(link)
    global teacher_tab
    teacher_tab = context.browser.window_handles[0]
    cs.lesson_link(context).send_keys(Keys.CONTROL, Keys.SHIFT, "n")
    time.sleep(1)
    student_tab = context.browser.window_handles[1]
    global student_tab
    context.browser.switch_to_window(student_tab)
    time.sleep(1)

    if (os.environ['location'] == "staging"):
        context.browser.get(skyengstaging)
    elif (os.environ['location'] == "prod"):
        context.browser.get(skyengprod)
    time.sleep(4)

    print(lg.header_login_obj(context))
    assert (lg.header_login_obj(context)).is_displayed()
    lg.header_login_click(context)
    time.sleep(2)
    lg.username(context).send_keys("test@ya.ru")
    lg.password(context).send_keys("111111")
    lg.loginbutton(context)
    time.sleep(3)
    print(lg.username_dropdown(context))
    assert (lg.username_dropdown(context)).is_displayed()

    context.browser.get(link)
    time.sleep(5)

@then(u'I should see that lesson loaded')
def step_impl(context):
    print(cs.st_lesson_title(context))
    assert cs.st_lesson_title(context) == "GE 1. Hello!"
    print(cs.st_task_title(context))
    assert cs.st_task_title(context) == "Listen to the dialogues. Then repeat the dialogues."
    time.sleep(1)
    print(cs.st_1st_item_text(context))
    assert cs.st_1st_item_text(context) == "Hi, I'm Molly."

@when(u'I click Next Page as a teacher')
def step_impl(context):
    context.browser.switch_to_window(teacher_tab)
    time.sleep(1)
    cs.tch_2nd_page(context)
    time.sleep(1)
    cs.tch_1st_page(context)
    time.sleep(1)
    cs.tch_2nd_page(context)
    time.sleep(2)

@then(u'I see that page switched to a teacher')
def step_impl(context):
    print(cs.tch_2nd_page_content1(context))
    assert cs.tch_2nd_page_content1(context) == "pause"
    print(cs.tch_2nd_page_content2(context))
    assert cs.tch_2nd_page_content2(context) == "Student"
    print(cs.lesson_2nd_page_image1(context))
    assert (cs.lesson_2nd_page_image1(context)).is_displayed()
    print(cs.lesson_2nd_page_image2(context))
    assert (cs.lesson_2nd_page_image2(context)).is_displayed()

@then(u'I see that slide switches for student too')
def step_impl(context):
    context.browser.switch_to_window(student_tab)
    time.sleep(5)
    print(cs.st_task_title(context))
    assert cs.st_task_title(context) == "Listen to the dialogues. Then repeat the dialogues."
    print(cs.lesson_2nd_page_image1(context))
    assert (cs.lesson_2nd_page_image1(context)).is_displayed()
    print(cs.lesson_2nd_page_image2(context))
    assert (cs.lesson_2nd_page_image2(context)).is_displayed()

@when(u'I open a slide for Preview mode')
def step_impl(context):
    context.browser.switch_to_window(teacher_tab)
    time.sleep(1)
    context.browser.execute_script("$('.lesson-plan_item_2C7Er:nth-child(3) .lesson-plan_preview_2OGb2.ng-hide>span>span:nth-child(2)').click();")
    time.sleep(3)
    print(cs.tch_3rd_page_preview_title(context))
    assert cs.tch_3rd_page_preview_title(context) == "Preview mode. Only you can see this slide now."
    print(cs.tch_3rd_page_content1(context))
    assert cs.tch_3rd_page_content1(context) == "to read"
    print(cs.tch_3rd_page_content6(context))
    assert cs.tch_3rd_page_content6(context) == "to complete"

@then(u'I see that slide not switches and not shown for student')
def step_impl(context):
    context.browser.switch_to_window(student_tab)
    time.sleep(1)
    print(cs.st_task_title(context))
    assert cs.st_task_title(context) == "Listen to the dialogues. Then repeat the dialogues."
    print(cs.lesson_2nd_page_image1(context))
    assert (cs.lesson_2nd_page_image1(context)).is_displayed()
    print(cs.lesson_2nd_page_image2(context))
    assert (cs.lesson_2nd_page_image2(context)).is_displayed()

@then(u'I close the Preview mode of the slide as teacher')
def step_impl(context):
    context.browser.switch_to_window(teacher_tab)
    time.sleep(1)
    cs.tch_3rd_page_preview_close(context)
    time.sleep(1)
    print(cs.tch_2nd_page_content1(context))
    assert cs.tch_2nd_page_content1(context) == "pause"
    print(cs.tch_2nd_page_content2(context))
    assert cs.tch_2nd_page_content2(context) == "Student"
    print(cs.lesson_2nd_page_image1(context))
    assert (cs.lesson_2nd_page_image1(context)).is_displayed()
    print(cs.lesson_2nd_page_image2(context))
    assert (cs.lesson_2nd_page_image2(context)).is_displayed()
