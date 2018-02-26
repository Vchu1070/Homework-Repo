
# WeatherPy - Chu
Observable Trend 1: As latitudes approach the equator, temperature rises
Observable Trend 2: As latitudes approach the equator, most cities cite humidity upwards of 60%
Observable Trend 3: Even distribution of cloudiness across all latitudes


```python
import requests
import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import random
from citipy import citipy
import csv
import os
```


```python
baseurl = "http://api.openweathermap.org/data/2.5/weather?"
api_key="1e30368c74b7ade947ced938f5b5a8c4"
```


```python
def format_query(baseurl, lat, lon, api_key):
    return f"{baseurl}lat={lat}&lon={lon}&APPID={api_key}"
```


```python
latitude = []
seen_lat = set()
for i in range(700):
    lat = random.uniform(-90,90)
    while lat in seen_lat:
        lat= random.uniform(-90,90)
        seen_lat.add(lat)
    latitude.append(lat)
longitude = []
seen_lon = set()
for i in range(700):
    lon= random.uniform(-180,180)
    while lon in seen_lon:
        lon = random.uniform(-180,180)
        seen_lon = add(lon)
    longitude.append(lon)
```


```python
citylist=[]
seen_city = set()
for i in range(700):
    api_query=format_query(baseurl,latitude[i],longitude[i],api_key)
    response = requests.get(api_query).json()
    city_lat = response["coord"]["lat"]
    city_lon = response["coord"]["lon"]
    cityname = citipy.nearest_city(city_lat,city_lon)
    city_list = cityname.city_name
    citylist.append(city_list)
```


```python
def format_url(baseurl,api_key,citylist):
    return f"{baseurl}&APPID={api_key}&q={citylist}&units=imperial".format(baseurl,api_key,citylist)
```


