from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from courses.models import CourseEnrollment

class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'birth_date', 'gender']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'birth_date', 'gender']

class CourseEnrollmentForm(forms.ModelForm):
    class Meta:
        model = CourseEnrollment
        fields = [] 
        
        
