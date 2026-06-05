import os
import datetime
from PIL import ImageGrab
import ollama
from utilidades.hablar import hablar

RUTA_CAPTURAS = os.path.join(os.getcwd(), "capturas")
if not os.path.exists(RUTA_CAPTURAS):
    os.makedirs(RUTA_CAPTURAS)

def analizar_pantalla(parametro=""):
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"captura_{timestamp}.png"
        ruta_archivo_imagen = os.path.join(RUTA_CAPTURAS, nombre_archivo)

        print(f"Tomando captura... Guardando en: {ruta_archivo_imagen}")
        screenshot = ImageGrab.grab()
        screenshot.save(ruta_archivo_imagen, "PNG")
        
        hablar("Dejame ver...")

        pregunta_ia = "Analiza esta captura de pantalla de mi escritorio de Windows de forma muy breve. "
        if parametro and parametro.lower() != "auto" and parametro.lower() != "vacio":
            pregunta_ia += f"El usuario quiere saber específicamente: {parametro}"

        #modelo llava para imagenes
        respuesta = ollama.chat(
            model='llava',
            messages=[{
                'role': 'user',
                'content': pregunta_ia,
                'images': [ruta_archivo_imagen] # Ollama lee la ruta directo, sin base64
            }]
        )

        resultado_texto = respuesta['message']['content'].strip()
        print(f"DDBOT vio (Local): {resultado_texto}")
        hablar(resultado_texto)

    except Exception as e:
        print(f"Error en analizar_pantalla local: {e}")
        hablar("Hubo un problema al intentar analizar tu pantalla.")

TOOLS = {"analizar_pantalla": analizar_pantalla}
PROMPT_REGLAS = "..." # Tus reglas actuales