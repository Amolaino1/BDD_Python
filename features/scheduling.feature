Feature: Scheduling interviews - https://untapt.atlassian.net/browse/NN-815
  As a user I would want to be able to create a schedule


  Background:
    Given the user is on the scheduling page

    Scenario: Create schedule
      When the user clicks add new schedule
      And types the name of the schedule
      And inputs the interview URL
      When the user saves the schedule
      Then the newly created schedule should be visible on the page


    Scenario: Edit schedule
      When the user clicks on edit on an existing interview schedule
      And changes the existing name to New inteview - updated
      Then the newly created schedule should be visible on the page


    Scenario: Delete interview schedule
      When user clicks on an existing schedule
      And clicks on the EDIT button
      And user clicks on delete
      Then the deleted schedule should no longer be available on the page








