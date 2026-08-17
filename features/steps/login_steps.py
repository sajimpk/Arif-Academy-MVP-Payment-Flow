import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.locators.locators import LoginPageLocators

@given("I navigate to the home page")
def step_impl(context):
    context.driver.get(context.base_url)
    time.sleep(2)

@then('the page title should contain "{text1}" or "{text2}"')
def step_impl(context, text1, text2):
    title = context.driver.title
    print(f"Current page title: {title}")
    assert text1 in title or text2 in title, f"Title '{title}' does not contain '{text1}' or '{text2}'"

@given('I navigate to the login page "{url}"')
def step_impl(context, url):
    context.driver.get(url)
    time.sleep(3)

@when('I log in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    driver = context.driver
    
    # Check if we need to click the password login tab first
    try:
        pw_tab = driver.find_element(*LoginPageLocators.PASSWORD_TAB)
        if "is-active" not in pw_tab.get_attribute("class"):
            pw_tab.click()
            time.sleep(1)
    except Exception:
        print("Password login tab not found or already active.")

    # Find the username/email input inside the main Student Login form
    username_input = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(LoginPageLocators.IDENTIFIER_INPUT)
    )
    username_input.send_keys(username)

    # Find the password input inside the main Student Login form
    password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
    password_input.send_keys(password)

    # Find and click the login button inside the main Student Login form
    login_button = driver.find_element(*LoginPageLocators.SUBMIT_BUTTON)
    login_button.click()
    
    # Wait for navigation or message
    time.sleep(5)

@then("I should be redirected to the dashboard or home page")
def step_impl(context):
    current_url = context.driver.current_url
    print(f"Current URL after login: {current_url}")
    # Verify if login succeeded (URL changed or dashboard elements exist)
    # We can print current URL or assert something
    assert "login" not in current_url or "dashboard" in current_url or current_url == context.base_url or "profile" in current_url, \
        f"Login might have failed. Current URL: {current_url}"

@when("I navigate to the mock test page")
def step_impl(context):
    # Navigate to the main IELTS CBT mock tests page
    # Since the homepage is the primary landing page for CBT mocks, let's navigate there
    context.driver.get(context.base_url)
    time.sleep(3)

@then("I should see the mock test content or panel")
def step_impl(context):
    driver = context.driver
    # Check for keywords like IELTS or Mock or check page source
    page_source = driver.page_source.lower()
    assert "mock" in page_source or "ielts" in page_source, "Mock test page/content did not load successfully"
