from tkinter import *
from weather import Weather
from adapter import SpecialAdapter

kelvin_weather = Weather("fisciano")
meteo = SpecialAdapter(kelvin_weather, dict(
    get_temp = lambda: (kelvin_weather.get_temp() - 273),
    get_temp_min = lambda: (kelvin_weather.get_temp_min() - 273),
    get_temp_max = lambda: (kelvin_weather.get_temp_max() - 273)
))

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
    kelvin_weather.set_location( e.get() )
    tempString.set( str(round(meteo.get_temp(), 2)) + "C" )
    tempMaxString.set( str(round(meteo.get_temp_max(), 2)) + "C" )
    tempMinString.set( str(round(meteo.get_temp_min(), 2)) + "C" )

# Bottone per richiamare la funzione getMeteo
b = Button(master, text = "cerca", width = 10, command = getMeteo)
b.pack()

mainloop()