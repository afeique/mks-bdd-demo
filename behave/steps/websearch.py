from behave import *
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

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
        'google-search-button': "//input[@value='Google Search' and @type='button' or @value='Google Search' and @type='submit']",
        'google-search-icon-button': "//button[@value='Search' and @aria-label='Google Search']",
        'google-result-stats': "//div[@id='resultStats']",
        'google-result-statistics': "//div[@id='resultStats']"
    }

    if formatted_english in lookup:
        return lookup[formatted_english]

    print('No xpath definition for "%s"' % english)
    assert False

@step('I visit "{url}"')
def test_visit_url(context, url):
    if not (url.startswith("http://") or url.startswith("https://")):
        context.driver.get("http://"+ url)
    else:
        context.driver.get(url)
    assert url in context.driver.current_url

@step('I see "{element}"')
def test_find_element(context, element):
    e = False
    xpath = english_to_xpath(element)
    try:
        e = context.driver.find_element_by_xpath(xpath)
    except:
        print('Could not find element with xpath "%s"' % xpath)
        assert False
    if e:
        assert isinstance(e, WebElement) is True
    return e

@step('"{element}" appears within "{wait_time}" seconds')
def test_wait_for_element(context, element, wait_time):
    e = False
    xpath = english_to_xpath(element)
    try:
        e = WebDriverWait(context.driver, float(wait_time)).until(EC.presence_of_element_located((By.XPATH, xpath)))
    except:
        print('Could not find element with xpath "%s"' % xpath)
        assert False
    if e:
        assert isinstance(e, WebElement) is True
    return e


@step('I enter "{data}" into "{element}"')
def test_enter_data_into_element(context, data, element):
    e = test_find_element(context, element)
    e.send_keys(data + Keys.ESCAPE)
    assert e.get_attribute('value') == data

@step('I click "{element}"')
def test_click_element(context, element):
    e = test_find_element(context, element)
    e.click()