```python
weather_data=[]
for i in citylist:
    city_link = format_url(baseurl,api_key,i)
    response=requests.get(city_link).json()
    if response["cod"]=="404":
        del(i)
    else:   
        weather_data.append(response)
    print(city_link)
    
```

    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=port alfred&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=port elizabeth&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kieta&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=airai&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hurricane&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=new norfolk&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=zaria&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=castro&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=lagoa&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=georgetown&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=leningradskiy&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=dikson&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=zambezi&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=albany&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mataura&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=zhezkazgan&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mahebourg&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=pangody&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=albany&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=thompson&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tsihombe&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=namibe&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=busselton&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hermanus&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=sao joao da barra&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=college&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=esperance&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=longyearbyen&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=nago&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bursa&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=busselton&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=port alfred&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hermanus&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=jalu&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kaitangata&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=keflavik&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cabo san lucas&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=the valley&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=geraldton&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kogon&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=coahuayana&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bonfim&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cockburn town&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=georgetown&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=barentsburg&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=vaini&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=port alfred&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=nanortalik&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=iqaluit&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=nome&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cooma&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=taolanaro&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=san patricio&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=airai&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cape town&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=vaini&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=provideniya&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ribeira grande&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mar del plata&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=khatanga&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kaeo&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=beaverlodge&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=vaitape&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=longyearbyen&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=puerto ayora&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bluff&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=makasar&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hobart&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=anadyr&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=lobito&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=pont-audemer&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=butaritari&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=marondera&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=vestmannaeyjar&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cidreira&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=provideniya&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=albany&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mahebourg&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mataura&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=malanje&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rungata&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=chuy&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bathsheba&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=marcona&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=jamestown&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=padang&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kamenskoye&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=soubre&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=jamestown&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tuktoyaktuk&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bredasdorp&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cleburne&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=harer&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mataura&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hermanus&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=oussouye&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=broome&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=laguna&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=nhulunbuy&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=saleaula&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tromso&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=the valley&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mar del plata&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=puerto ayora&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=abu kamal&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=nikolskoye&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=carnarvon&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mataura&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mys shmidta&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=zarya&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=santa helena&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=puerto ayora&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bonthe&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=vardo&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mar del plata&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=nikolskoye&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=albany&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=buraydah&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=muhos&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=chagoda&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=punta arenas&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=barentsburg&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=jonkoping&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=port augusta&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=quang ngai&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mahebourg&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=saint-philippe&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=port alfred&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=qaanaaq&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=college&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=biltine&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=srivardhan&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kingaroy&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=puerto ayora&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=sao filipe&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mar del plata&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=urumqi&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=jamestown&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=flinders&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=yerbogachen&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=victoria&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=camacha&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=khatanga&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ancud&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=olafsvik&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tasiilaq&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=xichang&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=puerto ayora&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=jamestown&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cabedelo&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cape town&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=amderma&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hermanus&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hermanus&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=arraial do cabo&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=salumbar&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=lompoc&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mackay&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=puerto ayora&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=piacabucu&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=pisco&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=chuy&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=nanortalik&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bourail&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=azimur&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=antofagasta&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=huazolotitlan&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hilo&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=gushikawa&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=paamiut&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=wanaka&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hilo&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=amderma&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=husavik&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=shagonar&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=port elizabeth&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mys shmidta&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tuktoyaktuk&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mataura&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=fortuna&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=clovis&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bredasdorp&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=matamoros&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=raudeberg&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=albany&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=vaini&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=gobabis&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=vaini&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=lorengau&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kununurra&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hermanus&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cape town&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=airai&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tsihombe&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=vaini&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=necochea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bluff&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=new norfolk&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=koslan&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kushiro&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=melivoia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=atuona&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=avarua&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ratnagiri&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=plettenberg bay&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tasiilaq&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=arraial do cabo&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hobart&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=yellowknife&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kaka&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=illoqqortoormiut&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=puerto ayora&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=higuey&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=punta arenas&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bolungarvik&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bambous virieux&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=suntar&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mataura&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hermanus&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kapaa&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=atar&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ust-maya&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=illoqqortoormiut&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bambous virieux&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=vestmannaeyjar&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kieta&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=nikolskoye&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=atuona&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=adelaide&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hirara&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=williston&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=belushya guba&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=grand island&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hualmay&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=chomun&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=clyde river&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mataura&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=san patricio&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=albany&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mataura&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hilo&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kemi&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=vaini&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hobart&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=uniao&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=norman wells&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=busselton&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=necochea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tala&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=padang&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=guerrero negro&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=lima&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=albany&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=danville&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=fortuna&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tuktoyaktuk&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=peniche&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mataura&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=severo-kurilsk&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=geraldton&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rorvik&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bambous virieux&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=abnub&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mataura&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=upernavik&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=airai&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hithadhoo&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=caravelas&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=punta arenas&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bilibino&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=avarua&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=davlekanovo&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bac can&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=chanthaburi&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=busselton&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=chapais&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=vanavara&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=berlevag&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bluff&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tura&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=prince rupert&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hilo&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=barentsburg&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=dikson&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=nikolskoye&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=sentyabrskiy&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bilma&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ngukurr&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kalabo&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=henties bay&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=iquitos&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hermanus&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=punta arenas&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=moose factory&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=butaritari&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=salinopolis&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kapaa&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cape town&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=azimur&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=marsa matruh&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mys shmidta&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=punta arenas&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=torbay&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=zhezkazgan&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bluff&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=lebu&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=takoradi&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ponta do sol&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bambous virieux&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=barentsburg&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=saint-avertin&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=attawapiskat&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=dikson&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=nizhneyansk&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=busselton&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=santa maria&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=provideniya&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tual&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=atuona&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=busselton&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=samusu&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=georgetown&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ausa&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=souillac&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=chokurdakh&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=adrar&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cape town&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=albany&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mahebourg&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=riachao das neves&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=provideniya&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=vaini&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=flinders&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=armacao dos buzios&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tsihombe&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=waw&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mataura&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bargal&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hamilton&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=sakakah&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bluff&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hambantota&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=illoqqortoormiut&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hami&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bargal&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kapaa&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=albany&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=veshenskaya&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ponta do sol&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=taolanaro&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=saleaula&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cape town&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=busselton&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bluff&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=grand gaube&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bethel&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=yumen&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=new norfolk&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=saskylakh&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mahebourg&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=provideniya&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tabou&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=punta arenas&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=thompson&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=faanui&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=fortuna&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=umzimvubu&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bluff&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=sicuani&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=busselton&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ponta do sol&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=busselton&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=malaya purga&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=morro bay&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=provideniya&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=fairbanks&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=saldanha&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=iqaluit&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=myitkyina&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=caravelas&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=acandi&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tumannyy&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hobart&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=brighton&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=abbiategrasso&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=balykshi&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mataura&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hobbs&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=pimentel&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=albany&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=garowe&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=attawapiskat&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=sao joao da barra&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ostrovnoy&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=san patricio&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mataura&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=port elizabeth&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=dingle&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kapaa&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=illoqqortoormiut&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ballina&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mataura&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cidreira&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=terrell&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=clyde river&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=eureka&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=buon me thuot&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=nemuro&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=punta arenas&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=san patricio&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=yellowknife&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hovd&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bluff&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=umm lajj&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ridgecrest&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kazalinsk&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kapaa&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=nikolskoye&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=coroico&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=pilao arcado&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=butaritari&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hermanus&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=manali&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=vaini&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=barcelona&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cervo&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=labuhan&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=boysun&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=togur&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=illoqqortoormiut&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=talnakh&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mataura&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hermanus&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ruwi&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=dunedin&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bethel&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bluff&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=butaritari&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=pisco&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=pevek&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=lincoln&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kapaa&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=patterson&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=sitka&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kapaa&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=aasiaat&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=carnarvon&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hattiesburg&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kavieng&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=sterlibashevo&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mongoumba&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=barentsburg&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hermanus&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=faanui&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=albany&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kuryk&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ilam&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kaitangata&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=talara&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=olafsvik&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=clearwater&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=lynn haven&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=taolanaro&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=port alfred&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=yudong&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=attawapiskat&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mar del plata&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=intipuca&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=darhan&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bardiyah&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=murgab&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cidreira&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=barentsburg&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rawannawi&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=avarua&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=pizhanka&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=malakal&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=los llanos de aridane&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=carnarvon&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=punta arenas&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=geraldton&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=pilar&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=yerbogachen&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kapaa&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tasiilaq&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hermanus&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cape town&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ostrovnoy&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mataura&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=busselton&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=oshakati&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=osa&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=krasnyy yar&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=faanui&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=palana&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bethel&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=envira&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=coahuayana&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cape town&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=gayny&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bredasdorp&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=constitucion&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=wattegama&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bluff&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=warqla&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=new norfolk&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cidreira&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=vostok&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ossora&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=husavik&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=yatou&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bluff&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=camapua&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=suifenhe&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=sakakah&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=castro&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=busselton&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=avarua&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tumannyy&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bredasdorp&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=grindavik&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=yellowknife&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ryotsu&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tubruq&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=am timan&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=nadym&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kavaratti&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cape town&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=salym&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bairiki&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=dusetos&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=pareora&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cidreira&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=leninskoye&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=saleaula&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kapaa&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=barrow&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=saint-philippe&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=san ramon&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kamaishi&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=albany&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=georgetown&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=berlevag&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ponta do sol&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=lianzhou&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=phrai bung&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=leeton&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mar del plata&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=punta arenas&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=qaanaaq&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mankono&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mataura&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hilo&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=punta arenas&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hithadhoo&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=galesong&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kavaratti&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hilo&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=aswan&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=dali&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kununurra&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=sinnamary&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tiksi&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=thompson&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=south venice&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=aklavik&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bredasdorp&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=muros&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=matara&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=arraial do cabo&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=alofi&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bluff&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=vestmannaeyjar&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cheuskiny&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=lavrentiya&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=lompoc&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=biak&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=iglesias&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=barentsburg&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cape town&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=albany&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=atuona&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ternate&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bethel&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=taolanaro&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=thaba-tseka&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=oktyabrskiy&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=sisimiut&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=aleksandrovskoye&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=fairbanks&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=souillac&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ratnagiri&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=leninsk&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bluff&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=louisbourg&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=naze&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=saskylakh&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=ushuaia&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cape town&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=thompson&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tuktoyaktuk&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=constitucion&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tacuarembo&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tuktoyaktuk&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tuatapere&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=nikolskoye&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=alice springs&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cayenne&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=yirol&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=wilmington island&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=cayenne&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=castro&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=butaritari&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bengkulu&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=jamestown&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hualmay&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=hobart&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kamaishi&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tuktoyaktuk&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kapaa&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=dzhebariki-khaya&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=mount gambier&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=arcachon&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=narsaq&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=provideniya&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=perigueux&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=castro&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=avarua&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=vaini&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=grand river south east&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=tiksi&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=punta arenas&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=naze&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=oktyabrskoye&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=attawapiskat&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=bethel&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kapaa&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=rikitea&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=albany&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=lebu&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=kelvington&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=puerto ayora&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=janesville&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=puerto ayora&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=dunedin&units=imperial
    http://api.openweathermap.org/data/2.5/weather?&APPID=1e30368c74b7ade947ced938f5b5a8c4&q=punta arenas&units=imperial
    


