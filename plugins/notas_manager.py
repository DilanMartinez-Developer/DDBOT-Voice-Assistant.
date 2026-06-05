import os
import datetime
import re # Usaremos expresiones regulares para extraer horas del texto
from utilidades.hablar import hablar

# --- DETECCIÓN DINÁMICA DE LA CARPETA DE DOCUMENTOS ---
ruta_usuario = os.path.expanduser('~')
ruta_documentos = os.path.join(ruta_usuario, 'Documents')

ruta_onedrive = os.path.join(ruta_usuario, 'OneDrive', 'Documents')
if not os.path.exists(ruta_documentos) and os.path.exists(ruta_onedrive):
    ruta_documentos = ruta_onedrive

ARCHIVO_NOTAS = os.path.join(ruta_documentos, "NotasByDDBOT.txt")
# ------------------------------------------------------


def guardar_nota(parametro):
    try:
        fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        with open(ARCHIVO_NOTAS, "a", encoding="utf-8") as file:
            file.write(f"[{fecha_actual}] {parametro}\n")
            
        print(f"Nota guardada en {ARCHIVO_NOTAS}: {parametro}")
        hablar("Nota guardada con éxito.")
    except Exception as e:
        print(f"Error al guardar la nota: {e}")
        hablar("Ups, hubo un error al intentar escribir la nota.")


def leer_notas(parametro=""):
    try:
        if os.path.exists(ARCHIVO_NOTAS):
            with open(ARCHIVO_NOTAS, "r", encoding="utf-8") as file:
                notas = file.readlines()
            
            if notas:
                texto_a_leer = ""
                for nota in notas:
                    partes = nota.split("] ")
                    if len(partes) > 1:
                        texto_a_leer += partes[1] + ". "
                
                print("Leyendo notas...")
                hablar("Tus notas pendientes son: " + texto_a_leer)
            else:
                print("El archivo está vacío.")
                hablar("No tienes ninguna nota guardada en este momento.")
        else:
            print("No existe el archivo de notas.")
            hablar("Aún no has guardado ninguna nota.")
    except Exception as e:
        print(f"Error al leer las notas: {e}")
        hablar("Hubo un error al intentar leer tu archivo de notas.")


def buscar_fecha_nota(parametro):
    try:
        if not parametro:
            hablar("¿De qué nota quieres saber la fecha?")
            return

        if os.path.exists(ARCHIVO_NOTAS):
            with open(ARCHIVO_NOTAS, "r", encoding="utf-8") as file:
                notas = file.readlines()

            encontrada = False
            for nota in reversed(notas):
                if parametro.lower() in nota.lower():
                    partes = nota.split("] ")
                    if len(partes) > 1:
                        fecha_completa = partes[0].replace("[", "").strip() # "05/06/2026 03:35"
                        texto_nota = partes[1].strip() # "debo dominar el mundo a las 5 p.m."
                        
                        # GUARDAMOS EN LA MEMORIA DEL PROCESO (Inmune a NameErrors)
                        os.environ["DDBOT_ULTIMA_HORA_PUBLICA"] = fecha_completa
                        os.environ["DDBOT_ULTIMO_TEXTO_NOTA"] = texto_nota
                        
                        fecha, hora = fecha_completa.split(" ")
                        print(f"📅 Fecha encontrada para '{parametro}': {fecha} a las {hora}")
                        hablar(f"Esa nota la guardaste el día {fecha} a las {hora}.")
                        encontrada = True
                        break

            if not encontrada:
                hablar(f"No encontré ninguna nota guardada que hable sobre {parametro}.")
        else:
            hablar("No tienes ninguna nota guardada todavía.")
            
    except Exception as e:
        print(f"Error al buscar la fecha de la nota: {e}")
        hablar("Hubo un error al buscar la fecha en tu archivo de notas.")


