# Blackjack (proyecto intencionalmente malo) 🃏

**Objetivo:** Proyecto **funcional** de Blackjack en Python, pero escrito **a propósito** con múltiples **malas prácticas** para ser analizadas por **SonarQube** (Security, Reliability, Maintainability, Hotspots, Coverage, Duplications).

> ⚠️ **Advertencia**: Este repositorio contiene *code smells*, *bugs potenciales*, *security hotspots* y decisiones cuestionables a propósito. **No uses este código como base real de producción.**

## Requisitos

- Python 3.10+ (se usa `match/case`)

## Instalación

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

pip install -r requirements.txt
```

## Ejecutar el juego

```bash
python run.py
```

## Ejecutar tests (malos / incompletos a propósito)

```bash
pytest -q
```

## Generar cobertura (para SonarQube)

```bash
pytest --maxfail=1 --disable-warnings --cov=blackjack --cov-report=xml:coverage.xml
```

## Análisis SonarQube (local)

1) Asegúrate de tener SonarQube corriendo (ej. Docker) y un token.

2) Ejecuta (ejemplo genérico):

```bash
sonar-scanner       -Dsonar.host.url=http://localhost:9000       -Dsonar.token=TU_TOKEN
```

El archivo `sonar-project.properties` ya viene incluido.

## Qué está "mal" (intencional)

- Complejidad cognitiva alta
- Métodos largos
- Código duplicado
- Variables con nombres malos (`x`, `tmp`, `data2`, `A`, `test123`)
- Imports sin uso
- Parámetros sin uso
- Manejo de excepciones incorrecto (try/except vacíos)
- Logs excesivos
- Valores hardcodeados, números mágicos
- Mezcla de responsabilidades
- Inconsistencia en nombres (camelCase, PascalCase, snake_case)
- Comentarios inútiles, TODOs, FIXMEs
- Y más…

## Estructura

```
blackjack_bad/
  run.py
  sonar-project.properties
  requirements.txt
  blackjack/
    app.py
    config/
    controllers/
    services/
    models/
    utils/
  tests/
```

---

Hecho para practicar revisiones y auditorías con SonarQube.
