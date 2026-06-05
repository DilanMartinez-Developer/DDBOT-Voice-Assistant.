import os
import importlib.util

# Variables globales para cachear la carga y no leer el disco varias veces
_tools_cargadas = None
_reglas_cargadas = None

def obtener_plugins():
    global _tools_cargadas, _reglas_cargadas
    
    # Si ya los cargamos antes, los devolvemos directamente
    if _tools_cargadas is not None:
        return _tools_cargadas, _reglas_cargadas
        
    _tools_cargadas = {}
    _reglas_cargadas = ""
    
    # Buscamos la carpeta 'plugins' en la raíz de tu proyecto
    ruta_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_plugins = os.path.join(ruta_raiz, 'plugins')
    
    # Si la carpeta no existe, la crea automáticamente
    if not os.path.exists(ruta_plugins):
        os.makedirs(ruta_plugins)
        print("Carpeta 'plugins' creada.")
        return _tools_cargadas, _reglas_cargadas

    # Escaneamos los archivos .py de la carpeta
    for archivo in os.listdir(ruta_plugins):
        if archivo.endswith(".py") and not archivo.startswith("__"):
            nombre_modulo = archivo[:-3]
            ruta_archivo = os.path.join(ruta_plugins, archivo)
            
            try:
                # Magia de Python para importar un archivo de texto como módulo dinámico
                spec = importlib.util.spec_from_file_location(nombre_modulo, ruta_archivo)
                modulo = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(modulo)
                
                # Si el plugin tiene funciones, las agregamos
                if hasattr(modulo, "TOOLS"):
                    _tools_cargadas.update(modulo.TOOLS)
                
                # Si el plugin tiene reglas para Groq, las sumamos
                if hasattr(modulo, "PROMPT_REGLAS"):
                    _reglas_cargadas += modulo.PROMPT_REGLAS + "\n"
                    
                print(f"Plugin cargado exitosamente: {nombre_modulo}")
                
            except Exception as e:
                print(f"Error al cargar el plugin '{nombre_modulo}': {e}")
                
    return _tools_cargadas, _reglas_cargadas