# Informe Técnico

1. Introducción
Este informe técnico presenta el desarrollo de un proyecto de software utilizando Git y GitHub como herramientas principales para la gestión de versiones. Durante el desarrollo se aplicaron buenas prácticas de gestión de código, el flujo de trabajo GitFlow, la automatización de procesos mediante CI/CD y la resolución de conflictos en el trabajo colaborativo.

2. Descripción del Proyecto
En esta sección se describe el problema seleccionado, los objetivos generales y específicos del proyecto, así como el alcance y las funcionalidades principales.

3. Uso de Git y GitHub
El proyecto fue gestionado mediante un repositorio en GitHub con la siguiente estructura inicial:
- /docs → Documentación del proyecto
- /src → Código fuente
- /tests → Pruebas automatizadas
- /.github → Workflows de CI/CD
- README.md → Descripción general del proyecto
- .gitignore → Exclusiones de archivos innecesarios
- LICENSE → Licencia del proyecto

4. Aplicación de GitFlow
Se implementó la estrategia de ramas GitFlow, asegurando un desarrollo ordenado:
- main → rama estable
- develop → rama de desarrollo
- feature/ → nuevas funcionalidades
- release/ → preparación de versiones
- hotfix/ → correcciones críticas

5. Gestión de Commits
Se utilizó una convención clara de mensajes de commit para garantizar legibilidad.

6. Automatización con CI/CD
Se configuraron workflows en GitHub Actions para ejecutar pruebas automáticas en cada push o pull request, asegurando la calidad del código y permitiendo despliegues automáticos.

7. Resolución de Conflictos
Los conflictos se resolvieron mediante revisiones de código en equipo y pruebas antes de la fusión.

8. Conclusiones
El uso de Git y GitHub permitió una gestión eficiente del proyecto. GitFlow facilitó la organización del trabajo en equipo, CI/CD garantizó la calidad del código y la resolución de conflictos promovió la colaboración efectiva.
