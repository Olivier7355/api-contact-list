### 1. How did you structure your application? Can you explain the different layers and their responsibilities? Explain your thought process.

The main layers are : 

- **The database creation:** This layer creates the SQLite database and table with columns id, name, phone_number, and email using SQLAlchemy.
- **The list_all_contacts endpoint:** This layer defines the endpoint “/contacts/” that queries the database to get and return all the contacts.
- **The read_contact endpoint:** This layer defines the endpoint “/contacts/{contact_id}” that queries the database to get and return a specific contact by id.
- **The create_contact endpoint:** This layer defines the endpoint “/contacts/” that adds the contact to the database, and returns a confirmation message with the id of the created contact.
- **The update_contact endpoint:** This layer defines the endpoint “/contacts/{contact_id}” that updates the contact in the database, and returns a confirmation message with the id of the updated contact.
- **The delete_contact endpoint:** This layer defines the endpoint “/contacts/{contact_id}” that deletes a contact from the database by id and returns a confirmation message with the id of the deleted contact.


### 2. Which framework did you use to implement the API endpoints and why? What do you like about the chosen framework in particular?

I directly settle for FastAPI since it is rather easy to understand and code. It also integrates very well with SQLAlchemy which I use in the code to query the database. Furthermore, contrary to Flask or Django Frameworks, FastAPI provides documentation that is automatically generated and makes it easy to test the endpoints (swagger docs).


### 3. Did you follow any best practices in terms of code styling? How did you ensure your code is clean? What did you use in the past to ensure code quality is high and what are your experiences with such checks?

I try to follow the PEP8 coding conventions. I always use the extension “Prettier” in VS code and Codespace to help me ensure that my code stays clean and readable.


### 4. How did you implement persistence, what frameworks did you use and why did you choose them? Did the time constraint have an impact on your choice?

I chose SQLAlchemy since I already used it for other development projects and it integrates very well with FastAPI. The time constraint did not have any impact on my choice.


### 5. How did you handle input validation?

I used the Pydantic module for input validation since it is considered as a best practice with FastAPI.


### 6. How did you handle errors and exceptions in your API? Would you handle this differently in a larger application that is going to be shipped to production?

I only handled 4xx client error exceptions. I would give more time and attention to errors and exceptions if the code had to be shipped in production. In that case, I would certainly add 5xx server error exceptions.  


### 7. How did you ensure the uniqueness of contact identifiers? Did you use any specific technique or library?
I use an unique id value acting as a primary key that is automatically assigned by the database to ensure that each contact has a unique identifier.


### 8. How would you add authentication to the app? Explain your thought process.

I never used authentication with FastAPI but that can be achieved thanks to a library such as JWT. I would create a new module to handle the authentication and add an endpoint to it to manage the login.   


### 9. Reflect on your implementation regarding performance. What did you consider from a performance point of view? What could you improve or optimise?

I should have used “async” to create all the endpoint functions since I was using FastAPI. I would also use PostgreSQL instead of SQLite for the database if the app had to be shipped in production.


### 10. Looking back on the assignment, is there anything you would do differently? If yes, what?

Reflecting on my previous answers, I would add asynchronous endpoint functions and server error exceptions. 
