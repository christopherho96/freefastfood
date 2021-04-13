from selenium import webdriver
import time
survey_url = "https://www.mybkexperience.com/?AspxAutoDetectCookieSupport=1"

try:
    browser = webdriver.Chrome('./chromedriver')
    browser.get(survey_url)
except Exception as e:
    print(e)
    quit()

def click_next_button():
    next_button = browser.find_element_by_id("NextButton")
    next_button.click()
    time.sleep(2)

def click_finish_button():
    finish_button = browser.find_element_by_id("buttonFinish")
    finish_button.click()
    time.sleep(2)

try:
    restaurant_number = browser.find_element_by_id('Initial_StoreID')
    restaurant_number.send_keys('13729')
    click_next_button()

    browser.find_element_by_xpath("//select[@name='BKLocation']/option[text()='Ontario']").click()
    browser.find_element_by_xpath("//select[@name='InputMonth']/option[text()='04']").click()
    browser.find_element_by_xpath("//select[@name='InputDay']/option[text()='10']").click()
    browser.find_element_by_xpath("//select[@name='InputHour']/option[text()='07']").click()
    browser.find_element_by_xpath("//select[@name='InputMinute']/option[text()='54']").click()
    browser.find_element_by_xpath("//select[@name='InputMeridian']/option[text()='PM']").click()
    click_next_button()

except Exception as e:
    print("Automation failed due to error: {}".format(e))
