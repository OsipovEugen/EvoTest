from django import forms
from django.core.exceptions import ValidationError
from .models import Person


# class GreetingsForm(forms.ModelForm):
# 	class Meta:
# 		model = Person
# 		fields = ['email']
# 		success_url = 'greetings/yes'


# 	def cleaned(self):
# 		cleaned_data = super().clean()
# 		email = cleaned_data.get['email']
# 		artist_exists = email is not None and Person.objects.filter(email=email).exists()
# 		if not artist_exists:
# 			raise forms.ValidationError("Hello, sir")
# 		return cleaned_data


class GreetingsForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ['email']

	def clean_email(self):	
			new_email = self.cleaned_data['email']
			if Person.objects.filter(email__iexact=new_email).count():
				raise ValidationError(f'Вже бачилися {new_email}') # Для создания только уникальных slug
			return new_email
