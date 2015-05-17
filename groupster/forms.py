from django import forms
from .models import JobSeeker


class JobseekerForm(forms.ModelForm):
	name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
	gender = forms.ChoiceField(choices= JobSeeker.gender_choices, widget=forms.Select(attrs={'class': 'form-control'}))
	college = forms.CharField(label="College", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Drexel University'}))
	year_in_college = forms.ChoiceField(label="grade", choices=JobSeeker.grade_choices, widget=forms.Select(attrs={'class': 'form-control'}))
	college_email = forms.CharField(label="College Email", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'jared@drexel.edu'}))
	positions_interested_in = forms.ChoiceField(label="What positions are you interested in?", choices=JobSeeker.open_position_choices, widget=forms.Select(attrs={'class':'form-control'}))
	affiliated_with_greek_life = forms.CharField(label="Are you affilliated with greek life?", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Your answer here...'}))
	why_groupster = forms.CharField(label="Why Do you want to work for Groupster?", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Because...'}))
	skills = forms.CharField(label="What would you be able to do for Groupster?", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "I'm really good at design!"}))
	why_hire = forms.CharField(label="Why Do you want to work for Groupster?", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is your chance to sell yourself.'}))
	resume = forms.FileField()
	class Meta:
		model = JobSeeker
		fields = ['name', 'gender', 'college', 'year_in_college', 'college_email', 'positions_interested_in', 'affiliated_with_greek_life', 'why_groupster', 'skills', 'why_hire', 'resume']
		
	
	