from django.shortcuts import render
from django.contrib import messages
import datetime
import requests

def home(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else :
        city = 'indore'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d905ae368a493542b8942421324cd599'
    PARAMS = {
        'q': city,
        'appid': 'AIzaSyDNT8q7p1ytoKEmOnW3dFrgy4cOohkpR_k',
        'units': 'metric'
    }

    API_KEY = 'AIzaSyDNT8q7p1ytoKEmOnW3dFrgy4cOohkpR_k'
    SEARCH_ENGINE_ID = 'b24d8c7ac50d9482f'

    query = city + "1920x1080"
    page = 1
    start = (page-1)*10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link']

    try:
          
          data = requests.get(url,params=PARAMS).json()
          description = data['weather'][0]['description']
          icon = data['weather'][0]['icon']
          temp = data['main']['temp']
          day = datetime.date.today()

          return render(request,'index.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city , 'exception_occurred':False ,'image_url':image_url})
    
    except KeyError:
          exception_occurred = True
          messages.error(request,'Entered data is not available to API')   
          # city = 'indore'
          # data = requests.get(url,params=PARAMS).json()
          
          # description = data['weather'][0]['description']
          # icon = data['weather'][0]['icon']
          # temp = data['main']['temp']
          day = datetime.date.today()

          return render(request,'index.html' ,{'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':'indore' , 'exception_occurred':exception_occurred } )
               
    
    