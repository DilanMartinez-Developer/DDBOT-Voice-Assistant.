
import subprocess
import webbrowser
from utilidades.memoriaDinamica import * 
from utilidades import Comandos
from utilidades.hablar import hablar
from datetime import datetime
import time

def procesar(comando):                  
    comandoSplit = comando.split()
    #nueva rutina
    if any(p in comando for p in Comandos.NEWRUTINA_WORDS):
        for p in Comandos.NEWRUTINA_WORDS:
            comando = comando.replace(p, "")
            consulta = comando.strip()
            
        ne, cm = consulta.split("luego", 1)

        ne = ne.strip()
        # separar comandos por coma
        lista_comandos = [c.strip() for c in cm.split("y ")]
        #guarda
        guardar_rutina(ne, lista_comandos)

    if any(p in comando for p in ["hora","qué hora"]):
        # Obtener fecha y hora actual local
        ahora = datetime.now()
        # Imprimir la hora en formato HH:MM:SS
        hablar("la hora actual es "+ ahora.strftime("%H:%M"))
    #logica para abrir aplicacion y carpetas
    if any(p in comando for p in Comandos.OPEN_WORDS):
        partes = comando.split(" ")
        #logica para saber que carpeta abrir
        if len(partes) < 2:
            hablar("No me dijiste que abrir")
            return
        nombre = partes[-1].lower()
        ruta = "C:\\Users\\galos\\" 

        if any(p in comando for p in Comandos.CARPETAS_WORDS):
            if nombre in Comandos.CARPETAS_WORDS:
                ruta = "C:\\Users\\galos\\" + Comandos.CARPETAS_WORDS[nombre]
                hablar("abriendo la carpeta " + nombre)
                subprocess.run(["cmd", "/c", "start", "",ruta])
                Comandos.CONTEXTO_TH["ultima_carpeta_ruta"] = ruta
            else:
                hablar("no conozco esa carpeta")
        else:
            # recorrer comandos
            for key in Comandos.OPEN_ROOTS:
                if key in comando:
                    hablar("abriendo "+key)
                    time.sleep(1)
                    Comandos.OPEN_ROOTS[key]()
                    #guardamos el contexto
                    Comandos.CONTEXTO_TH["ultima_app"] = key
                    memoria = cargar_memoria()
                    memoria["historial_Apps"].append(key)
                    guardar_memoria(memoria)
    #cuando se activa la plabra clave de busqueda, pasa a analizar que estas por buscar
    if any(p in comando for p in Comandos.BUSCAR_WORDS):
        for p in Comandos.BUSCAR_WORDS:
            comando = comando.replace(p, "")
            consulta = comando.strip()

        if any(p in comando for p in Comandos.GOOGLE_KEYS):
            Googlear(comando)
        if any(p in comando for p in Comandos.YOUTUBE_KEYS):
            YouTube(comando)
    guardar_memoria(cargar_memoria())


def YouTube(comando):
    for p in Comandos.YOUTUBE_KEYS:
        comando = comando.replace(p, "")
        consulta = comando.strip()

    if consulta != "" and consulta != "en youtube":
        hablar("buscando "+consulta+" en youtube")
        webbrowser.open("https://www.youtube.com/results?search_query=" + consulta)
        #guardar contexto
        Comandos.CONTEXTO_TH["ultima_busqueda_youtube"] = consulta  
        memoria = cargar_memoria()
        memoria["historial_busquedas_youtube"].append(consulta)
        guardar_memoria(memoria)
    else:
        hablar("No logre entender que me pediste que buscara en youtube")

def Googlear(comando):
    # limpiar palabra clave
    
    for p in Comandos.GOOGLE_KEYS:
        comando = comando.replace(p, "")
        consulta = comando.strip()
        
    if consulta != "" and consulta != "en internet":
        hablar("buscando "+consulta+" en internet")
        webbrowser.open("https://www.google.com/search?q=" + consulta)
        #guradar contexto
        Comandos.CONTEXTO_TH["ultima_busqueda_google"] = consulta
        memoria = cargar_memoria()
        memoria["historial_busquedas_google"].append(consulta)
        guardar_memoria(memoria)
    else:
        hablar("No logre entender que me pediste que buscara")    

def ejecutar_rutina(nombre):
    memoria = cargar_memoria()
    
    if nombre in memoria["rutinas"]:
        for comando in memoria["rutinas"][nombre]:
            procesar(comando)