# Estructura del Proyecto Ainglo

```
ainglo/
│
├── app/
│   ├── main.py
│   ├── config/
│   │   ├── settings.py
│   │   ├── constants.py
│   │   └── prompts.py
│   │
│   ├── bot/
│   │   ├── telegram_bot.py
│   │   ├── handlers/
│   │   │   ├── start_handler.py
│   │   │   ├── message_handler.py
│   │   │   ├── audio_handler.py
│   │   │   └── command_handler.py
│   │   │
│   │   └── keyboards/
│   │       └── menus.py
│   │
│   ├── ai/
│   │   ├── llm/
│   │   │   ├── base_provider.py       ← interfaz + factory
│   │   │   ├── gemini_client.py       ← Google Gemini
│   │   │   ├── groq_client.py         ← Groq
│   │   │   ├── prompts.py
│   │   │   └── conversation_manager.py
│   │   │
│   │   ├── speech_to_text/
│   │   │   ├── whisper_service.py
│   │   │   └── audio_preprocessor.py
│   │   │
│   │   ├── text_to_speech/
│   │   │   ├── piper_service.py
│   │   │   └── voice_generator.py
│   │   │
│   │   └── correction/
│   │       ├── grammar_corrector.py
│   │       ├── pronunciation_feedback.py
│   │       └── vocabulary_helper.py
│   │
│   ├── services/
│   │   ├── conversation_service.py
│   │   ├── speaking_service.py
│   │   ├── translation_service.py
│   │   └── user_progress_service.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   ├── models/
│   │   │   ├── user_model.py
│   │   │   ├── progress_model.py
│   │   │   └── vocabulary_model.py
│   │   │
│   │   └── repositories/
│   │       ├── user_repository.py
│   │       ├── progress_repository.py
│   │       └── vocabulary_repository.py
│   │
│   ├── utils/
│   │   ├── logger.py
│   │   ├── audio_utils.py
│   │   ├── text_utils.py
│   │   └── file_manager.py
│   │
│   └── tests/
│       ├── test_ai.py
│       ├── test_audio.py
│       └── test_bot.py
│
├── data/
│   ├── audios/
│   ├── temp/
│   ├── models/
│   └── database/
│
├── docs/
│   ├── architecture.md
│   ├── api_flow.md
│   ├── plan_desarrollo.md
│   └── roadmap.md
│
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── run.py
```

## Descripción de carpetas y archivos

- **app/**: Lógica principal del sistema.
  - **main.py**: Punto de entrada de la app.
  - **config/**: Configuración, constantes y prompts.
  - **bot/**: Todo lo relacionado con Telegram.
  - **ai/llm/**: Clientes de IA (Gemini, Groq). `base_provider.py` define la interfaz y la factory.
  - **ai/speech_to_text/**: Faster Whisper para transcripción de audios.
  - **ai/text_to_speech/**: TTS para generar audio de pronunciación.
  - **ai/correction/**: Lógica de corrección gramatical y pronunciación.
  - **services/**: Lógica de negocio.
  - **database/**: Modelos SQLAlchemy y repositorios SQLite.
  - **utils/**: Utilidades reutilizables.
  - **tests/**: Pruebas unitarias.
- **data/**: Archivos generados (audios, base de datos).
- **docs/**: Documentación técnica y plan de desarrollo.

## Flujo principal

```
Telegram
   ↓
Handler (bot/handlers/)
   ↓
Service (services/)
   ↓
AI Provider Interface (ai/llm/base_provider.py)
   ↓
Gemini API  /  Groq API
   ↓
Respuesta → Telegram
```

## Cambiar de proveedor AI

Solo requiere cambiar la variable de entorno:

```env
AI_PROVIDER=groq   # o gemini
AI_MODEL=          # dejar vacío para usar modelo por defecto
```

No se modifica ningún código de negocio.
