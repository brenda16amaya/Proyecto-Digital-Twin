import dash_bootstrap_components as dbc  # Importar las librerías necesarias de Dash Bootstrap Components
from  dash import html # Importa los componentes necesarios de la libreria de Dash

izquierdo = dbc.Container([  # Se crea un contenedor de Dash que señala los elementos que contendrán la parte izquierda de la página.
    html.Div([  # Contenido de la página para monitorear el asentamiento del edificio
    html.H2("Monitoreo de Asentamiento por Excavación Profunda"),  # Título de nivel 2
    html.P("Bienvenido a nuestra herramienta de monitoreo de asentamiento de edificios. Aquí explicaremos cómo utilizar este sistema para detectar y actuar ante asentamientos provocados por excavaciones profundas."),  # Párrafo introductorio

    html.H3("Sensores y Funcionamiento"),  # Título de nivel 3
    html.P("Nuestra aplicación está conectada a un sensor que mide la distancia entre el edificio y el suelo. Esta distancia es crucial para identificar asentamientos. Si el asentamiento supera los 0.5 mm, se activará un botón de alerta indicando la necesidad de una inyección de concreto."),  # Explicación sobre sensores y activación

    html.H3("Propósito y Funcionamiento"),  # Título de nivel 3
    html.P("El propósito principal de esta herramienta es garantizar la estabilidad del edificio frente a excavaciones profundas. El sistema monitorea continuamente el asentamiento. Si es mayor a 0.5 mm, se emite una alerta para tomar medidas correctivas, de lo contrario, se muestra una señal de estabilidad."),  # Explicación sobre el propósito del monitoreo

    html.P("Esta aplicación emplea conceptos de Gemelos Digitales, tal como se ha descrito en la literatura especializada. Los Gemelos Digitales se utilizan para simular y predecir el comportamiento del edificio en función de los datos obtenidos del sensor."),  # Conexión con el concepto de Gemelos Digitales

    html.P("Explora la sección 'Asentamiento del Edificio' para obtener información detallada sobre los valores medidos y cómo influyen en la estabilidad del edificio."),  # Invitación a explorar más información
])
])

