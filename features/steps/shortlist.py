from common_steps import *
from locators import Locators
from nose.tools import assert_false, assert_true
from selenium.webdriver.common.by import By

use_step_matcher("re")


@when('user creates a shortlist')
def step_impl(context):
    context.helperfunc.click(Locators.CREATE_SHORTLIST_BTN)


@when('updates shortlist name to (?P<shortlist_name>.+)')
def step_impl(context, shortlist_name):
    context.helperfunc.click(Locators.EDIT_SHORTLIST_BTN)
    context.helperfunc.click(Locators.SAVE_SHORT_LIST_BTN)
    context.helperfunc.click(Locators.EDIT_SHORTLIST_BTN)
    context.helperfunc.clear_text(Locators.SHORTLIST_NAME_INPUT)
    context.helperfunc.enter_text(Locators.SHORTLIST_NAME_INPUT, shortlist_name)
    context.helperfunc.click(Locators.SAVE_SHORT_LIST_BTN)


@when('reads shortlist by name (?P<shortlist_name>.+)')
def step_impl(context, shortlist_name):
    SHORTLIST_BY_NAME = (By.XPATH, "(//a//span[contains(text(),'" + shortlist_name + "')])[1]")
    context.helperfunc.click(SHORTLIST_BY_NAME)


@when('removes shortlist (?P<shortlist_name>.+)')
def step_impl(context, shortlist_name):
    context.helperfunc.click(Locators.DELETE_SHORTLIST_BTN)
    context.helperfunc.click(Locators.DELETE_SHORTLIST_YES_BTN)


@when('removes all shortlists')
def step_impl(context):
    if (context.helperfunc.get_current_url() == env_variables.NOVA_BASE_URL + "/shortlist/empty"):
        pass
    try:
        while not (context.helperfunc.get_current_url() == env_variables.NOVA_BASE_URL + "/shortlist/empty"):
            context.helperfunc.click(Locators.DELETE_SHORTLIST_BTN)
            context.helperfunc.click(Locators.DELETE_SHORTLIST_YES_BTN)
            context.helperfunc.wait_for_loader_disappear()
    except:
        print("context.helperfunc.get_current_url() = " + context.helperfunc.get_current_url() )
        print("is it equal to expected? " + env_variables.NOVA_BASE_URL + "/shortlist/empty" )


@when('removes talent from shortlist')
def step_impl(context):
    context.helperfunc.click(Locators.REMOVE_TALENT_FROM_SHORTLIST_BTN)


@then('No talents should be there')
def step_impl(context):
    context.helperfunc.assert_element_text(Locators.NO_TALENTS_IN_SHORTLIST_MESSAGE,
                                           "This shortlist has no prospects in it.")


@then('No shortlists should be there')
def step_impl(context):
    context.helperfunc.assert_element_text(Locators.NO_SHORTLISTS_MESSAGE,
                                           "Begin a search, or create a shortlist to get started.")
    context.helperfunc.assert_element_does_not_exist(Locators.SHORTLIST_LINK)


@then("the (?P<shortlist>.+) should not be present on list")
def step_impl(context, shortlist):
    element = context.helperfunc._driver.find_element_by_tag_name("body")
    assert_false(shortlist in element.text)
