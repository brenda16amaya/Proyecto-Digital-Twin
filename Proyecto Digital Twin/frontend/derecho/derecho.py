import dash
import dash_bootstrap_components as dbc
from dash import html

# Lista de equipos con sus descripciones y rutas de imagen
equipos = [
    {
        'nombre': 'Arduino Uno',
        'descripcion': 'Plataforma de prototipado electrónico con microcontrolador ATmega328P.',
        'imagen': 'https://cdnx.jumpseller.com/mactornica/image/8979530/ARDUINO_UNO_R3.png?1654715293'
    },
    {
        'nombre': 'Sensor Ultrasónico de distancia',
        'descripcion': 'Sensor ultrasónico para medir la distancia entre objetos.',
        'imagen': 'https://www.electronicaplugandplay.com/components/com_mijoshop/opencart/image/cache/catalog/sensores_y_transductores/distancia/Sensor_Ultrasonido_HR_SR04-500x500.png'
    },
    {
        'nombre': 'Protoboard',
        'descripcion': 'Tablero de pruebas para prototipado electrónico sin soldadura.',
        'imagen': 'https://electronicamade.com/wp-content/uploads/2020/04/Protoboard.jpg'
    },
    {
        'nombre': 'Cables',
        'descripcion': 'Cables y jumpers para conectar componentes electrónicos.',
        'imagen': 'https://electronilab.co/wp-content/uploads/2013/08/cables-protoboard-electronilabco-03.jpg'
    }
]

# Crear una lista de cartas con la información de cada equipo
derecho = []
for equipo in equipos:
    carta = dbc.Card(
        [
            dbc.CardImg(src=equipo['imagen'], top=True),
            dbc.CardBody(
                [
                    html.H4(equipo['nombre'], className="card-title"),
                    html.P(equipo['descripcion'], className="card-text"),
                ]
            ),
        ],
        style={"max-width": "300px", "margin": "10px"},  # Ajustar el ancho máximo y el margen,
    )
    derecho.append(carta)



