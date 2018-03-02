
# **WeatherPy**

### **Importing Dependancies**


```python
import gzip
import csv
import json
import pandas as pd
import random
import math
import numpy as np
from random import uniform
import matplotlib.pyplot as plt

import matplotlib

# Set style for plots
plt.style.use("seaborn")
```


```python
import requests as req
from citipy import citipy
```


```python
lats = np.random.uniform(low=-90.000, high=90.000, size=500)
longs = np.random.uniform(low=-180.000, high=180.000, size=500)
cities=[]
```


```python
for lat, long in zip(lats, longs):
    #print(lat,lang)
    cities.append(citipy.nearest_city(lat, long).city_name)

```


```python
api_key = "c7f9f57b4779391ea1f5ae067591c971"
url = "http://api.openweathermap.org/data/2.5/weather?"
units = "metric"
query_url = url + "appid=" + api_key + "&units=" + units + "&q="

#city = "London"
weather_data=[]
```

### **Generating URL**


```python

for city in cities:
    try:
        #print("*",city,"*")
        #print(url + "appid=" + api_key + "&units=" + units + "&q=" + city)
        weather_data.append(req.get(query_url + city).json())
    except:
        print('error')

#for data in weather_data:
    #print(data.get('main').get('temp_max'))
#weather_data[2]
```

### **Setting variables**


```python

temperature = [x for x in [data.get("main",{}).get("temp") for data in weather_data] if x is not None]
pressure = [x for x in [data.get("main",{}).get("pressure") for data in weather_data] if x is not None]
humidity = [x for x in [data.get("main",{}).get("humidity") for data in weather_data] if x is not None]
cloudiness=  [x for x in [data.get("clouds",{}).get("all") for data in weather_data] if x is not None]
wind_speed = [x for x in [data.get("wind",{}).get("speed") for data in weather_data] if x is not None]
latitude = [x for x in [data.get("coord",{}).get("lat") for data in weather_data] if x is not None]
Longitude = [x for x in [data.get("coord",{}).get("lon") for data in weather_data] if x is not None]
City_1 = [x for x in [data.get("name") for data in weather_data] if x is not None]
country = [x for x in [data.get("sys",{}).get("country") for data in weather_data] if x is not None]
#for temp,pre in zip(temperature,pressure):
 #   print(temp,pre)
#temperature = [x for x in temperature if x is not None]
#print(temperature)
```


```python
citi_df = pd.DataFrame({"City":City_1,"Country":country,"lat":latitude,"long":Longitude,"Temperature":temperature,
                       "Pressure":pressure,"Humidity":humidity,"Cloudiness":cloudiness,
                        "Wind Speed":wind_speed
                       })
citi_df.set_index('City')
citi_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Cloudiness</th>
      <th>Country</th>
      <th>Humidity</th>
      <th>Pressure</th>
      <th>Temperature</th>
      <th>Wind Speed</th>
      <th>lat</th>
      <th>long</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Saint-Philippe</td>
      <td>75</td>
      <td>CA</td>
      <td>86</td>
      <td>1012.00</td>
      <td>-1.50</td>
      <td>8.70</td>
      <td>45.36</td>
      <td>-73.48</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Butaritari</td>
      <td>56</td>
      <td>KI</td>
      <td>100</td>
      <td>1020.54</td>
      <td>28.18</td>
      <td>3.43</td>
      <td>3.07</td>
      <td>172.79</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mataura</td>
      <td>68</td>
      <td>NZ</td>
      <td>75</td>
      <td>1005.79</td>
      <td>21.68</td>
      <td>4.23</td>
      <td>-46.19</td>
      <td>168.86</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bathsheba</td>
      <td>40</td>
      <td>BB</td>
      <td>100</td>
      <td>1014.00</td>
      <td>22.00</td>
      <td>4.60</td>
      <td>13.22</td>
      <td>-59.52</td>
    </tr>
    <tr>
      <th>4</th>
      <td>East London</td>
      <td>40</td>
      <td>ZA</td>
      <td>94</td>
      <td>1015.00</td>
      <td>20.00</td>
      <td>3.10</td>
      <td>-33.02</td>
      <td>27.91</td>
    </tr>
  </tbody>
</table>
</div>



### ** Plot settings**


```python
def set_plot_prop(x_title,x_lim,y_title):
    plt.title(f"{y_title} vs {x_title}")
    plt.ylabel(y_title)
    plt.xlabel(x_title)
    plt.grid(True)
    plt.xlim(x_lim)
```

### **Temperature vs Latitude**


```python
citi_df.plot(kind="scatter",x="lat",y="Temperature",grid=True,color="blue")
set_plot_prop("Latitude",[-90,90],"Temperature (Celsius)")
plt.axvline(0, color='black',alpha=0.5)
plt.savefig("Temperature vs Latitude")
plt.show()
```


![png](output_15_0.png)


### **Temperature vs Humidity**


```python
citi_df.plot(kind="scatter",x="lat",y="Humidity",grid=True,color="blue")
set_plot_prop("Latitude",[-90,90],"Humidity")
plt.axvline(0, color='black',alpha=0.5)
plt.savefig("Humidity vs Latitude")
plt.show()
```


![png](output_17_0.png)


### **Cloudiness (%) vs. Latitude**


```python
citi_df.plot(kind="scatter",x="lat",y="Cloudiness",grid=True,color="blue")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x182440bb898>




```python
set_plot_prop("Latitude",[-90,90],"Cloudiness %")
plt.axvline(0, color='black',alpha=0.5)
plt.savefig("Cloudiness % vs Latitude")
plt.show()
```


![png](output_20_0.png)


### **Wind Speed(MPH) vs Latitude**


```python
citi_df.plot(kind="scatter",x="lat",y="Wind Speed",grid=True,color="blue")
set_plot_prop("Latitude",[-90,90],"Wind Speed(MPH) ")
plt.axvline(0, color='black',alpha=0.5)
plt.savefig("Wind Speed(MPH) vs Latitude")
plt.show()
```


![png](output_22_0.png)

