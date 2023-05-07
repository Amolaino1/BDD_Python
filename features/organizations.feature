Feature: Create New Organization
  As a sales manager, I would want to visit the organization page so that
  I am able to create new organization

  Background:
    Given sales manager is on Organizations page

    Scenario: Create new organization with required fields
      When sales manager creates new organization with required fields
      Then sales manager should see the organization created

    Scenario: Create new organization without required fields
      When sales manager creates new organization without required fields
      Then sales manager should see a notification indicating that entry can not be empty

    Scenario: Create new organization with an existing name
      When sales manager creates new organization with an existing name
      Then sales manager should see a notification indicating that an organization with such name already exist


