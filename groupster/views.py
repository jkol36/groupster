from django.shortcuts import render, redirect
from .forms import JobseekerForm
from django.contrib import messages



def LandingView(request):
	return render(request, 'landing.html')

def JobsView(request):
	if request.POST:
		print request.POST
		form = JobseekerForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, "Thank You! We'll be in touch!")
			return redirect('jobs')
		else:
			for t, z in form.errors.items():
				messages.error(request, t+z.as_text())
			return redirect('jobs')

	return render(request, 'jobs.html', {'form': JobseekerForm})

def AboutView(request):
	return render(request, 'about.html')

def ContactUsView(request):
	return render(request, 'contact.html')






