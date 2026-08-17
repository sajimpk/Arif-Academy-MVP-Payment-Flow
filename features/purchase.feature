Feature: Purchase Mock Test Plan Flow
  As a registered user or a guest
  I want to buy the Unlimited Plan 1 for Mock Test
  So that I can access unlimited mock exams and get redirected to the SSLCommerz payment page

  Scenario: Purchase plan WITH active login session
    Given I navigate to the login page "https://arifacademy.com/login-2/"
    When I log in with username "1212121212" and password "123456789"
    Then I should be redirected to the dashboard or home page
    When I add the 1 month unlimited mock test plan to cart
    And I navigate to the checkout page
    And I verify the checkout details and select SSLCommerz payment
    And I click on the Place Order button
    Then I should be redirected to the SSLCommerz payment checkout page

  Scenario: Purchase plan WITHOUT active login session
    Given I am not logged in
    When I add the 1 month unlimited mock test plan to cart
    And I navigate to the checkout page
    Then I should be redirected to the login page
    When I log in with username "1212121212" and password "123456789"
    Then I should be redirected to the checkout page
    When I verify the checkout details and select SSLCommerz payment
    And I click on the Place Order button
    Then I should be redirected to the SSLCommerz payment checkout page
