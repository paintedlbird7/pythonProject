# Created by rosaperez at 9/3/24
Feature: Search functionality

  Scenario: Search for a valid product
    Given I got navigated to Home page
    When I enter valid product into the Search box field
    And I click on Search button
    Then Valid product should get displayed in Search results