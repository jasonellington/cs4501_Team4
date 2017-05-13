# CS4501 Team 4 Project

Our app is an "Airbnb" for cars. We are a marketplace with sellers being car owners, and buyers being individuals in need of renting a car. 

## User Stories - Project 3 - 
User Stories:
- Application Users
  - As a user, I would like to have the ability to register an account
  - As a user, I would like to have the ability to add a credit card
  - As a user, I would like to find a car based off of the city I enter
  - As a user, I would like to view cars based off of price
- Car Owners
  - As a car owner, I would like to list my car
  - As a car owner, I would like to receive inquiries about my car

## User Stories - Project 4 - 
User Stories:
- As a user, I would like to register an account with a username and password
- As a user, I would like my password to be encrypted and protect
- As a user, I would like to have the ability to login to my account
- As a user, I would like to add a car listing
- As a user, I would like to logout and have my cookie deleted

## User Stories - Project 5 - 
- As a user, I would like to view the search results page
- As a user, I would like to make a search query using ES
- As a car owner, I would like the newly created listing to be added to a Kafka queue
- As a car owner, I would like for a my newly added listing to be added to the search engine


A new web front end page, the search result page, will be created. It will call a new experience service, the search experience service, to get the results for a user's query.

## User Stories - Project 6 -
- As a user, I would like to be able to access the site using DigitalOcean
- As a user, I would like usability test and integration test to be checked by TravisCI
- As a user, I would like load balance to be implemented using HAProxy

## User Stories - Project 7 -
- As a user, I would like the clicks to be logged to an access log
- As a user, I would like Spark to reduce the access log to create a recommendation system
- As a user, I would like the recommendation table to be in the database
- As a user, I would like to see the recommendations when I go to a specific page


## Instructions:
- Create an account by finding the register tab
	- users who do not have accounts do not have the ability to create a listing, they can only view them
- after creating an account, find the login tab and fill it out with the information you just provided
- Users who successfully login, have the ability to view the user portal and create a new listing
- You must create a listing FIRST, and THEN you are able to search for that listing
