Feature: filter candidate
  As a user I want to navigate to a search page where I can search for talent.
  I want to search for talent using a set of filters and/or text to match against.
  The results of a search is a list of talent(s) matching the applied filter(s)

  Background:
    Given the client is on Search page
    When User search by text match

    Scenario: filter using AND operator
      And filter by keywords using AND operator
      Then User should see search result(s) corresponding to AND operator usage

    Scenario: filter using implied OR operator
      And filter by keywords using implied OR operator
      Then User should see search result(s) corresponding to implied OR operator usage

    Scenario: filter using OR operator
      And filter by keywords using OR operator
      Then User should see search result(s) corresponding to OR operator usage

    Scenario: filter using NOT operator
      And filter by keywords using NOT operator
      Then User should see search result(s) corresponding to NOT operator usage

    Scenario: filter using asterisk operator
      And filter by keywords using asterisk operator
      Then User should see search result(s) corresponding to asterisk operator usage

    Scenario: filter using parenthsis operator
      And filter by keywords using parenthesis operator
      Then User should see search result(s) corresponding to parenthesis operator usage

    Scenario: filter using complex querry
      And filter by keywords using complex querry structure
      Then User should see search result(s) corresponding to complex querry structure used

    Scenario: clear multiple search filters
      And apply multiple search filters
      And remove multiple search filters
      Then multiple search filters should be removed

    Scenario: view keywork search querries
      And hovers on keyword tool tip
      Then User should see keyword search querries

    Scenario: filter by location
      And filter by candidates' location
      Then User should see candidate(s) corresponding to location

    Scenario: filter by excluding a location
      And filter by excluding a location
      Then User should not see candidate(s) from excluded location

    Scenario: filter by exact location
      And filter by exact location
      Then User should see candidate(s) within exact location

    Scenario: filter by location within a specified radius
      And filter by location within a specified radius
      Then User should see candidate(s) within the specified radius

    Scenario: filter by major degree
      And filter by major degree
      Then User should see candidate(s) who hold specified major degree

    Scenario: filter by excluding major degree
      And filter by excluding major degree
      Then User should not see candidate(s) who hold excluded major degree

    Scenario: filter by past and current school
      And filter by past and current school
      Then User should see candidate(s) with specified past and current school

    Scenario: filter by excluding past and current school
      And filter by excluding past and current school
      Then User should not see candidate(s) with excluded past and current school

    Scenario: filter by past and current job title
      And filter by past and current job title
      Then User should see candidate(s) with specified past and current job title

     Scenario: filter by excluding past and current job title
      And filter by excluding past and current job title
      Then User should not see candidate(s) with excluded past and current job title

    Scenario: filter by current job title
      And filter by current job title
      Then User should see candidate(s) with specified current job title

    Scenario: filter by excluding current job title
      And filter by excluding current job title
      Then User should not see candidate(s) with excluded current job title

     Scenario: filter by job experience
      And filter by specific period of experience
      Then User should see candidate(s) with specified period of experience

     Scenario: filter by candidate's name
      And filter by specific candidate's name
      Then User should see candidate with specified name

    Scenario: filter by multiple search inputs
      And filter by multiple search inputs
      Then User should see candidate(s) corresponding to specified multiple search inputs