```python
lat_data=[data.get("coord").get("lat") for data in weather_data]
temp_data = [data.get("main").get("temp") for data in weather_data]
clouds_data = [data.get("clouds").get("all") for data in weather_data]
humidity_data = [data.get("main").get("humidity") for data in weather_data]
maxtemp_data = [data.get("main").get("temp_max") for data in weather_data]
windspeed_data = [data.get("wind").get("speed") for data in weather_data]
city_datanames = [data.get("name") for data in weather_data]
```


```python
weather_data={"City Name": city_datanames,
            "Max temp": maxtemp_data,
              "lat": lat_data,
              "cloudiness": clouds_data,
             "humidity": humidity_data,
             "wind speed": windspeed_data}
weather_data_df = pd.DataFrame(weather_data)
weather_data_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City Name</th>
      <th>Max temp</th>
      <th>cloudiness</th>
      <th>humidity</th>
      <th>lat</th>
      <th>wind speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Port Alfred</td>
      <td>60.32</td>
      <td>0</td>
      <td>95</td>
      <td>-33.59</td>
      <td>5.64</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Port Elizabeth</td>
      <td>50.00</td>
      <td>90</td>
      <td>93</td>
      <td>39.31</td>
      <td>9.44</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kieta</td>
      <td>83.18</td>
      <td>8</td>
      <td>98</td>
      <td>-6.22</td>
      <td>2.39</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Airai</td>
      <td>73.41</td>
      <td>92</td>
      <td>91</td>
      <td>-8.93</td>
      <td>1.72</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Hurricane</td>
      <td>48.20</td>
      <td>1</td>
      <td>19</td>
      <td>37.18</td>
      <td>2.17</td>
    </tr>
  </tbody>
</table>
</div>



# Latitude v Temperature Plot


```python
sns.lmplot(x="lat",
            y="Max temp",
            data = weather_data_df,
            fit_reg=False,
            palette = "viridis",
            hue = "Max temp",
            legend = False)
        
           #scatter_kws={"alpha":.8,
                      # "linewidth":1,
                       # ""color": "purple",
                       #"edgecolor":"purple"})

