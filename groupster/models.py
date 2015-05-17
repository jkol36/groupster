from django.db import models


class JobSeeker(models.Model):
	gender_choices = (
		('Male', 'Male'),
		('Female', 'Female'),
	)
	grade_choices = (
		('Freshman', 'Freshman'),
		('Sophomore', 'Sophomore'),
		('Junior', 'Junior'),
		('Senior', 'Senior'),
		('Graduated', 'Graduated'),
		('Not_in_college', 'Not In College'),

	)
	open_position_choices = (
		('Campus Ambassador', 'Campus Ambassador'),
	)
	name = models.CharField(blank=True, null=True, max_length=200)
	gender = models.CharField(choices=gender_choices, max_length=200, blank=True, null=True)
	college = models.CharField(max_length=200, blank=True, null=True)
	year_in_college = models.CharField(choices=grade_choices, blank=True, null=True, max_length=200)
	college_email = models.EmailField(max_length=200, null=True, blank=True)
	positions_interested_in = models.CharField(choices=open_position_choices, max_length=200)
	affiliated_with_greek_life = models.CharField(max_length=200, null=True, blank=True)
	why_groupster = models.CharField(max_length=200, null=True, blank=True)
	skills = models.CharField(max_length=200, null=True, blank=True)
	why_hire = models.CharField(max_length=200, null=True, blank=True)



