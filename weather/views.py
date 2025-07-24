from django.shortcuts import render
import requests

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=71c406cd0696048af1069afda7277927'

    city = 'Las Vegas'

    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }
    
    context = {'weather' : weather}

    print(city_weather) #temporarily view output


    return render(request, 'weather/index.html',context) #returns the index.html template
