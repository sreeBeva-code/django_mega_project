from django import forms
from .models import Tweet  # Import the Tweet model for creating a form related to Tweets
from django.contrib.auth.forms import UserCreationForm  # Import the built-in UserCreationForm
from django.contrib.auth.models import User  # Import the User model for handling user registration

# Tweet form
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet  # Use the Tweet model for the form
        fields = ['text', 'photo']  # Include the 'text' and 'photo' fields in the form

# User registration form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()  # Add an email field to the registration form

    class Meta:
        model = User  # Use the User model for user registration
        fields = ('username', 'email', 'password1', 'password2')  # Include username, email, and password fields
