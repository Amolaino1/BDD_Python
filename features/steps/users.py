import time
from common_steps import *
from locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@when('sales manager navigates to next page')
def click_nextpage(context):
    context.helperfunc.wait_for_loader_disappear()
    context.helperfunc.click(Locators.USERS_NEXT_PAGE_BUTTON)


@then('sales manager should see users in next page')
def assert_nextpage(context):
    context.helperfunc.assert_element_start_with_text(Locators.USERS_PER_PAGE, "11–20 of ")


@when("sales manager clicks on {field}")
def step_impl(context, field):
    COLUMN_TITLE_SORTING_BUTTON = (By.XPATH, "//*[@data-field='" + field + "' and @role='columnheader']")
    context.helperfunc.click(COLUMN_TITLE_SORTING_BUTTON)


@when("sales manager creates a user")
def step_impl(context):
    time_str = time.strftime("%Y%m%d%H%M%S")
    context.helperfunc.click(Locators.CREATE_USER_BUTTON)

    context.helperfunc.click(Locators.SELECT_USER_TYPE_BUTTON)
    context.helperfunc.click(Locators.USER_TYPE_USER_OPTION)
    context.helperfunc.enter_text(Locators.ORGANISATION_COMBOBOX, "GQR Test")
    context.helperfunc.wait_for_loader_disappear()
    context.helperfunc.enter_text(Locators.ORGANISATION_COMBOBOX, Keys.DOWN)
    context.helperfunc.enter_text(Locators.ORGANISATION_COMBOBOX, "\n")
    context.helperfunc.enter_text(Locators.ORGANISATION_COMBOBOX, Keys.RETURN)
    context.helperfunc.enter_text(Locators.USERNAME_INPUT, "SeleniumUser" + time_str)
    context.helperfunc.enter_text(Locators.EMAIL_INPUT, "SeleniumUser" + time_str + "@test.com")
    context.helperfunc.enter_text(Locators.FIRST_NAME_INPUT, "SeleniumUser" + time_str)
    context.helperfunc.enter_text(Locators.LAST_NAME_INPUT, "USER")
    context.helperfunc.enter_text(Locators.PASSWORD_INPUT, "TryItOut!123")
    context.helperfunc.click(Locators.SUBMIT_CREATE_USER_BUTTON)


@then("sales manager should see confirmation message")
def step_impl(context):
    context.helperfunc.wait_for_loader_disappear()
    context.helperfunc.assert_element_text(Locators.DIALOG_WINDOW_TITLE,
                                           "This client will have to be sent their login credentials.")
    context.helperfunc.click(Locators.DIALOG_WINDOW_CLOSE_BUTTON)
