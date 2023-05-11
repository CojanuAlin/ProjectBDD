Feature: Check first page interaction

  Background:
    Given I am on the https://jules.app/search/all page

  Scenario: Check if you can search for something
    When I insert "something" in the search box and hit Enter
    Then I should have "something" in the search area