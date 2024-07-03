PREYECTO REPEKES

Proyecto final del curso de Python de Coderhouse.

Descripción
Este proyecto consiste en una aplicación web desarrollada con Python y Django que gestiona una base de datos de productos y categorías.
La misma tiene por obejtivo la venta de productos para niños pero bajo la metodología de moda CIRCULAR. En el footer se inlcuyeron enlaces funcionales de temas de interes para padres tales como JUEGOS, RECETAS, ETC

Estructura del Proyecto

    RePekes/: Directorio principal del proyecto Django.
    categorias_produc/: Directorio de la aplicación que maneja las categorías de los productos.
    manage.py: Script para interactuar con el proyecto Django.
    repekes.db: Base de datos SQLite del proyecto.

Instalación

    Clona el repositorio:
          git clone https://github.com/MF-Diez/preyectoRepekes.git

Navega al directorio del proyecto:
          cd preyectoRepekes

Instala las dependencias:
          pip install -r requirements.txt
          
Realiza las migraciones:
          python manage.py migrate

Uso
Para iniciar el servidor de desarrollo, ejecuta:
          python manage.py runserver
Luego, abre tu navegador y visita http://127.0.0.1:8000/ para interactuar con la aplicación.




    
