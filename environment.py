from selenium import webdriver


def before_feature(context, feature):
    context.driver = webdriver.Chrome("/Users/apple/PycharmProjects/chromedriver")
    context.driver.maximize_window()
    context.driver.implicitly_wait(15)

def after_feature(context, feature):
    context.driver.quit()


