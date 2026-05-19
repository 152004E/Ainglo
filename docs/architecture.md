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
│   │   │   ├── ollama_client.py
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
│   └── roadmap.md
│
├── requirements.txt
├── .env
├── .gitignore
├── README.md
├── run.py
└── Estructura.md
```

## Descripción de carpetas y archivos

- **app/**: Lógica principal del sistema.
  - **main.py**: Punto de entrada de la app.
  - **config/**: Configuración, constantes y prompts.
  - **bot/**: Todo lo relacionado con Telegram.
  - **ai/**: Módulos de IA (Ollama, Whisper, Piper, etc).
  - **services/**: Lógica de negocio.
  - **database/**: Modelos y acceso a base de datos.
  - **utils/**: Utilidades reutilizables.
  - **tests/**: Pruebas unitarias.
- **data/**: Archivos generados por el sistema (audios, modelos, base de datos).
- **docs/**: Documentación técnica y roadmap.
- **requirements.txt**: Dependencias del proyecto.
- **.env**: Variables de entorno sensibles.
- **.gitignore**: Archivos y carpetas ignorados por git.
- **README.md**: Descripción general del proyecto.
- **run.py**: Script para lanzar la app.
- **Estructura.md**: Este archivo, con la estructura y explicación.
