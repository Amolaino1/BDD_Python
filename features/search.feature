Feature: Search talents
  As a user I want to navigate to a search page where I can search for talent.
  I want to search for talent using a set of filters and/or text to match against.
  The results of a search is a list of talent that I can add a talent to a shortlist - either a new shortlist or pre-existing one.

  Background:
    Given the client is on Search page

    Scenario: Search by match text
      When User search by text match
      Then User should see some talents


    Scenario: Search and use pagination
      When User search by text match
      And navigates to "3" page
      Then User should see list of talents "21 - 30"


    Scenario: Search and use pagination and filter
      When User search by text match
      And navigates to "3" page
      And filters by education schools "university"
      Then User should see list of talents "1 - 10"


    Scenario: Search by match text and ByeBias - name
      When User search by text match
      And toggle ByeBias
      Then User should see talent names with initials


    Scenario: Search by match text and ByeBias - image
      When User search by text match
      And toggle ByeBias
      Then User should see profile icon as default


    Scenario: Search by match text and hide
      When User search by text match
      And hides a talent
      Then talent card should disappear from the list


    Scenario: Search by match text and add to new Shortlist
      When User search by text match
      And adds talent to new shortlist
      Then User should receive successful notification


    Scenario: Search by match text and keyword filter
      When User search by text match
      And filters by keyword "Javascript -Java"
      Then User should see some talents


    Scenario: Search by match text and other filters
      When User search by text match
      And filters by education degree "master"
      And filters by education schools "university"
      And filters by experience "Analyst"
      Then User should see some talents


    Scenario: Search by match text and filters - no results found
      When User search by text match
      And filters by education degree "qwerty"
      Then User should see 0 results message
