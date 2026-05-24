import webbrowser
import subprocess
from utilidades.hablar import hablar
import utilidades.Comandos as texts
#masnos para el asist
import pyautogui
import pygetwindow as gw
import time

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

        ruta = (
            "C:\\Users\\galos\\"
            + texts.CARPETAS_ROOTS[parametro]
        )

        subprocess.run(
            ["cmd", "/c", "start", "", ruta]
        )

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

    pyautogui.press(
        parametro
    )


def tecla_combo(parametro):

    teclas = parametro.split("+")

    pyautogui.hotkey(
        *teclas
    )


def activar_ventana(parametro):

    ventanas = gw.getWindowsWithTitle(
        parametro
    )

    if ventanas:

        try:

            ventana = ventanas[0]

            if ventana.isMinimized:
                ventana.restore()

            ventana.activate()

            print(
                "ventana activada"
            )

            return True

        except:

            return False

    return False


def esperar(parametro):

    time.sleep(
        float(parametro)
    )



TOOLS = {
    #comandos basicos
    "abrir_aplicacion": abrir_aplicacion,
    "buscar_google": buscar_google,
    "buscar_youtube": buscar_youtube,
    "abrir_carpeta": abrir_carpeta,
    #manos
    "escribir": escribir,
    "tecla_combo": tecla_combo,
    "presionar_tecla": presionar_tecla,
    "activar_ventana": activar_ventana,
    
    "esperar": esperar
}