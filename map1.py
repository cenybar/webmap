import folium
import pandas as pd

data = pd.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
nam = list(data['NAME'])
elev = list(data['ELEV'])

def color_produce(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'
    

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

# Para iterar en dos listas se utiliza la función ZIP
for lt, ln, nm, el in zip(lat, lon, nam, elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=nm + " altitude is " + str(el) + "m", fill_color=color_produce(el), 
    color='grey', fill = True, fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fg)
map.save("Map1.html")
