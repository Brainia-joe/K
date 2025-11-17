from django.contrib import admin
from .models import ContactMessage, TourBooking
from .models import User

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email']

@admin.register(TourBooking)
class TourBookingAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'property_name', 'preferred_date', 'created_at']
    list_filter = ['property_name', 'preferred_date']
    search_fields = ['full_name', 'email']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name', 'email', 'phone', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['username', 'full_name', 'email']
    readonly_fields = ['password', 'created_at']