from behave import *
import time
from selenium.webdriver.support.ui import Select

@given("I land on main page")
def step_impl(context):
    context.driver.get("https://demo-biq.dev.tradecore.io/#/")
@then("First title is {headline}")
def step_imp(context,headline):
    head = context.driver.find_element_by_xpath('//h2[text()="Create your account"]')
    print(head)
    try:
        assert headline in head.text
    except Exception as e:
        print ('Assertion failed',format(e))



@when("I enter first name {first_name}")
def step_impl(context,first_name):
   name = context.driver.find_element_by_xpath('//input[@id="form-first_name"]')
   try:
       name.send_keys(first_name)
   except Exception as e:
       print('Can not find this element',e)

@step('I enter last name {last_name}')
def step_impl(context,last_name):
    entered_last_name = context.driver.find_element_by_xpath('//input[@id="form-last_name"]')
    try:
        entered_last_name.send_keys(last_name)
    except Exception as e:
        print('Can not find this element',e)


@step("I enter email {email}")
def step_impl(context,email):
    entered_mail = context.driver.find_element_by_xpath('//input[@id="form-email"]')
    try:
        entered_mail.send_keys(email)
    except Exception as e:
        print('Can not find this element', e)


@step("i enter password {password}")
def step_impl(context,password):
    entered_pass = context.driver.find_element_by_xpath('//input[@id="form-password"]')
    try:
        entered_pass.send_keys(password)
    except Exception as e:
        print('Can not find this element', e)


@step("I enter phone number {phone}")
def step_impl(context,phone):
    entered_phone = context.driver.find_element_by_xpath('//input[@id="form-telephone"]')
    try:
        entered_phone.send_keys(phone)
    except Exception as e:
        print('Can not find this element', e)


@step("i enter Birthday {b_day}")
def step_impl(context,b_day):
    entered_b_day = context.driver.find_element_by_xpath('//input[@id="form-date_of_birth"]')
    try:
        entered_b_day.send_keys(b_day)
    except Exception as e:
        print('Can not find this element', e)


@step("I enter postcode {post_code}")
def step_impl(context,post_code):
    entered_post_code = context.driver.find_element_by_xpath('//input[@id="form-addr_zip"]')
    try:
        entered_post_code.send_keys(post_code)
    except Exception as e:
        print('Can not find this element', e)


@step("I enter address line 1 {add_1}")
def step_impl(context,add_1):
    entered_add_1 = context.driver.find_element_by_xpath('//input[@id="form-addr_street"]')
    try:
        entered_add_1.send_keys(add_1)
    except Exception as e:
        print('Can not find this element', e)


@step("I enter address line 2 {add_2}")
def step_impl(context,add_2):
    entered_add_2 = context.driver.find_element_by_xpath('//input[@id="form-addr_line_2"]')
    try:
        entered_add_2.send_keys(add_2)
    except Exception as e:
        print('Can not find this element', e)


@step("I enter City name {city}")
def step_impl(context,city):
    entered_city = context.driver.find_element_by_xpath('//input[@id="form-addr_city"]')
    try:
        entered_city.send_keys(city)
    except Exception as e:
        print('Can not find this element', e)


@step("I submit the form")
def step_impl(context):
    submit = context.driver.find_element_by_xpath('//button[@id="button-step"]')
    try:
        submit.click()
    except Exception as e:
        print('Can not find this element', e)


@given("Landing page is opened")
def step_impl(context):
    time.sleep(4)
    pass


@then("Title is {title}")
def step_impl(context,title):
    head = context.driver.find_element_by_xpath(
        '//h2[text()="Have you traded in any of the following in the past three years?"]')
    print(head)
    try:
        assert title in head.text
    except Exception as e:
        print ('Assertion failed', format(e))


@when("I enter shares {item}")
def step_impl(context,item):
    select = context.driver.find_element_by_xpath('/descendant::a[@class="chosen-single chosen-default"][1]')
    try:
        select.click()
        option = context.driver.find_element_by_xpath(
            '/descendant::div[@class="chosen-drop"][2]//li[contains(text(),"'+item+'")]')
        option.click()
    except Exception as e:
        print('Can not find this element', e)

@step("I enter forex {item}")
def step_impl(context,item):
    select = context.driver.find_element_by_xpath('/descendant::a[@class="chosen-single chosen-default"][1]')
    try:
        select.click()
        option = context.driver.find_element_by_xpath(
            '/descendant::div[@class="chosen-drop"][3]//li[contains(text(),"' + item + '")]')
        option.click()
    except Exception as e:
        print('Can not find this element', e)



