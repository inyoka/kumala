from django.contrib.auth.models import User
from www.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'first_name','last_name', 'email', 'password')

class ProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('bio', 'site', 'picture')