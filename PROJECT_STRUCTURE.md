# Project Structure

## Overview
This document explains the organization of the Kenyan Homes project.

## Directory Structure
```
kenyan_homes_project/
│
├── kenyan_homes/                    # Main project folder
│   ├── __init__.py                 # Makes it a Python package
│   ├── settings.py                 # Project settings & configuration
│   ├── urls.py                     # Main URL routing
│   ├── wsgi.py                     # WSGI config for deployment
│   └── asgi.py                     # ASGI config for async
│
├── properties/                      # Main application
│   ├── migrations/                 # Database migrations
│   ├── templates/                  # HTML templates
│   │   └── properties/
│   │       ├── index.html         # Homepage
│   │       ├── profile.html       # User profile
│   │       └── reset_password.html # Password reset
│   ├── __init__.py
│   ├── admin.py                    # Admin panel configuration
│   ├── apps.py                     # App configuration
│   ├── models.py                   # Database models
│   ├── urls.py                     # App URL routing
│   ├── views.py                    # Business logic
│   └── tests.py                    # Unit tests
│
├── staticfiles/                     # Static files (CSS, JS, images)
├── media/                           # User uploaded files
│
├── db.sqlite3                       # Database file
├── manage.py                        # Django management script
│
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Git ignore rules
├── README.md                        # Installation guide
├── USER_GUIDE.md                   # User documentation
├── DEPLOYMENT_GUIDE.md             # Deployment instructions
├── CHANGELOG.md                     # Version history
└── PROJECT_STRUCTURE.md            # This file
```

## Key Files Explained

### settings.py
- Database configuration
- Installed apps
- Email settings
- Security settings
- Static files config

### models.py
Contains 3 main models:
- **ContactMessage** - Stores contact form submissions
- **TourBooking** - Stores tour booking requests
- **User** - Stores user accounts

### views.py
Contains all business logic:
- `home()` - Homepage
- `signup()` - User registration
- `login_user()` - User login
- `logout_user()` - User logout
- `submit_contact()` - Contact form handler
- `submit_booking()` - Booking handler
- `user_profile()` - Profile page
- `verify_email()` - Email verification
- `reset_password_request()` - Password reset request
- `reset_password_confirm()` - Password reset confirmation

### urls.py
Maps URLs to views:
- `/` → Homepage
- `/signup/` → Signup
- `/login/` → Login
- `/profile/` → User profile
- `/admin/` → Admin panel
- etc.

## Database Schema

### User Model
- id (Primary Key)
- full_name
- email (Unique)
- phone
- username (Unique)
- password (Hashed)
- email_verified
- verification_token
- created_at
- is_active

### ContactMessage Model
- id (Primary Key)
- name
- email
- message
- created_at
- is_read
- replied

### TourBooking Model
- id (Primary Key)
- full_name
- email
- phone
- property_name
- preferred_date
- number_of_people
- message
- created_at

## Technologies Used

### Backend
- **Python 3.13**
- **Django 5.1**
- **SQLite** (development)

### Frontend
- **HTML5**
- **CSS3**
- **JavaScript**
- **Bootstrap 5.3.6**
- **Font Awesome 6.7.2**

### Security
- CSRF Protection
- Password Hashing (PBKDF2)
- Session Management
- Email Verification

## API Endpoints

All endpoints use POST method:

- `POST /signup/` - Create new user
- `POST /login/` - User login
- `GET /logout/` - User logout
- `POST /contact/` - Submit contact message
- `POST /book/` - Submit tour booking
- `GET /verify-email/<token>/` - Verify email
- `POST /reset-password/` - Request password reset
- `POST /reset-password/<token>/` - Confirm password reset

## Environment Variables (Production)

For production, set these:
- `DEBUG=False`
- `SECRET_KEY=<random-secret-key>`
- `DATABASE_URL=<database-connection-string>`
- `EMAIL_HOST_USER=<email-address>`
- `EMAIL_HOST_PASSWORD=<email-password>`
- `ALLOWED_HOSTS=<your-domain.com>`

## Maintenance

### Regular Tasks
1. **Weekly:** Check error logs
2. **Monthly:** Backup database
3. **Quarterly:** Update dependencies
4. **Yearly:** Security audit

### Backup Commands
```bash
# Backup database
python manage.py dumpdata > backup_$(date +%Y%m%d).json

# Restore database
python manage.py loaddata backup_20250114.json
```

### Update Commands
```bash
# Update Django
pip install --upgrade django

# Update all packages
pip install --upgrade -r requirements.txt
```