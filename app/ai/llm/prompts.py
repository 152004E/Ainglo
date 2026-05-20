from app.config.prompts import SYSTEM_PROMPT, CORRECTION_PROMPT, TRANSLATION_PROMPT


def build_system_message() -> dict:
    return {"role": "system", "content": SYSTEM_PROMPT}


def build_correction_message(text: str) -> dict:
    return {"role": "user", "content": CORRECTION_PROMPT.format(text=text)}


def build_translation_message(text: str, target_language: str) -> dict:
    return {
        "role": "user",
        "content": TRANSLATION_PROMPT.format(text=text, target_language=target_language),
    }
