# EmailApp

# EmailApp

## Overview

EmailApp is a Django web application designed to handle email-related tasks efficiently. It provides a user-friendly interface for users to upload CSV files containing email addresses, validates the emails, stores the results in a PostgreSQL database, and offers the capability to send emails to valid addresses.

## Features

- **File Upload and Processing:**
  - Users can upload CSV files with email addresses.
  - Uploaded files are processed to extract and validate email addresses.

- **Email Validation:**
  - Utilizes Django's `EmailValidator` for email validation.
  - Categorizes email addresses as valid or invalid based on the validation results.

- **Database Storage:**
  - Stores valid and invalid email addresses in a PostgreSQL database.
  - Django model (`Uploaded_File`) captures file details and timestamps.

- **Frontend Interface:**
  - User-friendly interface for file uploads using Django templates.
  - HTML templates for displaying email validation results.

- **Email Sending:**
  - Allows users to send emails to valid addresses.
  - Utilizes Django's `send_mail` function for email sending.

- **Notification Handling:**
  - Provides pop-up dialogue boxes for displaying success or failure messages.

## Usage

1. Clone the repository.
2. Set up a virtual environment and install dependencies: `pip install -r requirements.txt`.
3. Run migrations: `python manage.py migrate`.
4. Start the development server: `python manage.py runserver`.
5. Access the application at [http://localhost:8000](http://localhost:8000).

Feel free to explore, contribute, and enhance the functionality of EmailApp!

