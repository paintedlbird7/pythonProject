Feature: Ebay regression

Scenario: Main workflow - Daily Deals
  Then open ebay.com
  And goto  Daily Deals
  Then check landing on Daily Deals on eBay | Best deals and Free Shipping

Scenario: Main workflow - Sell
  Then open ebay.com
  And goto  Sell
  Then check landing on Selling on eBay | Electronics, Fashion, Home & Garden | eBay

Scenario: Main workflow - My eBay
  Then open ebay.com
  And goto  My eBay
  Then check landing on eBay shopping cart

Scenario: Main workflow - Watchlist
  Then open ebay.com
  And goto  Watchlist
  Then check landing on My eBay - My eBay - Watchlist

Scenario: Main workflow -  Notification
   Then open ebay.com
   And goto  Notification
   Then check landing on Notifications









#Scenario: ebay test
#  Then open eBay.com
#  Then you verify logo present on page
