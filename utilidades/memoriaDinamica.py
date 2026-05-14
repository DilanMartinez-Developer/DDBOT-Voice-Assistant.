import json
import os

MEMORIA_PATH = "memento.json"

def cargar_memoria():
    memoria_default = {
        "rutinas": {},
        "preferencias": {},
        "historial_busquedas_google": [],
        "historial_busquedas_youtube": [],
        "historial_Apps": [],
        "historial_Carpetas ": []
    }

    if not os.path.exists(MEMORIA_PATH):
        guardar_memoria(memoria_default)
        return memoria_default

    try:
        with open(MEMORIA_PATH, "r") as f:
            memoria = json.load(f)
    except:
        # archivo vacío o corrupto
        guardar_memoria(memoria_default)
        return memoria_default

    return memoria

def guardar_memoria(memoria):
    with open(MEMORIA_PATH, "w") as f:
        json.dump(memoria, f, indent=4)

def guardar_rutina(nombre, comandos):
    memoria = cargar_memoria()
    memoria["rutinas"][nombre] = comandos
    guardar_memoria(memoria)