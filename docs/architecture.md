# Estructura del Proyecto Ainglo

```
ainglo/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── constants.py
│   │   └── prompts.py
│   │
│   ├── bot/
│   │   ├── __init__.py
│   │   ├── telegram_bot.py
│   │   │
│   │   ├── handlers/
│   │   │   ├── __init__.py
│   │   │   ├── start_handler.py
│   │   │   ├── message_handler.py
│   │   │   ├── audio_handler.py
│   │   │   └── command_handler.py
│   │   │
│   │   └── keyboards/
│   │       ├── __init__.py
│   │       └── menus.py
│   │
│   ├── ai/
│   │   ├── __init__.py
│   │   │
│   │   ├── llm/                          ← Solo APIs cloud
│   │   │   ├── __init__.py
│   │   │   ├── base_provider.py          ← Interfaz + factory
│   │   │   ├── gemini_client.py          ← Google Gemini API
│   │   │   ├── groq_client.py            ← Groq API
│   │   │   ├── conversation_manager.py
│   │   │   └── prompts.py
│   │   │
│   │   ├── speech_to_text/
│   │   │   ├── __init__.py
│   │   │   ├── whisper_service.py
│   │   │   └── audio_preprocessor.py
│   │   │
│   │   ├── text_to_speech/
│   │   │   ├── __init__.py
│   │   │   ├── piper_service.py
│   │   │   └── voice_generator.py
│   │   │
│   │   └── correction/
│   │       ├── __init__.py
│   │       ├── grammar_corrector.py
│   │       ├── pronunciation_feedback.py
│   │       └── vocabulary_helper.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── conversation_service.py
│   │   ├── speaking_service.py
│   │   ├── translation_service.py
│   │   └── user_progress_service.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── connection.py
│   │   │
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user_model.py
│   │   │   ├── progress_model.py
│   │   │   └── vocabulary_model.py
│   │   │
│   │   └── repositories/
│   │       ├── __init__.py
│   │       ├── user_repository.py
│   │       ├── progress_repository.py
│   │       └── vocabulary_repository.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   ├── audio_utils.py
│   │   ├── text_utils.py
│   │   └── file_manager.py
│   │
│   └── tests/
│       ├── __init__.py
│       ├── test_ai.py
│       ├── test_audio.py
│       └── test_bot.py
│
├── data/
│   ├── audios/
│   ├── temp/
│   └── database/
│
├── docs/
│   ├── architecture.md
│   ├── api_flow.md
│   ├── plan_desarrollo.md
│   ├── reglas.md
│   └── roadmap.md
│
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── run.py
```

## Filosofía del proyecto

Ainglo está diseñado bajo un enfoque **cloud-first**. Toda la inteligencia artificial del
proyecto se consume mediante APIs en la nube. No se utilizan modelos descargados
localmente, inferencia local pesada ni pipelines dependientes de GPU.

Esto permite:
- desarrollo más rápido,
- menor complejidad operativa,
- menor consumo de recursos locales,
- mejor compatibilidad con hardware modesto,
- y un MVP realista sin depender de hardware especializado.

## Descripción de carpetas y archivos

- **app/**: Lógica principal del sistema.
  - **main.py**: Punto de entrada de la app.
  - **config/**: Configuración, constantes y prompts del sistema.
  - **bot/**: Todo lo relacionado con Telegram (handlers y menús).
  - **ai/llm/**: Proveedores de IA vía APIs cloud. `base_provider.py` define la interfaz y la factory. Proveedores actuales: Gemini API, Groq API.
  - **ai/speech_to_text/**: Faster Whisper para transcripción de audios (ejecución local ligera).
  - **ai/text_to_speech/**: TTS para generar audio de pronunciación.
  - **ai/correction/**: Lógica de corrección gramatical y pronunciación.
  - **services/**: Lógica de negocio (orquestación entre handlers, AI y base de datos).
  - **database/**: Modelos SQLAlchemy y repositorios SQLite.
  - **utils/**: Utilidades reutilizables.
  - **tests/**: Pruebas unitarias.
- **data/**: Archivos generados en tiempo de ejecución (audios, base de datos, archivos temporales).
- **docs/**: Documentación técnica y plan de desarrollo.

## Arquitectura por capas

```
Telegram
    ↓
Handler (bot/handlers/)
    ↓
Service Layer (services/)
    ↓
AI Provider Layer (ai/llm/base_provider.py)
    ↓
Gemini API  |  Groq API
```

### Capas del sistema

| Capa | Responsabilidad | No debe |
|------|----------------|---------|
| **Handler** | Recibir y responder mensajes de Telegram | Contener lógica de negocio |
| **Service** | Orquestar flujos, coordinar AI + DB | Conocer detalles de Telegram |
| **AI Provider** | Interfaz unificada para APIs cloud | Acoplarse a un proveedor específico |
| **Database** | Persistencia de datos | Contener lógica de negocio |

## Capa de proveedores IA (AI Provider Layer)

El sistema usa una interfaz abstracta (`BaseAIProvider`) que permite cambiar entre
proveedores cloud sin modificar el código de negocio.

```
Service Layer
    ↓
BaseAIProvider (interfaz)
    ↓
GeminiProvider  |  GroqProvider  |  (futuro: OpenAI, Claude, etc.)
```

Actualmente soportados:
- **Gemini API** — proveedor principal (gratuito vía Google AI Studio)
- **Groq API** — alternativa rápida (gratuito vía console.groq.com)

A futuro se pueden agregar:
- OpenAI API
- Claude API (Anthropic)
- Cualquier proveedor compatible con la interfaz

## Cambiar de proveedor AI

Solo requiere cambiar la variable de entorno:

```env
AI_PROVIDER=groq   # o gemini
AI_MODEL=          # dejar vacío para usar modelo por defecto
```

No se modifica ningún código de negocio.

## Variables de entorno

```env
TELEGRAM_TOKEN=       # Token de @BotFather
AI_PROVIDER=gemini    # gemini | groq
AI_MODEL=             # Dejar vacío para usar modelo por defecto
GEMINI_API_KEY=       # API Key de Google AI Studio
GROQ_API_KEY=         # API Key de Groq (opcional)
DB_PATH=data/database/ainglo.db
TEMP_AUDIO_DIR=data/temp
AUDIO_DIR=data/audios
```

## Prioridades del proyecto

- APIs gratuitas o freemium
- Rapidez de desarrollo
- Arquitectura modular y desacoplada
- Facilidad para cambiar de proveedor IA
- Sin dependencia de hardware especializado (GPU, RAM, etc.)
