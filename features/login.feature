Feature: Login
  Verify login functionality for the application using Given/When/Then steps.

  Background:
    Given the login page is opened

  Scenario: Successful login with valid credentials
    When the user logs in with username "Sai" and password "Imedx@123"
    Then the user should be logged in successfully

  Scenario: Login fails with incorrect password
    When the user logs in with username "Sai" and password "WrongPassword"
    Then the login should fail with an error message

  Scenario: Login fails with empty username
    When the user logs in with username "" and password "Imedx@123"
    Then the login should fail with validation error

  Scenario: Login fails with empty password
    When the user logs in with username "Sai" and password ""
    Then the login should fail with validation error
