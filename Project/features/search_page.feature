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

  Scenario Outline: Go to notification settings and deselect all the notifications
    When I click on the notification type "<notif_name>"
    Then I receive a notification with the message "<notification_message>"
  Examples:
    | notif_name                   | notification_message                            |
    | I.D. Expiration Dates        | Success |
    | Next Scheduled Service       | Notification type disabled successfully! |
    | Vehicle Registration         | Notification type disabled successfully! |
    | HVAC Filter Replacement      | Notification type disabled successfully! |
    | Insurance Policy Expiration  | Notification type disabled successfully! |
    | Warranty Expiration          | Notification type disabled successfully! |
    | Item's Projected End of Life | Notification type disabled successfully! |
    | Scheduled Vaccination        | Notification type disabled successfully! |
    | Birthdays                    | Notification type disabled successfully! |


