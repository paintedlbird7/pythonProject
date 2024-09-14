Feature: Ebay regression

Background: start from ebay
  Then open eBay.com

Scenario: Main workflow - search for dress and make sure we land correctly
  Then open ebay.com
  Then In search field type "dress"
  Then Click "Search" button
#  Then All items are "dress" related
