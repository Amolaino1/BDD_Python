import time

from common_steps import *
from features.steps import env_variables
from locators import Locators
from nose.tools import assert_false, assert_true
from selenium.webdriver.common.by import By

@given('I am logged in as Administrator')
def step_impl(context):
    context.helperfunc.navigate_to(env_variables.NOVA_BASE_URL + "/search")
    context.helperfunc.enter_text(Locators.USERNAME, env_variables.NOVA_USERNAME)
    context.helperfunc.enter_text(Locators.PASSWORD, env_variables.NOVA_PASSWORD)
    context.helperfunc.click(Locators.LOGIN_BUTTON)

@when('I search for talent profiles')
def step_impl(context):
    context.helperfunc.enter_text(Locators.MATCH_INPUT, env_variables.TALENT_FULL_PROFILE_INPUT_QUERY)
    context.helperfunc.click(Locators.FIND_MATCH_BUTTON)
    context.helperfunc.scroll_into_view(Locators.TALENT_EMAIL_BUTTON)
    context.helperfunc.click(Locators.TALENT_EMAIL_BUTTON)
    context.helperfunc.click(Locators.LOOKUP_TOKEN_CONFIRM_BUTTON)

@then('I should be able to send email to talants')
def step_impl(context):
    context.helperfunc.enter_text(Locators.EMAIL_SUBJECT_FIELD, env_variables.EMAIL_SUBJECT)
    context.helperfunc.click(Locators.EMAIL_PERSONALIZED_GREETING)
    context.helperfunc.enter_text(Locators.EMAIL_BODY, env_variables.EMAIL_MESSAGE)
    context.helperfunc.click(Locators.EMAIL_SEND_BUTTON)
    context.helperfunc.assert_element_text(Locators.EMAIL_SENT_CONFIRMED_ALERT, "Your Email Will Be Sent")

@when('I access the shorslist page')
def step_impl(context):
    context.helperfunc.click(Locators.SHORTLISTS_BUTTON)
    context.helperfunc.scroll_into_view(Locators.TALENT_EMAIL_BUTTON)
    context.helperfunc.click(Locators.TALENT_EMAIL_BUTTON)
    context.helperfunc.click(Locators.LOOKUP_TOKEN_CONFIRM_BUTTON)

@then('I should be able to send email to talant')
def step_impl(context):
    context.helperfunc.enter_text(Locators.EMAIL_SUBJECT_FIELD, env_variables.EMAIL_SUBJECT)
    context.helperfunc.click(Locators.EMAIL_PERSONALIZED_GREETING)
    context.helperfunc.enter_text(Locators.EMAIL_BODY, env_variables.EMAIL_MESSAGE)
    context.helperfunc.click(Locators.EMAIL_SEND_BUTTON)
    context.helperfunc.assert_element_text(Locators.EMAIL_SENT_CONFIRMED_ALERT, "Your Email Will Be Sent")