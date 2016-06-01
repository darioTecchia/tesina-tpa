import requests, json

class Weather(object):
  
    __URL__ = 'http://api.openweathermap.org/data/2.5/weather?q='
    __API_KEY__ = '0cc418d28075d2b9ddc300c3493046e4'
    
    def __init__(self, location):
        self.location = location
        
    def set_location(self, location):
        self.location = location
    
    def get_temp(self):
        r = requests.get(self.__URL__ + self.location + '&APPID=' + self.__API_KEY__).json()
        return r['main']['temp']
    
    def get_temp_min(self):
        r = requests.get(self.__URL__ + self.location + '&APPID=' + self.__API_KEY__).json()
        return r['main']['temp_min']
        
    def get_temp_max(self):
        r = requests.get(self.__URL__ + self.location + '&APPID=' + self.__API_KEY__).json()
        return r['main']['temp_max']