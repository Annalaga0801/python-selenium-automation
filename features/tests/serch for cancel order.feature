# Created by Анна at 5/19/2022
  Scenario: Verify that user can search for coffee
  Scenario Outline: Verify that user can search for products
    Given Open Amazon page
    When Search for table
    Then Verify search results for "table" are shown
    When Search for <search_word>
    Then Verify search results for <search_result> are shown
    Examples:
    |search_word  |search_result  |
    |table        |"table"        |
    |dress        |"dress"        |
    |spoons       |"spoons"       |

  Scenario: Verify that user can search for dress

  Scenario: User sees ham menu btn on the main page
    Given Open Amazon page
    When Search for dress
    Then Verify search results for "dress" are shown
    Then Verify hamburger menu btn present

  Scenario: User sees correct amount of footer links
    Given Open Amazon page
    Then Verify there are 38 footer links