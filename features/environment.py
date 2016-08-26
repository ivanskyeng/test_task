import os, sys, time
from behave import *
from selenium import webdriver
#from functions.Log_Results import Results
#from functions.Browserstak_Status import Changestatus

#status = Changestatus()
#log = Results()

# def before_all(context):
#     context.title = "ResultLogs/test_task.txt"
#     f = open(context.title, "w")
#     f.write("test_task Results: " + time.strftime("%Y-%m-%d %H:%M") + "\n\n")
#     f.close()

def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    #Browserstak from Local
    #'''desired_cap = {'name': context.scenario.name, 'browser': 'Chrome', 'browser_version': '45.0', 'os': 'OS X', 'os_version': 'Yosemite', 'resolution': '1280x1024', 'build': '113', 'project': 'test_task', 'name': context.scenario.name}
    #context.browser = webdriver.Remote(desired_capabilities=desired_cap, command_executor="http://user:token@hub.browserstack.com:80/wd/hub")
    #context.browser.implicitly_wait(30)'''

    context.browser.implicitly_wait(15)
    # #Browserstak from Jenkins
    # desired_capabilities = {}
    # #desired_capabilities['browserstack.debug'] = True
    # desired_capabilities['resolution'] = '1280x1024'
    # desired_capabilities['browser'] = os.environ["SELENIUM_BROWSER"]
    # desired_capabilities['browser_version'] = os.environ['SELENIUM_VERSION']
    # desired_capabilities['os'] = os.environ['SELENIUM_PLATFORM']
    # desired_capabilities['os_version'] = os.environ['SELENIUM_PLATFORM_VERSION']
    # desired_capabilities['name'] = context.scenario.name
    # desired_capabilities['build'] = os.environ['BUILD_NUMBER']
    # desired_capabilities['project'] = 'test_task'
    # #command_executor = "http://%s:%s@%s:%s/wd/hub" % ("user", "password", "hub.browserstack.com", "80")
    # #print (command_executor)
    # #context.browser = webdriver.Remote(desired_capabilities=desired_capabilities, command_executor=command_executor)
    # context.browser.maximize_window()

def before_step(context, step):
    context.step = step
    src = context.browser.page_source

def after_scenario(context, scenario):
    context.browser.quit()
    # if context.step.status == "failed":
    #     status.error(context)
    #     print ("Session Id for Failed Test:  "+context.browser.session_id)
    #     print ("Scenario Name: "+context.scenario.name)
    #     context.output = context.scenario.status.upper()
    #     res = context.scenario.name + " : " + context.output + "\n"
    #     log.log_results_to_file(context, context.title, res)
