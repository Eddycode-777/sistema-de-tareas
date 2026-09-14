# Sistema Web de Gestión de Tareas

Aplicación web desarrollada con Python y Flask que permite administrar tareas personales mediante operaciones CRUD. Proyecto de demostración para la aplicación de un Plan de Gestión de Configuración de Software (SCMP) basado en IEEE 828.

## Tecnologías

- **Python 3** — lenguaje principal
- **Flask** — framework web
- **SQLite** — base de datos embebida
- **Jinja2** — motor de plantillas HTML
- **pytest** — pruebas unitarias

## Arquitectura

El proyecto sigue el patrón **MVC (Modelo-Vista-Controlador)**:

| Capa | Archivo | Responsabilidad |
|------|---------|----------------|
| Modelo | `app/models/tarea.py` | Entidad Tarea y acceso a SQLite |
| Controlador | `app/controllers/tarea_controller.py` | Rutas HTTP y lógica de negocio |
| Vista | `app/views/tareas/*.html` | Plantillas Jinja2 |

## Estructura del proyecto

```
sistema-tareas/
├── app/
│   ├── __init__.py             # App Factory
│   ├── models/
│   │   └── tarea.py            # Modelo Tarea + acceso a BD
│   ├── controllers/
│   │   └── tarea_controller.py # Blueprint con rutas HTTP
│   ├── views/
│   │   ├── base.html           # Plantilla base
│   │   └── tareas/
│   │       ├── lista.html      # Lista de tareas
│   │       ├── crear.html      # Formulario de creación
│   │       ├── editar.html     # Formulario de edición
│   │       └── detalle.html    # Vista de detalle
│   └── static/
│       └── css/
│           └── style.css       # Estilos CSS
├── database/
│   └── tareas.db               # BD SQLite (generada al ejecutar)
├── tests/
│   └── test_tareas.py          # Suite de pruebas
├── run.py                      # Punto de entrada
├── requirements.txt            # Dependencias
├── plan_configuracion.md       # SCMP IEEE 828
└── historial_cambios.txt       # Registro de cambios
```

## Instalación y ejecución

### Prerrequisitos

- Python 3.8 o superior instalado
- Git instalado

### Pasos

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/<usuario>/configuracion-equipoX.git
   cd configuracion-equipoX
   ```

2. **Crear el entorno virtual:**
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual:**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

4. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecutar la aplicación:**
   ```bash
   python run.py
   ```

6. **Abrir en el navegador:**
   ```
   http://127.0.0.1:5000
   ```

## Ejecución de pruebas

```bash
pytest tests/ -v
```

## Funcionalidades

| Operación | Descripción |
|-----------|-------------|
| Listar tareas | Muestra todas las tareas con su estado |
| Crear tarea | Formulario con título (obligatorio) y descripción |
| Ver detalle | Información completa de una tarea |
| Editar tarea | Modificar título y descripción |
| Eliminar tarea | Eliminación permanente con confirmación |
| Cambiar estado | Alterna entre `pendiente` y `completada` |

## Esquema de versiones

| Versión | Descripción |
|---------|-------------|
| v1.0 | Primera entrega — funcionalidades CRUD completas |
| v1.1 | Correcciones y mejoras (rama `fix/validaciones`) |

## Licencia

Proyecto académico — Ingeniería de Software.
