import webbrowser
import subprocess
WAKE_WORDS = [
    "jarvis",
    "j",
    "javier",
    "bavier", 
    "asistente", 
    "didi's bot",
    "didi bot", 
    "didi",
    "didi's"
    "hey jarvis", 
    "hey siri",
    "siri",
    "pívot",
    "didi would"]

CARPETAS_WORDS = {
    "carpeta",
    "carpetas", 
    "carpet",
    "la carpeta", 
    "le carpeta", 
    "l carpeta",
    "abrir_carpeta"
}

TY_WORDS = [
    "Gracias",
    "gracias", 
    "grazias",
    "Grazias",
    "gracia",
    "Gracia"]

CLOSE_WORDS = [
    "apagar",
    "cerrar programa",
    "close program",
    "fin programa",
    "detener programa", 
    "pausar programa", 
    "detener ai", 
    "chau didi bot", 
    "nos vemos",
    "clóset program",
    "cerrar_aplicacion"]

CARPETAS_ROOTS = {
    "descargas": "Downloads",
    "documentos": "Documents",
    "escritorio": "Desktop",
    "imágenes": "Pictures",
    "musica": "Music",
    "videos": "Videos",
    "appdata": "AppData",
    "youtube": "YouTube AD",
    "utec": "utec AD",
    "trabajo": "Laburo AD"
        }

OPEN_WORDS = {
    "abrir", 
    "abrime", 
    "abre",
    "open",
    "ejecuta",
    "inicia",
    "run",
    "abrir_aplicacion"
}

#Rutas Para abrir cosas
OPEN_ROOTS = {
    "google": lambda: webbrowser.open("https://www.google.com"),
    "clima": lambda: subprocess.run(["cmd", "/c", "start", "","bingweather:"]),
    "visual": lambda: subprocess.run(["cmd", "/c", "start", "","Code.exe"]),
    "steam": lambda: subprocess.run(["cmd", "/c", "start", "","C:\\Program Files (x86)\\Steam\\steam.exe"]),    
}

BUSCAR_WORDS = {
    "buscar",
    "serch",
    "busca",
    "buscá"
}

GOOGLE_KEYS = { 
    "internet",
    "en google", 
    "en internet",
    "buscar_google"
    }

YOUTUBE_KEYS = { 
    "Yutub", 
    "Video", 
    "en youtube",
    "video",
    "videos",
    "el video", 
    "en Yutub",
    "buscar_youtube"
    }


CONTEXTO_TH = {
    "ultima_busqueda_google": None,
    "ultima_busqueda_youtube": None,
    "ultima_ruta": None,
    "ultima_app": None,
    "ultima_carpeta_ruta": None
}


NEWRUTINA_WORDS = {
    "cuando diga",
    "con el comando", 
    "ahora el comando", 
    "la frase ahroa"
}