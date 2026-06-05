# DDBOT - AI Powered Voice Assistant
### Asistente de Voz Autónomo y Modular para Windows

<p align="center">
  <img src="docs/ddbot-banner.png" alt="DDBOT Banner" width="100%">
</p>

## 📝 Descripción
DDBOT es un asistente de voz avanzado desarrollado en Python que combina el procesamiento de lenguaje natural en la nube con automatización local y una arquitectura modular basada en plugins. 

El sistema utiliza un flujo optimizado: captura audio mediante control de actividad de voz (VAD), transcribe de forma local y ultrarrápida con **Faster-Whisper**, procesa e interpreta la intención del usuario a través de los LLMs de **Groq** devolviendo un plan estructurado en **JSON**, y finalmente ejecuta secuencias lógicas e independientes a bajo nivel en el sistema operativo.

El objetivo principal es explorar el desarrollo de **Agentes Autónomos Resolutivos** capaces de encadenar acciones complejas y expandir sus habilidades dinámicamente.

---

## 🚀 Características Clave
* **Escucha Activa con VAD (Voice Activity Detection):** Detección automática de silencio para cortar la grabación de forma inteligente cuando terminas de hablar.
* **Cerebro con LLM Avanzado:** Respuestas estructuradas nativas en formato JSON mediante Groq (Llama 3.3).
* **Planificación Multi-Acción Autónoma:** Capacidad de la IA para razonar y encadenar múltiples comandos secuenciales en una sola petición (ej. activar ventana, esperar, escribir y ejecutar combo).
* **Arquitectura de Plugins Modulares:** Sistema desacoplado que inyecta dinámicamente herramientas y reglas al prompt del sistema sin tocar el núcleo del código.
* **Feedback Auditivo Integral:** Tonos de notificación (*beeps*) nativos del sistema para estados de escucha y procesamiento.
* **Freno de Emergencia (Kill Switch):** Comando físico por teclado (`Ctrl+Shift+F10`) para detener procesos descontrolados instantáneamente.
* **Automatización de Escritorio Humanoide:** Escritura con intervalos, manejo tolerante de títulos de ventana (*fuzzy matching*) y emulación de periféricos.

---

## 🛠️ Arquitectura del Sistema

```text
  Micrófono (Entrada de Voz)
          │
          ▼
   Stream de Audio (VAD) ──► [Beep Inicio]
          │
          ▼
    Faster-Whisper (Transcripción Local) ──► [Beep Fin]
          │
          ▼
     Texto Limpio
          │
          ▼
     Groq (LLM) ◄─── [Inyección Dinámica de Plugins / Reglas]
          │
          ▼
  JSON Plan de Acciones (Multi-acción / Auto-parámetros)
          │
          ▼
    Ejecutor Central
          │
          ├──► Plugins Internos (broma, volumen_manager, notas_manager)
          └──► Herramientas de Sistema (PyAutoGUI, PyGetWindow, Teclado)
          │
          ▼
   Acción Ejecutada en Windows
📂 Estructura del Proyecto
Plaintext
DDBOT/
│
├── MAIN.py                 # Núcleo del programa y atajos globales
│
├── utilidades/             # Módulos core de hardware y utilidades del sistema
│   ├── escucharNEW.py      # Stream de audio con VAD y Faster-Whisper
│   ├── hablar.py           # Motor de síntesis de voz (TTS)
│   ├── memoriaDinamica.py  # Sistema de persistencia contextual
│   ├── procesar.py         # Formateador de texto de entrada
│   └── Comandos.py         # Diccionarios de palabras clave y rutas fijas
│
├── UtilidadesConIA/        # Lógica de Inteligencia Artificial
│   ├── iaGroq.py           # Conector con la API de Groq y estructurador JSON
│   ├── ejecutorIA.py       # Orquestador tolerante a fallos del plan de acción
│   └── herramientas.py     # Diccionario base TOOLS (ventanas, teclas, mouse)
│
├── plugins/                # ¡NUEVO! Sistema Modular de Plugins Autónomos
│   ├── volumen_manager.py  # Control del mezclador de volumen de Windows (PyCaw)
│   ├── notas_manager.py    # Gestor de notas temporales con análisis de horario (Regex)
│   └── broma.py            # Módulo de entretenimiento
│
├── docs/
│   └── ddbot-banner.png    # Recursos visuales del repositorio
│
├── requirements.txt        # Dependencias del entorno
└── README.md
⌨️ Ejemplos de Razonamiento Autónomo
1. Encadenamiento Secuencial Complejo
Usuario: "Abre steam espera tres segundos y pulsa alt mas f4"

JSON Plan de Acción:

JSON
{
  "tipo": "acciones",
  "acciones": [
    { "accion": "abrir_aplicacion", "parametros": "steam" },
    { "accion": "esperar", "parametros": "3" },
    { "accion": "tecla_combo", "parametros": "alt+f4" }
  ]
}
2. Extracción de Datos en Plugins con Parámetros Automáticos
Usuario: "Dime cuánto falta desde que publiqué esta nota para dominar el mundo"

Ejecución Multi-Acción en Cadena:

El bot detecta que requiere el plugin notas_manager.

Ejecuta buscar_fecha_nota para obtener la fecha de publicación original.

Al detectar una consulta de tiempo relativo, pasa automáticamente el parámetro "auto" a calcular_tiempo_restante.

El script lee el texto interno de la nota ("debo dominar el mundo a las 5 p.m."), extrae la hora militar (17:00) mediante expresiones regulares (re) y procesa la matemática de tiempos frente a la hora de publicación original (03:35).

Salida por voz: "Faltan exactamente 13 horas y 25 minutos para las 17:00 desde la hora de publicación."

🔧 Instalación y Configuración
Clonar el repositorio:

Bash
git clone [https://github.com/DilanMartinez-Developer/DDBOT.git](https://github.com/DilanMartinez-Developer/DDBOT.git)
cd DDBOT
Instalar dependencias necesarias:
(Asegúrate de tener instaladas las librerías de audio nativas de Windows para el control de volumen)

Bash
pip install -r requirements.txt
pip install pycaw comtypes
Configurar variables de entorno:
Crea un archivo .env en la raíz del proyecto y añade tu API Key de Groq:

Fragmento de código
Groq_Api_KEY=TU_API_KEY_DE_GROQ
Ejecutar el asistente:

Bash
python MAIN.py
Presiona F10 para empezar a hablar o Ctrl+Shift+F10 en cualquier momento para el apagado de emergencia.

🗺️ Roadmap de Desarrollo
[x] Reconocimiento de voz local y optimización de audio (VAD)

[x] Integración con Groq Cloud LLM

[x] Sistema de automatización de ventanas y emulación de teclado

[x] Contexto conversacional y memoria de acciones

[x] Arquitectura Modular por Sistema de Plugins (¡Logrado!)

[ ] Plugin de Visión Avanzada: Capturas de pantalla ocultas y análisis visual del escritorio con modelos de visión (Próximamente)

[ ] Implementación de OCR en pantalla para clics dinámicos sobre texto

[ ] Interfaz gráfica de usuario (GUI) interactiva

🎓 Objetivo Educativo
Este proyecto es un entorno de experimentación personal diseñado para profundizar en la integración práctica de Inteligencia Artificial Generativa con automatización nativa de sistemas operativos, procesamiento de señal de voz y desarrollo de herramientas asistidas por IA.

👤 Autor
Dilan Martínez - Estudiante de Ingeniería en Mecatrónica.

GitHub: @DilanMartinez-Developer