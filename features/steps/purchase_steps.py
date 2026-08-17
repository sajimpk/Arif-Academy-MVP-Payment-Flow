import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.locators.locators import CheckoutPageLocators

@given("I am not logged in")
def step_impl(context):
    # Clear all cookies to ensure a guest/not logged in session
    context.driver.delete_all_cookies()
    context.driver.refresh()
    time.sleep(2)

@when("I add the 1 month unlimited mock test plan to cart")
def step_impl(context):
    # Navigating directly to WooCommerce add-to-cart link is standard and robust
    add_to_cart_url = "https://arifacademy.com/?add-to-cart=35998"
    context.driver.get(add_to_cart_url)
    time.sleep(5)

@when("I navigate to the checkout page")
def step_impl(context):
    checkout_url = "https://arifacademy.com/checkout/"
    context.driver.get(checkout_url)
    time.sleep(6)

@then("I should be redirected to the login page")
def step_impl(context):
    # Confirm redirected to login
    current_url = context.driver.current_url
    assert "login-2" in current_url, f"Expected redirect to login page, but current URL is: {current_url}"

@then("I should be redirected to the checkout page")
def step_impl(context):
    # Wait for the redirection to checkout page to complete after login
    checkout_url = "https://arifacademy.com/checkout/"
    # Wait up to 10 seconds for checkout page load
    WebDriverWait(context.driver, 10).until(
        lambda driver: "checkout" in driver.current_url
    )
    time.sleep(4)

@when("I verify the checkout details and select SSLCommerz payment")
def step_impl(context):
    driver = context.driver
    
    # Verify billing email is present (this confirms WooCommerce checkout fields are fully loaded)
    email_field = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(CheckoutPageLocators.BILLING_EMAIL)
    )
    email_val = email_field.get_attribute("value")
    print(f"Verified billing email value: {email_val}")
    assert email_val != "", "Billing email should not be empty"

    # Select SSLCommerz payment method
    ssl_radio = driver.find_element(*CheckoutPageLocators.PAYMENT_SSLCOMMERZ)
    if not ssl_radio.is_selected():
        driver.execute_script("arguments[0].click();", ssl_radio)
        time.sleep(2)

@when("I click on the Place Order button")
def step_impl(context):
    driver = context.driver
    place_order_btn = driver.find_element(*CheckoutPageLocators.PLACE_ORDER)
    driver.execute_script("arguments[0].click();", place_order_btn)
    # Wait for redirection to payment gateway
    time.sleep(12)

@then("I should be redirected to the SSLCommerz payment checkout page")
def step_impl(context):
    current_url = context.driver.current_url
    print(f"Payment gateway URL: {current_url}")
    assert "sslcommerz" in current_url or "sslcz" in current_url, \
        f"Expected to redirect to SSLCommerz gateway, but current URL is: {current_url}"
