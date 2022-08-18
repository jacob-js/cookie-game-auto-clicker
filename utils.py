from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def get_store_item_name(item: WebElement):
    text = item.find_element(By.TAG_NAME, "b").text
    name = text.replace("-", " ").split("   ")[0]
    return name


def get_store_item_count(item: WebElement):
    text = item.find_element(By.TAG_NAME, "b").text
    count = text.replace("-", " ").split("   ")[1]
    number = count.replace(",", "")
    return int(number)


def buy_item(items_to_buy, driver):
    max_key = max(items_to_buy, key=items_to_buy.get)
    to_buy = driver.find_element(By.XPATH, f'//*[@id="buy{max_key}"]')
    to_buy.click()
