from django.shortcuts import render
# views.py
# Create your views here.


def home(request):
	import json
	import requests
	api_requests= requests.get('http://api.openweathermap.org/data/2.5/weather?lat=35.2434&lon=58.4687&appid=1e1072d2385783cf795223083eea52fd')
	
	try:
		api=json.loads(api_requests.content)

	except Exception as e:
		api= "Error ...."
#		api_requests_1= requests.get('api.openweathermap.org/data/2.5/forecast/daily?lat=35.2434&lon=58.4687&cnt=7&appid=1e1072d2385783cf795223083eea52fd')
	
#	try:
#		api_1=json.loads(api_requests_1.content)

#	except Exception as e:
#		api_1= "Error ...."

	#https://api.openweathermap.org/data/2.5/onecall?lat={35.2434}&lon={58.4687}&appid={1e1072d2385783cf795223083eea52fd}
	return render(request, 'home_1.html', {'api': api })


def about(request):
	return render(request, 'about.html', {})