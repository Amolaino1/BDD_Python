import time

from common_steps import *
from locators import Locators
from nose.tools import assert_false, assert_true
from selenium.webdriver.common.by import By


@given(u'the user is on the scheduling page')
def step_impl(context):
    context.helperfunc.navigate_to(env_variables.NOVA_BASE_URL + "/user-settings")


@when(u'the user clicks add new schedule')
def step_impl(context):
    context.helperfunc.click(Locators.ADD_NEW_SCHEDULE_BUTTON)


@when(u'types the name of the schedule')
def step_impl(context):
    context.helperfunc.enter_text(Locators.SCHEDULE_NAME_INPUT, "New Interview")
    context.helperfunc.clear_text(Locators.SCHEDULE_NAME_INPUT)


@when(u'inputs the interview URL')
def step_impl(context):
    context.helperfunc.enter_text(Locators.SCHEDULE_LOCATION_INPUT, "https://monday.com/")


@when(u'the user saves the schedule')
def step_impl(context):
    context.helperfunc.click(Locators.SAVE_SCHEDULE_BUTTON)


@then(u'the newly created schedule should be visible on the page')
def step_impl(context):
    time.sleep(5)
    assert_true("New Interview" in context.helperfunc._driver.page_source)


@when(u'the user clicks on edit on an existing interview schedule')
def step_impl(context):
    context.helperfunc.click(Locators.EDIT_SCHEDULE_BUTTON)


@when(u'changes the existing name to New inteview - updated')
def step_impl(context):
    context.helperfunc.click(Locators.SCHEDULE_NAME_INPUT)
    context.helperfunc.clear_text(Locators.SCHEDULE_NAME_INPUT)
    context.helperfunc.enter_text(Locators.SCHEDULE_NAME_INPUT," - updated")
    context.helperfunc.click(Locators.SAVE_SCHEDULE_BUTTON)


@when(u'user clicks on an existing schedule')
def step_impl(context):
    context.helperfunc.click(Locators.EDIT_SCHEDULE_BUTTON)


@when(u'clicks on the EDIT button')
def step_impl(context):
    pass


@when(u'user clicks on delete')
def step_impl(context):
    context.helperfunc.click(Locators.DELETE_SCHEDULE_BUTTON)


@then(u'the deleted schedule should no longer be available on the page')
def step_impl(context):
    pass
