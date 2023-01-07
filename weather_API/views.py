from dataclasses import dataclass
from datetime import datetime
from multiprocessing import context
from django.shortcuts import render
import requests




'''*******************************************-------------------------------------'''
tnow=datetime.now()
# new_var = day=datetime.date.today()

'''*******************************************-------------------------------------'''
def index(request):

    city=request.GET.get('city',"Kolkata")
    url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=992d226ac056c15f09f12cadf860f9ec'
    data=requests.get(url).json()
    
    payload={
        
        'city' : data['name'],
        'weather': data['weather'][0]['main'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon'],#"https://openweathermap.org/img/wn/04d.png
        'K_temperature': int(data['main']['temp']),
        'C_temperature':int(data['main']['temp']-273),
        'pressure':data['main']['pressure'],
        'humidity':data['main']['humidity'],
        'wind_speed':data['wind']['speed'],
        'Time':tnow,
        # 'nowday': day
        
    }

    context={'data':payload}
    #

   

    return render(request,'index.html',context)




'''{"coord":{"lon":88.3697,"lat":22.5697},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],
"base":"stations",
"main":{"temp":300.12,"feels_like":303.7,"temp_min":300.12,"temp_max":300.12,"pressure":1005,"humidity":89,"sea_level":1005,"grnd_level":1003},
"visibility":3200,
"wind":{"speed":4.12,"deg":110},
"clouds":{"all":75}
"dt":1663645666,
"sys":{"type":1,"id":9114,
"country":"IN","sunrise":1663631673,"sunset":1663675547},"timezone":19800,"id":1275004,"name":"Kolkata","cod":200}
'''


