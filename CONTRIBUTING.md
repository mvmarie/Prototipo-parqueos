# Contribuir

## Estilo y criterios de evaluación del curso
- No usar `global`, `while True`, `if __name__ == "__main__"` innecesario.
- No usar `print()` ni `input()` dentro de funciones (solo en el bloque principal).
- Usar **listas** y **CSV** (evitar diccionarios).
- Nombres de variables y funciones **descriptivos**.
- Comentarios **no redundantes**; preferir docstrings breves.

## Flujo de trabajo con Git
1. Crear rama: `git checkout -b feat/nombre-corto`
2. Commits atómicos y claros (imperativo):
   - `feat: agregar persistencia CSV`
   - `refactor: extraer formateo de tabla`
   - `fix: validar índice de parqueo`
3. Pull Request con breve descripción del cambio y evidencia (captura/GIF).
