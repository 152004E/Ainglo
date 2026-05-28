# Guía de instalación — Ainglo

## Requisitos del sistema

- Python 3.10 o superior
- `pip` y `venv`
- FFmpeg (para procesar audios)
- Git

### Instalar FFmpeg

```bash
# Ubuntu / Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows (con scoop)
scoop install ffmpeg
# o descargar desde https://ffmpeg.org/download.html
```

---

## Instalación paso a paso

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/ainglo.git
cd ainglo
```

### 2. Crear entorno virtual

```bash
python3 -m venv .venv
```

### 3. Activar el entorno

```bash
# Linux / macOS
source .venv/bin/activate

# Windows (cmd)
.venv\Scripts\activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

Deberías ver `(.venv)` al inicio del prompt.

### 4. Instalar dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Configurar variables de entorno

Crear archivo `.env` en la raíz del proyecto:

```ini
TELEGRAM_TOKEN=tu_token_aqui
AI_PROVIDER=gemini
AI_MODEL=gemini-2.0-flash-lite
GEMINI_API_KEY=tu_api_key_aqui
GROQ_API_KEY=
DB_PATH=data/database/ainglo.db
TEMP_AUDIO_DIR=data/temp
AUDIO_DIR=data/audios
```

> `AI_PROVIDER` puede ser `gemini` o `groq`.  
> `AI_MODEL` déjalo vacío para usar el modelo por defecto del proveedor.

### 6. Obtener API Keys

| Servicio | Cómo obtenerla |
|----------|---------------|
| **Telegram Token** | Hablar con [@BotFather](https://t.me/BotFather) en Telegram |
| **Gemini API Key** | [Google AI Studio](https://aistudio.google.com/) — gratis |
| **Groq API Key** | [Groq Console](https://console.groq.com/) — gratis |

### 7. Ejecutar el bot

```bash
python run.py
```

Si todo funciona, verás algo como:

```
Ainglo iniciado correctamente
```

---

## Dependencias del proyecto

| Paquete | Propósito |
|---------|-----------|
| `python-telegram-bot` | Bot de Telegram |
| `google-genai` | Cliente Gemini API |
| `groq` | Cliente Groq API |
| `python-dotenv` | Cargar `.env` |
| `sqlalchemy` | ORM para SQLite |
| `pydub` | Manipulación de audios |
| `ffmpeg-python` | Procesar audios con FFmpeg |
| `faster-whisper` | Transcripción de voz a texto |

> Nota: `faster-whisper` descarga un modelo pequeño (~1.5 GB) la primera vez que se usa. Es la única dependencia local y es ligera.

---

## Script rápido para Linux / macOS

```bash
#!/bin/bash
git clone https://github.com/tu-usuario/ainglo.git
cd ainglo
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "Crea tu archivo .env y luego ejecuta: python run.py"
```

---

## Notas importantes

- El `.env` contiene claves de API **no se debe subir a Git** (ya está en `.gitignore`).
- La base de datos SQLite se crea automáticamente al ejecutar el bot.
- Los audios temporales se guardan en `data/temp/` y se limpian automáticamente.
- Para desactivar el entorno virtual: `deactivate`.
- Para actualizar dependencias: `pip install -r requirements.txt --upgrade`.

---

## Solución de problemas

| Problema | Causa probable | Solución |
|----------|---------------|----------|
| `ModuleNotFoundError` | No activaste el venv | `source .venv/bin/activate` |
| `TELEGRAM_TOKEN no configurado` | Falta `.env` | Crear `.env` con el token |
| `ffmpeg not found` | FFmpeg no instalado | `sudo apt install ffmpeg` |
| Error de Whisper | Modelo no descargado | Ejecutar una vez, se descarga solo |
