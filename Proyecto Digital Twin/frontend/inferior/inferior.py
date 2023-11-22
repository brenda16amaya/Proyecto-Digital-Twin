import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

# Define los botones para inyección y estable
boton_inyeccion = dbc.Button('Se necesita inyección', color='danger', id='boton-inyeccion', disabled=True)
boton_estable = dbc.Button('Estable', color='success', id='boton-estable', disabled=True)


# Define las variables Distancia_Inicial y Distancia_Final como componentes de entrada
Distancia_Inicial = dcc.Input(id='input-distancia-inicial', type='number', placeholder='Introduce la distancia inicial', value='')
Distancia_Final = dcc.Input(id='input-distancia-final', type='number', placeholder='Introduce la distancia final', value='')
# Estructura del diseño con los componentes creados
inferior =  dbc.Container([
    dbc.Row([
        dbc.Col(["Distancia Inicial",Distancia_Inicial], md=4, style={'background-color': 'white'}),
        dbc.Col(["Distancia Final",Distancia_Final], md=4, style={'background-color': 'white'}),
    ]),
    dbc.Row([
        dbc.Col(boton_inyeccion, md=6),
        dbc.Col(boton_estable, md=6),
    ])
])
