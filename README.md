# Login Application

This is a login application that allows users to log in using a correct username and password and welcomes them when they login.

# Purpose

This project makes a login system using Flask. It includes two HTML templates one for login page and the other for the profile page, and a simple database to store user information.

# Functionality
  - Users enter their username and password on the login page.
  - If the entered values match the defined database, the user is directed to the profile page that gives a welcome message.
  - If login fails, an error message is displayed on the login page.


## Dependencies

- Setting up the virtualenv
- Flask

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/maysam-asser/login-app
```

2. Set up a virtual environment:

```bash
virtualenv venv
venv/Scripts/activate       
```
1. Install dependencies:

```bash
pip install Flask
```

4. Run the application:
    
```bash
flask run
```

5. Access the application: Open your browser and navigate to http://127.0.0.1:5000.

## How to Use
1. Open the login page.
2. Enter one of the predefined usernames and passwords from `db.py`. For example:
Username: maysam, Password: 1234
3. If the credentials are correct, you will be taken to the profile page.
4. If the credentials are incorrect, an error message will appear.