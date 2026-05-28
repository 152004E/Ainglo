# Ainglo

Ainglo es un asistente inteligente para aprender inglés mediante inteligencia artificial, enfocado especialmente en hispanohablantes que desean mejorar su speaking, pronunciación y vocabulario de una manera práctica, natural y accesible.

El proyecto combina modelos de IA en la nube, reconocimiento de voz y generación de audio para crear una experiencia de aprendizaje personalizada directamente desde Telegram.

## Características principales

- Corrección de inglés escrito con explicaciones en español
- Conversaciones naturales en inglés con IA
- Memoria personalizada para recordar errores y progreso
- Análisis de audios de voz (speaking)
- Generación de pronunciación correcta (TTS)
- Diccionario inteligente con traducciones y ejemplos
- Integración con Telegram para acceso rápido

## Stack tecnológico

| Herramienta | Uso |
|---|---|
| Python | Lenguaje principal |
| python-telegram-bot | Bot de Telegram |
| Gemini API (Google) | LLM principal (conversación, corrección) |
| Groq API | LLM alternativo (alta velocidad) |
| Faster Whisper | Speech-to-Text (audios) |
| Piper TTS / Edge TTS | Text-to-Speech |
| SQLite + SQLAlchemy | Base de datos local |

## Arquitectura

```
Telegram → Handler → Service → AI Provider → Respuesta
                                    ↕
                             Gemini / Groq
```

El sistema usa una interfaz de proveedor (`BaseAIProvider`) que permite cambiar entre Gemini y Groq con una variable de entorno, sin modificar el código de negocio.

## Configuración rápida

1. Clonar el repositorio
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Crear archivo `.env`:
   ```
   TELEGRAM_TOKEN=tu_token_aqui
   AI_PROVIDER=gemini
   GEMINI_API_KEY=tu_api_key_aqui
   ```
4. Correr el bot:
   ```bash
   python run.py
   ```

## Variables de entorno

```env
TELEGRAM_TOKEN=       # Token de @BotFather
AI_PROVIDER=gemini    # gemini | groq
AI_MODEL=             # Dejar vacío para usar modelo por defecto
GEMINI_API_KEY=       # API Key de Google AI Studio
GROQ_API_KEY=         # API Key de Groq (opcional)
DB_PATH=data/database/ainglo.db
```

## Objetivo del proyecto

Construir una plataforma inteligente de aprendizaje de inglés que ayude a mejorar speaking y pronunciación de forma personalizada, usando APIs de IA en la nube y herramientas de bajo costo.

## Estado del proyecto

MVP en desarrollo activo. Ver `docs/plan_desarrollo.md` para el plan completo.

## Visión a futuro

- Análisis avanzado de speaking y pronunciación
- Modo shadowing
- Panel web de progreso
- Aplicación móvil
- Sistema premium escalable
- source venv/bin/activate 
