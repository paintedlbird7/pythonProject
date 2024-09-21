# Created by rosaperez at 9/12/24
Feature: HM4filter

Scenario: Filtering by multiple filters
    Then open ebay.com
    Then In search field type "dress"
    Then Click the "Search" button
    Then filter "Dress Length" option "Short"
    Then filter "Brand" option "Calvin Klein"
    And All items should be related to following
    # uncomment to test exception, expected Short, received/actual Long
#    And All items should be related to "Dress Length" value | "Long"
        | filter name  | filter value      |
        | Brand        | Calvin Klein    |
        | Dress Length | Short           |
