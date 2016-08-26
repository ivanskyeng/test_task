Feature: SkyEng Login

@prod
Scenario: Valid Login to SkyEng
Given I navigate to SkyEng
When I go to Login page
Then I log in with "test@ya.ru" and "111111"
And I should see that Cabinet is loaded