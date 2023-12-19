# Portfolio y Blog en Django

Este proyecto es un completo portfolio personal desarrollado en Django que integra un sistema de blogging. El objetivo principal es mostrar mis habilidades, proyectos y experiencia, además de proporcionar un espacio para compartir publicaciones y artículos relacionados con mi campo de interés.

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

- Python 3.12
- Django (se recomienda la versión 5.0)

## Instalación y configuración

1. Clona el repositorio a tu máquina local:

   ```bash
   git clone https://github.com/tu_usuario/tu_portfolio.git
   ```

2. Accede al directorio del proyecto:

   ```bash
   cd tu_portfolio
   ```

3. Crea un entorno virtual (se recomienda el uso de `virtualenv`):

   ```bash
   virtualenv venv
   ```

4. Activa el entorno virtual:

   - En Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - En macOS/Linux:

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

7. Carga datos iniciales (opcional):

   ```bash
   python manage.py loaddata initial_data
   ```

8. Inicia el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

   El sitio estará disponible en [http://localhost:8000/](http://localhost:8000/).

## Personalización

- Actualiza el archivo `portfolio/settings.py` con tu configuración personal.
- Modifica los archivos HTML, CSS y JavaScript en la carpeta `templates` según tus preferencias de diseño.
- Agrega tu información personal en las vistas y modelos correspondientes.
- Personaliza la sección de blog y portfolio mediante la administración de Django.

## Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras errores o tienes ideas para mejorar el portfolio o el blog, no dudes en crear un _pull request_.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.

---

Espero que encuentres útil este proyecto de portfolio con blog desarrollado en Django. ¡Buena suerte con tu presentación en línea y tus publicaciones!