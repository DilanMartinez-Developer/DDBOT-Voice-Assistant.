from utilidades.hablar import hablar
import time

def hacer_broma(parametro):
    hablar("Preparando sistema de autodestrucción en 3, 2, 1...")
    time.sleep(2)
    hablar(f"Es broma, solo querías que haga algo relacionado con {parametro}")

# El diccionario que herramientas.py va a chupar
TOOLS = {
    "ejecutar_broma": hacer_broma
}

# Las reglas que iaGroq.py le va a mandar al LLM
PROMPT_REGLAS = """
- ejecutar_broma: usa esta acción solo cuando el usuario pida un chiste, una broma, o algo gracioso.
"""