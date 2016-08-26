import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Case_1_Page:
    def menu_avatar(self, context):
        context.browser.find_element_by_css_selector('.menu_avatar-image_2aFIB').click()

    def new_student(self, context):
        context.browser.find_element_by_css_selector('.students_new_3eht4 .students_circle_3Klap').click() #.students_circle_3Klap

    def new_student_mode_title(self, context):
        return context.browser.find_element_by_css_selector('.notice_title_1LCpi>vim-gui-notice-title').text

    def mode_general(self, context):
        context.browser.find_element_by_css_selector('.tabs_item_HrEYk.tabs_selected_1jnrm').click()

    def mode_level_beginner(self, context):
        context.browser.find_element_by_css_selector('.tabs_size_16_1i9ng .tabs_item_HrEYk:nth-child(1)').click()

    def mode_lesson_index(self, context):
        context.browser.find_element_by_css_selector('.lessons_lessons-table_1-i1j .lessons_lesson_3O0jy:nth-child(1)').click()

    def mode_lesson_1_title(self, context):
        return context.browser.find_element_by_css_selector('.lessons_lessons-table_1-i1j .lessons_lesson_3O0jy:nth-child(2) .lessons_title_cQN_N').text

    def mode_lesson_1(self, context):
        context.browser.find_element_by_css_selector('.lessons_lessons-table_1-i1j .lessons_lesson_3O0jy:nth-child(2)').click()

    def mode_lesson_1_obj(self, context):
        return context.browser.find_element_by_css_selector('.lessons_lessons-table_1-i1j .lessons_lesson_3O0jy:nth-child(2)')

    def mode_lesson_1_hover(self, context):
        return context.browser.find_element_by_css_selector('.lessons_lessons-table_1-i1j .lessons_lesson_3O0jy:nth-child(2)').hoverover

    def start_lesson(self, context):
        context.browser.find_element_by_css_selector('.lessons_lesson_3O0jy:nth-child(2) .lessons_buttons-block_3coUp').click()
        #context.browser.find_element_by_css_selector('.button_root_22nBk').click()

    def lesson_link(self, context):
        return context.browser.find_element_by_css_selector('.default[value]')
        #return context.browser.find_element_by_css_selector('.default').get_attribute('value').contains('http')

    def lesson_link_text(self, context):
        return context.browser.find_element_by_xpath('//input[@value[contains(.,"http")]]')
        #return context.browser.find_element_by_xpath('//input[@value[contains(.,"http")]]')
        #return context.browser.find_element_by_css_selector('.default[value]').text

    def copy_link_btn(self, context):
        context.browser.find_element_by_css_selector('.alerts_plate_1r3XF .button_root_22nBk').click()

    def listen_repeat_title(self, context):
        return context.browser.find_element_by_css_selector('.b-vc-format-text__task:nth-child(1)').text

    def st_lesson_title(self, context):
        return context.browser.find_element_by_css_selector('.lesson-tab_left_3cpiE').text

    def st_task_title(self, context):
        return context.browser.find_element_by_css_selector('.b-vc-format-text__task').text

    def st_1st_item_text(self, context):
        return context.browser.find_element_by_css_selector('.b-vc-material-imageSet__item:nth-child(1) .b-vc-material-image__title').text

    def st_conf_status(self, context):
        return context.browser.find_element_by_css_selector('conference_statuses_2kUeJ')

    def tch_1st_page(self, context):
        context.browser.find_element_by_css_selector('div [class^="lesson-plan_item"]:nth-child(1) div[class*="lesson-plan_title-block"] span:nth-child(2)').click()
        #context.browser.find_element_by_css_selector('.lesson-plan_item_2C7Er:nth-child(1) .lesson-plan_title-block_3lZx7>span').click()

    def tch_2nd_page(self, context):
        context.browser.find_element_by_css_selector('.lesson-plan_item_2C7Er:nth-child(2) .lesson-plan_title-block_3lZx7>span').click()

    def tch_3rd_page(self, context):
        return context.browser.find_element_by_css_selector('.lesson-plan_item_2C7Er:nth-child(3) .lesson-plan_title-block_3lZx7')

    def tch_3rd_page_preview(self, context):
        context.browser.find_element_by_css_selector('.lesson-plan_item_2C7Er:nth-child(3) .lesson-plan_preview_2OGb2.ng-hide>span>span').click()

    def tch_3rd_page_preview_close(self, context):
        context.browser.find_element_by_css_selector('.lesson-plan_item_2C7Er:nth-child(3) .lesson-plan_preview-cross_12H0r').click()

    def tch_2nd_page_content1(self, context):
        return context.browser.find_element_by_css_selector('.b-vc-format-text__p:nth-child(3) .word_meaningful_2F-1C:nth-child(3) .word_word_2dfyX>span').text
    #"pause"

    def tch_2nd_page_content2(self, context):
        return context.browser.find_element_by_css_selector('.b-vc-format-text__p:nth-child(3) .word_meaningful_2F-1C:nth-child(6) .word_word_2dfyX>span').text
    #"Student"

    def st_2nd_page_content1(self, context):
        return context.browser.find_element_by_css_selector('.b-vc-format-text__p:nth-child(2) .word_word_2dfyX>span').text
    #"Excuse"

    def tch_3rd_page_content1(self, context):
        return context.browser.find_element_by_xpath('.//*[@id="viewport-legacy-scrollable"]//div[2]//li[1]/vim-word/span/span').text
    #to read

    def tch_3rd_page_content6(self, context):
        return context.browser.find_element_by_xpath('.//*[@id="viewport-legacy-scrollable"]//div[2]//li[6]/vim-word/span/span').text
    #to complete

    def lesson_2nd_page_image1(self, context):
        return context.browser.find_element_by_css_selector('.b-vc-material-image__single[src="//resource.skyeng.ru/image/custom/333/222/14fc90fc495b85fc1e796af9dbcc96ba.jpg"]')

    def lesson_2nd_page_image2(self, context):
        return context.browser.find_element_by_css_selector('.b-vc-material-image__single[src="//resource.skyeng.ru/image/custom/333/222/02744d114284e4a078969a68147b4ef3.jpg"]')

    def tch_3rd_page_preview_title(self, context):
        return context.browser.find_element_by_css_selector('.alerts_plate-text_33VhN').text
