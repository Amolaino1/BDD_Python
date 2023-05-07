import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from helper.helper_web import get_browser
from steps.common_steps import login_if
from steps.env_variables import *

caps = {}


def before_all(context):
    caps['browserName'] = context.config.userdata['browser']
    caps['version'] = context.config.userdata['browser_version']
    caps['platform'] = context.config.userdata['platform']
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    helper_func = get_browser(caps['browserName'], caps['version'], caps['platform'], context.config.userdata['user'],
                              context.config.userdata['accessKey'])
    context.helperfunc = helper_func
    context.helperfunc.navigate_to(NOVA_BASE_URL)
    context.helperfunc.maximize()
    login_if(context)


def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.helperfunc._driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=AttachmentType.PNG)


def after_all(context):
    context.helperfunc.close()