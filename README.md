# Flask Form - Job Application Form

A Flask web application that collects job application data through an interactive form. The application stores submissions in a SQLite database and sends confirmation emails to applicants.

## Features

- **Interactive Job Application Form**: Bootstrap-styled form with the following fields:
  - First Name
  - Last Name
  - Email Address
  - Available Start Date (date picker)
  - Current Occupation (radio buttons: Employed, Unemployed, Self-Employed, Student)
- **Database Integration**: Uses SQLAlchemy to store form submissions in a SQLite database
- **Email Notifications**: Automatically sends confirmation emails to applicants after form submission
- **Flash Messages**: User-friendly success messages after successful form submission
- **Responsive Design**: Bootstrap 5 for modern, mobile-friendly UI

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Mail

## Installation

1. Clone or download this repository

2. Install the required dependencies:

```bash
pip install flask flask-sqlalchemy flask-mail
```

## Configuration

### Email Setup

**Important**: Before running the application, you need to configure your email settings in `app.py`:

1. **Gmail Users**: 
   - Enable "Less secure app access" or use an App Password
   - Go to your Google Account settings
   - Generate an App Password for this application
   - Update the `MAIL_USERNAME` and `MAIL_PASSWORD` in `app.py`

2. **Other Email Providers**:
   - Update `MAIL_SERVER`, `MAIL_PORT`, and `MAIL_USE_SSL` settings accordingly

3. **Security Recommendation**: 
   - Store sensitive credentials in environment variables instead of hardcoding them
   - Consider using a `.env` file with `python-dotenv` for better security

Example using environment variables:
```python
import os
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
```

### Secret Key

Update the `SECRET_KEY` in `app.py` to a secure random string for production use.

## Usage

1. Navigate to the project directory:

```bash
cd Flask_Form
```

2. Run the Flask application:

```bash
python app.py
```

3. Open your web browser and navigate to:

```
http://localhost:5001
```

4. Fill out the job application form and submit

5. Check the submitted email address for the confirmation email

## File Structure

```
Flask_Form/
├── app.py              # Main Flask application file
├── templates/
│   └── index.html      # HTML template for the form
├── data.db             # SQLite database (created automatically)
└── README.md           # This file
```

## Database Schema

The application uses a `Form` model with the following fields:

- `id`: Primary key (auto-increment)
- `first_name`: String (80 characters)
- `last_name`: String (80 characters)
- `email`: String (80 characters)
- `date`: Date field
- `occupation`: String (80 characters)

The database file (`data.db`) is created automatically on first run.

## How It Works

1. **Form Submission**: User fills out the job application form
2. **Data Processing**: Flask receives the POST request and extracts form data
3. **Database Storage**: Form data is saved to the SQLite database using SQLAlchemy
4. **Email Sending**: A confirmation email is sent to the applicant's email address
5. **Flash Message**: Success message is displayed to the user

## Email Template

The confirmation email includes:
- Personalized greeting with the applicant's first name
- Submission confirmation message
- Summary of submitted data (name and date)

## API Endpoints

- `GET /`: Displays the job application form
- `POST /`: Processes form submission, saves to database, and sends email

## Technologies Used

- **Flask**: Web framework
- **SQLAlchemy**: Database ORM
- **Flask-Mail**: Email functionality
- **Bootstrap 5**: Frontend styling
- **SQLite**: Database storage
- **Jinja2**: Template engine (included with Flask)

## Development Notes

- The application runs in debug mode on port 5001
- Database tables are automatically created on first run using `db.create_all()`
- Flash messages use Flask's built-in messaging system

## Security Considerations

For production deployment:

1. **Never commit sensitive credentials** (email passwords, secret keys) to version control
2. Use environment variables or secure configuration management
3. Change the default `SECRET_KEY` to a strong, random value
4. Use HTTPS in production
5. Implement proper error handling
6. Consider adding form validation and CSRF protection
7. Use a production-grade web server (e.g., Gunicorn) instead of Flask's development server

## Troubleshooting

### Email Not Sending

- Verify your email credentials are correct
- Check that "Less secure app access" is enabled (Gmail) or use App Passwords
- Verify SMTP server settings match your email provider
- Check firewall/network settings

### Database Issues

- Ensure you have write permissions in the project directory
- Delete `data.db` to reset the database (data will be lost)
- Check that SQLAlchemy is properly installed

### Port Already in Use

- Change the port number in `app.py` (currently set to 5001)
- Or stop the process using port 5001

## License

This project is open source and available for personal and educational use.
