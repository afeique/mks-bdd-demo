from getgauge.python import *
# step, after_suite, Messages, DataStoreFactory

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re

p_whitespace = re.compile(r'\s+')
p_nonword = re.compile(r'[^\w-]+')

def format_english(english):
    f = re.sub(p_whitespace, '-', english.strip().lower())
    f = re.sub(p_nonword, '', f)
    return f

def english_to_xpath(english):
    formatted_english = format_english(english)
    lookup = {
        'google-in-title': "/html/head/title[contains(.,'Google')]",
        'google-search-field': "//input[@name='q' and @value='']",
        'google-search-box': "//input[@name='q' and @value='']",
        'google-search-button': "//input[@value='Google Search' and @type='submit']",
        'google-search-icon-button': "//button[@value='Search' and @aria-label='Google Search']",
        'google-result-stats': "//div[@id='resultStats']",
        'google-result-statistics': "//div[@id='resultStats']"
    }

    if formatted_english in lookup:
        return lookup[formatted_english]

    print('No xpath definition for "%s"' % english)
    assert False

class Context(object):
    pass

context = Context()

# --------------------------
# Gauge step implementations
# --------------------------


@step('Visit <url>')
def test_visit_url(url):
    if not (url.startswith("http://") or url.startswith("https://")):
        context.driver.get("http://"+ url)
    else:
        context.driver.get(url)
    assert url in context.driver.current_url

@step('Look for <element>')
def test_find_element(element):
    xpath = english_to_xpath(element)
    try:
        e = context.driver.find_element_by_xpath(xpath)
    except:
        Messages.write_message('Could not find element with xpath "%s"' % xpath)
    assert isinstance(e, WebElement) is True
    return e

@step('<element> appears within <wait_time> seconds')
def test_wait_for_element(element, wait_time):
    xpath = english_to_xpath(element)
    try:
        e = WebDriverWait(context.driver, float(wait_time)).until(EC.presence_of_element_located((By.XPATH, xpath)))
    except:
        Messages.write_message('Could not find element with xpath "%s"' % xpath)
    assert isinstance(e, WebElement) is True
    return e


@step('Enter <data> into <element>')
def test_enter_data_into_element(data, element):
    e = test_find_element(element)
    e.send_keys(data)
    assert e.get_attribute('value') == data

@step('Click <element>')
def test_click_element(element):
    e = test_find_element(element)
    e.click()


# ---------------
# Execution Hooks
# ---------------

@before_spec()
def before_websearch():
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)

@after_spec()
def after_websearch():
    context.driver.quit()