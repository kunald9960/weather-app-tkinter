import tkinter as tk
from tkinter.constants import ANCHOR
import requests
from tkinter.font import BOLD
from PIL import Image,ImageTk #pip install pillow

root=tk.Tk()
root.title("Weather App")
root.geometry("580x400")

def format_response(weather):
    try:
        city=weather['name']
        condition=weather['weather'][0]['main']
        temp=weather['main']['temp']
        humidity=weather['main']['humidity']
        country=weather['sys']['country']
        final_str='City : %s\nCondition : %s\nTemperature : %s\nHumidity : %s\nCountry: %s'%(city,condition,temp,humidity,country)
    except:
        final_str='Cannot show the data due to some error'
    return final_str

def weather1(city):
    weather_key='e299a13093bb78424d806adc86ba1adf' #if its not working you can use your own API keys from the link given in READ.ME
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units':'imperial'}
    response=requests.get(url,params)
    weather=response.json()
    result['text']=format_response(weather)
    icon_name=weather['weather'][0]['icon']
    open_img(icon_name)

def open_img(icon):
    size=int(frame_two.winfo_height()*0.6)
    img=ImageTk.PhotoImage(Image.open('--IMG PATH--'+icon+'.png').resize((size,size)))
    weathericon.delete('all')
    weathericon.create_image(0,0,anchor='nw',image=img)
    weathericon.image=img

img=Image.open("--IMG PATH--")
img=img.resize((600,420))
img_photo=ImageTk.PhotoImage(img)

bg_lbl=tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=420)

heading_title=tk.Label(bg_lbl,text='Weather App GUI',bg='#D7E9F7',font=('poppins,sans-serif',30))
heading_title.place(x=128,y=18)

frame_one=tk.Frame(bg_lbl,bg="#08D9D6",bd=5)
frame_one.place(x=45,y=80,width=490,height=50)

txt_box=tk.Entry(frame_one,font=('poppins,sans-serif',23),width=20)
txt_box.grid(row=0,column=0,sticky='W')

btn=tk.Button(frame_one,text='Search',font=('poppins,sans-serif',15),width=11,command=lambda:weather1(txt_box.get()))
btn.grid(row=0,column=1,padx=5)

frame_two=tk.Frame(bg_lbl,bg="#FF2E63",bd=5)
frame_two.place(x=45,y=150,width=490,height=232)

result=tk.Label(frame_two,font=('poppins,sans-serif',22),justify='left',anchor='nw')
result.place(relwidth=1,relheight=1)#relation for parent class

weathericon=tk.Canvas(result,bd=0,highlightthickness=0)
weathericon.place(relx=.75,rely=0,relwidth=2,relheight=2)

root.mainloop()
