from selenium import webdriver


def before_feature(context, feature):
    context.driver = webdriver.Chrome("/Users/apple/PycharmProjects/chromedriver")
    context.driver.implicitly_wait(10)

def after_feature(context, feature):
    context.driver.quit()


