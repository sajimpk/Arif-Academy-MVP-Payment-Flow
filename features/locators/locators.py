from selenium.webdriver.common.by import By

class LoginPageLocators:
    PASSWORD_TAB = (By.XPATH, "//button[contains(text(), 'Password Login')]")
    IDENTIFIER_INPUT = (By.XPATH, "//form[@id='aa-login-password-form']//input[@name='identifier']")
    PASSWORD_INPUT = (By.XPATH, "//form[@id='aa-login-password-form']//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//form[@id='aa-login-password-form']//button[@type='submit']")

class CheckoutPageLocators:
    BILLING_FIRST_NAME = (By.ID, "billing_first_name")
    BILLING_ADDRESS_1 = (By.ID, "billing_address_1")
    BILLING_CITY = (By.ID, "billing_city")
    BILLING_EMAIL = (By.ID, "billing_email")
    PAYMENT_SSLCOMMERZ = (By.ID, "payment_method_sslcommerz")
    PLACE_ORDER = (By.ID, "place_order")
