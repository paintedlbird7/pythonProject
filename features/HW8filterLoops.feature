# Created by rosaperez at 9/12/24
Feature: HM4filter

Scenario: Filter by Dress Length
    Then open ebay.com
    Then In search field type "dress"
    Then Click the "Search" button
    Then filter "Dress Length" option "Short"
    And All items should be related to "Dress Length" value | "Short"