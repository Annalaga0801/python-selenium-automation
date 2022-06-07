# Created by Анна at 6/6/2022
#Feature: Amazon help search

  Scenario: Verify user can search help for Cancel order
    Given Open Amazon Help page
    When Search for Cancel order
    And click Enter
    Then Verify search results for Cancel Items or Orders are shown