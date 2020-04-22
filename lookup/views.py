from django.shortcuts import render
# views.py
# Create your views here.
def home(request):
	return render(request, 'home_1.html', {})


def about(request):
	return render(request, 'about.html', {})