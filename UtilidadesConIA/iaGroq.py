import os
import json
from groq import Groq
from dotenv import load_dotenv
#cargo las variables .env
load_dotenv()

client = Groq(
    api_key= os.getenv("Groq_Api_KEY")
)

SYSTEM_PROMPT = """
Eres el cerebro de un asistente Windows.

Tu trabajo es interpretar lo que desea el usuario.

Solo puedes responder con JSON valido.
Nunca expliques.
Nunca agregues texto fuera del JSON.

Tipos posibles:

1 respuesta

{
"tipo":"respuesta",
"contenido":"..."
}

2 acciones

{
"tipo":"acciones",
"acciones":[
{
"accion":"...",
"parametros":"..."
}
]
}

Acciones permitidas:

- abrir_aplicacion
- buscar_youtube
- buscar_google
- abrir_carpeta

No inventes acciones.
Usa solamente las permitidas.

Interpreta la intención del usuario.

Ejemplos:

Usuario: abre steam

{
"tipo":"acciones",
"acciones":[
{
"accion":"abrir_aplicacion",
"parametros":"steam"
}
]
}

Usuario: busca hollow knight en youtube

{
"tipo":"acciones",
"acciones":[
{
"accion":"buscar_youtube",
"parametros":"hollow knight"
}
]
}

Usuario: abre google y busca clima en internet

{
"tipo":"acciones",
"acciones":[
{
"accion":"abrir_aplicacion",
"parametros":"google"
},
{
"accion":"buscar_google",
"parametros":"clima"
}
]
}

Usuario: que es una integral

{
"tipo":"respuesta",
"contenido":"explicacion breve"
}
"""

def pensar(texto):

    respuesta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"system",
                "content": SYSTEM_PROMPT
            },
            {
                "role":"user",
                "content": texto
            }
        ],
        temperature=0.2
    )

    contenido = respuesta.choices[0].message.content

    try:
        return json.loads(contenido)
    except:
        return {
            "tipo":"respuesta",
            "contenido":contenido
        }