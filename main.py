import json
import csv
import requests
#import numpy as np
from datetime import datetime as dt 
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt
from matplotlib import style
plt.style.use('grayscale')

#import pandas as pd
#import pandas_datareader.data as web


#Citam podatke sa Steam-a
cookie = {'steamLoginSecure':' your SLS here'}    
raw = requests.get('http://steamcommunity.com/market/pricehistory/?country=PT&currency=3&appid=730&market_hash_name=Special Agent Ava | FBI', cookies=cookie)
raw2 = requests.get('http://steamcommunity.com/market/pricehistory/?country=PT&currency=3&appid=730&market_hash_name=The Elite Mr. Muhlik | Elite Crew', cookies=cookie)
raw3 = requests.get("http://steamcommunity.com/market/pricehistory/?country=PT&currency=3&appid=730&market_hash_name='The Doctor' Romanov | Sabre", cookies=cookie)
data=json.loads(raw.text)
data2=json.loads(raw2.text)
data3=json.loads(raw3.text)
#print(data2)
#print(data_json)

def delkljuceve(informacija):
    del informacija['success']
    del informacija['price_prefix']
    del informacija['price_suffix']
    #return data_json=json.dumps(informacija, indent=2)

def delpolja(informacija):
    for i in informacija['prices']:
        pom =i[0]
        po=pom.split(":")
        po.pop()
        del i[0]
        pomo= " "
        pomo=pomo.join(po)
        i.insert(0,pomo)
        i[0]=pomo

def val_to_list(informacija):
    zz=[]
    for i in informacija['prices'][1:]:
        zz.append(i[1])    
    return zz

def vreme(informacja):
    ww=[]
    for i in informacja['prices'][1:]:
        pom =i[0]
        pomocni=dt.strptime(pom,'%b %d %Y %H')
        ww.append(pomocni)
    return ww

delkljuceve(data)
delkljuceve(data2)
delkljuceve(data3)

delpolja(data)
delpolja(data2)
delpolja(data3)


x=vreme(data)
x2=vreme(data2)
x3=vreme(data3)
y=val_to_list(data)
y2=val_to_list(data2)
y3=val_to_list(data3)

#if(len(x)!=len(x2)):
plt.plot(x,y,label='Ava')
plt.plot(x,y2,label='Ricksaw') 
plt.plot(x,y3,label='Romanov')

#else:
 #   plt.plot(x2,y,label='Ava')
 #   plt.plot(x2,y2,label='Ricksaw')
  #  plt.plot(x2,y3,label='Romanov')

#Graf i njegova podesavanja 

#plt.style.use('seaborn-paper')
plt.xlabel('Time')
plt.ylabel('Price')
plt.xticks(rotation=45)
#plt.plot(x,y,label='Ava')
#plt.plot(x2,y2,label='Ricksaw')
plt.legend()
plt.show()