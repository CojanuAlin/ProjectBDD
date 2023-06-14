Feature: Check if you can login to the desired page


  Background:
    Given I am on the https://jules.app/sign-in page


# Scenariul 1: Introducem username corect si parola gresita
# Scenariul 2: Introducem username gresit si parola corecta
# Scenariul 3: Introducem username gresit si parola gresita
# Scenariul 4: Introducem username incorrect si parola gresita
# Scenariul 5: Introducem username incorrect si parola corecta
# Scenariul 6: Introducem username si parola valide si ne logam


  Scenario Outline: Check if you can not log in the application page with incorrect credentials
    When I insert username "<username>" and password "<password>"
    And I click the login button
    Then I can not login into the application and I receive "<error_message>" error
  Examples:
    | username | password | error_message |
    | alin_nicusor@outlook.com | incorrect_password | Invalid email/password combination |
    | incorrect_user@yahoo.com | Digital1!          | Invalid email/password combination |
    | incorrect_user@yahoo.com | incorrect_password | Invalid email/password combination |


  Scenario Outline: Check if you can not log in the application page with no or wrong username
    When I insert username '<utilizator_gresit>' and password '<parola>'
    Then I can not login into the application and I receive '<no_user>' error
  Examples:
    | utilizator_gresit | parola             | no_user                             |
    | wrong_user        | incorrect_password | Please enter a valid email address! |
    | wrong_user        | Digital1!          | Please enter a valid email address! |


  Scenario: Check if you can Log In with correct credentials
      When I insert username "alin_nicusor@outlook.com" and password "Digital1!"
      And I click the login button
      Then I can login into the application and I am redirected to the https://jules.app/search/all page

