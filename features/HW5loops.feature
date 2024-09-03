Feature: hw3

Scenario: Main workflow - search for dress and make sure we land correctly
  Then open ebay.com
  Then In search field type "dress"
  Then Click the "Search" button
  Then All items are "dress" related

  Scenario: Search functionality- happy path
  Then open ebay.com
  Then In search field type "iphone"
  Then Click the "Search" button
  Then Item list should have only "iphone" related