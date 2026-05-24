import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
import unicodedata
#Configuracion
DURACION = 5  # segundos
FS = 16000    # frecuencia recomendada para Whisper

#Iniciamos el modelo 
model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)
#funcion encargada de depurar el texto
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

#funcion escuchar
def escuchar():

    print("Escuchando...")

    # grabar audio
    audio = sd.rec(
        int(DURACION * FS),
        samplerate=FS,
        channels=1,
        dtype='int16'
    )

    sd.wait()

    print("Procesando...")

    # guardar wav temporal
    audioFloat = audio.flatten().astype("float32") / 32768.0

    # transcribir
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