from django import forms
from.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__" #sobgula asbe field
        # fields = ['name', 'bio'] shudu name r bio field use korar jonno
        # exclude =  ['name'] shudu name chara baki sob use korar jonno 