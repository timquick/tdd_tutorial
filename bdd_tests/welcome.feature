Feature: Welcome Page
	As an internet user
	I want to be able to see all my lists in one page
	So that I can find them all after I've written them
	
	Scenario:  Launch Welcome Page
	
	   Given  I launch my browser
	   When I navigate to "http://ec2-54-191-108-220.us-west-2.compute.amazonaws.com/"
	    Then I should see a page titled "To-Do"
		

