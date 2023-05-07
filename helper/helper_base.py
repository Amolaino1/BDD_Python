import selenium.webdriver.common.by
from selenium.webdriver import ActionChains
import unicodedata
from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


class HelperFunc(object):
    __TIMEOUT = 30

    def __init__(self, driver):
        super(HelperFunc, self).__init__()
        ignored_exc = (NoSuchElementException, StaleElementReferenceException,)
        self._driver_wait = WebDriverWait(driver, HelperFunc.__TIMEOUT, ignored_exceptions=ignored_exc)
        self._driver = driver

    def navigate_to(self, url):
        self._driver.get(url)

    def get_current_url(self):
        return self._driver.current_url

    def get_current_title(self):
        return self._driver.title

    def maximize(self):
        self._driver.maximize_window()

    def close(self):
        self._driver.quit()

    # Helper functions that are used to identify the web locators

    def find_by_xpath(self, xpath):
        return self._driver_wait.until(EC.visibility_of_element_located((selenium.webdriver.common.by.By.XPATH, xpath)))

    def find_by_name(self, name):
        return self._driver_wait.until(EC.visibility_of_element_located((selenium.webdriver.common.by.By.NAME, name)))

    def find_by_id(self, id):
        return self._driver_wait.until(EC.visibility_of_element_located((selenium.webdriver.common.by.By.ID, id)))

    def enter_text(self, by_locator, text):
        return self._driver_wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def clear_text(self, by_locator):
        return self._driver_wait.until(EC.visibility_of_element_located(by_locator)).clear()

    def select_by_text(self, by_locator, text):
        self._driver_wait.until(EC.visibility_of_element_located(by_locator)).click()
        self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, "//li[text()='{}']".format(text)))).click()

    def click(self, by_locator):
        self._driver_wait.until(EC.visibility_of_element_located(by_locator))
        return self._driver_wait.until(EC.element_to_be_clickable(by_locator)).click()

    def get_element_text(self, by_locator):
        return self._driver_wait.until(EC.visibility_of_element_located(by_locator)).get_attribute('innerText')

    def get_element_attribute(self, by_locator, attribute):
        return self._driver_wait.until(EC.visibility_of_element_located(by_locator)).get_attribute(attribute)

    def assert_element_text(self, by_locator, element_text):
        self._driver_wait.until(EC.text_to_be_present_in_element(by_locator, element_text))
        web_element = self._driver_wait.until(EC.visibility_of_element_located(by_locator)).get_attribute('innerText')
        unicodedata.normalize('NFD', web_element)
        unicodedata.normalize('NFC', web_element)
        web_element = unicodedata.normalize('NFKD', web_element)
        web_element = str(web_element)
        assert_equal(web_element, element_text, "Expected: " + element_text + " but received " + web_element)

    def assert_element_attribute(self, by_locator, attribute, exp_attribute):
        actual_attribute = self._driver_wait.until(EC.visibility_of_element_located(by_locator)).get_attribute(attribute)
        assert_equal(actual_attribute, exp_attribute, "Expected: " + exp_attribute + " but received " + actual_attribute)

    def assert_element_start_with_text(self, by_locator, element_text):
        actual_text = self._driver_wait.until(EC.visibility_of_element_located(by_locator)).get_attribute('innerText')
        assert_true(actual_text.startswith(element_text), "Expected: " + element_text + " but received " + actual_text)

    def assert_element_exists(self, by_locator):
        assert_true(self._driver_wait.until(EC.visibility_of_element_located(by_locator)))

    def assert_element_does_not_exist(self, by_locator):
        assert_true(self._driver_wait.until(EC.invisibility_of_element_located(by_locator)))

    def triple_click_element(self, locator):
        triple_click_element = self._driver.find_element_by_xpath(locator)
        actions = ActionChains(self._driver)
        for i in range(4):
            actions.move_to_element(triple_click_element).click()
        actions.perform()

    def search_text_on_page(self, text):
        get_source = self._driver.page_source
        search_text = text
        print(search_text in get_source)

    def wait_for_loader_disappear(self):
        self._driver_wait.until(EC.invisibility_of_element_located(((By.CLASS_NAME, "MuiCircularProgress-svg"))))

    def wait_for_search_results_to_appear(self):
        self._driver_wait.until(EC.visibility_of_element_located(((By.ID, "talent-card-content"))))

    def scroll_into_view(self, by_locator):
        self._driver_wait.until(EC.visibility_of_element_located(by_locator)).execute_script("arguments[0].scrollIntoView();", by_locator)

    def scroll_into_view(self, by_locator):
        self._driver.execute_script("arguments[0].scrollIntoView();", self._driver_wait.until(EC.visibility_of_element_located((by_locator))))

    def window_handle(self):
        handles = self._driver.window_handles
        size = len(handles)
        for x in range(size):
            if handles[x] != self._driver.current_window_handle:
                self._driver.switch_to.window(handles[x])
