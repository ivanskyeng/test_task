Feature: Case 1

@prod
Scenario: Case 1
Given I navigate to Vimbox login page
When I log in with "mr.warning2014@mail.ru" and "111111"
Then I should see that Virtual Classroom is loaded
And I select New Student
And I select options General English, Beginner, 1st lesson
When I click Start the lesson
Then I see that lesson started
Then I navigate to the lesson as a student
And I should see that lesson loaded
When I click Next Page as a teacher
Then I see that page switched to a teacher
And I see that slide switches for student too
When I open a slide for Preview mode
Then I see that slide not switches and not shown for student
And I close the Preview mode of the slide as teacher