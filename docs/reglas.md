# Reglas del Proyecto Ainglo

## 1. Consulta obligatoria de documentación

Antes de crear, modificar o proponer cualquier funcionalidad, siempre se deben revisar los siguientes archivos:

- `README.md`
- `architecture.md`

Objetivo:

- comprender la visión del proyecto,
- respetar la arquitectura definida,
- mantener consistencia en nombres y carpetas,
- evitar código duplicado,
- y seguir la filosofía del sistema.

---

## 2. Respetar la arquitectura del proyecto

Toda nueva funcionalidad debe seguir la estructura modular definida en `Estructura.md`.

Reglas importantes:

- No mezclar lógica de negocio dentro de handlers.
- Los handlers solo deben recibir y responder solicitudes.
- La lógica debe ir en `services/`.
- La comunicación con IA debe ir en `ai/`.
- El acceso a datos debe ir en `database/repositories/`.
- Las utilidades reutilizables deben ir en `utils/`.

Arquitectura esperada:

```text
Handler → Service → AI/Database → Response
```

---

## 3. No modificar estructura sin autorización

No se deben:

- crear carpetas innecesarias,
- mover archivos,
- cambiar nombres importantes,
- ni alterar la arquitectura base

sin autorización previa.

---

## 4. Código limpio y escalable

Todo el código debe seguir estas reglas:

- funciones pequeñas y claras,
- nombres descriptivos,
- separación de responsabilidades,
- evitar lógica duplicada,
- evitar código innecesario,
- comentar únicamente cuando sea necesario.

---

## 5. Desarrollo incremental

Las funcionalidades deben desarrollarse por etapas pequeñas y funcionales.

Prioridad:

1. funcionalidad mínima,
2. pruebas,
3. refactorización,
4. mejoras.

Nunca intentar construir todo el sistema de una sola vez.

---

## 6. Priorizar MVP funcional

Antes de implementar características avanzadas, primero debe existir un flujo funcional mínimo.

Ejemplo:

```
Telegram → Mensaje → IA → Respuesta
```

Luego se agregan:

- memoria,
- audios,
- pronunciación,
- métricas,
- personalización.

---

## 7. No subir archivos a GitHub automáticamente

El asistente NO debe:

- hacer commits,
- generar comandos git automáticos,
- subir archivos,
- ni asumir despliegues.

Toda la gestión de Git y GitHub será realizada manualmente por el propietario del proyecto.

---

## 8. Mantener enfoque en bajo costo y APIs cloud

Las soluciones propuestas deben priorizar:

- APIs gratuitas o freemium,
- proveedores cloud en lugar de ejecución local pesada,
- bajo consumo de recursos locales,
- arquitectura modular para cambiar de proveedor fácilmente,
- y facilidad de escalabilidad futura.

Queda excluido el uso de:
- inferencia local con modelos LLM,
- pipelines que dependan de GPU potente,
- descarga y ejecución de modelos de lenguaje locales (Ollama, etc.).

---

## 9. Pensar primero en hispanohablantes

Las funcionalidades de aprendizaje deben enfocarse especialmente en usuarios hispanohablantes aprendiendo inglés.

Prioridades:

- corrección de pronunciación latina,
- errores comunes en speaking,
- explicaciones claras,
- aprendizaje conversacional natural.

---

## 10. Documentar decisiones importantes

Toda decisión importante de arquitectura, flujo o tecnología debe quedar documentada en:

- `README.md`
- `docs/`
- o archivos técnicos relacionados.
