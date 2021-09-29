import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url="https://weather.com/en-IN/weather/today/l/5b820928fa0d62db5f789c705901d462a1132494082633c46cc2c5e8b8c14546"

master = Tk()
master.title=("Weather App")
master.config(bg= "white")

img = Image.open("C:/Users/Kunal/Desktop/Weather.png")
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

def getWeather():
    page= requests.get(url)
    soup= BeautifulSoup(page.content, "html.parser")
    location= soup.find('h1', class_="CurrentConditions--location--kyTeL").text
    temperature = soup.find('span', class_="CurrentConditions--tempValue--3a50n").text
    weatherPrediction= soup.find('div', class_="CurrentConditions--phraseValue--2Z18W").text
    High= soup.find('div', class_="WeatherDetailsListItem--label--3PkXl").text
    locationLable.config(text=location)
    temperatureLable.config(text=temperature)
    weatherPredictionLabel.config(text=weatherPrediction)

locationLable= Label(master, font=("Sans Seriff", 20,"bold"))
locationLable.grid(row=0, sticky="N",padx=100)

temperatureLable= Label(master, font=("Sans Seriff", 80,"bold"))
temperatureLable.grid(row=1, sticky="W",padx=30,pady=0)

Label(master, image=img, bg="White").grid(row=1, sticky="E")
weatherPredictionLabel= Label(master, font=("Sans Seriff", 15, "bold"), bg="white")
weatherPredictionLabel.grid(row=2, sticky="W",padx=30,pady=0)

getWeather()
master.mainloop()
