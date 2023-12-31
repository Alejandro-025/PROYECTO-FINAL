import folium

# Crear el mapa centrado en las coordenadas del barrio
barrio_Ciudad_Verde = folium.Map(location=[4.601528, -74.214722], zoom_start=13)

# Guardar el mapa en un archivo HTML
barrio_Ciudad_Verde.save('mapa.html')

# Agregar marcadores para cada panadería en el barrio
Panaderias = [
    {"nombre": "Panaderia del Carajo Express", "latitud": 4.60280, "longitud": -74.22060, "telefono": "3172647476", "horario": "10:00AM-8:00PM", "productos destacados": "Pan de masa madre, Croissants, Tortas", "precios productos destacados": "$3.000, $4.000, $5.000", "promociones": "Descuento del 10% los martes"},
    {"nombre": "Panaderia Isvy de Moreno", "latitud": 4.61142, "longitud": -74.22547, "telefono": "3108723011", "horario": "9:00AM-9:00PM", "productos destacados": "Pan integral, Empanadas, Galletas", "precios productos destacados": "$5.500, $2.500, $1.500", "promociones": "2x1 en empanadas los jueves"},
    {"nombre": "Panaderia Ponquesillo", "latitud": 4.61041, "longitud": -74.22498, "telefono": "3108553661", "horario": "9:00AM-10:00PM", "productos destacados": "Galleta de leche, Buñuelo, Pan integral", "precios productos destacados": "$2.000, $2.000, $4.000", "promociones": "2x1 en buñuelos los domingos"},
    {"nombre": "Panaderia Reina Mariana", "latitud": 4.61020, "longitud": -74.21697, "telefono": "Sin contacto", "horario": "7:00AM-9:00PM", "productos destacados": "Roscon, Almohabana", "precios productos destacados": "$2.200, $3.000", "promociones": "La panaderia no cuenta con promociones"},
    {"nombre": "Panaderia Austrias", "latitud": 4.60576, "longitud": -74.22268, "telefono": "3164843118", "horario": "7:00AM-10:00PM", "productos destacados": "Empanadas", "precios productos destacados": "$2.800", "promociones": "10% de descuento los miercoles"},
    {"nombre": "Panaderia Salemh", "latitud": 4.60561, "longitud": -74.22288, "telefono": "3219926114", "horario": "7:00AM-10:00PM", "productos destacados": "Postre de limon, Postre de maracuya", "precios productos destacados": "$5.000, $5.000", "promociones": "Postre de mora a mitad de precio los viernes"},
    {"nombre": "Panaderia monserrat", "latitud": 4.60838, "longitud": -74.21456, "telefono": "Sin contacto", "horario": "7:00AM-9:00PM", "productos destacados": "Mariposa, Flauta", "precios productos destacados": "$3.000, $2.700", "promociones": "Compras mayores a $10.000 lleve tres panes de leche"},
    {"nombre": "Panaderia El Sol", "latitud": 4.60746, "longitud": -74.21347, "telefono": "Sin contacto", "horario": "7:00AM-9:00PM", "productos destacados": "Pan de la abuela", "precios productos destacados": "$5.200", "promociones": "Galletas a $1.000 los martes"},
    {"nombre": "Panaderia Aroma de Pan", "latitud": 4.60714, "longitud": -74.21357, "telefono": "Sin contacto", "horario": "7:00AM-9:00PM", "productos destacados": "Pan bagette, Pan de leche", "precios productos destacados": "$1.800, $800", "promociones": "12 panes de leche por $8.000"},
    {"nombre": "Panaderia Alamo", "latitud": 4.60454, "longitud": -74.21269, "telefono": "Sin contacto", "horario": "7:00AM-9:00PM", "productos destacados": "Buñuelo con natilla, Arroz de leche", "precios productos destacados": "$4.000, $3.500", "promociones": "La panaderia no cuenta con promociones"},
    {"nombre": "Panaderia Dulce Corazon", "latitud": 4.60689, "longitud": -74.21815, "telefono": "3504903641", "horario": "8:00AM-10:00PM", "productos destacados": "Pan hawaiano, Pan de queso", "precios productos destacados": "$4.600, $3.000", "promociones": "2x1 en arroz de leche los lunes"},
    {"nombre": "Panaderia El Buñuelo Feliz y Sus Amigos", "latitud": 4.60461, "longitud": 74.21690, "telefono": "3187061130", "horario": "7:00AM-10:00PM", "productos destacados": "Galleta de avena, Torta de mazorca, Mariposa", "precios productos destacados": "$1.700, $3.000, $3.000", "promociones": "La panaderia no cuenta con promociones"},
    {"nombre": "Panaderia Ricuras y Detalles", "latitud": 4.60470, "longitud": -74.21537, "telefono": "3138883399", "horario": "7:00AM-10:00PM", "productos destacados": "Pan italiano", "precios productos destacados": "$6.000", "promociones": "2x1 en empanadas los jueves"}, 
    {"nombre": "Panaderia Nueva Zelanda", "latitud": 4.60231, "longitud": -74.21702, "telefono": "3204016239", "horario": "24 horas", "productos destacados": "Pan frances, Pan ingles", "precios productos destacados": "$5.000, $4.500", "promociones": "Compras mayores a $10.000 lleve un cafe gratis"},
    {"nombre": "Panaderia Valentina´s Cake", "latitud": 4.60106, "longitud": -74.21966, "telefono": "3202825278", "horario": "7:00AM-9:00PM", "productos destacados": "Pastel de yuca, Papa", "precios productos destacados": "$2.900, $3.000", "promociones": "La panaderia no cuenta con promociones"},
    {"nombre": "Panaderia Heidy", "latitud": 4.59801, "longitud": -74.21654, "telefono": "3228468614", "horario": "6:00AM-10:00PM", "productos destacados": "Dedos de queso", "precios productos destacados": "$2.500", "promociones": "La panaderia no cuenta con promociones"},
    
]

# Crear una tabla HTML para cada panadería y agregar botones
for Panaderia in Panaderias:
    tabla_html = f'''
    <h2>{Panaderia["nombre"]}</h2>
    <table>
        <tr>
            <th>Nombre</th>
            <th>Teléfono</th>
            <th>Horario de atención</th>
            <th>Productos Relevantes</th>
            <th>Precios de los productos relevantes</th>
            <th>Promociones</th>
        </tr>
        <tr>
            <td>{Panaderia["nombre"]}</td>
            <td>123456789</td>
            <td>8:00 AM - 6:00 PM</td>
            <td>Pan de masa madre, Croissants, Pasteles</td>
            <td>$2.50, $1.75, $3.00</td>
            <td>Descuento del 10% en pasteles</td>
        </tr>
    </table>
    <button onclick="mostrarTabla('tabla-{Panaderia["nombre"]}')">Mostrar Tabla</button>
    '''

    # Agregar el marcador con el botón y la tabla como contenido emergente
    marcador = folium.Marker(
        location=[Panaderia["latitud"], Panaderia["longitud"]],
        popup=folium.Popup(tabla_html, max_width=300),
        icon=folium.Icon(color="red", icon="bread-slice")
    ).add_to(barrio_Ciudad_Verde)

    # Agregar el botón al contenido emergente del marcador
    marcador.add_child(folium.Button('Mostrar Tabla'))

# Guardar el mapa en HTML
barrio_Ciudad_Verde.save("mapa.html")