def calcular_tiempo_restante(parametro):
    try:
        # 1. Obtener la hora en la que se publicó la nota desde os.environ
        ultima_hora_env = os.environ.get("DDBOT_ULTIMA_HORA_PUBLICA")
        texto_nota_env = os.environ.get("DDBOT_ULTIMO_TEXTO_NOTA", "")

        if ultima_hora_env:
            hora_inicio = datetime.datetime.strptime(ultima_hora_env, "%d/%m/%Y %H:%M")
            origen_txt = "la hora de publicación"
        else:
            hora_inicio = datetime.datetime.now()
            origen_txt = "la hora actual"

        # 2. Determinar la hora objetivo de forma inteligente
        hora_objetivo_str = None
        parametro_limpio = parametro.strip().lower()

        # Si Groq nos manda una hora real en formato HH:MM (ej: "17:00") la usamos directamente
        match_param = re.search(r'(\d{1,2}):(\d{2})', parametro_limpio)
        if match_param:
            hora_objetivo_str = f"{int(match_param.group(1)):02d}:{int(match_param.group(2)):02d}"
        
        # Si mandó un placeholder ("hora_encontrada", "auto", etc.), la extraemos del texto de la nota
        else:
            print(f"🔍 Analizando texto de la nota para extraer el horario: '{texto_nota_env}'")
            texto_minusculas = texto_nota_env.lower()
            
            match_nota_hhmm = re.search(r'(\d{1,2}):(\d{2})', texto_minusculas)
            match_pm = re.search(r'(\d{1,2})\s*(p\.?m\.?|pm|tarde|noche)', texto_minusculas)
            match_am = re.search(r'(\d{1,2})\s*(a\.?m\.?|am|mañana)', texto_minusculas)

            if match_nota_hhmm:
                hora_objetivo_str = f"{int(match_nota_hhmm.group(1)):02d}:{int(match_nota_hhmm.group(2)):02d}"
            elif match_pm:
                h = int(match_pm.group(1))
                if h < 12: h += 12 # Convertir 5 p.m. a 17
                hora_objetivo_str = f"{h:02d}:00"
            elif match_am:
                h = int(match_am.group(1))
                if h == 12: h = 0 # Convertir 12 a.m. a 00
                hora_objetivo_str = f"{h:02d}:00"

        if not hora_objetivo_str:
            print("⚠️ No se pudo determinar ninguna hora objetivo en el parámetro ni en la nota.")
            hablar("No pude encontrar a qué hora límite te referías en la nota.")
            return

        # 3. Calcular la diferencia matemática
        hora_obj = datetime.datetime.strptime(hora_objetivo_str, "%H:%M")
        hora_destino = hora_inicio.replace(hour=hora_obj.hour, minute=hora_obj.minute, second=0, microsecond=0)

        diferencia = hora_destino - hora_inicio
        total_segundos = int(diferencia.total_seconds())

        if total_segundos < 0:
            total_segundos = abs(total_segundos)
            horas = total_segundos // 3600
            minutos = (total_segundos % 3600) // 60
            mensaje = f"Ya pasaron {horas} horas y {minutos} minutos de las {hora_objetivo_str} desde {origen_txt}."
        else:
            horas = total_segundos // 3600
            minutos = (total_segundos % 3600) // 60
            mensaje = f"Faltan exactamente {horas} horas y {minutos} minutos para las {hora_objetivo_str} desde {origen_txt}."

        print(f"{mensaje}")
        hablar(mensaje)

    except Exception as e:
        print(f"Error en calcular_tiempo_restante: {e}")
        hablar("Hubo un problema matemático al calcular el tiempo restante.")


def borrar_notas(parametro=""):
    try:
        if os.path.exists(ARCHIVO_NOTAS):
            os.remove(ARCHIVO_NOTAS)
            print("Notas borradas.")
            hablar("Todas tus notas han sido eliminadas exitosamente.")
        else:
            print("No hay archivo para borrar.")
            hablar("No tenías notas guardadas para borrar.")
    except Exception as e:
        print(f"Error al borrar las notas: {e}")
        hablar("No pude borrar el archivo de notas.")

TOOLS = {
    "borrar_notas": borrar_notas,
    "leer_notas": leer_notas,
    "guardar_nota": guardar_nota,
    "buscar_fecha_nota": buscar_fecha_nota,
    "calcular_tiempo_restante": calcular_tiempo_restante
}

# --- INSTRUCCIONES ACTUALIZADAS PARA LA IA ---
PROMPT_REGLAS = """
- guardar_nota: usa esta acción cuando el usuario te pida anotar, guardar, recordar algo o tomar una nota. Parámetro: el texto exacto que debe recordar (ej: "llamar al dentista mañana").
- leer_notas: usa esta acción cuando el usuario pregunte por sus notas, qué tiene pendiente, o te pida que le leas sus recordatorios. Parámetro: vacío "".
- borrar_notas: usa esta acción cuando el usuario te pida eliminar, borrar, limpiar o vaciar todas sus notas o recordatorios. Parámetro: vacío "".
- buscar_fecha_nota: usa esta acción cuando el usuario te pregunte CUÁNDO anotó algo, en qué fecha, qué día o a qué hora guardó una nota específica. Parámetro: la palabra clave de la nota (ej: "mundo", "novia", "pan").
- calcular_tiempo_restante: usa esta acción cuando el usuario te pregunte cuánto tiempo falta, cuánto tiempo pasó o qué diferencia hay hacia un evento o una hora específica del día. Parámetro: Si el usuario dice una hora ponla en formato militar "HH:MM" (ej: "17:00"). Si se refiere a la hora de la nota que acabas de buscar, pon simplemente "auto".
"""