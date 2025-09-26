# decisiones.md

## Identidad y configuración
- `user.name`: "tomllenovich jeremias"
- `user.email`: "2107117@ucc.edu.ar"
- Scope: local del repo (no global) para separar proyectos.
- Remotos:
  - origin: fork propio


## Funcionalidad desarrollada
- Rama: `feature/contador-lineas`
- Descripción: script `tools/line_counter.py` que cuenta líneas del repo.
- Commits:
  - `<SHA1>` feat(tools): script para contar líneas del repositorio
  - `<SHA2>` docs(readme): instrucciones de uso para contador de líneas
- Justificación de commits atómicos: separar código y documentación mejora revertibilidad y revisión.

## Error simulado y hotfix
- Error simulado en `main`: comando incorrecto en README (`python` en lugar de `python3`).
- Rama de fix: `hotfix/fix-readme-python3`
- Commit de fix: `<SHA_FIX>` fix(readme): corregir comando de ejecución a python3
- Integración elegida:
  - A `main`: **PR + merge commit** (trazabilidad del hotfix).
  - A mi rama de desarrollo: **cherry-pick** de `<SHA_FIX>` para traer solo el fix.
- Motivo: cherry-pick evita traer cambios no relacionados de `main`.

## Versionado
- Tag creado: `v1.0`
- Convención: SemVer. Se usa `1.0` al ser la primera versión estable de la funcionalidad.

## Problemas y resolución
- Ej: conflicto al hacer cherry-pick en `README.md`.  
  Resolución: resolver manualmente, `git add .`, `git cherry-pick --continue`.

## Calidad y trazabilidad en un equipo real
- PRs obligatorios con revisión por pares.
- Commits con convención y *scope*.
- Issues enlazados a PRs (closes #X).
- CI: lint + tests (GitHub Actions).
- Protecciones en `main`: PRs requeridos, status checks, branch protection.
- CODEOWNERS para rutas críticas.
- Releases con changelog y tags firmados (opcional GPG).


git rebase reaplica commits de una rama sobre otra.
Básicamente “cambia la base” de tu rama, como si hubieras empezado a desarrollarla desde el último commit de la otra rama.

Ventajas:

Historia lineal y clara.

Facilita lectura y seguimiento de cambios.

Desventajas:

Reescribe commits, por eso no se recomienda usarlo en ramas compartidas ya pusheadas, porque puede generar conflictos con otros colaboradores.
¿Lo usé en este TP?

No lo usé, porque:

Mi estrategia fue feature branch + hotfix.

Preferí merge o cherry-pick, que son más seguros y trazables para un TP donde cada commit debe ser visible.

Con rebase hubiera reescrito la historia de los commits, y en un entorno real con PRs y revisiones eso puede complicar la trazabilidad.

¿Cómo revertís un commit ya push?

Si ya pusheaste un commit a main o cualquier rama compartida, hay dos opciones:

Opción segura: git revert

Crea un nuevo commit que deshace los cambios del commit anterior, sin alterar la historia.

rebase → reescribe la historia de tu rama sobre otra, útil para historia limpia.

En este TP no se usó, usamos merge y cherry-pick para mantener trazabilidad.

Para revertir commits pusheados, revert es seguro; reset --hard + push force es peligroso en ramas compartidas.