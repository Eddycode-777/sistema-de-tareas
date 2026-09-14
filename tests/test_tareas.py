"""
Tests — Sistema de Gestión de Tareas
Pruebas unitarias para las operaciones CRUD del modelo Tarea.
Usa un archivo de base de datos temporal para cada test.
"""

import pytest
import sys
import os
import tempfile

# Agregar la raíz del proyecto al path de Python
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import app.models.tarea as modelo_tarea
from app.models.tarea import Tarea, init_db


# ------------------------------------------------------------------
# Fixture: BD temporal aislada por test
# ------------------------------------------------------------------

@pytest.fixture(autouse=True)
def db_temporal(tmp_path):
    """
    Crea una base de datos SQLite temporal en un directorio aislado
    para cada test, garantizando que los tests no se interfieran.
    """
    db_file = str(tmp_path / "test_tareas.db")
    modelo_tarea.DB_PATH = db_file
    init_db()
    yield db_file
    # El directorio tmp_path se limpia automáticamente por pytest


# ------------------------------------------------------------------
# Tests de creación
# ------------------------------------------------------------------

class TestCrearTarea:

    def test_crear_tarea_exitosa(self):
        """Debe crear una tarea y retornar un ID válido."""
        tarea_id = Tarea.crear("Tarea de prueba", "Descripción de prueba")
        assert tarea_id is not None
        assert tarea_id > 0

    def test_crear_tarea_sin_descripcion(self):
        """Debe crear una tarea válida sin descripción."""
        tarea_id = Tarea.crear("Solo título")
        assert tarea_id is not None
        assert tarea_id > 0

    def test_tarea_creada_tiene_estado_pendiente(self):
        """Una tarea recién creada debe tener estado 'pendiente'."""
        tarea_id = Tarea.crear("Tarea nueva")
        tarea = Tarea.obtener(tarea_id)
        assert tarea.estado == "pendiente"

    def test_tarea_creada_tiene_fecha(self):
        """Una tarea creada debe tener fecha de creación."""
        tarea_id = Tarea.crear("Tarea con fecha")
        tarea = Tarea.obtener(tarea_id)
        assert tarea.fecha_creacion is not None
        assert len(tarea.fecha_creacion) > 0


# ------------------------------------------------------------------
# Tests de listado
# ------------------------------------------------------------------

class TestListarTareas:

    def test_listar_sin_tareas(self):
        """Debe retornar lista vacía cuando no hay tareas."""
        tareas = Tarea.listar()
        assert tareas == []

    def test_listar_con_tareas(self):
        """Debe retornar todas las tareas creadas."""
        Tarea.crear("Tarea 1")
        Tarea.crear("Tarea 2")
        Tarea.crear("Tarea 3")
        tareas = Tarea.listar()
        assert len(tareas) == 3

    def test_listar_retorna_objetos_tarea(self):
        """Cada elemento de la lista debe ser una instancia de Tarea."""
        Tarea.crear("Tarea de tipo")
        tareas = Tarea.listar()
        assert all(isinstance(t, Tarea) for t in tareas)


# ------------------------------------------------------------------
# Tests de obtención
# ------------------------------------------------------------------

class TestObtenerTarea:

    def test_obtener_tarea_existente(self):
        """Debe retornar la tarea correcta por ID."""
        tarea_id = Tarea.crear("Tarea específica", "Mi descripción")
        tarea = Tarea.obtener(tarea_id)
        assert tarea is not None
        assert tarea.titulo == "Tarea específica"
        assert tarea.descripcion == "Mi descripción"

    def test_obtener_tarea_inexistente(self):
        """Debe retornar None para un ID que no existe."""
        tarea = Tarea.obtener(99999)
        assert tarea is None


# ------------------------------------------------------------------
# Tests de actualización
# ------------------------------------------------------------------

class TestActualizarTarea:

    def test_actualizar_titulo(self):
        """Debe actualizar el título de la tarea correctamente."""
        tarea_id = Tarea.crear("Título original")
        resultado = Tarea.actualizar(tarea_id, "Título nuevo", "")
        assert resultado is True
        tarea = Tarea.obtener(tarea_id)
        assert tarea.titulo == "Título nuevo"

    def test_actualizar_descripcion(self):
        """Debe actualizar la descripción de la tarea."""
        tarea_id = Tarea.crear("Mi tarea", "Descripción original")
        Tarea.actualizar(tarea_id, "Mi tarea", "Nueva descripción")
        tarea = Tarea.obtener(tarea_id)
        assert tarea.descripcion == "Nueva descripción"

    def test_actualizar_tarea_inexistente(self):
        """Debe retornar False al intentar actualizar una tarea que no existe."""
        resultado = Tarea.actualizar(99999, "Título", "Descripción")
        assert resultado is False


# ------------------------------------------------------------------
# Tests de eliminación
# ------------------------------------------------------------------

class TestEliminarTarea:

    def test_eliminar_tarea_existente(self):
        """Debe eliminar la tarea y retornar True."""
        tarea_id = Tarea.crear("Tarea a eliminar")
        resultado = Tarea.eliminar(tarea_id)
        assert resultado is True
        assert Tarea.obtener(tarea_id) is None

    def test_eliminar_tarea_inexistente(self):
        """Debe retornar False al eliminar una tarea que no existe."""
        resultado = Tarea.eliminar(99999)
        assert resultado is False

    def test_eliminar_reduce_lista(self):
        """Después de eliminar, la lista debe tener un elemento menos."""
        Tarea.crear("Tarea 1")
        id2 = Tarea.crear("Tarea 2")
        Tarea.crear("Tarea 3")
        Tarea.eliminar(id2)
        tareas = Tarea.listar()
        assert len(tareas) == 2


# ------------------------------------------------------------------
# Tests de cambio de estado
# ------------------------------------------------------------------

class TestCambiarEstado:

    def test_completar_tarea_pendiente(self):
        """Debe cambiar el estado de pendiente a completada."""
        tarea_id = Tarea.crear("Tarea para completar")
        Tarea.cambiar_estado(tarea_id)
        tarea = Tarea.obtener(tarea_id)
        assert tarea.estado == "completada"

    def test_reabrir_tarea_completada(self):
        """Debe cambiar el estado de completada a pendiente."""
        tarea_id = Tarea.crear("Tarea para reabrir")
        Tarea.cambiar_estado(tarea_id)  # pendiente → completada
        Tarea.cambiar_estado(tarea_id)  # completada → pendiente
        tarea = Tarea.obtener(tarea_id)
        assert tarea.estado == "pendiente"

    def test_cambiar_estado_tarea_inexistente(self):
        """Debe retornar False para una tarea que no existe."""
        resultado = Tarea.cambiar_estado(99999)
        assert resultado is False
