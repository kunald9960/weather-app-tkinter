import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url="https://weather.com"#use this link and select your own country and paste the same address

master = Tk()
master.title=("Weather App")
master.config(bg="white")

img = Image.open("---the image path---")#copy paste your image path
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

def getWeather():
    page= requests.get(url)
    soup= BeautifulSoup(page.content, "html.parser")
    location= soup.find('h1', class_= "CurrentConditions--location--kyTeL").text
    temperature = soup.find('span', class_= "CurrentConditions--tempValue--3a50n").text
    weatherPrediction= soup.find('div', class_= "CurrentConditions--phraseValue--2Z18W").text
    locationLable.config(text= location)
    temperatureLable.config(text= temperature)
    weatherPredictionLabel.config(text= weatherPrediction)

locationLable= Label(master, font=("Sans Seriff", 20, "bold"))
locationLable.grid(row=0, sticky="N", padx=100)

temperatureLable= Label(master, font=("Sans Seriff", 80, "bold"))
temperatureLable.grid(row=1, sticky="W", padx=30, pady=0)

Label(master, image=img, bg="White").grid(row=1, sticky="E")
weatherPredictionLabel= Label(master, font=("Sans Seriff", 15, "bold"), bg="white")
weatherPredictionLabel.grid(row=2, sticky="W", padx=30, pady=0)

getWeather()
master.mainloop()
