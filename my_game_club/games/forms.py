from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(max_length=30, required=True)
	last_name = forms.CharField(max_length=30, required=True)

	class Meta:
		model = User
		fields = (
			"username",
			"email",
			"first_name",
			"last_name",
			"password1",
			"password2",
		)
   

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# 🔇 Remove Django help texts
		for field in self.fields.values():
			field.help_text = ""

		# ✨ Add placeholders (labels stay clean)
		self.fields["username"].widget.attrs.update({"placeholder": "Username"})
		self.fields["email"].widget.attrs.update({"placeholder": "Email address"})
		self.fields["first_name"].widget.attrs.update({"placeholder": "First name"})
		self.fields["last_name"].widget.attrs.update({"placeholder": "Last name"})
		self.fields["password1"].widget.attrs.update({"placeholder": "Password"})
		self.fields["password2"].widget.attrs.update({"placeholder": "Confirm password"})
	 
		
	
	def save(self, commit=True):
		user = super().save(commit=False)
		user.first_name = self.cleaned_data["first_name"]
		user.last_name = self.cleaned_data["last_name"]
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user