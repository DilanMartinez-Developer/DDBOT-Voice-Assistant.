from UtilidadesConIA.iaGroq import pensar
from UtilidadesConIA.ejecutorIA import ejecutarIA

from utilidades.escuchar import escuchar
from utilidades.hablar import hablar
import utilidades.Comandos as texts
import time
import keyboard
import os
import json

historial_conversacion = []
MAX_MEMORIA = 12

CONTEXTO_IA = {
    "ultima_respuesta": "",
    "ultimo_comando": "",
    "ultima_accion": ""
}

def ActivacionPorTecla():
    global historial_conversacion
    texto = escuchar()

    print("texto:", texto)

    if texto in texts.TY_WORDS:
        hablar("pa eso estamos mano")
        return

    comando = texto.strip()

    if comando == "":
        hablar("no logre escucharte bien")
        return

    print("pensando...")

    if texto:
        print(f"Usuario: {texto}")

        # 1. Agregamos lo que dijo el usuario al historial
        historial_conversacion.append({"role": "user", "content": texto})

        # 2. Recortamos el historial si se hace muy largo (para ahorrar tokens)
        if len(historial_conversacion) > MAX_MEMORIA:
            # Nos quedamos solo con los últimos mensajes
            historial_conversacion = historial_conversacion[-MAX_MEMORIA:]

        # 3. Llamamos a Groq, pasándole TODA la lista
        respuestaIA = pensar(historial_conversacion)

        # 4. Agregamos la respuesta del bot al historial (para que recuerde lo que hizo)
        # Lo guardamos como texto JSON puro
        historial_conversacion.append({"role": "assistant", "content": json.dumps(respuestaIA)})

        # 5. Ejecutamos la acción como siempre
        ejecutarIA(respuestaIA)
    else:
        print("no logre escuchar nada")

def abortarMision():
    print("¡ABORTANDO!")
    os._exit(0)

keyboard.add_hotkey('ctrl+shift+f10', abortarMision)
keyboard.add_hotkey('F10',  ActivacionPorTecla)

print("Esperando tecla...")
keyboard.wait()
