# Created by Анна at 5/19/2022
Feature: Amazon Help search

  Scenario: Verify that user can search for Cancel Order
    Given open Amazon help search
    When search for Cancel order
    When click Enter
    Then verify Cancel order result is present