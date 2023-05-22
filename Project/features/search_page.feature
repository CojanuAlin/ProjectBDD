Feature: Check first page interaction

  Background:
    Given I am on the Jules app page

  Scenario: I login to the desired page
    When I login to the Jules app page
    Then I am redirected to the search area

  Scenario Outline: Check if you can search for something
    When I insert "<text>" in the "<search_area>" box and hit Enter
    Then I should have "<message>" in the search area
  Examples:
    | text      | search_area    | message   |
    | something | all items      | something |
    | another   | my items       | another   |
    | last      | external items | last      |

  Scenario: Check if you can access notification bell
    When I press the notification button
    Then I can see the notification area message


