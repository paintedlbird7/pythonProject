# Created by rosaperez at 9/5/24
Feature: Register Account functionality

  Scenario: Register with mandatory fields
    Given I navigated to Register page
    When I enter mandatory fields
    And I click on Continue button
    Then Account should get created

Scenario: Register with all fields
  Given I navigated to Register page
  When I enter all fields
  And I click on Continue button
  Then Account should get created

Scenario: Register with a duplicate email address
  Given I navigated to Register page
  When I enter details into all fields except email fields
  And I enter existing accounts into email fields
  And I click on Continue button
  Then Proper warning message informing about duplicate account should be displayed

Scenario:  Register without providing any details
  Given I navigated to Register page
  When I don't enter anything in the fields
  And I click on Continue button
  Then Proper warning messages for every mandatory field should be displayed




