import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless")
options.add_argument("--guest")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = "https://www.saucedemo.com/"
login_standard_user = "standard_user"
password_all = "secret_sauce"
driver.get(base_url)
driver.maximize_window()

"""--------------Log in--------------------"""

print("Trying to Log in")
username = driver.find_element(By.XPATH, '//input[@id="user-name"]')
username.send_keys(login_standard_user)
password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
login_button.click()
inventory_url = "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url
assert inventory_url == get_url
print("Passed\n")

"""--------------Get Products From Catalog--------------------"""

"""---Product 1---"""
print("Trying get catalog product 1 name and price")
catalog_product_1_name = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
catalog_product_1_name_value = catalog_product_1_name.text
catalog_product_1_price = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[1]")
catalog_product_1_price_value = catalog_product_1_price.text
print(f"Passed. Name = {catalog_product_1_name_value}; Price = {catalog_product_1_price_value}.\n")

"""---Product 2---"""
print("Trying get catalog product 2 name and price")
catalog_product_2_name = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
catalog_product_2_name_value = catalog_product_2_name.text.replace('$', '')
catalog_product_2_price = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[2]")
catalog_product_2_price_value = catalog_product_2_price.text.replace('$', '')
print(f"Passed. Name = {catalog_product_2_name_value}; Price = {catalog_product_2_price_value}.\n")

"""--------------Get "Add to cart" and Cart Buttons of Products From Catalog--------------------"""
add_to_cart_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
add_to_cart_product_2 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
cart_button = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")

"""--------------Add Products To Cart--------------------"""
print("Trying add product 1 to cart")
add_to_cart_product_1.click()
assert cart_button.text == "1"
print("Passed\n")
print("Trying add product 2 to cart")
add_to_cart_product_2.click()
assert cart_button.text == "2"
print("Passed\n")

"""--------------Open Cart--------------------"""
cart_button.click()


"""--------------Sleep and close browser--------------------"""

time.sleep(1)
print("All tests passed. Closing browser")
driver.close()