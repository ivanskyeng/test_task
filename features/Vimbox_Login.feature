Feature: Vimbox Login

@prod
Scenario: Valid Login to Vimbox
Given I navigate to Vimbox login page
When I log in with "mr.warning2014@mail.ru" and "111111"
Then I should see that Virtual Classroom is loaded