# Plan de Desarrollo — Ainglo

> Basado en `reglas.md`, `README.md` y `architecture.md`.  
> Filosofía: incremental, MVP primero, bajo costo, API-based.

---

## Stack base del proyecto

| Herramienta | Uso | Costo |
|---|---|---|
| Python | Lenguaje | Gratis |
| python-telegram-bot | Bot Telegram | Gratis |
| Gemini API | LLM principal | Gratis (free tier) |
| Groq API | LLM alternativo | Gratis (free tier) |
| SQLite | Base de datos | Gratis |
| Faster Whisper | STT (audios) | Gratis, local ligero |

**Sin servidores potentes. Sin modelos locales pesados. Solo requests HTTP.**

---

## Principio de ejecución

Cada fase debe quedar **funcional y probada** antes de avanzar a la siguiente.  
Nunca construir todo de una vez.

---

## Fase 0 — Base del proyecto ✅

**Objetivo:** Proyecto arranca sin errores.

| Tarea | Archivo | Estado |
|---|---|---|
| Estructura de carpetas | `app/`, `data/`, `docs/` | ✅ |
| Variables de entorno | `app/config/settings.py` + `.env` | ✅ |
| Constantes globales | `app/config/constants.py` | ✅ |
| Logger centralizado | `app/utils/logger.py` | ✅ |
| Conexión SQLite | `app/database/connection.py` | ✅ |
| Punto de entrada | `run.py` + `app/main.py` | ✅ |
| Dependencias | `requirements.txt` | ✅ |

**Criterio de éxito:** `python run.py` arranca sin errores.

---

## Fase 1 — MVP: Flujo mínimo funcional ✅

**Objetivo:** Bot responde mensajes de texto usando Gemini/Groq.

```
Telegram → mensaje texto → Gemini/Groq API → respuesta texto → Telegram
```

| Tarea | Archivo | Estado |
|---|---|---|
| Interfaz AI Provider | `app/ai/llm/base_provider.py` | ✅ |
| Cliente Gemini | `app/ai/llm/gemini_client.py` | ✅ |
| Cliente Groq | `app/ai/llm/groq_client.py` | ✅ |
| Prompts base para inglés | `app/ai/llm/prompts.py` + `app/config/prompts.py` | ✅ |
| Servicio de conversación | `app/services/conversation_service.py` | ✅ |
| Bot Telegram inicializado | `app/bot/telegram_bot.py` | ✅ |
| Handler /start | `app/bot/handlers/start_handler.py` | ✅ |
| Handler mensajes | `app/bot/handlers/message_handler.py` | ✅ |
| Comandos /reset /help | `app/bot/handlers/command_handler.py` | ✅ |

**Criterio de éxito:** Usuario escribe en Telegram → bot responde con corrección o conversación en inglés.

**Para arrancar necesitas:**
1. Token de [@BotFather](https://t.me/BotFather) en Telegram
2. API Key de [Google AI Studio](https://aistudio.google.com/) (Gemini) o [Groq](https://console.groq.com/)
3. Crear `.env` con esas claves
4. `pip install -r requirements.txt`
5. `python run.py`

---

## Fase 2 — Memoria y usuarios

**Objetivo:** Bot recuerda quién es cada usuario y su historial de conversación en base de datos.

```
Usuario → mensaje → historial cargado desde DB → respuesta contextual
```

| Tarea | Archivo |
|---|---|
| Modelo de usuario | `app/database/models/user_model.py` |
| Repositorio de usuario | `app/database/repositories/user_repository.py` |
| Modelo de progreso | `app/database/models/progress_model.py` |
| Repositorio de progreso | `app/database/repositories/progress_repository.py` |
| Gestor de conversación persistente | `app/ai/llm/conversation_manager.py` |
| Servicio de progreso | `app/services/user_progress_service.py` |

**Criterio de éxito:** Bot recuerda errores previos del usuario aunque se reinicie el servidor.

---

## Fase 3 — Audio de entrada (Speech-to-Text)

**Objetivo:** Usuario envía nota de voz → bot transcribe y responde.

```
Audio Telegram → Faster Whisper → texto → AI API → respuesta
```

| Tarea | Archivo |
|---|---|
| Preprocesador de audio | `app/ai/speech_to_text/audio_preprocessor.py` |
| Servicio Whisper | `app/ai/speech_to_text/whisper_service.py` |
| Handler de audios Telegram | `app/bot/handlers/audio_handler.py` |
| Servicio de speaking | `app/services/speaking_service.py` |
| Utilidades de audio | `app/utils/audio_utils.py` |
| Gestión de archivos temporales | `app/utils/file_manager.py` |

**Criterio de éxito:** Usuario envía nota de voz → bot transcribe y da feedback sobre el speaking.

---

## Fase 4 — Corrección y feedback

**Objetivo:** Bot analiza errores gramaticales y los explica en español.

| Tarea | Archivo |
|---|---|
| Corrector gramatical | `app/ai/correction/grammar_corrector.py` |
| Feedback de pronunciación | `app/ai/correction/pronunciation_feedback.py` |
| Ayuda de vocabulario | `app/ai/correction/vocabulary_helper.py` |
| Utilidades de texto | `app/utils/text_utils.py` |

**Criterio de éxito:** Bot detecta errores comunes de hispanohablantes y los explica con claridad.

---

## Fase 5 — Audio de salida (Text-to-Speech)

**Objetivo:** Bot responde también con audio pronunciando el inglés correcto.

```
Respuesta texto → TTS → audio → Telegram
```

| Tarea | Archivo | Opción |
|---|---|---|
| Servicio TTS | `app/ai/text_to_speech/piper_service.py` | Edge TTS (gratis, online) |
| Generador de voz | `app/ai/text_to_speech/voice_generator.py` | Piper (gratis, local) |

**Criterio de éxito:** Usuario recibe audio con pronunciación correcta de la frase corregida.

---

## Fase 6 — Funcionalidades avanzadas

**Objetivo:** Diccionario, traducción, vocabulario persistente, menús.

| Tarea | Archivo |
|---|---|
| Servicio de traducción | `app/services/translation_service.py` |
| Modelo de vocabulario | `app/database/models/vocabulary_model.py` |
| Repositorio de vocabulario | `app/database/repositories/vocabulary_repository.py` |
| Comandos avanzados | `app/bot/handlers/command_handler.py` |
| Menús y teclados Telegram | `app/bot/keyboards/menus.py` |

---

## Fase 7 — Pruebas y documentación

| Tarea | Archivo |
|---|---|
| Pruebas de IA | `app/tests/test_ai.py` |
| Pruebas de audio | `app/tests/test_audio.py` |
| Pruebas del bot | `app/tests/test_bot.py` |
| Flujo de API | `docs/api_flow.md` |
| Roadmap completo | `docs/roadmap.md` |

---

## Resumen de fases

| Fase | Nombre | Estado |
|---|---|---|
| 0 | Setup base | ✅ Completo |
| 1 | MVP texto + AI API | ✅ Completo |
| 2 | Memoria BD | Pendiente |
| 3 | STT (audios entrada) | Pendiente |
| 4 | Corrección y feedback | Pendiente |
| 5 | TTS (audio salida) | Pendiente |
| 6 | Features avanzadas | Pendiente |
| 7 | Pruebas | Pendiente |
