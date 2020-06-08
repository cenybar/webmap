import folium
import pandas as pd

data = pd.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
nam = list(data['NAME'])

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

# Para iterar en dos listas se utiliza la función ZIP
for lt, ln, nm in zip(lat, lon, nam):
    fg.add_child(folium.Marker(location=[lt,ln], popup=nm, icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
