# DDBOT - AI Powered Voice Assistant

<p align="center">
  <img src="docs/ddbot-banner.png" width="800">
</p>

<p align="center">
  <strong>Asistente de voz para Windows impulsado por IA</strong>
</p>

---

## Descripción

DDBOT es un proyecto personal desarrollado en Python que combina reconocimiento de voz, modelos de lenguaje e integración con el sistema operativo para crear un asistente capaz de interpretar instrucciones en lenguaje natural y ejecutarlas en Windows.

El flujo principal consiste en capturar audio desde el micrófono, convertirlo a texto mediante Faster-Whisper, interpretar la intención del usuario utilizando un modelo de lenguaje alojado en Groq y finalmente transformar esa intención en acciones estructuradas que pueden ser ejecutadas por el sistema.

El objetivo del proyecto es explorar la integración práctica de IA generativa con automatización de escritorio y asistentes inteligentes.

---

## Características actuales

* Conversión de voz a texto mediante Faster-Whisper
* Interpretación de lenguaje natural usando modelos LLM de Groq
* Respuestas estructuradas en formato JSON
* Apertura de aplicaciones
* Apertura de carpetas
* Búsquedas en Google
* Búsquedas en YouTube
* Control de ventanas activas
* Escritura automática de texto
* Combinaciones de teclas
* Esperas temporizadas
* Contexto conversacional básico
* Memoria de acciones previas

---

## Arquitectura

```text
Micrófono
    │
    ▼
Faster-Whisper
    │
    ▼
Texto transcrito
    │
    ▼
Groq (LLM)
    │
    ▼
JSON estructurado
    │
    ▼
Ejecutor de acciones
    │
    ▼
Windows
```

---

## Ejemplos

### Abrir una aplicación

Entrada:

```text
abre steam
```

Salida generada:

```json
{
  "tipo": "acciones",
  "acciones": [
    {
      "accion": "abrir_aplicacion",
      "parametros": "steam"
    }
  ]
}
```

---

### Buscar en YouTube

Entrada:

```text
busca terraria en youtube
```

Salida generada:

```json
{
  "tipo": "acciones",
  "acciones": [
    {
      "accion": "buscar_youtube",
      "parametros": "terraria"
    }
  ]
}
```

---

### Secuencia compleja

Entrada:

```text
abre steam espera tres segundos y pulsa alt f4
```

Salida generada:

```json
{
  "tipo": "acciones",
  "acciones": [
    {
      "accion": "abrir_aplicacion",
      "parametros": "steam"
    },
    {
      "accion": "esperar",
      "parametros": "3"
    },
    {
      "accion": "tecla_combo",
      "parametros": "alt+f4"
    }
  ]
}
```

---

## Tecnologías utilizadas

* Python 3.13
* Faster-Whisper
* Groq API
* PyAutoGUI
* PyGetWindow
* Keyboard
* SoundDevice
* Pyttsx3

---

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/DilanMartinez-Developer/DDBOT.git
```

Ingresar al proyecto:

```bash
cd DDBOT
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Crear un archivo `.env`:

```env
Groq_Api_KEY=TU_API_KEY
```

Ejecutar:

```bash
python MAIN.py
```

---

## Estructura del proyecto

```text
DDBOT/
│
├── MAIN.py
│
├── utilidades/
│   ├── escucharNEW.py
│   ├── hablar.py
│   ├── memoriaDinamica.py
│   ├── procesar.py
│   └── Comandos.py
│
├── UtilidadesConIA/
│   ├── iaGroq.py
│   ├── ejecutorIA.py
│   └── herramientas.py
│
├── docs/
│   └── ddbot-banner.png
│
├── requirements.txt
│
└── README.md
```

---

## Roadmap

* [x] Reconocimiento de voz
* [x] Integración con Groq
* [x] Automatización básica de Windows
* [x] Contexto conversacional
* [x] Control de ventanas
* [ ] OCR de pantalla
* [ ] Comprensión visual del escritorio
* [ ] Automatización basada en elementos detectados
* [ ] Interfaz gráfica propia
* [ ] Sistema de plugins

---

## Objetivo educativo

Este proyecto fue desarrollado principalmente con fines educativos y de experimentación para profundizar conocimientos en:

* Inteligencia Artificial
* Automatización de escritorio
* Procesamiento de voz
* Integración de APIs
* Desarrollo de herramientas asistidas por IA

---

## Autor

**Dilan Martínez**

Estudiante de Ingeniería en Mecatrónica.

GitHub:
https://github.com/DilanMartinez-Developer
