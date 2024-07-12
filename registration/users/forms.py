from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields=[
            'first_name','email','username','password1','password2'
        ]

        
        def __init__(self, *args, **kwargs):
            super(UserCreationForm, self).__init__(*args, **kwargs)

            for name, filed in self.fields.items():
                filed.widget.attrs.update({'class': 'form-styling'})