# Portfolio y Blog en Django

Este proyecto es un completo portfolio personal desarrollado en Django que integra un sistema de blogging. El objetivo principal es mostrar mis habilidades, proyectos y experiencia, además de proporcionar un espacio para compartir publicaciones y artículos relacionados con mi campo de interés.

## Tabla de Contenidos
- [Descripción](#descripción)
- [Características principales](#características-principales)
  - [Página de inicio](#página-de-inicio)
  - [Sección de Proyectos](#sección-de-proyectos)
  - [Blog](#blog)
- [Requisitos del sistema](#requisitos-del-sistema)
- [Instalación y configuración](#instalación-y-configuración)
- [Personalización](#personalización)
- [Capturas de Pantalla](#capturas-de-pantalla)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Contacto](#contacto)
- [Créditos](#créditos)

## Descripción

Este es un portafolio personal dinámico desarrollado con **Django 4.2** y **Bootstrap 5**, utilizando **Python 3.10.12**. El sitio incluye las siguientes páginas:

- **Inicio**: Una introducción breve y atractiva.
- **Blog**: Información sobre ti y tu experiencia.

## Características principales

### Página de inicio:

- Breve presentación y descripción personal.
- Enlaces a secciones clave del portfolio.

### Sección de Proyectos:

- Lista de proyectos destacados con imágenes, descripciones y enlaces.
- Filtrado y categorización de proyectos para una fácil navegación.

### Blog:

- Publicaciones
- Funcionalidad de interacción para los lectores.

## Requisitos del sistema

- Python 3.10.12
- Django 4.2

## Instalación y configuración

1. Clona el repositorio a tu máquina local:

   ```bash
   git clone https://github.com/tu_usuario/tu_portfolio.git

2. Accede al directorio del proyecto

   ```bash
   cd tu_portfolio
   ```

3. Crea un entorno virtual (se recomienda el uso de virtualenv):
   ```bash
   virtualenv venv
   ```

4. Activa el entorno virtual:

   En Windows:

      ```bash
      .\venv\Scripts\activate
      ```

   En macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

5. Instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```

6. Aplica las migraciones:
   ```bash
   python manage.py migrate
   ```

7. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

El sitio estará disponible en http://localhost:8000/.

## Personalización

- Actualiza el archivo `portfolio/settings.py` con tu configuración personal.
- Modifica los archivos HTML, CSS y JavaScript en la carpeta `templates` según tus preferencias de diseño.
- Agrega tu información personal en las vistas y modelos correspondientes.
- Personaliza la sección de blog y portfolio mediante la administración de Django.

## Capturas de Pantalla

- **Inicio**
- **Blog**

## Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras errores o tienes ideas para mejorar el portfolio o el blog, no dudes en crear un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.

## Contacto

- **Correo Electrónico**: alucase@gmail.com
- **LinkedIn**: [Lucas Acosta](https://www.linkedin.com/in/alucase/)
- **GitHub**: [ALucasE](https://github.com/ALucasE)
- **Web**: [alucase.github.io/](https://alucase.github.io/)

## Créditos

- **Bootstrap**: [Bootstrap 5](https://getbootstrap.com/)
- **Django**: [Django 4.2](https://www.djangoproject.com/)

Espero que encuentres útil este proyecto de portfolio con blog desarrollado en Django. ¡Buena suerte con tu presentación en línea y tus publicaciones!
