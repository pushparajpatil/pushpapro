from django import forms

class StudentForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    address=forms.CharField() 
    # password=forms.CharField( max_length=50 , required=False,widget=forms.Textarea())
    # feepaid=forms.CharField(widget=forms.TextInput())