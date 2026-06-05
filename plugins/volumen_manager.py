from utilidades.hablar import hablar
import pythoncom
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Necesitas instalar esta librería para controlar el volumen:
# pip install pycaw comtypes

def ajustar_volumen(parametro):
    """
    Parametro esperado: un numero del 0 al 100
    Ejemplo: "50"
    """
    try:
        nivel = int(parametro)

        if 0 <= nivel <= 100:
            
            # Inicializamos COM para que Windows permita tocar el audio desde este hilo
            pythoncom.CoInitialize() 
            
            # Obtenemos el dispositivo (Esto devuelve un objeto AudioDevice)
            device = AudioUtilities.GetSpeakers()
            
            # LA NUEVA FORMA: Accedemos directamente a EndpointVolume
            volume = device.EndpointVolume
            
            # Convertimos a escala de 0.0 a 1.0
            vol_scalar = nivel / 100
            
            # Ajustamos el volumen escalar
            volume.SetMasterVolumeLevelScalar(vol_scalar, None)
            
            # Desvinculamos el COM por buenas prácticas
            pythoncom.CoUninitialize()
            
            print(f" Éxito: Volumen ajustado al {nivel}%")
            # Asegúrate de tener tu función de hablar() definida en tu archivo
            # hablar(f"Volumen ajustado al {nivel} por ciento")
            
        else:
            print("El volumen debe estar entre 0 y 100")
            hablar("El volumen debe estar entre 0 y 100")
            
    except Exception as e:
        print(f" ERROR en ajustar_volumen: {e}")
        # hablar("No pude ajustar el volumen.")

def silenciar_sistema(parametro=""):
    """
    
    Silencia el sistema operativo (Mute).
    """
    try:
        pythoncom.CoInitialize() 
        
        device = AudioUtilities.GetSpeakers()
        volume = device.EndpointVolume
        
        # 1 significa , 0 significa desmutear
        volume.SetMute(1, None) 
        
        pythoncom.CoUninitialize()
        
        print(" Éxito: Sistema silenciado")
        
    except Exception as e:
        print(f" ERROR en silenciar_sistema: {e}")

def desmutear_sistema(parametro=""):
    """

    reactivar el audio (desMute). 
    """
    try:
        pythoncom.CoInitialize() 
        
        device = AudioUtilities.GetSpeakers()
        volume = device.EndpointVolume
        
        volume.SetMute(0, None) 
        
        pythoncom.CoUninitialize()
        
        print(" Éxito: audio reactivado")
        
    except Exception as e:
        print(f" ERROR en desmutear_sistema: {e}")

# Acciones que exponemos a DDBOT
TOOLS = {
    "ajustar_volumen": ajustar_volumen,
    "silenciar_sistema": silenciar_sistema,
    "desmutear_sistema": desmutear_sistema
}

# Instrucciones para la IA
PROMPT_REGLAS = """
- ajustar_volumen: usa esta acción cuando el usuario pida cambiar el volumen, subir, bajar o poner un porcentaje específico. Parámetro: el número (ej: 50).
- silenciar_sistema: usa esta acción cuando el usuario diga silenciar, mute, apagar sonido o callar.
- desmutear_sistema: usa esta accion cuando el usuario dega reactivar audio, des mutear, des silenciar o prender sonido.
"""