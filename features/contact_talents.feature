Feature: Contact talent
As a Hiring Manager/Recruiter, I want to be able to access talent contact page so that I can contact talent via email

  Background:
    Given I am logged in as Administrator

  Scenario: Contact talent from the search page
    When I search for talent profiles
    Then I should be able to send email to talants

  Scenario:Contact talent from shortlist page
    When I access the shorslist page
    Then I should be able to send email to talant