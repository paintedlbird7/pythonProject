Feature: Ebay regression

Background: start from ebay
  Then open eBay.com

Scenario Outline: Main workflow - header navigation links
  And goto <link text>
  Then check landing on <expected title>

  Examples:  left top links
    | link text | expected title    |
    | Watchlist | Watchlist related |
#    | Sell      | Sell related      |
#    | My Ebay   | My Ebay related   |
#
#  Examples:  right top links
#    | link text | expected title    |
#    | Watchlist | Watchlist related |
#    | Sell      | Sell related      |
#    | My Ebay   | My Ebay related   |

Scenario: Main workflow - Daily Deals
  And goto  Daily Deals
  Then check landing on Daily Deals on eBay | Best deals and Free Shipping

Scenario: Main workflow -  Notification
   And goto  Notification
   Then check landing on Notifications

Scenario: Main workflow - item can be added to the cart
  Then In search field type "dress"
  Then Click the "Search" button
#  Then Pick the first available item from results page