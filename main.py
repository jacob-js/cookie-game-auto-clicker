import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from utils import get_store_item_name, get_store_item_count, buy_item

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
money = driver.find_element(By.ID, "money").text
store = driver.find_elements(By.CSS_SELECTOR, "#store > div")

money = int(money.replace(",", ""))


items = {
    get_store_item_name(item): get_store_item_count(item) for item in store
    if len(item.find_element(By.TAG_NAME, "b").text) > 0
}


timeout = time.time() + (60*5)
buy_timeout = time.time() + 5
time.sleep(1)
while True:
    cookie.click()
    money = driver.find_element(By.ID, "money").text
    money = int(money.replace(",", ""))
    can_i_buy = {item: count for (item, count) in items.items() if count <= money}
    if time.time() > buy_timeout:
        buy_item(can_i_buy, driver)
        buy_timeout += 5
    if time.time() > timeout:
        break

driver.quit()
print(f"The money you earned : {money}")
