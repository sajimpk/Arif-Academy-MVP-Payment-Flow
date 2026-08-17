Feature: Arif Academy Automation MVP

  Scenario: Verify Home Page is accessible
    Given I navigate to the home page
    Then the page title should contain "Arif Academy" or "Mock Tests"

  Scenario: Verify Login and Mock Test Navigation
    Given I navigate to the login page "https://arifacademy.com/login-2/"
    When I log in with username "1212121212" and password "123456789"
    Then I should be redirected to the dashboard or home page
    When I navigate to the mock test page
    Then I should see the mock test content or panel
