"""
Controller: TareaController
Responsable: Gestiona las rutas HTTP y coordina operaciones con el modelo Tarea.
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.tarea import Tarea

tareas_bp = Blueprint("tareas", __name__)


# ------------------------------------------------------------------
# Listado de tareas
# ------------------------------------------------------------------

@tareas_bp.route("/")
def lista():
    """Muestra la lista de todas las tareas."""
    tareas = Tarea.listar()
    return render_template("tareas/lista.html", tareas=tareas)


# ------------------------------------------------------------------
# Crear tarea
# ------------------------------------------------------------------

@tareas_bp.route("/crear", methods=["GET", "POST"])
def crear():
    """Muestra el formulario de creación y procesa la nueva tarea."""
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descripcion = request.form.get("descripcion", "").strip()

        if not titulo:
            flash("El título es obligatorio.", "error")
            return render_template("tareas/crear.html", titulo=titulo, descripcion=descripcion)

        if len(titulo) > 120:
            flash("El título no puede superar los 120 caracteres.", "error")
            return render_template("tareas/crear.html", titulo=titulo, descripcion=descripcion)

        Tarea.crear(titulo, descripcion)
        flash(f"Tarea '{titulo}' creada exitosamente.", "success")
        return redirect(url_for("tareas.lista"))

    return render_template("tareas/crear.html", titulo="", descripcion="")


# ------------------------------------------------------------------
# Detalle de tarea
# ------------------------------------------------------------------

@tareas_bp.route("/detalle/<int:tarea_id>")
def detalle(tarea_id):
    """Muestra el detalle de una tarea específica."""
    tarea = Tarea.obtener(tarea_id)
    if not tarea:
        flash("Tarea no encontrada.", "error")
        return redirect(url_for("tareas.lista"))
    return render_template("tareas/detalle.html", tarea=tarea)


# ------------------------------------------------------------------
# Editar tarea
# ------------------------------------------------------------------

@tareas_bp.route("/editar/<int:tarea_id>", methods=["GET", "POST"])
def editar(tarea_id):
    """Muestra el formulario de edición y procesa los cambios."""
    tarea = Tarea.obtener(tarea_id)
    if not tarea:
        flash("Tarea no encontrada.", "error")
        return redirect(url_for("tareas.lista"))

    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descripcion = request.form.get("descripcion", "").strip()

        if not titulo:
            flash("El título es obligatorio.", "error")
            return render_template("tareas/editar.html", tarea=tarea)

        if len(titulo) > 120:
            flash("El título no puede superar los 120 caracteres.", "error")
            return render_template("tareas/editar.html", tarea=tarea)

        Tarea.actualizar(tarea_id, titulo, descripcion)
        flash(f"Tarea '{titulo}' actualizada correctamente.", "success")
        return redirect(url_for("tareas.detalle", tarea_id=tarea_id))

    return render_template("tareas/editar.html", tarea=tarea)


# ------------------------------------------------------------------
# Eliminar tarea
# ------------------------------------------------------------------

@tareas_bp.route("/eliminar/<int:tarea_id>", methods=["POST"])
def eliminar(tarea_id):
    """Elimina una tarea de la base de datos."""
    tarea = Tarea.obtener(tarea_id)
    if not tarea:
        flash("Tarea no encontrada.", "error")
        return redirect(url_for("tareas.lista"))

    Tarea.eliminar(tarea_id)
    flash(f"Tarea '{tarea.titulo}' eliminada.", "info")
    return redirect(url_for("tareas.lista"))


# ------------------------------------------------------------------
# Cambiar estado (completar / reabrir)
# ------------------------------------------------------------------

@tareas_bp.route("/completar/<int:tarea_id>", methods=["POST"])
def completar(tarea_id):
    """Alterna el estado de la tarea entre pendiente y completada."""
    tarea = Tarea.obtener(tarea_id)
    if not tarea:
        flash("Tarea no encontrada.", "error")
        return redirect(url_for("tareas.lista"))

    Tarea.cambiar_estado(tarea_id)
    nuevo_estado = "completada" if tarea.estado == "pendiente" else "pendiente"
    flash(f"Tarea marcada como '{nuevo_estado}'.", "success")
    return redirect(url_for("tareas.lista"))
