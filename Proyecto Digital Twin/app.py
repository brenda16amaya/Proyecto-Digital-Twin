import dash  # Importar la biblioteca Dash para crear aplicaciones web interactivas
from dash import html, dcc  # Importa los componentes necesarios de la libreria de Dash
import dash_bootstrap_components as dbc  # Importar las librerías necesarias de Dash Bootstrap Components
from dash.dependencies import Input, Output  # Importar las librerías necesarias de Dash dependencies para emplear los elementos de Input y Output
import plotly.graph_objs as go

from frontend.derecho.derecho import *  # Importar la variable "derecho" de la carpeta del frontend
from frontend.izquierdo.izquierdo import *    # Importar la variable "izquierdo" de la carpeta del frontend
from frontend.inferior.inferior import inferior    # Importar la variable "inferior" de la carpeta del frontend

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP]) # Crear una instancia de la aplicación Dash
server = app.server
app.layout = layout

# Crear el diseño de la página web
layout = dbc.Container([  # Se crea un contenedor de Dash que señala los elementos que contendrán la página.
    dbc.Row([  # Crear una fila para el encabezado
        dbc.Col(html.H1('Monitoreo de Asentamiento Tuneladora',style = {'background-color': '#188EBE', 'color': 'white','text-align': 'center'}), md = 12),  # Crear una columna que contiene un título de nivel 1 y su estilo
    ]),
    dbc.Row([  # Crear una fila para los contenidos principales
        dbc.Col(izquierdo, md=5, style = {'background-color' : '#E9F3FF'}),  # Crear una columna que contiene el componente "izquierdo", que se importa de otra carpeta donde ya esta definida y el estilo de esta
        dbc.Col(derecho, md=7,className="d-flex flex-wrap justify-content-center", style = {'background-color' : '#C9E2FF'}),  # Crear una columna que contiene el componente "derecho", que se importa de otra carpeta donde ya esta definida y el estilo de esta
    ]),
    html.H2("Gráfica Asentamiento Tuneladora", style={'text-align': 'center'}),
    html.Hr(),
    html.H4(id='distancia-actual', style={'text-align': 'center'}),
    dcc.Graph(id='asentamiento'),
    dcc.Interval(
        id='interval-component',
        interval=1 ,  # en milisegundos, actualiza cada 1 segundo
        n_intervals=0
    ),
    html.Div(id='alerta-texto', style={'text-align': 'center', 'margin-top': '10px'})
])

#Base de datos
from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://cagomezj:1234@cluster0.lg8bsx8.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.sensores.sensor_1
result = 0

# Declarar data_dist fuera de la función para evitar el UnboundLocalError
data_dist = []


@app.callback(
    [Output('asentamiento', 'figure'),
     Output('distancia-actual', 'children'),
     Output('alerta-texto', 'children')],
    [Input('interval-component', 'n_intervals')]
)
def consultar(n):
    
    # Utilizar la variable global data_dist
    global data_dist , result , db
    result = db.find_one(sort=[('updated_at', -1)])
    distancia = int(result['distancia'])
    data_dist.append(distancia)
    
    # Crear el objeto de figura de Plotly
    fig = go.Figure(data=[go.Scatter(y=data_dist, mode='lines+markers')])
    
     # Agregar una línea horizontal en y=5
    fig.add_shape(
        type="line",
        x0=0,
        x1=len(data_dist),
        y0=10,
        y1=10,
        line=dict(color="red", width=2),
    )
    
    # Agregar un texto según la condición
    if distancia >= 10:
        alerta_texto = html.Span("ALERTA", style={'color': 'red', 'font-size': '24px'})
    else:
        alerta_texto = html.Span("VAMOS BIEN", style={'color': 'green', 'font-size': '24px'})
    
    
    # Formatear la distancia para mostrarla en el H1
    distancia_texto = f"El asentamiento fue: {distancia} cm"
    
    return fig, distancia_texto,alerta_texto


if __name__ == "__main__":
    app.run_server(debug=True)
