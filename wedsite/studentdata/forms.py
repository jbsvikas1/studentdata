from django import forms
from studentdata.models import student

class studentForm(forms.ModelForm):
	class Meta:
		model=student
		fields="__all__"