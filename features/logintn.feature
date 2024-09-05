# Created by rosaperez at 9/5/24
Feature: Login Functionality

Scenario: Login with valid credentials
  Given I navigated to Login page
  When I enter valid email address and valid password into the field
  And I click on Login button
  Then I should get logged in

Scenario:
  Given I navigated to Login page
  When I enter invalid email address and valid password into the field
  And I click on Login button
  Then I should get a proper warning message

Scenario: Login with valid email and invalid password
  Given I navigated to Login page
  When I enter valid email address and invalid password into the field
  And I click on Login button
  Then I should get a proper warning message

Scenario: Login with invalid credentials
  Given I navigated to Login page
  When I enter invalid email address and invalid password into the field
  And I click on Login button
  Then I should get a proper warning message

Scenario:  Login without entering any credentials
  Given I got navigated to Login page
  When I don't enter anything into the into the email and password fields
  And I click on Login button
  Then I should get a proper warning message

