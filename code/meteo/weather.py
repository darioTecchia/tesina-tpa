import requests, json

class Weather(object):
  
    __URL__ = 'http://api.openweathermap.org/data/2.5/weather?q='
    __API_KEY__ = '0cc418d28075d2b9ddc300c3493046e4'
    
    def get_weather(self, location):
        r = requests.get(self.__URL__ + location + '&APPID=' +  self.__API_KEY__).json()
        
        info = {
            'temp'      : r['main']['temp'],
            'temp_max'  : r['main']['temp_max'],
            'temp_min'  : r['main']['temp_min']
        }
        return info
        