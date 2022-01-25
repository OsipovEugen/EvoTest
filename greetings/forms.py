from django import forms
from django.core.exceptions import ValidationError
from .models import Person

class GreetingsForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ['email']

	def clean_email(self):	
			new_email = self.cleaned_data['email']
			if Person.objects.filter(email__iexact=new_email).count():
				raise ValidationError(f'Вже бачилися {new_email}') 
			return new_email
