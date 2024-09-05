# Created by rosaperez at 9/3/24
Feature: Search functionality

@completed
Scenario: Search for a valid product
  Given I got navigated to Home page
  When I enter valid product into the Search box field
  And I click on Search button
  Then Valid product should get displayed in Search results

@completed
Scenario: I search for an invalid product
  Given I got navigated to Home page
  When I enter invalid product into the Search box field
  And I click on Search button
  And Proper message should be displayed in Search results

Scenario: Search without entering any product
  Given I got navigated to Home page
  When I don't enter anything into the Search box field
  And I click on Search button
  Then proper message will display in Search results
















