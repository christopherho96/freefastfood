from selenium import webdriver
import time

email = input("Enter your email address to receive coupon: ")
survey_url = "https://www.mypopeyesfeedback.com/Index.aspx?c=040323"

try:
    browser = webdriver.Chrome('./chromedriver')
    browser.get(survey_url)
except Exception as e:
    print(e)
    quit()

def click_next_button():
    next_button = browser.find_element_by_id("NextButton")
    next_button.click()
    time.sleep(0.5)

try:

    click_next_button()

    restaurant_number = browser.find_element_by_id('CN1')
    restaurant_number.send_keys('12258')

    browser.find_element_by_xpath("//select[@name='InputMonth']/option[text()='04']").click()
    browser.find_element_by_xpath("//select[@name='InputDay']/option[text()='10']").click()
    browser.find_element_by_xpath("//select[@name='InputHour']/option[text()='07']").click()
    browser.find_element_by_xpath("//select[@name='InputMinute']/option[text()='54']").click()
    browser.find_element_by_xpath("//select[@name='InputMeridian']/option[text()='PM']").click()
    click_next_button()
    click_next_button()

    radios = browser.find_elements_by_class_name("radioSimpleInput")
    radios[0].click()
    click_next_button()

    radios = browser.find_elements_by_class_name("radioSimpleInput")
    radios[0].click()
    click_next_button()

    radios = browser.find_elements_by_class_name("radioSimpleInput")
    radios[0].click()
    click_next_button()

    for radio in browser.find_elements_by_xpath("//*[@class='Opt5 inputtyperbloption']/span[@class='radioSimpleInput']"):
        radio.click()
    click_next_button()

    for radio in browser.find_elements_by_xpath("//*[@class='Opt5 inputtyperbloption']/span[@class='radioSimpleInput']"):
        radio.click()
    click_next_button()

    browser.find_element_by_xpath("//*[@class='Opt2 inputtyperbloption']/span[@class='radioSimpleInput']").click()
    click_next_button()

    for radio in browser.find_elements_by_xpath("//*[@class='Opt5 inputtyperbloption']/span[@class='radioSimpleInput']"):
        radio.click()
    click_next_button()

    browser.find_element_by_id("S000037").send_keys("The food was great, staff were very friendly!")
    click_next_button()

    click_next_button()

    click_next_button()

    try:
        browser.find_element_by_xpath("//*[@id='FNSR000067']/*[@class='Opt2 inputtyperbloption']/span[@class='radioSimpleInput']").click()
    except Exception as e:
        print(e)
    try:
        browser.find_element_by_xpath("//*[@id='FNSR000148']/*[@class='Opt1 inputtyperbloption']/span[@class='radioSimpleInput']").click()
    except Exception as e:
        print(e)

    try:
        browser.find_element_by_xpath("//*[@id='FNSR000041']/*[@class='Opt1 inputtyperbloption']/span[@class='radioSimpleInput']").click()
    except Exception as e:
        print(e)

    click_next_button()

    browser.find_element_by_xpath("//*[@class='Opt1 rbloption']/*[@class='radioButtonHolder']/span[@class='radioSimpleInput']").click()
    click_next_button()

    browser.find_element_by_xpath("//select[@name='R000134']/option[text()='One']").click()
    click_next_button()

    browser.find_element_by_id("S000058").send_keys(email)
    browser.find_element_by_id("S000059").send_keys(email)
    click_next_button()

except Exception as e:
    print("Automation failed due to error: {}".format(e))
