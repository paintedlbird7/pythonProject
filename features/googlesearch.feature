# Created by rosaperez at 8/24/24
Feature: Google search test

  Scenario: Test google search
    Given I am on google search page
    When I type in text to search
    And I hit search button
    Then I should be on the search results page