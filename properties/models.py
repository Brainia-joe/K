from django.db import models
from django.contrib.auth.hashers import make_password, check_password
import secrets

# This stores contact form messages
class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    replied = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.email}"

# This stores tour bookings
class TourBooking(models.Model):
    PROPERTY_CHOICES = [
        ('wilma', 'Wilma Towers'),
        ('diamond', 'Diamond Homes'),
    ]
    
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    property_name = models.CharField(max_length=50, choices=PROPERTY_CHOICES)
    preferred_date = models.DateField()
    number_of_people = models.IntegerField(default=1)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.full_name} - {self.get_property_name_display()}"

# This stores user accounts
class User(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    email_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.username} ({self.email})"
    
    def set_password(self, raw_password):
        """Hash the password before saving"""
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        """Check if password is correct"""
        return check_password(raw_password, self.password)
    
    def generate_verification_token(self):
        """Generate unique verification token"""
        self.verification_token = secrets.token_urlsafe(32)
        return self.verification_token