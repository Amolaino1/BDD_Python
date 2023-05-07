Feature: List of users
  As a sales manager, I would want to be able to visit the users page
  So that I am able to see the list of users

  Scenario: 1.Create User
    Given sales manager is on users page
    When sales manager creates a user
    Then sales manager should see confirmation message

  Scenario: 2. User functionality
    Given sales manager is on users page
    When sales manager navigates to next page
    Then sales manager should see users in next page

