from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile
from .models import Book  # Ensure Book model is imported



from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email


class SignInForm(AuthenticationForm):
    pass


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']


        from django import forms
from .models import Book

class AddBookForm(forms.ModelForm):
    search_title = forms.CharField(
        max_length=255, required=False, 
        widget=forms.TextInput(attrs={
            'id': 'book-search', 
            'placeholder': 'Search for a book...',
            'autocomplete': 'off'
        })
    )

class Meta:
    model = Book
    fields = ['title', 'author', 'genre', 'pages', 'cover_image', 'status']
    widgets = {
    'status': forms.Select(choices=Book.STATUS_CHOICES),
 }


class AddBookForm(forms.ModelForm):
    search_title = forms.CharField(
        max_length=255, required=False, 
        widget=forms.TextInput(attrs={
            'id': 'book-search', 
            'placeholder': 'Search for a book...',
            'autocomplete': 'off'
        })
    )

    class Meta:
        model = Book  # Ensure this is correctly defined!
        fields = ['title', 'author', 'genre', 'pages', 'cover_image', 'status']
        widgets = {
            'status': forms.Select(choices=Book.STATUS_CHOICES),
        }
