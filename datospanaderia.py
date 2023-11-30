import pandas as pd

# Crear un DataFrame de ejemplo
panaderias_ciudad_verde = { 
 
    "NOMBRE":["Panaderia del Carajo Express", "Panaderia Isvy de Moreno", "Panaderia Ponquesillo", "Panaderia Reina Mariana", "Panaderia Austrias", "Panaderia Salemh", "Panaderia monserrat", "Panaderia El Sol", "Panaderia Aroma de Pan", "Panaderia Alamo", "Panaderia Dulce Corazon", "Panaderia El Buñuelo Feliz y Sus Amigos", "Panaderia Ricuras y Detalles", "Panaderia Nueva Zelanda", "Panaderia Valentina Cake", "Panaderia Heidy"],
    "LATITUD":[4.60280, 4.61142, 4.61041, 4.61020, 4.60576, 4.60561, 4.60838, 4.60746, 4.60714, 4.60454, 4.60689, 4.60461, 4.60470, 4.60231, 4.60106, 4.59801],
    "LONGITUD":[-74.22060, -74.22547, -74.22498, -74.21697, -74.22268, -74.22288, -74.21456, -74.21347, -74.21357, -74.21269, -74.21815, 74.21690, -74.21537, -74.21702, -74.21966, -74.21654],
    "TELEFONO":["3172647476", "3108723011", "3108553661", "Sin contacto", "3164843118", "3219926114", "Sin contacto", "Sin contacto", "Sin contacto", "Sin contacto", "3504903641", "3187061130", "3138883399", "3204016239", "3202825278", "3228468614"],
    "HORARIO":["10:00AM-8:00PM", "9:00AM-9:00PM", "9:00AM-10:00PM", "7:00AM-9:00PM", "7:00AM-10:00PM", "7:00AM-10:00PM", "7:00AM-9:00PM", "7:00AM-9:00PM", "7:00AM-9:00PM", "7:00AM-9:00PM", "8:00AM-10:00PM", "7:00AM-10:00PM", "24 HORAS", "7:00AM-10:00PM", "7:00AM-9:00PM", "6:00AM-10:00PM"],
    "PRODUCTOS DESTACADOS":["Pan de masa madre, Croissants, Tortas", "Pan integral, Empanadas, Galletas", "Galleta de leche, Buñuelo, Pan integral", "Roscon, Almohabana", "Empanadas", "Postre de limon, Postre de maracuya", "Mariposa, Flauta", "Pan de la abuela", "Pan bagette, Pan de leche", "Buñuelo con natilla, Arroz de leche", "Galleta de avena, Torta de mazorca, Mariposa", "Pan italiano", "Pan frances, Pan ingles", "Pastel de yuca, Papa", "Dedos de queso", "Buñuelos y Pan de ajo"],
    "PRECIOS PRODUCTOS DESTACADOS":["$3.000, $4.000, $5.000", "$5.500, $2.500, $1.500", "$2.000, $2.000, $4.000", "$2.200, $3.000", "$2.800", "$5.000, $5.000", "$3.000, $2.700", "$5.200", "$1.800, $800", "$4.000, $3.500", "$4.600, $3.000", "$1.700, $3.000, $3.000", "$6.000", "$5.000, $4.500", "$2.900, $3.000", "$2.500", ],
    "PROMOCIONES":["Descuento del 10% los martes", "2x1 en empanadas los jueves", "2x1 en buñuelos los domingos", "La panaderia no cuenta con promociones", "10% de descuento los miercoles", "Postre de mora a mitad de precio los viernes", "Compras mayores a $10.000 lleve tres panes de leche", "Galletas a $1.000 los martes", "12 panes de leche por $8.000", "La panaderia no cuenta con promociones", "2x1 en arroz de leche los lunes", "La panaderia no cuenta con promociones", "2x1 en empanadas los jueves", "Compras mayores a $10.000 lleve un cafe gratis", "La panaderia no cuenta con promociones", "La panaderia no cuenta con promociones"]
    }    
df = pd.DataFrame(panaderias_ciudad_verde)

# Convertir el DataFrame en una tabla HTML
tabla_html = df.to_html()

# Imprimir la tabla HTML
print(tabla_html)
