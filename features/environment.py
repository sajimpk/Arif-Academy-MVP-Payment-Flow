import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    print("Setting up global test environment...")
    context.base_url = "https://arifacademy.com/"

def before_scenario(context, scenario):
    print(f"Starting scenario: {scenario.name}")
    options = webdriver.ChromeOptions()
    # By default, we run in headless mode for CI/CD compatibility,
    # but we can disable this if needed.
    # options.add_argument("--headless")
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Initialize Chrome WebDriver
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    context.driver.implicitly_wait(10)

def after_scenario(context, scenario):
    print(f"Finishing scenario: {scenario.name}")
    if hasattr(context, "driver"):
        context.driver.quit()

def after_all(context):
    print("Teardown global test environment complete.")
