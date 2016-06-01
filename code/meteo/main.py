from tkinter import *
from weather import Weather
from meteo import MeteoAdapter

a_legacy_weather_station = Weather()
celsius_weather = MeteoAdapter(a_legacy_weather_station)

master = Tk()

# Text Input
e = Entry(master)
e.pack()

# Label per la Temperatura
temp = Label(master, text='Temperatura:')
temp.pack()

# Label per visualizzare la temperatura
tempString = StringVar()
tempLabel = Label(master, textvariable=tempString)
tempLabel.pack()

# Label per la Temperatura Minima
tempmin = Label(master, text='Minima:')
tempmin.pack()

# Label per visualizzare la temperatura minima
tempMinString = StringVar()
tempMinLabel = Label(master, textvariable=tempMinString)
tempMinLabel.pack()

# Label per la Temperatura Massima
tempmax = Label(master, text='Massima:')
tempmax.pack()

# Label per visualizzare la temperatura massima
tempMaxString = StringVar()
tempMaxLabel = Label(master, textvariable=tempMaxString)
tempMaxLabel.pack()

# Funzione per ottenere temperatura attuale, minima e massima convertite in celsius
def getMeteo():
    info = celsius_weather.get_meteo( e.get() )
    tempString.set( str(round(info['temp'], 2)) + "C" )
    tempMaxString.set( str(round(info['temp_max'], 2)) + "C" )
    tempMinString.set( str(round(info['temp_min'], 2)) + "C" )

# Bottone per richiamare la funzione getMeteo
b = Button(master, text = "cerca", width = 10, command = getMeteo)
b.pack()

mainloop()