Feature: Check first page interaction

  Background:
    Given I am on the Jules app page

  @phone
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
    | notif_name                   | notification_message |
    | I.D. Expiration Dates        | Success |
    | Next Scheduled Service       | Success |
    | Vehicle Registration         | Success |
    | HVAC Filter Replacement      | Success |
    | Insurance Policy Expiration  | Success |
    | Warranty Expiration          | Success |
    | Item's Projected End of Life | Success |
    | Scheduled Vaccination        | Success |
    | Birthdays                    | Success |

  @question
  Scenario Outline: Go to question mark button and select each item
    When I press the question mark button
    And I select "<question_item>"
    Then Another page opens with proper "<question_url>"
  Examples:
    | question_item      | question_url                                 |
    | FAQ                | https://static.jules.app/faq.html            |
    | Tutorials          | https://julesapp.com/tutorials/              |
    | Privacy Policy     | https://static.jules.app/privacy_policy.html |
    | Terms & Conditions | https://static.jules.app/terms_of_use.html   |

  @phone
  Scenario: Check if you can save your phone number
    When I click on the person icon and select My account
    Then The number is saved in the phone field
