# import time

# from common_steps import *
# from features.steps import env_variables
# from locators import Locators
# from nose.tools import assert_false, assert_true
# from selenium.webdriver.common.by import By

from behave import *
from locators import Locators
from datetime import datetime
from selenium.webdriver.common.by import By
from env_variables import *


use_step_matcher("re")
DEFAULT_SEARCH_MATCH = "Starting is as easy as putting in a relevant portion of a job description or even a list of skills"

@when('I run a search for talent profiles')
def step_impl(context):
    context.helperfunc.enter_text(Locators.MATCH_INPUT, DEFAULT_SEARCH_MATCH)
    context.helperfunc.click(Locators.FIND_MATCH_BUTTON)
    context.helperfunc.scroll_into_view(Locators.OPEN_TALENT_FULL_PROFILE_IN_NEW_TAB_BUTTON)
    context.helperfunc.click(Locators.OPEN_TALENT_FULL_PROFILE_IN_NEW_TAB_BUTTON)


@then('I should be a able to view talents full profile')
def step_impl(context):
    context.helperfunc.window_handle()
    context.helperfunc.assert_element_exists(Locators.TALENT_PROFILE_READ_MORE_BUTTON)


@when('I visit the shortlist page')
def step_impl(context):
    context.helperfunc.click(Locators.SHORTLISTS_BUTTON)
    context.helperfunc.scroll_into_view(Locators.EXPAND_TALENT_FULL_PROFILE)
    context.helperfunc.click(Locators.EXPAND_TALENT_FULL_PROFILE)
    context.helperfunc.scroll_into_view(Locators.OPEN_IN_NEW_TAB)
    context.helperfunc.click(Locators.OPEN_IN_NEW_TAB)


@then('I should be able to view talents full profile')
def step_impl(context):
    context.helperfunc.window_handle()
    context.helperfunc.assert_element_exists(Locators.TALENT_PROFILE_READ_MORE_BUTTON)
    context.helperfunc.assert_element_exists(Locators.READ_MORE)
