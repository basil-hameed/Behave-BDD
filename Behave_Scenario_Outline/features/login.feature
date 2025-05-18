Feature: Login functionality for OrangeHRM Web App

  Scenario Outline: Login with different credentials - datasets
    Given the user is on the OrangeHRM login page
    When the user enters username "<username>" and password "<password>"
    And the user click login button
    Then login should "<result>"

    Examples:
      | username | password | result  |
      | Admin    | admin123 | success |
      | invalid  | pass33   | failure |
