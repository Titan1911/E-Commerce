from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegiserUserForm(UserCreationForm):
    # email = forms.EmailField(widget=forms.EmailInput())
    # password1 = forms.CharField(max_length=50, help_text=None, label='Password')
    # password2 = forms.CharField(max_length=50, help_text=None, label='Password confirmation')
	# name = forms.CharField(max_length=50, widget=forms.TextInput()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # help_texts = {
        #     'username': None,
        #     'email': None,
        # }
    