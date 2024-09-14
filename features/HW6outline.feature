Feature: Ebay regression

Background: start from ebay
  Then open eBay.com

Scenario Outline: Main workflow - header navigation links
  And goto <link text>
  Then check landing <expected title>

  Examples:  left top links
    | link text     | expected title                                                 |
    | Watchlist     | Electronics, Cars, Fashion, Collectibles & More \| eBay        |
    | Sell          | Selling on eBay \| Electronics, Fashion, Home & Garden \| eBay |
#    | Daily Deals   | Daily Deals on eBay\| Best deals and Free Shipping              |
#
#  Examples:  right top links
#    | link text | expected title    |
#    | Watchlist | Watchlist related |
#    | Sell      | Sell related      |
#    | My Ebay   | My Ebay related   |
#