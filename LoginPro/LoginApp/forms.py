from django import forms

class RegForm(forms.Form):
    first_name=forms.CharField(
        label='Enter Your Name:',
        widget=forms.TextInput(
            attrs={
                'placeholder':'First Name',
                'class':'form-control'
            }
        )
    )

    last_name=forms.CharField(
        label='Enter Your Last Name:',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Last Name',
                'class':'form-control'
            }
        )
    )

    username=forms.CharField(
        label='Enter Username:',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Username',
                'class':'form-control'
            }
        )
    )

    password=forms.CharField(
        label='Enter Password:',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Password',
                'class':'form-control'
            }
        )
    )

    mobile=forms.IntegerField(
        label='Enter Mobile Number:',
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Mobile Number',
                'class':'form-control'
            }
        )
    )

    email=forms.EmailField(
        label='Enter Your Email:',
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Email',
                'class':'form-control'
            }
        )
    )

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Enter Username:',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Usrname',
                'class': 'form-control'
            }
        )
    )

    password = forms.CharField(
        label='Enter Password:',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control'
            }
        )
    )
