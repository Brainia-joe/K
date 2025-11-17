# Kenyan Homes Website

A modern real estate website with user authentication, contact forms, and WhatsApp booking integration.

## Features

✅ User Registration & Login
✅ Email Verification
✅ Password Reset
✅ User Profile Management  
✅ Contact Form (saves to database)
✅ WhatsApp Direct Booking
✅ Tour Booking System
✅ Admin Panel
✅ Password Strength Indicator
✅ Responsive Design

## Installation Guide

### Requirements
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Extract Files
Extract the project ZIP file to a location on your computer.

### Step 2: Install Dependencies
Open Command Prompt in the project folder and run:
```bash
pip install -r requirements.txt
```

### Step 3: Setup Database
```bash
python manage.py migrate
```

### Step 4: Create Admin Account
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

### Step 5: Run the Website
```bash
python manage.py runserver
```

### Step 6: Access the Website
Open your browser and go to:
- **Website:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

## Admin Panel Access

Login with the superuser account you created to:
- View all user registrations
- View contact form submissions  
- View tour booking requests
- Manage user accounts

## Email Configuration (For Production)

To enable real email sending:

1. Open `kenyan_homes/settings.py`
2. Find the EMAIL settings section
3. Update with your email credentials:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'kenyanhomes1@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = 'kenyanhomes1@gmail.com'
```

**Note:** For Gmail, you need to create an App Password:
https://myaccount.google.com/apppasswords

## WhatsApp Integration

The "Book Tour" buttons are configured to open WhatsApp with:
- **Phone Number:** +254729869849
- Pre-filled messages for each property

To change the phone number, update in `index.html`.

## Deployment Options

### Option 1: PythonAnywhere (Free)
1. Go to https://www.pythonanywhere.com/
2. Create free account
3. Upload project files
4. Follow their Django deployment guide

### Option 2: Heroku (Easy)
1. Go to https://www.heroku.com/
2. Create account
3. Install Heroku CLI
4. Deploy using Git

### Option 3: DigitalOcean ($5/month)
- Full control
- Better performance
- Requires more technical knowledge

## Support & Maintenance

For any issues or questions:
- **Developer:** [Kellen Kanyi]
- **Email:** [kellyally968@gmail.com]
- **Phone:** [0113992867]
-**Website:** [kellenkanyi.com]

## File Structure
```
kenyan_homes_project/
├── kenyan_homes/          # Project settings
│   ├── settings.py       # Configuration
│   ├── urls.py           # Main URL routing
│   └── wsgi.py           # Deployment config
├── properties/           # Main app
│   ├── models.py         # Database models
│   ├── views.py          # Business logic
│   ├── urls.py           # App URL routing
│   ├── admin.py          # Admin configuration
│   └── templates/        # HTML files
│       └── properties/
│           ├── index.html
│           ├── profile.html
│           └── reset_password.html
├── manage.py             # Django management script
├── db.sqlite3            # Database file
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## License

© 2025 Kenyan Homes. All rights reserved.