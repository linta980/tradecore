# Created by apple at 2019-02-16
Feature: Register a User Form1
  # Enter feature description here
  Scenario: Test Login
    Given I go to my login form
    Then the title should be "TradeCore - Step 1 | Registration"

  Scenario: Check landing page 1
    Given I land on main page
    Then First title is "Create your account"

  Scenario: Fill out the form 1
    Given I land on main page
    When I enter first name Dragan
    And I enter last name Lintner
    And I enter email dragan+1@tradecore.com
    And i enter password KnKnPnKn@@345
    And I enter phone number 694158040
    And i enter Birthday 26/03/1980
    And I enter postcode 11070
    And I enter address line 1 oml brigada 87
    And I enter address line 2 oml brigada 87
    And I enter City name Belgrade
    And I submit the form

  Scenario: Check Landing page 2
    Given Landing page is opened
    Then Title is Have you traded in any of the following in the past three years?

  Scenario: Fill out the form 1
    Given Landing page is opened
    When I enter shares frequently
    And I enter forex frequently
    And I enter cfds frequently
    And I enter Spread betting frequently
    And I enter relevant expirience no_experience
    And I enter tranding platform 2
    And I enter tranding currency USD
    And I enter aproximate anual income income_50k_99k
    And I enter employment status employed
    And i enter aproximate value of assets income_over_100k
    And I check Terms and Conditions