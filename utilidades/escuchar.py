import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel
import unicodedata
import queue
import winsound # <-- Librería nativa de Windows para los beeps

# Configuracion
FS = 16000
UMBRAL_SILENCIO = 0.015  # Sensibilidad del micro
SILENCIO_MAX = 1.2       # Segundos de silencio para cortar

# Iniciamos el modelo 
model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

def limpiarTexto(texto):
    texto = texto.lower().strip()

    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )    
    
    signos = "¡!¿?;()[]{}\"'"

    texto = texto.translate(
        str.maketrans('', '', signos)
    )
    return texto


def escuchar():
    print("Escuchando...")
    
    # Feedback auditivo de INICIO (Tono ascendente)
    # winsound.Beep(frecuencia_en_hertz, duracion_en_milisegundos)
    winsound.Beep(1000, 100)
    winsound.Beep(1500, 100)
    
    q = queue.Queue()

    def callback(indata, frames, time, status):
        if status:
            print(status)
        q.put(indata.copy())

    grabacion = []
    silencio_frames = 0
    empezo_a_hablar = False
    
    blocksize = int(FS * 0.1) 

    with sd.InputStream(samplerate=FS, channels=1, dtype='float32', blocksize=blocksize, callback=callback):
        while True:
            data = q.get()
            grabacion.append(data)
            
            volumen = np.sqrt(np.mean(data**2))
            
            if volumen > UMBRAL_SILENCIO:
                empezo_a_hablar = True
                silencio_frames = 0
            elif empezo_a_hablar:
                silencio_frames += 1
                
            if empezo_a_hablar and (silencio_frames * blocksize / FS) >= SILENCIO_MAX:
                break

    # Feedback auditivo de FIN / PROCESANDO (Tono grave y corto)
    winsound.Beep(800, 150)
    print("Procesando...")

    audioFloat = np.concatenate(grabacion).flatten()

    segments, info = model.transcribe(
        audioFloat,
        beam_size=3,
        vad_filter=False,
        language="es",
        initial_prompt="""
        español con palabras:
        steam discord youtube github windows python spotify entre otras en ingles
        """
    )
    
    texto = ""
    for segment in segments:
        texto += segment.text
    
    return limpiarTexto(texto).strip()