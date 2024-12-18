from django import forms
from .models import Contact
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):

    picture = forms.ImageField(
        widget= forms.FileInput(
            attrs= {
                'accept': 'image/*'
            }
        )
    )
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs= {
                'placeholder': 'Escreva Aqui' 
            }
        ),
        help_text= 'Texto de ajuda'
    )

    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'phone','email','description','category','picture',

    def clean(self):
 
        return super().clean()
    

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 
                  'username', 'password1', 'password2',)
        
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error('email',
                           ValidationError('Já existe este email', code='invalid'))