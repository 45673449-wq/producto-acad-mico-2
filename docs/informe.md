# Informe Técnico - Proyecto con Git y GitHub

## 1. Introducción
Este informe técnico presenta el desarrollo de un proyecto de software utilizando **Git** y **GitHub** como herramientas principales para la gestión de versiones.  
Durante el desarrollo se aplicaron buenas prácticas de gestión de código, el flujo de trabajo **GitFlow**, la automatización de procesos mediante **CI/CD** y la resolución de conflictos en el trabajo colaborativo.

---

## 2. Descripción del Proyecto
En esta sección se describe el problema seleccionado, los objetivos generales y específicos del proyecto, así como el alcance y las funcionalidades principales.

---

## 3. Uso de Git y GitHub
El proyecto fue gestionado mediante un repositorio en GitHub con la siguiente estructura inicial:

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

## 4. Aplicación de GitFlow
Se implementó la estrategia de ramas **GitFlow**, asegurando un desarrollo ordenado:

- `main` → rama estable  
- `develop` → rama de desarrollo  
- `feature/` → nuevas funcionalidades  
- `release/` → preparación de versiones  
- `hotfix/` → correcciones críticas  

Ejemplo de flujo: creación de una rama feature, desarrollo, *pull request* hacia `develop` y posterior integración en `main`.

> **Figura 1**: Ejemplo de flujo de GitFlow (inserte aquí un diagrama).

---

## 5. Gestión de Commits
Se utilizó una convención clara de mensajes de *commit* para garantizar legibilidad:

| Tipo     | Descripción                         | Ejemplo                                 |
|----------|-------------------------------------|-----------------------------------------|
| feat     | Nueva funcionalidad                 | `feat: agregar validación de usuario`    |
| fix      | Corrección de errores               | `fix: corregir bug en login`             |
| docs     | Cambios en documentación            | `docs: actualizar README`                |
| test     | Pruebas añadidas o corregidas       | `test: agregar prueba unitaria en login` |
| refactor | Reestructuración sin cambiar lógica | `refactor: optimizar función de búsqueda`|

---

## 6. Automatización con CI/CD
Se configuraron workflows en **GitHub Actions** para ejecutar pruebas automáticas en cada *push* o *pull request*, asegurando la calidad del código y permitiendo despliegues automáticos.

> **Figura 2**: Esquema de flujo CI/CD (inserte aquí un diagrama).

---

## 7. Resolución de Conflictos
Los conflictos se resolvieron mediante revisiones de código en equipo y pruebas antes de la fusión.  
Cuando se detectaron conflictos, estos fueron corregidos manualmente y validados con nuevos *commits*.

> **Figura 3**: Ejemplo de resolución de conflictos en GitHub (inserte captura de pantalla).

---

## 8. Conclusiones
El uso de Git y GitHub permitió una gestión eficiente del proyecto.  
**GitFlow** facilitó la organización del trabajo en equipo, **CI/CD** garantizó la calidad del código y la resolución de conflictos promovió la colaboración efectiva.  
Este proyecto sirvió para aplicar buenas prácticas de desarrollo de software.
