from sys import platform
from selenium import webdriver
import time
survey_url="https://survey.medallia.ca/?McD-GSS-FeedlessSurvey"
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
if platform == "darwin":
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

try:
    browser = webdriver.Chrome('./chromedriver')
    browser.get(survey_url)
except Exception as e:
    print(e)

def click_next_button():
    next_button = browser.find_element_by_id("buttonNext")
    next_button.click()
    time.sleep(2)

def click_finish_button():
    finish_button = browser.find_element_by_id("buttonFinish")
    finish_button.click()
    time.sleep(2)

try:
    restaurant_number = browser.find_element_by_id('spl_q_mcd_gss_restaurant_number_text')
    restaurant_number.send_keys('40675')

    begin_survey_button = browser.find_element_by_id("buttonBegin")
    begin_survey_button.click()
    time.sleep(1)

    age_box = browser.find_elements_by_class_name("indicatorRadio")
    age_box[2].click()

    click_next_button()
    last_visit_date = browser.find_element_by_id("cal_q_mcd_gss_visit_date_date_")
    last_visit_date.send_keys('04/09/2021')

    dropdown_selectors = browser.find_elements_by_class_name("dropdown_dropdownSelector")
    hour_dropdown = dropdown_selectors[0]
    hour_dropdown.click()
    time.sleep(1)

    hour_drop_down_list_items = browser.find_elements_by_class_name("dropdown_dropdownListItem")
    hour_drop_down_list_items[2].click()
    time.sleep(1)

    minutes_dropdown = dropdown_selectors[2]
    minutes_dropdown.click()
    time.sleep(1)

    minutes_drop_down_list_items = browser.find_elements_by_class_name("dropdown_dropdownListItem")
    minutes_drop_down_list_items[27].click()

    amount_spent = browser.find_element_by_id("spl_q_mcd_gss_amount_text")
    amount_spent.send_keys("3.67")

    click_next_button()

    in_restaurant_radio_box = browser.find_elements_by_class_name("indicatorRadio")
    in_restaurant_radio_box[0].click()

    click_next_button()

    take_out_radio_box = browser.find_elements_by_class_name("indicatorRadio")
    take_out_radio_box[1].click()

    click_next_button()

    burger_check_box = browser.find_elements_by_class_name("indicatorCheckbox")
    burger_check_box[2].click()

    click_next_button()

    cheese_burger_check_box = browser.find_elements_by_class_name("indicatorCheckbox")
    cheese_burger_check_box[2].click()

    click_next_button()

    rating_cells = browser.find_elements_by_class_name("cellOption_input")
    rating_cells[0].click()
    rating_cells[5].click()
    rating_cells[10].click()
    rating_cells[15].click()
    rating_cells[20].click()

    click_next_button()

    radio_boxs = browser.find_elements_by_class_name("indicatorRadio")
    order_accurate_radio_box = radio_boxs[0]
    no_problems_experienced_radio_box = radio_boxs[3]
    order_accurate_radio_box.click()
    no_problems_experienced_radio_box.click()

    click_next_button()

    restaurant_experience_details_text_box = browser.find_element_by_class_name("textarea_textarea")
    restaurant_experience_details_text_box.send_keys("The food was great, staff was very friendly!")
    time.sleep(1)

    click_next_button()

    rating_cells = browser.find_elements_by_class_name("cellOption_input")
    rating_cells[0].click()

    click_next_button()

    covid_improvements_text_box = browser.find_element_by_class_name("textarea_textarea")
    covid_improvements_text_box.send_keys("Continue to make sure the kiosks are wiped down. I like using those.")
    time.sleep(1)

    click_next_button()

    rating_cells = browser.find_elements_by_class_name("cellOption_input")
    rating_cells[0].click()

    click_next_button()

    postal_code_text_box = browser.find_element_by_class_name("textField_textField")
    postal_code_text_box.send_keys("M1P0C7")
    time.sleep(1)

    radio_boxs = browser.find_elements_by_class_name("indicatorRadio")
    no_child_visited = radio_boxs[1]
    no_child_visited.click()

    click_next_button()

    radio_boxs  =browser.find_elements_by_class_name("indicatorRadio")
    email_coupon = radio_boxs[0]
    email_coupon.click()

    click_finish_button()

    email_text_box = browser.find_element_by_class_name("textField_textField")
    email_text_box.send_keys("ho.christopher.tak@gmail.com")

    click_finish_button()

except Exception as e:
    print("Automation failed due to error: {}".format(e))
