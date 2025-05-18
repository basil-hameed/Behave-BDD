Feature: Login Functionality on SauceDemo

  Scenario: Successful login with valid credentials
    Given I am on the sauce demo login page
    When I enter valid username and password
    And I click the login button
    Then I should be redirected to the inventory page

Scenario: Unsuccessful login with invalid credentials
    Given I am on the sauce demo login page
    When I enter invalid username and password
    And I click the login button
    Then I should see an error message