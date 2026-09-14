"""
App Factory — Sistema de Gestión de Tareas
Inicializa la aplicación Flask, registra blueprints y prepara la base de datos.
"""

import os
from flask import Flask
from app.models.tarea import init_db


def create_app():
    """Crea y configura la instancia de la aplicación Flask."""
    app = Flask(
        __name__,
        template_folder="views",
        static_folder="static"
    )

    # Clave secreta para las sesiones y flash messages
    app.secret_key = os.environ.get("SECRET_KEY", "clave-secreta-dev-2024")

    # Crear el directorio de la base de datos si no existe
    os.makedirs("database", exist_ok=True)

    # Inicializar la base de datos
    init_db()

    # Registrar blueprints
    from app.controllers.tarea_controller import tareas_bp
    app.register_blueprint(tareas_bp)

    return app
