Assignment 7: Yelp Database Application

Megan Andrews 301423531
This is a Python application that allows a user to log in to the Yelp Database
and complete a variety of functions using a GUI.

Installation:
    1. Clone the repository
    2. Create and activate a new virtual environment:
        cd Assignment7
        python -m venv venv
        myenv\Scripts\activate
    3. Install the required dependencies
        pip install -r requirements.txt
    4. Deactivate the virtual environment
        deactivate

Usage:
    To run the application, activate the virtual environment and run the main script:
        myenv\Scripts\activate
        python assignment7.py
    This will start the application and you can interact with it using the GUI.
    Remember to deactivate the virtual environment when you're done:
        deactivate

Guide:
    1. Log In
        Enter a valid username to login the Yelp applplication. 
        Click "Log in"
    2. Main menu 
        Select one of the four functions by clicking on the respective button.
        "Search Business" skip to step 3.
        "Search User" skip to step 4.
        "Write Review" skip to step 5a.
        "Make Friend" skip to step 6a.
        Or log out with the log out button in the top right corner.
    3. Search Business
        Enter search parameters into the search fields.
        Click "Search" 
        Click on one of the businesses displayed to write a review (skip to step 5b).
        You can also go back to the main menu by clicking the menu button in the top right corner.
        Or log out with the log out button in the top right corner.
    4. Search User
        Enter search parameters into the search fields.
        Click "Search" 
        NOTE: If you enter no search parameters and submit, it may take a 1-2 seconds for the results to appear.
        Click on one of the user displayed to make a friend (skip to setp 6b).
        You can also go back to the main menu by clicking the menu button in the top right corner.
        Or log out with the log out button in the top right corner.
    5. Write review
        a. Enter the business id and click "Submit"
        b. Enter the number of stars you would like to leave and click "Submit"
        You can also go back to the main menu by clicking the menu button in the top right corner.
    6. Make Friend
        a. Enter the user id of the friend and click "Submit"
        b. Click "Add friend"
        You can also go back to the main menu by clicking the menu button in the top right corner.
    7. Close the application



