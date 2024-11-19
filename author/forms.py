from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = "__all__" #sobgula asbe field
#         # fields = ['name', 'bio'] shudu name r bio field use korar jonno
#         # exclude =  ['name'] shudu name chara baki sob use korar jonno 

class RegistrationForm(UserCreationForm):
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
            
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']         
        
class ChangeUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields =  ['username', 'first_name', 'last_name', 'email']
     
                                                            