@step("I enter cfds {item}")
def step_impl(context,item):
    select = context.driver.find_element_by_xpath('/descendant::a[@class="chosen-single chosen-default"][1]')
    try:
        select.click()
        option = context.driver.find_element_by_xpath(
            '/descendant::div[@class="chosen-drop"][4]//li[contains(text(),"' + item + '")]')
        option.click()
    except Exception as e:
        print('Can not find this element', e)


@step("I enter Spread betting {item}")
def step_impl(context,item):
    select = context.driver.find_element_by_xpath('/descendant::a[@class="chosen-single chosen-default"][1]')
    try:
        select.click()
        option = context.driver.find_element_by_xpath(
            '/descendant::div[@class="chosen-drop"][5]//li[contains(text(),"' + item + '")]')
        option.click()
    except Exception as e:
        print('Can not find this element', e)


@step("I enter relevant expirience {item}")
def step_impl(context,item):
    select = context.driver.find_element_by_xpath('/descendant::a[@class="chosen-single chosen-default"][1]')
    try:
        select.click()
        time.sleep(3)
        select.click()
        time.sleep(3)
        option = context.driver.find_element_by_xpath(
            '/descendant::div[@class="chosen-drop"][6]//li[contains(text(),"' + item + '")]')
        option.click()
        time.sleep(3)
    except Exception as e:
        print('Can not find this element', e)


@step("I enter tranding platform {item}")
def step_impl(context,item):
    select = context.driver.find_element_by_xpath('/descendant::a[@class="chosen-single chosen-default"][1]')
    try:
        select.click()
        option = context.driver.find_element_by_xpath(
            '/descendant::div[@class="chosen-drop"][7]//li[contains(text(),"' + item + '")]')
        option.click()
    except Exception as e:
        print('Can not find this element', e)


@step("I enter tranding currency {item}")
def step_impl(context,item):
    # Scroll down to bottom
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    select = context.driver.find_element_by_xpath('/descendant::a[@class="chosen-single chosen-default"][1]')
    try:
        select.click()
        option = context.driver.find_element_by_xpath(
            '/descendant::div[@class="chosen-drop"][8]//li[contains(text(),"' + item + '")]')
        option.click()
    except Exception as e:
        print('Can not find this element', e)


@step("I enter aproximate anual income {item}")
def step_impl(context,item):
    select = context.driver.find_element_by_xpath('/descendant::a[@class="chosen-single chosen-default"][1]')
    try:
        select.click()
        option = context.driver.find_element_by_xpath(
            '/descendant::div[@class="chosen-drop"][9]//li[contains(text(),"' + item + '")]')
        option.click()
    except Exception as e:
        print('Can not find this element', e)


@step("I enter employment status {item}")
def step_impl(context,item):
    select = context.driver.find_element_by_xpath('/descendant::a[@class="chosen-single chosen-default"][1]')
    try:
        select.click()
        option = context.driver.find_element_by_xpath(
            '/descendant::div[@class="chosen-drop"][10]//li[contains(text(),"' + item + '")]')
        option.click()
    except Exception as e:
        print('Can not find this element', e)


@step("i enter aproximate value of assets {item}")
def step_impl(context,item):
    select = context.driver.find_element_by_xpath('/descendant::a[@class="chosen-single chosen-default"][1]')
    try:
        select.click()
        option = context.driver.find_element_by_xpath(
            '/descendant::div[@class="chosen-drop"][11]//li[contains(text(),"' + item + '")]')
        option.click()
    except Exception as e:
        print('Can not find this element', e)


@step("I check Terms and Conditions")
def step_impl(context):
    try:
        option = context.driver.execute_script("document.getElementsByClassName('checkbox').item(0).click()")
    except Exception as e:
        print('Can not find this element', e)


@step("I click on finish")
def step_impl(context):
    option = context.driver.find_element_by_xpath('//button[@id="button-step"]')
    try:
        option.click()
    except Exception as e:
        print('Can not find this element', e)


@given("I land on page 3")
def step_impl(context):
    time.sleep(10)
    pass



@step("Page 3 Title is {title}")
def step_impl(context,title):
    head = context.driver.find_element_by_xpath(
        '//title[text()="TradeCore - Account"]')
    print(head)
    try:
        assert title in head.text
        time.sleep(3)
    except Exception as e:
        print ('Assertion failed', format(e))