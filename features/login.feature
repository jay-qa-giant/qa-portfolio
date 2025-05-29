Feature: Login functionality

  Scenario: Valid login
    Given I am on the login page
    When I login with username "student" and password "Password123"
    Then I should see the successful login page

  Scenario: Invalid username
    Given I am on the login page
    When I login with username "incorrectUser" and password "Password123"
    Then I should see an error message