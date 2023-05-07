Feature: View talents full profile
  As a user, I want to view a talent's full profile from the search page and shortlist page so that I can a better view

  Background:
    Given I am logged in as Admin

    Scenario: View from search page
     When I run a search for talent profiles
     Then I should be a able to view talents full profile

    Scenario:View from shortlist page
     When I visit the shortlist page
     Then I should be able to view talents full profile