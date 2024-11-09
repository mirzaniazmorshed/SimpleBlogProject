from django import forms
from.models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__" #sobgula asbe field
        # fields = ['name', 'bio'] shudu name r bio field use korar jonno
        # exclude =  ['name'] shudu name chara baki sob use korar jonno 