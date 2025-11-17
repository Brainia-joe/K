# Kenyan Homes - Quick Start Guide

## For the Client

### What You Received
✅ Complete website source code
✅ User authentication system
✅ Admin panel for management
✅ Contact form with database
✅ WhatsApp booking integration
✅ Full documentation

---

## STEP 1: Extract Files
1. Extract `KenyanHomes_Website_v1.0.zip`
2. Open folder in File Explorer

## STEP 2: Install Python
1. Download Python from: https://www.python.org/downloads/
2. Install (CHECK "Add Python to PATH")
3. Verify: Open Command Prompt, type: `python --version`

## STEP 3: Install Dependencies
```cmd
cd path\to\kenyan_homes_project
pip install -r requirements.txt
```

## STEP 4: Setup Database
```cmd
python manage.py migrate
```

## STEP 5: Create Admin Account
```cmd
python manage.py createsuperuser
```
- Enter username, email, password
- Remember these credentials!

## STEP 6: Run Website
```cmd
python manage.py runserver
```

## STEP 7: Open Website
- Website: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

---

## Daily Usage

### Start Website
```cmd
cd path\to\kenyan_homes_project
python manage.py runserver
```

### Stop Website
Press `Ctrl + C` in Command Prompt

### View Messages
1. Go to: http://127.0.0.1:8000/admin/
2. Login with admin credentials
3. Click "Contact messages" or "Tour bookings"

---

## Need Help?
Contact Developer:
- Name: Kellen Kanyi
- Email: [kellyally968@gmail.com]
- Phone: [0113992867]
- Website: [kellenkanyi.com]

---

## Next Steps (Optional)
1. Deploy to live server (see DEPLOYMENT_GUIDE.md)
2. Configure email (see README.md)
3. Buy domain name
4. Setup SSL certificate
```

---

## **STEP 12: Convert to PDF (Optional)**

Use this free online tool:
1. Go to: https://www.markdowntopdf.com/
2. Upload `QUICK_START_GUIDE.md`
3. Download as PDF
4. Add to delivery folder

---

## **STEP 13: Final Checklist Before Delivery**
```
✅ All code files included
✅ requirements.txt created
✅ README.md complete with your contact info
✅ USER_GUIDE.md created
✅ DEPLOYMENT_GUIDE.md created
✅ CHANGELOG.md created
✅ PROJECT_STRUCTURE.md created
✅ ADMIN_CREDENTIALS.txt created
✅ QUICK_START_GUIDE created
✅ .gitignore created
✅ Database migrated
✅ Static files collected
✅ All features tested
✅ Admin account created
✅ Documentation reviewed
✅ Project zipped