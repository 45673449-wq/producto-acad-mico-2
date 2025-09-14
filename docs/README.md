# 📌 Proyecto Académico - Gestión con Git y GitHub

Este proyecto académico demuestra el uso de **Git** y **GitHub** aplicando buenas prácticas de gestión de código, la estrategia **GitFlow**, automatización con **CI/CD** y resolución de conflictos en trabajo colaborativo.  

---

## 📂 Estructura del Repositorio

| Carpeta/Archivo | Descripción                          |
|-----------------|--------------------------------------|
| /docs           | Documentación del proyecto           |
| /src            | Código fuente                        |
| /tests          | Pruebas automatizadas                |
| /.github        | Workflows de CI/CD                   |
| README.md       | Descripción general del proyecto     |
| .gitignore      | Exclusiones de archivos innecesarios |
| LICENSE         | Licencia del proyecto                |

---

## 🚀 Flujo de Trabajo - GitFlow

- `main` → rama estable  
- `develop` → rama de desarrollo  
- `feature/` → nuevas funcionalidades  
- `release/` → preparación de versiones  
- `hotfix/` → correcciones críticas  

> **Ejemplo**: creación de una rama `feature`, desarrollo, *pull request* hacia `develop` y posterior integración en `main`.

---

## 📝 Convenciones de Commits

| Tipo     | Descripción                         | Ejemplo                                 |
|----------|-------------------------------------|-----------------------------------------|
| feat     | Nueva funcionalidad                 | `feat: agregar validación de usuario`    |
| fix      | Corrección de errores               | `fix: corregir bug en login`             |
| docs     | Cambios en documentación            | `docs: actualizar README`                |
| test     | Pruebas añadidas o corregidas       | `test: agregar prueba unitaria en login` |
| refactor | Reestructuración sin cambiar lógica | `refactor: optimizar función de búsqueda`|

---

## ⚙️ CI/CD con GitHub Actions

Se configuraron **workflows** que ejecutan pruebas automáticas en cada *push* o *pull request*, garantizando calidad del código y permitiendo despliegues continuos.

---

## ✅ Conclusiones

- Git y GitHub permitieron una **gestión eficiente** del proyecto.  
- GitFlow facilitó la **organización del trabajo en equipo**.  
- CI/CD aseguró la **calidad del código**.  
- La resolución de conflictos fomentó la **colaboración efectiva**.  

---

📖 Para más detalle, revisa la [documentación completa](./docs/informe.md).
