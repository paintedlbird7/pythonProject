# Created by rosaperez at 8/27/24
Feature: HM4filter

Scenario: Filter by Features Camera
    Then open ebay.com
    Then In search field type "iphone"
    Then Click the "Search" button
    Then filter "Features" option "Camera"

Scenario: Filter by Dress Length
    Then open ebay.com
    Then In search field type "dress"
    Then Click the "Search" button
    #Then filter "Dress Length" option "Short"
#
Scenario: Filter by Features Model
    Then open ebay.com
    Then In search field type "iphone"
    Then Click the "Search" button
    #Then filter "Model" option "iPhone 11"
