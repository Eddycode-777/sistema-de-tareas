# Plan de Gestión de Configuración del Software (SCMP)

**Proyecto:** Sistema Web de Gestión de Tareas
**Estándar:** IEEE 828 — Software Configuration Management Plan
**Repositorio:** GitHub
**Rama principal:** `main`
**Versión inicial:** `v1.0`

---

## 1. Propósito y Alcance

### Propósito

El propósito de este Plan de Gestión de Configuración del Software (SCMP) es establecer cómo se controlarán, registrarán y revisarán los cambios realizados en el Sistema Web de Gestión de Tareas, utilizando Git y GitHub.

El plan permite mantener la trazabilidad de los cambios y asegurar que las versiones del sistema puedan ser identificadas y controladas.

### Alcance

El plan se aplica al código fuente, vistas HTML, estilos CSS, pruebas, configuración, documentación y demás archivos relacionados con el proyecto.

La actividad se realiza de forma individual. Por esta razón, el mismo estudiante desempeña los roles de Responsable de Configuración, Desarrollador y Auditor Interno en diferentes etapas del proceso.

---

## 2. Elementos bajo Control de Configuración

Los principales elementos que estarán bajo control de configuración son:

* Código fuente desarrollado en Python y Flask.
* Plantillas HTML/Jinja2.
* Hojas de estilo CSS.
* Base de datos SQLite y archivos relacionados.
* Pruebas del sistema.
* Archivo `README.md`.
* Archivo `plan_configuracion.md`.
* Archivo `historial_cambios.txt`.
* Archivo `requirements.txt`.
* Ramas, commits, Pull Requests y etiquetas de versión del repositorio Git.

Estos elementos serán controlados mediante Git y almacenados en el repositorio de GitHub.

---

## 3. Control de Versiones

El proyecto utiliza Git para controlar las versiones y GitHub como repositorio remoto.

La rama `main` contiene las versiones estables del sistema. Para realizar cambios se utilizarán ramas independientes, siguiendo una nomenclatura descriptiva como:

```text
feature/nombre-del-cambio
```

Las versiones estables serán identificadas mediante etiquetas (tags) de Git.

El esquema utilizado para esta actividad es:

* **v1.0:** primera versión estable y funcional del sistema.
* **v1.1:** versión posterior a la implementación, revisión y aprobación de un cambio.

La versión inicial `v1.0` fue creada mediante un tag de Git asociado al commit de la versión inicial.

---

## 4. Control de Cambios

Todo cambio realizado al sistema seguirá el siguiente procedimiento:

1. Identificar y definir el cambio solicitado.
2. Crear una rama independiente para realizar el cambio.
3. Implementar la modificación correspondiente.
4. Realizar al menos dos commits documentados.
5. Crear un Pull Request hacia la rama `main`.
6. Revisar el cambio mediante el rol de Auditor Interno.
7. Aprobar y fusionar el Pull Request si cumple los requisitos.
8. Registrar el cambio en `historial_cambios.txt`.
9. Crear una nueva versión cuando corresponda.

Para esta actividad se simulará un cambio relacionado con la validación del título de las tareas, evitando que se creen tareas con el título vacío.

---

## 5. Auditoría de Configuración

El Auditor Interno será responsable de revisar los cambios antes de que sean incorporados a la rama `main`.

La auditoría verificará principalmente:

* Que los commits describan correctamente los cambios realizados.
* Que el código funcione correctamente.
* Que las pruebas correspondientes sean satisfactorias.
* Que el Pull Request contenga la información necesaria.
* Que la documentación y el historial de cambios estén actualizados.
* Que el cambio corresponda con la solicitud planteada.

Al tratarse de una actividad individual, el mismo estudiante desempeñará el rol de Auditor Interno durante la simulación.

La revisión se realizará antes del merge del Pull Request.

---

## 6. Entregas y Releases

Las versiones estables del proyecto serán identificadas mediante tags en Git y podrán ser utilizadas como referencia para las entregas.

La primera versión corresponde a:

```text
v1.0 — Versión inicial funcional del Sistema Web de Gestión de Tareas.
```

Después de realizar, revisar y aprobar el cambio planteado, se generará:

```text
v1.1 — Versión con validación del título de las tareas.
```

El procedimiento general de liberación será:

```text
Desarrollo → Revisión → Aprobación → Merge → Tag de versión
```

De esta manera, cada versión liberada queda asociada a un estado específico del repositorio y puede ser identificada mediante su etiqueta correspondiente.

---

## Control de roles

| Rol                          | Responsabilidad                                                    |
| ---------------------------- | ------------------------------------------------------------------ |
| Responsable de configuración | Gestionar el repositorio, ramas, versiones, tags y merges.         |
| Desarrollador                | Implementar cambios, crear ramas y realizar commits.               |
| Auditor interno              | Revisar cambios, commits, pruebas y documentación antes del merge. |

En esta actividad los tres roles son desempeñados por el mismo estudiante en diferentes etapas del proceso.
