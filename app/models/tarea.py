"""
Model: Tarea
Responsable: Gestiona la entidad Tarea y la persistencia en SQLite.
"""

import sqlite3
from datetime import datetime

DB_PATH = "database/tareas.db"


def get_connection():
    """Retorna una conexión a la base de datos SQLite."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Inicializa la base de datos creando la tabla tareas si no existe."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            estado TEXT NOT NULL DEFAULT 'pendiente',
            fecha_creacion TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


class Tarea:
    """Representa la entidad Tarea y encapsula las operaciones de datos."""

    def __init__(self, id=None, titulo="", descripcion="",
                 estado="pendiente", fecha_creacion=None):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
        self.fecha_creacion = fecha_creacion or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ------------------------------------------------------------------
    # Operaciones CRUD
    # ------------------------------------------------------------------

    @staticmethod
    def crear(titulo, descripcion=""):
        """Inserta una nueva tarea en la base de datos."""
        conn = get_connection()
        cursor = conn.cursor()
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO tareas (titulo, descripcion, estado, fecha_creacion) VALUES (?, ?, ?, ?)",
            (titulo, descripcion, "pendiente", fecha)
        )
        conn.commit()
        tarea_id = cursor.lastrowid
        conn.close()
        return tarea_id

    @staticmethod
    def listar():
        """Retorna todas las tareas ordenadas por fecha de creación descendente."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tareas ORDER BY fecha_creacion DESC, id DESC")
        filas = cursor.fetchall()
        conn.close()
        return [Tarea._from_row(fila) for fila in filas]

    @staticmethod
    def obtener(tarea_id):
        """Retorna una tarea por su ID, o None si no existe."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tareas WHERE id = ?", (tarea_id,))
        fila = cursor.fetchone()
        conn.close()
        if fila:
            return Tarea._from_row(fila)
        return None

    @staticmethod
    def actualizar(tarea_id, titulo, descripcion):
        """Actualiza el título y la descripción de una tarea existente."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tareas SET titulo = ?, descripcion = ? WHERE id = ?",
            (titulo, descripcion, tarea_id)
        )
        conn.commit()
        filas_afectadas = cursor.rowcount
        conn.close()
        return filas_afectadas > 0

    @staticmethod
    def eliminar(tarea_id):
        """Elimina una tarea de la base de datos por su ID."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tareas WHERE id = ?", (tarea_id,))
        conn.commit()
        filas_afectadas = cursor.rowcount
        conn.close()
        return filas_afectadas > 0

    @staticmethod
    def cambiar_estado(tarea_id):
        """Alterna el estado de una tarea entre 'pendiente' y 'completada'."""
        tarea = Tarea.obtener(tarea_id)
        if not tarea:
            return False
        nuevo_estado = "completada" if tarea.estado == "pendiente" else "pendiente"
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tareas SET estado = ? WHERE id = ?",
            (nuevo_estado, tarea_id)
        )
        conn.commit()
        conn.close()
        return True

    # ------------------------------------------------------------------
    # Métodos auxiliares
    # ------------------------------------------------------------------

    @staticmethod
    def _from_row(row):
        """Convierte una fila de SQLite en un objeto Tarea."""
        return Tarea(
            id=row["id"],
            titulo=row["titulo"],
            descripcion=row["descripcion"],
            estado=row["estado"],
            fecha_creacion=row["fecha_creacion"]
        )

    def __repr__(self):
        return f"<Tarea id={self.id} titulo='{self.titulo}' estado='{self.estado}'>"
