from django import forms
from crud.models import Student
# Create your tests here.
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
