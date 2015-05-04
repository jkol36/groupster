from django.contrib import admin
from .models import JobSeeker

class JobSeekerAdmin(admin.ModelAdmin):
	list_display = ['name', 'gender', 'college', 'year_in_college', 'college_email', 'positions_interested_in', 'affiliated_with_greek_life', 'why_groupster', 'skills', 'why_hire']


admin.site.register(JobSeeker, JobSeekerAdmin)