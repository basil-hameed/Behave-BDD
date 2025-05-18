@smoke
Feature: Login Functionality on OrangeHRM Website

  @valid
  Scenario: Successful login with valid credentials
    Given I am on the orangehrm login page
    When I login with username "Admin" and password "admin123"
    And I click the login button
    Then I should be redirected to the dashboard page

  @invalid
  Scenario: Unsuccessful login with invalid credentials
    Given I am on the orangehrm login page
    When I login with username "invaliduser" and password "invalidpass"
    And I click the login button
    Then I should see an error message

  @random
  Scenario: Unsuccessful login with valid username and invalid password
    Given I am on the orangehrm login page
    When I login with username "Admin" and password "invalidpass"
    And I click the login button
    Then I should see an error message