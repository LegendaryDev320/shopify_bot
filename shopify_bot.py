import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def load_information():
    profile = {
        "email": "haha.dreamy@gmail.com",
        "firstname": "aaa",
        "lastname": "bbb",
        "ship_address": {
            "country": "Mexico",
            "address": "aaaa",
            "city": "",
            "state": "",
            "zipCode": "",
            "apartment": ""
        },
        "bill_address": "",
        "credit_card_info": "",
        "coupon_code": "",
        "place_order": ""
    }
    return profile


def load_product_quantity():
    product_quantity = {
        "quantity": 5,
        "url": "https://tastesalud.com/products/passion-fruit-bundle"
    }
    return product_quantity


def input_credit_info(driver):
    card_info = {
        "number": "11111",
        "expire_date": "0232",
        "code": "2341asd",
        "name": "asdf"
    }
    input_number = driver.find_element(By.ID, "number")
    input_number.send_keys(card_info["number"])
    input_expire_date = driver.find_element(By.ID, "expiry")
    input_expire_date.send_keys(card_info["expire_date"])
    input_code = driver.find_element(By.ID, "verification_value")
    input_code.send_keys(card_info["code"])
    input_name = driver.find_element(By.ID, "name")
    input_name.send_keys(card_info["name"])


def input_ship_address(driver, profile):
    select_deliver = Select(driver.find_element(By.ID, "Select0"))
    select_deliver.select_by_visible_text(profile.get("ship_address").get("country"))
    input_firstname = driver.find_element(By.XPATH, '//input[@id="TextField0"]')
    input_firstname.send_keys(profile.get("firstname"))
    input_lastname = driver.find_element(By.XPATH, '//input[@id="TextField1"]')
    input_lastname.send_keys(profile.get("lastname"))
    input_address = driver.find_element(By.XPATH, '//input[@id="shipping-address1"]')
    input_address.send_keys(profile.get("ship_address").get("address"))
    input_apart = driver.find_element(By.XPATH, '//input[@id="TextField2"]')
    input_apart.send_keys(profile.get("ship_address").get("apartment"))
    # differs from country
    city_id = ""
    state_id = ""
    post_id = ""
    if profile.get("ship_address").get("country") == "United States":
        city_id = "TextField44"
        state_id = "Select17"
        post_id = "TextField45"
    elif profile.get("ship_address").get("country") == "Mexico":
        city_id = "TextField48"
        state_id = "Select18"
        post_id = "TextField47"
    elif profile.get("ship_address").get("country") == 'Canada':
        city_id = "TextField49"
        state_id = "Select19"
        post_id = "TextField50"
    input_city = driver.find_element(By.XPATH, f'//input[@id="{city_id}"]')
    input_city.send_keys(profile.get("ship_address").get("city"))
    input_postal_code = driver.find_element(By.XPATH, f'//input[@id="{post_id}"]')
    input_postal_code.send_keys(profile.get("ship_address").get("zipCode"))
    select_state = Select(driver.find_element(By.ID, state_id))
    select_state.select_by_value(profile.get("ship_address").get("state"))


def input_bill_address(driver, profile):
    select_deliver = Select(driver.find_element(By.ID, "Select2"))
    select_deliver.select_by_visible_text(profile.get("ship_address").get("country"))
    input_firstname = driver.find_element(By.XPATH, '//input[@id="TextField6"]')
    input_firstname.send_keys(profile.get("firstname"))
    input_lastname = driver.find_element(By.XPATH, '//input[@id="TextField7"]')
    input_lastname.send_keys(profile.get("lastname"))
    input_address = driver.find_element(By.XPATH, '//input[@id="billing-address1"]')
    input_address.send_keys(profile.get("bill_address").get("address"))
    input_apart = driver.find_element(By.XPATH, '//input[@id="TextField8"]')
    input_apart.send_keys(profile.get("bill_address").get("apartment"))
    # differs from country
    city_id = "TextField9"
    state_id = "Select3"
    post_id = "TextField10"
    input_city = driver.find_element(By.XPATH, f'//input[@id="{city_id}"]')
    input_city.send_keys(profile.get("bill_address").get("city"))
    input_postal_code = driver.find_element(By.XPATH, f'//input[@id="{post_id}"]')
    input_postal_code.send_keys(profile.get("bill_address").get("zipCode"))
    select_state = Select(driver.find_element(By.ID, state_id))
    select_state.select_by_value(profile.get("bill_address").get("state"))


def main():
    try:
        product = load_product_quantity()
        url = product.get("url")
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # chrome_driver = "C:\chromedriver.exe"
        driver = webdriver.Chrome(chrome_options)
        print(driver.title)
        driver.get(url)
        print("chrome opened")
        submit_button = driver.find_element(By.XPATH,
                                            '//button[contains(@class, "product-form__submit") and @type="submit"]')
        # When popup comes, removes it
        popup_dlg = driver.find_element(By.ID, "amped-8274-38728")
        if popup_dlg and popup_dlg.is_displayed():
            driver.find_element(By.ID, "el_4JqkKNzNkA9").click()

        submit_button.click()
        print("Add to bag clicked")
        # Wait for a button to finish loading
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.product-form__submit.loading'))
        )

        # Optionally, wait for the 'loading' class to disappear
        WebDriverWait(driver, 10).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.product-form__submit.loading'))
        )

        quantity = product.get("quantity")
        current_quantity = (driver.find_element(By.XPATH, '//span[@class="rebuy-cart__flyout-item-quantity-widget'
                                                          '-label"]')
                            .text.strip())
        print(f"current_quantity: {current_quantity}")
        increase_button = driver.find_element(By.XPATH,
                                              '//button[contains(@alt, "Increase quantity") and @type="button"]')
        decrease_button = driver.find_element(By.XPATH,
                                              '//button[contains(@alt, "Decrease quantity") and @type="button"]')
        dif = quantity - int(current_quantity)
        step = -1 if dif < 0 else 1
        while dif != 0:
            dif += step
            if step < 0:
                decrease_button.click()
            else:
                increase_button.click()
        checkout_button = driver.find_element(By.XPATH,
                                              '//button[contains(@class, "rebuy-cart__checkout-button") and '
                                              '@type="button"]')
        checkout_button.click()
        print("checkout button clicked")
        # Wait for a new page to be loaded
        WebDriverWait(driver, 10).until(
            EC.title_contains("Checkout")  # Replace with expected title or other condition
        )

        # Optionally, wait for a specific element to be visible or present
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="checkout-main"]'))
        )
        # load personal information
        profile = load_information()
        # input email
        input_email = driver.find_element(By.XPATH, '//input[@id="email"]')
        input_email.send_keys(profile.get("email"))
        # input ship address
        input_ship_address(driver, profile)
        # input billing address
        input_bill_address(driver, profile)
        # input credit card info
        input_credit_info(driver)

        # press pay button
        pay_button = driver.find_element(By.ID, "checkout-pay-button")
        pay_button.click()

        time.sleep(2)
        driver.close()
        time.sleep(5)
    except Exception as e:
        print(f"error occured: {e}")
    print('DONE')


if __name__ == '__main__':
    main()
