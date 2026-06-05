import webbrowser
import subprocess
import os
from utilidades.hablar import hablar
import utilidades.Comandos as texts
import pyautogui
import pygetwindow as gw
import time
import pyperclip
from utilidades.gestor_plugins import obtener_plugins

def abrir_aplicacion(parametro):

    if parametro in texts.OPEN_ROOTS:

        hablar(
            "abriendo " + parametro
        )
        texts.OPEN_ROOTS[parametro]()

    else:

        hablar(
            "no conozco " + parametro
        )


def buscar_google(parametro):

    hablar(
        "buscando " + parametro + " en google"
    )

    webbrowser.open(
        "https://www.google.com/search?q=" + parametro
    )


def buscar_youtube(parametro):

    hablar(
        "buscando " + parametro + " en youtube"
    )

    webbrowser.open(
        "https://www.youtube.com/results?search_query=" + parametro
    )


def abrir_carpeta(parametro):

    if parametro in texts.CARPETAS_ROOTS:

        hablar(
            "abriendo la carpeta " + parametro
        )

        # Detecta automáticamente "C:\Users\tu_usuario"
        usuario_root = os.path.expanduser("~")

        ruta = os.path.join(
            usuario_root, 
            texts.CARPETAS_ROOTS[parametro]
        )

        try:
            subprocess.run(
                ["cmd", "/c", "start", "", ruta]
            )
        except Exception as e:
            print(f"Error de sistema: {e}")
            hablar("Hubo un problema al abrir esa ruta")

    else:

        hablar(
            "no conozco esa carpeta"
        )


def escribir(parametro):

    time.sleep(1)

    pyautogui.write(
        parametro,
        interval=0.03
    )


def presionar_tecla(parametro):
    try:
        pyautogui.press(
            parametro
        )
    except Exception as e:
        print(f"Tecla no válida: {e}")


def tecla_combo(parametro):
    try:
        teclas = parametro.split("+")

        pyautogui.hotkey(
            *teclas
        )
    except Exception as e:
        print(f"Combo no válido: {e}")


def activar_ventana(parametro):
    todas_las_ventanas = gw.getAllTitles()
    
    # Buscamos coincidencias ignorando mayúsculas
    for titulo in todas_las_ventanas:
        if parametro.lower() in titulo.lower() and titulo.strip() != "":
            ventanas = gw.getWindowsWithTitle(titulo)
            if ventanas:
                try:
                    ventana = ventanas[0]
                    if ventana.isMinimized:
                        ventana.restore()
                    ventana.activate()
                    print(f"Ventana activada: {titulo}")
                    return True
                except:
                    continue
                    
    print(f"No se encontró ninguna ventana con: {parametro}")
    return False


def esperar(parametro):

    time.sleep(
        float(parametro)
    )


def buscar_portapapeles(parametro):
    texto_copiado = pyperclip.paste()
    if texto_copiado:
        hablar("Buscando lo que copiaste")
        webbrowser.open("https://www.google.com/search?q=" + texto_copiado)
    else:
        hablar("El portapapeles está vacío")


TOOLS = {
    # comandos basicos
    "abrir_aplicacion": abrir_aplicacion,
    "buscar_google": buscar_google,
    "buscar_youtube": buscar_youtube,
    "abrir_carpeta": abrir_carpeta,
    # manos
    "escribir": escribir,
    "tecla_combo": tecla_combo,
    "presionar_tecla": presionar_tecla,
    "activar_ventana": activar_ventana,
    "esperar": esperar
}

# Inyectar dinámicamente las herramientas de los plugins
tools_extras, _ = obtener_plugins()
TOOLS.update(tools_extras)