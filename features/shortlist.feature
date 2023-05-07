Feature: Shortlists
  As a user when I click into a shortlist I want to be presented with a list of Talent Cards that display many talent’s information
  Each of these Talent Cards should have shortlist specific CTAs - e.g. Remove and Contact Buttons

  Background:
    Given the client is on Shortlist page


  Scenario: Delete all shortlists
    When removes all shortlists
    Then No shortlists should be there


  Scenario Outline: CRUD shortlist
    When user creates a shortlist
    And updates shortlist name to <shortlist_name>
    And reads shortlist by name <shortlist_name>
    And removes shortlist <shortlist_name>
    Then the <shortlist_name> should not be present on list
    Examples:
      | shortlist_name                |
      | Selenium Test shortlist UPD  |

  Scenario Outline: Search talent, add to shortlist and remove from shortlist
    Given the client is on Search page
    When User search by text match
    And adds talent to new shortlist <shortlist_name>
    And the client is on Shortlist page
    And reads shortlist by name <shortlist_name>
    And removes talent from shortlist
    Then No talents should be there
    Examples:
      | shortlist_name          |
      | Selenium remove talent  |













