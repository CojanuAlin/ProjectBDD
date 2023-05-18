Feature: Check first page interaction

  Background:
    Given I am on the https://jules.app/search/all page

  Scenario Outline: Check if you can search for something
    When I insert "<text>" in the "<search_area>" box and hit Enter
    Then I should have "<message>" in the search area
  Examples:
    | text      | search_area    | message   |
    | something | all items      | something |
    | another   | my items       | another   |
    | last      | external items | last      |

