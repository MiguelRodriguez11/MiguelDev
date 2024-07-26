"""
Este modulo configura las rutas.
"""

from enum import Enum


class Route(Enum):
    """
    Enum para definir las rutas de la aplicación.

    Attributes:
        INDEX (str): Ruta para la página principal.
        COURSES (str): Ruta para la página de cursos.
    """
    INDEX = "/"
    COURSES = "/cursos"
