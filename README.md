# Ami-Coding-Pari-Na

# Django Web Application: User Input Analysis

This is a Django web application that allows users to perform input values and search for an input value. The application features user authentication, input value searching, and an API for retrieving user input records.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Usage Instructions](#usage-instructions)
  - [Installation](#installation)
  - [Run the Development Server](#run-the-development-server)
  - [Access the Application](#access-the-application)
  - [API Endpoints](#api-endpoints)


## Features

- User creation and authentication.
- Search page for performing input value searches.
- Sorted storage of input values in the database.
- API endpoint for retrieving user input records within a specified time range.

## Project Structure

The project follows a standard Django structure:



- `Ami-Coding-Pari-Na/`: The main project directory.
- `Ami-Coding-Pari-Na/settings.py`: Configuration settings for the project.
- `Ami-Coding-Pari-Na/urls.py`: Project-level URL configuration.
- `khoj/`: The app containing the main functionality.
- `khoj/migrations/`: Database migration files.
- `khoj/templates/`: HTML templates.
- `khoj/admin.py`: Custom admin display for `InputRecord` model.
- `khoj/forms.py`: Form definitions.
- `khoj/models.py`: Model definitions.
- `khoj/serializers.py`: Serializers for API data.
- `khoj/urls.py`: App-level URL configuration.
- `khoj/views.py`: Views for handling user interactions.

## Usage Instructions

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MuntasirShoumik/Ami-Coding-Pari-Na
   

2. go to the directory

3. Create and activate a virtual environment (optional):

   ```bash
   python -m venv venv
   source venv/bin/activate

4. Install the required packages:
   
   ```bash
   pip install -r requirements.txt
   
5. Run the Django development server:

   ```bash
   python manage.py runserver   

6. Access the application in your web browser:

   ```bash
   http://127.0.0.1:8000/search/

API Endpoints

Endpoint: http://127.0.0.1:8000/api/get-input-values/<br>

Parameters:<br>

user_id: User ID.<br>
start_datetime: Start datetime in ISO format.<br>
end_datetime: End datetime in ISO format.<br>
Returns: JSON response containing user input records within the specified time range<br>

Or, <br>

1. Open the get_response.py script
2. set the parameters

```bash
python get_response.py

It will print the api response in the consol
