# views.py contains views for authentication and user management.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import Userform, LoginForm
from .models import User

# login_view implements role-based login: email for admin, username/ID/QR for instructor/student, enforcing role restrictions.
def login_view(request):
    # TODO: Implement QR code parsing and mapping to username/ID for instructor/student login
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        identifier = form.cleaned_data['identifier']
        password = form.cleaned_data['password']
        user = None
        # Admin login via email
        if '@' in identifier:
            try:
                user_obj = User.objects.get(email=identifier)
                if user_obj.role == User.ADMIN:
                    user = authenticate(request, email=identifier, password=password)
                else:
                    messages.error(request, 'Only admins can login with email.')
            except User.DoesNotExist:
                messages.error(request, 'Invalid credentials.')
        else:
            # Instructor/Student login via username/ID
            try:
                user_obj = User.objects.get(username=identifier)
                if user_obj.role in [User.INSTRUCTOR, User.STUDENT]:
                    user = authenticate(request, username=identifier, password=password)
                else:
                    messages.error(request, 'Only instructors/students can login with ID/username.')
            except User.DoesNotExist:
                messages.error(request, 'Invalid credentials.')
        if user is not None:
            login(request, user)
            return redirect('profile')  # or dashboard
        else:
            if not messages.get_messages(request):
                messages.error(request, 'Invalid credentials.')
    return render(request, 'registration/login.html', {'form': form})

# signup_view handles user registration.
def signup_view(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            #  set our password in an hashed format in here !
            user.set_password(form.cleaned_data['password'])
            user.role = User.STUDENT
            user.save()
            messages.success(request, 'Registration successful!')
            # login(request, user)
            return redirect('signup')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = Userform()
    return render(request, 'registration/register.html', {'form': form})
    
# def password_reset_view(request):
#     return render(request, 'registration/password_reset.html')

# def password_reset_done_view(request):
#     return render(request, 'registration/password_reset_done.html')

# def password_reset_confirm_view(request, uidb64, token):
#     return render(request, 'registration/password_reset_confirm.html', {'uidb64': uidb64, 'token': token})

# def password_reset_complete_view(request):
#     return render(request, 'registration/password_reset_complete.html')

def forgot_password_view(request):
    return HttpResponse('Forgot password page (placeholder).')

# def edit_profile_view(request):
#     return render(request, 'registration/edit_profile.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def profile_view(request):
    return render(request, 'registration/profile.html')
# Create your views here.
