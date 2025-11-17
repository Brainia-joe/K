from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage, TourBooking
from .models import User
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    """Show the homepage"""
    return render(request, 'properties/index.html')

def submit_contact(request):
    """Handle contact form submission"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        messages.success(request, 'Thank you! Your message has been sent.')
        return redirect('home')
    
    return redirect('home')

def submit_booking(request):
    """Handle tour booking submission"""
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        property_name = request.POST.get('property')
        preferred_date = request.POST.get('date')
        number_of_people = request.POST.get('people')
        message = request.POST.get('message')
        
        # Save to database
        TourBooking.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            property_name=property_name,
            preferred_date=preferred_date,
            number_of_people=number_of_people,
            message=message
        )
        
        messages.success(request, 'Tour booking submitted! We will contact you soon.')
        return redirect('home')
    
    return redirect('home')

def signup(request):
    """Handle user signup with email verification"""
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        # Validation
        if password != password_confirm:
            messages.error(request, 'Passwords do not match!')
            return redirect('home')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return redirect('home')
        
        # Create user
        user = User(
            full_name=full_name,
            email=email,
            phone=phone,
            username=username,
            email_verified=False  # Not verified yet
        )
        user.set_password(password)
        token = user.generate_verification_token()
        user.save()
        
        # Send verification email
        verification_url = request.build_absolute_uri(f'/verify-email/{token}/')
        try:
            send_mail(
                subject='Verify Your Email - Kenyan Homes',
                message=f'''
            Hello {full_name},

            Thank you for signing up at Kenyan Homes!

            Please verify your email by clicking the link below:
            {verification_url}

            If you didn't create this account, please ignore this email.

            Best regards,
            The Kenyan Homes Team
                            ''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            messages.success(request, f'Account created! Please check your email ({email}) to verify your account.')
        except:
            messages.warning(request, 'Account created but verification email failed to send. Please contact support.')
        
        return redirect('home')
    
    return redirect('home')

def login_user(request):
    """Handle user login"""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        
        try:
            user = User.objects.get(email=email)
            
            if user.check_password(password):
                # Store user info in session
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                request.session['full_name'] = user.full_name
                
                # Set session expiry
                if remember:
                    request.session.set_expiry(1209600)  # 2 weeks
                else:
                    request.session.set_expiry(0)  # Browser close
                
                messages.success(request, f'Welcome back, {user.full_name}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password.')
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
        
        return redirect('home')
    
    return redirect('home')

def logout_user(request):
    """Handle user logout"""
    username = request.session.get('full_name', 'User')
    request.session.flush()  # Clear all session data
    messages.success(request, f'Goodbye, {username}! You have been logged out.')
    return redirect('home')

def verify_email(request, token):
    """Verify user email"""
    try:
        user = User.objects.get(verification_token=token)
        user.email_verified = True
        user.verification_token = None
        user.save()
        
        # Auto-login after verification
        request.session['user_id'] = user.id
        request.session['username'] = user.username
        request.session['full_name'] = user.full_name
        
        messages.success(request, 'Email verified successfully! You are now logged in.')
    except User.DoesNotExist:
        messages.error(request, 'Invalid verification link.')
    
    return redirect('home')

def reset_password_request(request):
    """Request password reset"""
    if request.method == 'POST':
        email = request.POST.get('email')
        
        try:
            user = User.objects.get(email=email)
            token = user.generate_verification_token()
            user.save()
            
            reset_url = request.build_absolute_uri(f'/reset-password/{token}/')
            
            send_mail(
                subject='Password Reset - Kenyan Homes',
                message=f'''
            Hello {user.full_name},

            You requested to reset your password.

            Click the link below to reset your password:
            {reset_url}

            If you didn't request this, please ignore this email.

            Best regards,
            The Kenyan Homes Team
                            ''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            messages.success(request, 'Password reset link sent to your email!')
        except User.DoesNotExist:
            messages.error(request, 'Email not found.')
        
        return redirect('home')
    
    return redirect('home')

def reset_password_confirm(request, token):
    """Confirm password reset"""
    try:
        user = User.objects.get(verification_token=token)
    except User.DoesNotExist:
        messages.error(request, 'Invalid reset link.')
        return redirect('home')
    
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('reset_password_confirm', token=token)
        
        user.set_password(new_password)
        user.verification_token = None
        user.save()
        
        messages.success(request, 'Password reset successfully! Please log in.')
        return redirect('home')
    
    return render(request, 'properties/reset_password.html', {'token': token})

def user_profile(request):
    """User profile page"""
    if not request.session.get('user_id'):
        messages.error(request, 'Please log in to view your profile.')
        return redirect('home')
    
    user = User.objects.get(id=request.session['user_id'])
    
    if request.method == 'POST':
        user.full_name = request.POST.get('full_name')
        user.phone = request.POST.get('phone')
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('user_profile')
    
    # Get user's bookings and messages
    bookings = TourBooking.objects.filter(email=user.email).order_by('-created_at')
    contact_messages = ContactMessage.objects.filter(email=user.email).order_by('-created_at')
    
    return render(request, 'properties/profile.html', {
        'user': user,
        'bookings': bookings,
        'contact_messages': contact_messages
    })