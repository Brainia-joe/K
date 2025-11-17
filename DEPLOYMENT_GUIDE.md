# Deployment Guide

## Option 1: PythonAnywhere (Free - Recommended for Beginners)

### Step 1: Create Account
1. Go to: https://www.pythonanywhere.com/
2. Sign up for a **free account**
3. Confirm your email

### Step 2: Upload Files
1. Click **"Files"** tab
2. Click **"Upload a file"**
3. Upload your project ZIP
4. Or use **"Open Bash console"** and use Git

### Step 3: Setup Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.10 myenv
workon myenv
pip install -r requirements.txt
```

### Step 4: Configure Web App
1. Click **"Web"** tab
2. Click **"Add a new web app"**
3. Choose **"Manual configuration"**
4. Select **Python 3.10**
5. Set paths:
   - **Source code:** `/home/yourusername/kenyan_homes_project`
   - **Working directory:** Same as above
   - **WSGI file:** Edit and configure

### Step 5: Setup Static Files
1. In Web tab, under **"Static files"**
2. Add:
   - URL: `/static/`
   - Directory: `/home/yourusername/kenyan_homes_project/staticfiles`

### Step 6: Run Migrations
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

### Step 7: Reload Web App
Click the green **"Reload"** button

---

## Option 2: Heroku (Easy - $5-7/month)

### Prerequisites
- Install Git
- Install Heroku CLI

### Step 1: Install Heroku CLI
Download from: https://devcenter.heroku.com/articles/heroku-cli

### Step 2: Login to Heroku
```bash
heroku login
```

### Step 3: Prepare Project
Create `Procfile`:
```
web: gunicorn kenyan_homes.wsgi
```

Install gunicorn:
```bash
pip install gunicorn
pip freeze > requirements.txt
```

### Step 4: Create Heroku App
```bash
heroku create kenyan-homes-app
```

### Step 5: Deploy
```bash
git init
git add .
git commit -m "Initial deployment"
git push heroku main
```

### Step 6: Run Migrations
```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Step 7: Open App
```bash
heroku open
```

---

## Option 3: DigitalOcean ($5/month - Best Performance)

### Requirements
- Basic Linux knowledge
- SSH access
- Domain name (optional)

### Quick Setup
1. Create Droplet (Ubuntu 22.04)
2. SSH into server
3. Install Python, pip, nginx
4. Clone/upload project
5. Setup Gunicorn + Nginx
6. Configure domain (optional)

**Full guide:** https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu

---

## Email Configuration for Production

### Using Gmail

1. Go to: https://myaccount.google.com/apppasswords
2. Create app password
3. Update `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'kenyanhomes1@gmail.com'
EMAIL_HOST_PASSWORD = 'your-16-char-app-password'
DEFAULT_FROM_EMAIL = 'kenyanhomes1@gmail.com'
```

---

## Security Checklist for Production

Before going live, ensure:

- [ ] `DEBUG = False` in settings.py
- [ ] Change `SECRET_KEY` to new random value
- [ ] Add your domain to `ALLOWED_HOSTS`
- [ ] Setup HTTPS/SSL certificate
- [ ] Configure real email backend
- [ ] Setup proper database (PostgreSQL)
- [ ] Enable CSRF protection
- [ ] Setup static files serving
- [ ] Regular backups enabled

---

## Custom Domain Setup

### If client has domain (e.g., kenyanhomes.co.ke):

1. **On Hosting Provider:**
   - Point domain to server IP
   
2. **In Django settings.py:**
```python
   ALLOWED_HOSTS = ['kenyanhomes.co.ke', 'www.kenyanhomes.co.ke']
```

3. **Setup SSL:**
   - Use Let's Encrypt (free)
   - Certbot for auto-renewal

---

## Monitoring & Maintenance

### Regular Tasks:
- Check error logs weekly
- Backup database monthly
- Update dependencies quarterly
- Monitor disk space
- Review user accounts

### Useful Commands:
```bash
# Check logs
tail -f /var/log/nginx/error.log

# Backup database
python manage.py dumpdata > backup.json

# Restore database
python manage.py loaddata backup.json
```