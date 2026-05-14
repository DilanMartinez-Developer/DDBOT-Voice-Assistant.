import pyttsx3
def hablar(texto):
    engine = pyttsx3.init()
    #propiedades VOZ
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.5)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) 

    engine.say(texto)
    engine.runAndWait()
    engine.stop()