from helper.helper_base import HelperFunc
from selenium import webdriver

caps = {}


def get_browser(browser, browser_version, platform, name, access_key):
    remote_url = "https://" + name + ":" + access_key + "@hub.lambdatest.com/wd/hub"
    caps['name'] = "Nova Web v1.3"
    caps['build'] = "Nova Web v1.3"
    caps['browserName'] = browser
    caps['version'] = browser_version
    caps['platform'] = platform
    caps['network'] = True
    caps['visual'] = True
    caps['video'] = True
    caps['console'] = True

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument('--headless')
        return HelperFunc(webdriver.Remote(command_executor=remote_url, desired_capabilities=caps))