from UtilidadesConIA.iaGroq import pensar
from UtilidadesConIA.ejecutorIA import ejecutarIA

from utilidades.escucharNEW import escuchar
from utilidades.hablar import hablar
import utilidades.Comandos as texts
import time
import keyboard

CONTEXTO_IA = {
    "ultima_respuesta": "",
    "ultimo_comando": "",
    "ultima_accion": ""
}

def ActivacionPorTecla():

    texto = escuchar()

    print("texto:", texto)

    if texto in texts.TY_WORDS:
        hablar("pa eso estamos mano")
        return

    if texto in texts.CLOSE_WORDS:
        hablar("deteniendo programa")
        time.sleep(0.2)
        exit()

    comando = texto.strip()

    if comando == "":
        hablar("no logre escucharte bien")
        return

    print("pensando...")

    respuestaIA = pensar(comando, CONTEXTO_IA)

    if respuestaIA["tipo"] == "respuesta":
        CONTEXTO_IA["ultima_respuesta"] = respuestaIA["contenido"]

    if respuestaIA["tipo"] == "acciones":
        CONTEXTO_IA["ultima_accion"] = str(
        respuestaIA["acciones"]
    )
    CONTEXTO_IA["ultimo_comando"] = comando
    
    print(respuestaIA)

    ejecutarIA(respuestaIA)



keyboard.add_hotkey('F10',  ActivacionPorTecla)
print("Esperando tecla...")
keyboard.wait()
