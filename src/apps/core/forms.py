from dataclasses import field
from .models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):

    # used to edit the CSS/HTML of the form input fields
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            'id':'name',
            'class':'input'
        })
        self.fields["email"].widget.attrs.update({
            'id':'email',
            'class':'input'
        })
        self.fields["password1"].widget.attrs.update({
            'id':'password1',
            'class':'input'
        })
        self.fields["password2"].widget.attrs.update({
            'id':'password2',
            'class':'input'
        })

    class Meta:
        model=User
        fields=['name','email','password1','password2']
