from behave import given, when, then
from locators import Locators
import env_variables
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains

@when(u'sales manager creates new organization with required fields')
def step_impl(context):
    now = datetime.now()
    context.helperfunc.click(Locators.CREATE_NEW_ORG_BUTTON)
    context.helperfunc.enter_text(Locators.ORG_NAME_INPUT, "Selenium organization" + now.strftime("%d/%m/%Y %H:%M:%S"))
    context.helperfunc.enter_text(Locators.NUMBER_OF_CONTACTS_INPUT, 4)
    context.helperfunc.click(Locators.SUBMIT_BUTTON_NEW_ORG)


@then(u'sales manager should see the organization created')
def step_impl(context):
    context.helperfunc.assert_element_text(Locators.TOAST_MESSAGE, "CREATED SUCCESSFULLY")


@when(u'sales manager creates new organization without required fields')
def step_impl(context):
    context.helperfunc.click(Locators.CREATE_NEW_ORG_BUTTON)
    context.helperfunc.click(Locators.SUBMIT_BUTTON_NEW_ORG)


@then(u'sales manager should see a notification indicating that entry can not be empty')
def step_impl(context):
    context.helperfunc.assert_element_text(Locators.ORG_NAME_INPUT_VALIDATION, "Organization Name is required.")


@when(u'sales manager creates new organization with an existing name')
def step_impl(context):
    context.helperfunc.click(Locators.CREATE_NEW_ORG_BUTTON)
    context.helperfunc.enter_text(Locators.ORG_NAME_INPUT, "GQR")
    context.helperfunc.enter_text(Locators.NUMBER_OF_CONTACTS_INPUT, 4)
    context.helperfunc.click(Locators.SUBMIT_BUTTON_NEW_ORG)


@then(u'sales manager should see a notification indicating that an organization with such name already exist')
def step_impl(context):
    context.helperfunc.assert_element_text(Locators.ASSERT_ORG_ALREADY_EXIST,
                                           "An organization with this name already exists.")
