import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
# chrome_options = webdriver.ChromeOptions()
# # Connect to the existing Chrome instance
# chrome_service = webdriver.ChromeService(executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe")  # Replace with your chromedriver path
# # chrome_service.("Debugger.enable", {})

# driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
# driver.get('https://tastesalud.com/products/passion-fruit-bundle')
# # try:
# #     submit_button = driver.find_element_by_css_selector(".product-form__submit.button[type='submit']")
# #     submit_button.click()
# #     print("Clicked the submit button successfully.")
# # except Exception as e:
# #     print(f"Failed to click the submit button: {e}")

# time.sleep(10)  #
# # driver.

# response = requests.get(url)

# soup = BeautifulSoup(response.text, 'html.parser')
# button = soup.find('button', {'class': lambda x: x and 'product-form__submit' in x.split(), 'type': 'submit'})
# if not button:
#     print("Button found:")
#     quit()

def loadInformation():
    profile = {
        "email" : "haha.dreamy@gmail.com",
        "firstname" : "aaa",
        "lastname" : "bbb",
        "ship_address" : {
            "country": "Mexico",
            "address": "aaaa",
            "city": "",
            "state": "",
            "zipCode": "",
            "apartment": ""
        },
        "bill_address" : "",
        "credit_card_info" : "",
        "coupon_code" : "",
        "place_order" : ""
    }
    return profile
def loadCreditCardInfo():
    cardInfo = {
        "number": "11111",
        "expire_date": "23/423",
        "code": "2341asd",
        "name": "asdf"
    }
    return cardInfo

def inputShipAddress(driver, profile):
    select_deliver = Select(driver.find_element(By.ID, "Select0"))
    select_deliver.select_by_visible_text(profile.ship_address.country)
    input_firstname = driver.find_element(By.XPATH, '//input[@id="TextField0"]')
    input_firstname.send_keys(profile.firstname)
    input_lastname = driver.find_element(By.XPATH, '//input[@id="TextField1"]')
    input_lastname.send_keys(profile.lastname)
    input_address = driver.find_element(By.XPATH, '//input[@id="shipping-address1"]')
    input_address.send_keys(profile.ship_address.address)
    input_apart = driver.find_element(By.XPATH, '//input[@id="TextField2"]')
    input_apart.send_keys(profile.ship_address.apartment)
    input_city = driver.find_element(By.XPATH, '//input[@name="city"]')
    input_city.send_keys(profile.ship_address.city)
    input_postalCode = driver.find_element(By.XPATH, '//input[@name="postalCode"]')
    input_postalCode.send_keys(profile.ship_address.zipCode)

    select_deliver = Select(driver.find_element(By.NAME, "zone"))
    select_deliver.select_by_value(profile.ship_address.state)

def main():
    try: 
        url = 'https://tastesalud.com/products/passion-fruit-bundle'
        driver = webdriver.Chrome()
        driver.get(url)

        submit_button = driver.find_element(By.XPATH, '//button[contains(@class, "product-form__submit") and @type="submit"]')
        submit_button.click()
        quantity = 5
        current_quantity = driver.find_element(By.XPATH, '//span[@class="rebuy-cart__flyout-item-quantity-widget-label"]').text().strip()
        print(current_quantity)
        increase_button = driver.find_element(By.XPATH, '//button[contains(@alt, "Increase quantity") and @type="button"]')
        decrease_button = driver.find_element(By.XPATH, '//button[contains(@alt, "Decrease quantity") and @type="button"]')
        dif = quantity - current_quantity
        step = -1 if dif < 0 else 1
        while dif != 0 :
            dif += step
            if step < 0:
                decrease_button.click()
            else :
                increase_button.click()
        checkout_button = driver.find_element(By.XPATH, '//button[contains(@class, "rebuy-cart__checkout-button") and @type="button"]')
        checkout_button.click

        # load personal information
        profile = loadInformation()
        #input email
        input_email = driver.find_element(By.XPATH, '//input[@id="email"]')
        input_email.send_keys(profile.email)
        #input ship address
        inputShipAddress(driver, profile)


        time.sleep(0.5)
        driver.close()
        time.sleep(5)
    except Exception as e:
        print(f"error occured: {e}")
    
    print('DONE')


if __name__ == '__main__':
    main()