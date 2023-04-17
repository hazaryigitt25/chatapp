from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label="User Name")
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    confirm = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        
        if password and confirm and password != confirm:
            raise forms.ValidationError('Passwords Does Not Match!')
        
        values = {
            'username' : username,
            'email' : email,
            'password' : password
        }
        return values

class LoginForm(forms.Form):
    username = forms.CharField(max_length=80,label="Username")
    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    
class ChatForm(forms.Form):
    chat_name = forms.CharField( max_length=80, required=True,label="Chat Name")
    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    confirm = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
    
    def clean(self):
        chat_name = self.cleaned_data.get('chat_name')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        
        if password and confirm and password != confirm:
            raise forms.ValidationError('Passwords Does Not Match!')
        
        values = {
            'chat_name':chat_name,
            'password' : password
        }
        return values
    
class ChatLoginForm(forms.Form):
    password = forms.CharField(label="Chat Password",widget=forms.PasswordInput)
    
class ChangePasswordForm(forms.Form):
    oldpassword = forms.CharField(label="Current Password",widget=forms.PasswordInput)
    newpassword = forms.CharField(label="New Password",widget=forms.PasswordInput)
    confirm = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
    
    def clean(self):
        oldpassword = self.cleaned_data.get('oldpassword')
        newpassword = self.cleaned_data.get('newpassword')
        confirm = self.cleaned_data.get('confirm')
        
        if newpassword != confirm:
            raise forms.ValidationError('Passwords does not match!')
        
        values = {
            'oldpassword':oldpassword,
            'newpassword':newpassword
        }
        return values