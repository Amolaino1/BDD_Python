from steps import locators
from behave import *
from steps.locators import Locators
from steps import env_variables


@given(u'User signs in to nova')
def login_if(context):
    context.helperfunc.wait_for_loader_disappear()
    if context.helperfunc.get_current_title() == "Sign in to Nebula":
        context.helperfunc.navigate_to(env_variables.NOVA_BASE_URL)
        context.helperfunc.enter_text(Locators.USERNAME, env_variables.NOVA_USERNAME)
        context.helperfunc.enter_text(Locators.PASSWORD, env_variables.NOVA_PASSWORD)
        context.helperfunc.click(Locators.LOGIN_BUTTON)


@step(u'the client is on Search page')
def login_and_go_to_search(context):
    login_if(context)
    context.helperfunc.navigate_to(env_variables.NOVA_BASE_URL + "/search")
    context.helperfunc.wait_for_loader_disappear()


@step(u'the client is on Shortlist page')
def login_and_go_to_shortlist(context):
    login_if(context)
    context.helperfunc.navigate_to(env_variables.NOVA_BASE_URL + "/shortlist")
    context.helperfunc.wait_for_loader_disappear()


@step(u'sales manager is on Users page')
def login_and_go_to_users(context):
    login_if(context)
    context.helperfunc.navigate_to(env_variables.NOVA_BASE_URL + "/admin/users")
    context.helperfunc.wait_for_loader_disappear()


@step(u'sales manager is on Organizations page')
def login_and_go_to_organizations(context):
    login_if(context)
    context.helperfunc.navigate_to(env_variables.NOVA_BASE_URL + "/admin/organizations")
    context.helperfunc.wait_for_loader_disappear()


