from utilidades.escuchar import escuchar
from utilidades.hablar import hablar
from utilidades.procesar import procesar
import utilidades.Comandos as texts
import time


while True:  
    texto = escuchar()
    print("texto :",texto)
    if texto in texts.TY_WORDS:
        hablar("Pa eso estamos mano")

    if texto in texts.CLOSE_WORDS:
        hablar("deteniendo programa, nos vemos luego")
        time.sleep(0.2)
        exit()

    if any(p in texto for p in texts.WAKE_WORDS):
        #limpiar wake word para que no queden en los comandos
        for palabra in texts.WAKE_WORDS:
            if palabra in texto:
                texto = texto.replace(palabra, "")
                break
        comando = texto.strip()
        if comando != "":
            procesar(comando)
        else:
            hablar("Que pasò ? ")
                
