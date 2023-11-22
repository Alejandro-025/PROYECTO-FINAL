import folium

# Crear el mapa centrado en las coordenadas del barrio
barrio_Ciudad_Verde = folium.Map(location=[4.601528, -74.214722], zoom_start=13)

# Agregar marcadores para cada panadería en el barrio
Panaderias = [
    {"nombre": "Panaderia del Carajo Express", "latitud": 4.60280, "longitud": -74.22060},
    {"nombre": "Panaderia Isvy de Moreno", "latitud": 4.61142, "longitud": -74.22547},
    {"nombre": "Panaderia Ponquesillo", "latitud": 4.61041, "longitud": -74.22498},
    {"nombre": "Panaderia Reina Mariana", "latitud": 4.61020, "longitud": -74.21697},
    {"nombre": "Panaderia Austrias", "latitud": 4.60576, "longitud": -74.22268},
    {"nombre": "Panaderia Salemh", "latitud": 4.60561, "longitud": -74.22288},
    {"nombre": "Panaderia monserrat", "latitud": 4.60838, "longitud": -74.21456},
    {"nombre": "Panaderia El Sol", "latitud": 4.60746, "longitud": -74.21347},
    {"nombre": "Panaderia Aroma de Pan", "latitud": 4.60714, "longitud": -74.21357},
    {"nombre": "Panaderia Alamo", "latitud": 4.60454, "longitud": -74.21269},
    {"nombre": "Panaderia Dulce Corazon", "latitud": 4.60689, "longitud": -74.21815},
    {"nombre": "Panaderia El Buñuelo Feliz y Sus Amigos", "latitud": 4.60461, "longitud": -74.21690},
    {"nombre": "Panaderia Ricuras y Detalles", "latitud": 4.60470, "longitud": -74.21537},
    {"nombre": "Panaderia Nueva Zelanda", "latitud": 4.60231, "longitud": -74.21702},
    {"nombre": "Panaderia Valentinas Cake", "latitud": 4.60106, "longitud": -74.21966},
    {"nombre": "Panaderia Heidy", "latitud": 4.59801, "longitud": -74.21654},
    
]

for Panaderia in Panaderias:
    folium.Marker(
        location=[Panaderia["latitud"], Panaderia["longitud"]],
        popup=Panaderia["nombre"],
        icon=folium.Icon(color="red", icon="bread-slice")
    ).add_to(barrio_Ciudad_Verde)

# Mostrar el mapa del barrio con las panaderías
barrio_Ciudad_Verde