import speech_recognition as sr
#parte encargada de reconocer la voz y pasarla a texto  
recognizer = sr.Recognizer()
recognizer.energy_threshold = 500
recognizer.dynamic_energy_threshold = False
#toma el audio del micro, le reduce el ruido ambiente y lo pasa a un string
with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=1)


def escuchar():
    with sr.Microphone() as source:
        #listen bolquea el proceso hasta que se hable
        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )
        except sr.WaitTimeoutError:
            return "."   
            #utiliza una api, solo funciona con internet
        try:
            texto = recognizer.recognize_google(audio, language="es-ES")
            return texto.lower()

        except sr.UnknownValueError:
            #hablar("No entendí")
            #time.sleep(1)
            return ""
        except sr.RequestError:
            #hablar("Error con la API")
            #time.sleep(1)
            return ""
