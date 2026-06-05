import pyttsx3
import pythoncom

def hablar(texto):
    try:
        # Inicializamos COM antes de que pyttsx3 intente usar la voz de Windows
        pythoncom.CoInitialize()
        
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()
        
    except Exception as e:
        print(f"Error al intentar hablar: {e}")
    finally:
        # El bloque finally asegura que siempre se desvincule, falle o no
        pythoncom.CoUninitialize()