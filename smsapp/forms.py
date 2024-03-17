from django import forms
from .models import StudentModel  # Import your StudentModel

class StudentForm(forms.ModelForm):
	class Meta:
		model = StudentModel
		fields = "__all__"
       
