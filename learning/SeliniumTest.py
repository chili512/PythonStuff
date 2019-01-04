import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

try:
    browser = webdriver.Firefox()
    browser.get("https://www.earthtrack.rct.net.au")
    assert "Welcome to Earthtrack Fleet Management" in browser.title
    username = browser.find_element_by_name("Username")
    username.send_keys("SeleniumTest")
    password = browser.find_element_by_name("Password")
    password.send_keys("Python33!")
    button = browser.find_element_by_xpath("//*[@id=\"form\"]//input[@type=\"submit\"]")
    button.send_keys(Keys.RETURN)
    time.sleep(10.2)
    assert browser.find_element_by_id("chart-dashboard")

except NoSuchElementException:
    print("An exception occured")
except Exception:
    print("Oops")
finally:
    browser.close()
