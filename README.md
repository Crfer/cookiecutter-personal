# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Configuración](#configuración)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Requisitos

- [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
- [git](https://git-scm.com/)

## Instalación

Sigue estos pasos para generar y configurar tu proyecto usando esta plantilla:

1. **Clonar el repositorio de Cookiecutter:**

    ```sh
    cookiecutter https://github.com/Crfer/cookiecutter-plantilla.git
    ```

2. **Navegar al directorio del proyecto:**

    ```sh
    cd {{ cookiecutter.project_slug }}
    ```

3. **Inicializar Git (esto se realiza automáticamente):**

    ```sh
    git init
    git add .
    git commit -m "Initial commit"
    ```

4. **Crear el entorno conda:**

    ```sh
    conda env create --file environment.yml
    ```

5. **Activar el entorno conda:**

    En Windows:
    ```sh
    conda activate {{ cookiecutter.project_slug }}_env
    ```

    En macOS/Linux:
    ```sh
    source activate {{ cookiecutter.project_slug }}_env
    ``

## Uso

Después de la configuración inicial, puedes comenzar a trabajar en tu proyecto. Aquí hay algunos comandos útiles:

- **Activar el entorno conda:**

    En Windows:
    ```sh
    conda activate {{ cookiecutter.project_slug }}_env
    ```

    En macOS/Linux:
    ```sh
    source activate {{ cookiecutter.project_slug }}_env
    ```

- **Ejecutar Jupyter Notebook/Lab (si está instalado):**

    ```sh
    jupyter lab
    ```

- **Realizar un commit con pre-commit hooks:**

    ```sh
    git add .
    git commit -m "Tu mensaje de commit"
    ```

## Configuración

### Personalización del Proyecto

Para personalizar tu proyecto, edita los siguientes archivos:

- `cookiecutter.json`: Define las variables y opciones para la generación del proyecto.

- `environment.yml`: Lista las dependencias del entorno conda.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue estos pasos para contribuir:

1. Realiza un fork del proyecto.
2. Crea una nueva rama para tu funcionalidad (`git checkout -b feature/tu-funcionalidad`).
3. Realiza un commit de tus cambios (`git commit -am 'Añade tu funcionalidad'`).
4. Empuja la rama (`git push origin feature/tu-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).
