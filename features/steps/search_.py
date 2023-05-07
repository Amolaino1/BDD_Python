from behave import *
from locators import Locators
from datetime import datetime
from selenium.webdriver.common.by import By
from env_variables import *

use_step_matcher("re")
DEFAULT_SEARCH_MATCH = "REQUIREMENTS Experience in designing, building and testing Java applications In-depth knowledge " \
                       "of popular Java frameworks like Spring (Boot, Core, MVC) and JPA (Hibernate) Familiarity with " \
                       "architecture styles/APIs (REST) Experience with Object-Oriented Design (OOD) Good knowledge of " \
                       "SQL Good delegation, time management skills and problem-solving abilities Familiarity with " \
                       "cloud platforms (AWS) and CI/CD pipeline in the cloud Knowledge of TDD and BDD approaches in " \
                       "software development Advocate of Agile methodologies Advanced knowledge of KISS, SOLID, " \
                       "DRY principles Excellent understanding of software design patterns "

first_talent_name = ""


@when("User search by text match")
def step_impl(context):
    context.helperfunc.enter_text(Locators.MATCH_INPUT, DEFAULT_SEARCH_MATCH)
    context.helperfunc.click(Locators.FIND_MATCH_BUTTON)


@then('User should see list of talents "(?P<talents_count>.+)"')
def step_impl(context, talents_count):
    context.helperfunc.assert_element_text(Locators.TALENTS_PER_PAGE_TEXT, talents_count)


@step('navigates to "(?P<page>.+)" page')
def step_impl(context, page):
    for i in range(int(page) - 1):
        context.helperfunc.wait_for_search_results_to_appear()
        context.helperfunc.click(Locators.NEXT_PAGE_BUTTON)


@step('filters by education schools "(?P<school>.+)"')
def step_impl(context, school):
    context.helperfunc.click(Locators.FILTER_EDUCATION_SECTION)
    context.helperfunc.click(Locators.FILTER_EDUCATION_EXPAND_FILTERS)
    context.helperfunc.click(Locators.FILTER_EDUCATION_INSTITUTION)
    context.helperfunc.enter_text(Locators.FILTER_EDUCATION_INPUT, school + "\n")


@step('filters by education degree "(?P<degree>.+)"')
def step_impl(context, degree):
    context.helperfunc.click(Locators.FILTER_EDUCATION_SECTION)
    context.helperfunc.enter_text(Locators.FILTER_EDUCATION_INPUT, degree + "\n")


@step('toggle ByeBias')
def step_impl(context):
    context.first_talent_name = context.helperfunc.get_element_text(Locators.FIRST_TALENT_NAME)
    context.first_talent_profile_img = context.helperfunc.get_element_attribute(Locators.FIRST_TALENT_PROFILE_IMG, "src")
    context.first_talent_initials = get_initials(context.first_talent_name)
    context.helperfunc.click(Locators.BYEBIAS_TOGGLE)


@then("User should see talent names with initials")
def step_impl(context):
    context.helperfunc.assert_element_text(Locators.FIRST_TALENT_NAME, context.first_talent_initials)


def get_initials(fullname):
    xs = (fullname)
    name_list = xs.split()
    initials = ""
    for name in name_list:  # go through each name
        initials += name[0].upper()+"."  # append the initial
    return initials


@then("User should see profile icon as default")
def step_impl(context):
    context.helperfunc.assert_element_attribute(Locators.FIRST_TALENT_PROFILE_IMG, "src", NOVA_BASE_URL + "/assets/logos/Nebula-color-stacked.png")


@step("hides a talent")
def step_impl(context):
    context.first_talent_name = context.helperfunc.get_element_text(Locators.FIRST_TALENT_NAME)
    context.helperfunc.click(Locators.HIDE_TALENT_BUTTON)


@then("talent card should disappear from the list")
def step_impl(context):
    locator = (By.XPATH, "//span[@text='"+context.first_talent_name+"']")
    context.helperfunc.assert_element_does_not_exist(locator)


@step("adds talent to new shortlist")
def step_impl(context):
    now = datetime.now()
    shortlist_name = "Selenium Search " + now.strftime("%d/%m/%Y %H:%M:%S")
    context.helperfunc.click(Locators.ADD_TO_SHORTLIST_ICON)
    context.helperfunc.click(Locators.CREATE_NEW_SHORTLIST_SECTION)
    context.helperfunc.enter_text(Locators.CREATE_NEW_SHORTLIST_NAME_INPUT, shortlist_name)
    context.helperfunc.click(Locators.CREATE_NEW_SHORTLIST_ADD_BUTTON)


@then("User should receive successful notification")
def step_impl(context):
    context.helperfunc.assert_element_text(Locators.CREATE_NEW_SHORTLIST_NOTIFICATION, "ADDED!")


@step('filters by keyword "(?P<keyword>.+)"')
def step_impl(context, keyword):
    context.helperfunc.click(Locators.FILTER_KEYWORD_SECTION)
    context.helperfunc.enter_text(Locators.FILTER_KEYWORD_INPUT, keyword + "\n")


@step('filters by experience "(?P<experience>.+)"')
def step_impl(context, experience):
    context.helperfunc.click(Locators.FILTER_EMPLOYMENT_SECTION)
    context.helperfunc.enter_text(Locators.FILTER_EMPLOYMENT_INPUT, experience + "\n")


@then("User should see 0 results message")
def step_impl(context):
    context.helperfunc.assert_element_text(Locators.NO_TALENTS_MESSAGE_TEXT, "No talent matches your search criteria.")


@then("User should see some talents")
def step_impl(context):
    context.helperfunc.assert_element_exists(Locators.TALENT_CARD)


@step("adds talent to new shortlist (?P<shortlist_name>.+)")
def step_impl(context, shortlist_name):
    context.helperfunc.click(Locators.ADD_TO_SHORTLIST_ICON)
    context.helperfunc.click(Locators.CREATE_NEW_SHORTLIST_SECTION)
    context.helperfunc.enter_text(Locators.CREATE_NEW_SHORTLIST_NAME_INPUT, shortlist_name)
    context.helperfunc.click(Locators.CREATE_NEW_SHORTLIST_ADD_BUTTON)
