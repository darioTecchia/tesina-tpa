class MeteoAdapter(object):
    
    def __init__(self, legacy_weather):
        self.legacy_weather = legacy_weather
    
    def get_meteo(self, posizione):
        meteo = self.legacy_weather.get_weather(posizione)
        meteo['temp']       = (meteo['temp'] - 273)
        meteo['temp_min']   = (meteo['temp_min'] - 273)
        meteo['temp_max']   = (meteo['temp_max'] - 273)
        return meteo