plt.title("City Latitude v Max Temperature (2/23/2018", size = 15)
plt.ylabel("Temperature in Farenheit")
plt.xlabel("Latitude")
plt.grid(True)
plt.savefig("LatitudevTemp.png")
plt.xlim(-90,90)
plt.ylim(-50,100)
plt.figure(figsize=(24,4))

```




    <matplotlib.figure.Figure at 0x1659e622208>




![png](output_11_1.png)



    <matplotlib.figure.Figure at 0x1659e622208>



```python
sns.lmplot(x="lat",
          y="humidity",
          data = weather_data_df,
          fit_reg=False,
           palette = "cubehelix",
           hue = "humidity",
           legend = False,
           scatter_kws={"alpha":.8,
                       "linewidth":1})

plt.title("City Latitude v Humidity (2/23/2018)", size = 15)
plt.ylabel("% Humidity")
plt.xlabel("Latitude")
plt.grid(True)
plt.savefig("LatitudevHumidity.png")

plt.xlim(-90,90)
plt.ylim(0,100)
```




    (0, 100)




![png](output_12_1.png)



```python
sns.lmplot(x="lat",
          y="cloudiness",
          data = weather_data_df,
          fit_reg=False,
           legend = False,
           hue = "cloudiness",
           palette = "husl",
           scatter_kws={"alpha":.8,
                       "linewidth":1})

plt.title("City Latitude v Cloudiness (2/23/2018)", size = 15)
plt.ylabel("% Cloudiness", size = 10)
plt.xlabel("Latitude")
plt.grid(True)
plt.savefig("LatitudevClouds.png")
plt.xlim(-90,90)
plt.ylim(0,100)
```




    (0, 100)




![png](output_13_1.png)



```python
sns.lmplot(x="lat",
          y="wind speed",
          data = weather_data_df,
          fit_reg=False,
           hue = "wind speed",
           legend = False,
           scatter_kws={"alpha":.8,
                       "linewidth":1,
                       "color": "purple"})

plt.title("City Latitude v Wind Speed (2/23/2018)", size = 15)
plt.ylabel("Wind Speed")
plt.xlabel("Latitude")
plt.grid(True)
plt.savefig("Latitudevwind.png")
plt.xlim(-90,90)
plt.ylim(0,35)
```




    (0, 35)




![png](output_14_1.png)



```python
cleanWeatherdata = zip(city_datanames, maxtemp_data, lat_data, humidity_data, clouds_data, windspeed_data)
```


```python
weatherdataCSV = os.path.join("06WeatherCSV_Chu.csv")
```


```python
with open(weatherdataCSV, 'w', newline="") as csvFile:
    csvWriter = csv.writer(csvFile, delimiter=",")
    csvWriter.writerow(["City Name", "Max Temperature", "Latitude", "% Cloudiness", "% Humidity", "Wind Speed"])
    csvWriter.writerows(cleanWeatherdata)
```
