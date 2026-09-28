# Sistema de Gestión de Inventarios 📦

Aplicación desarrollada en Python para el control, administración y seguimiento de stock de productos. 
Este proyecto fue diseñado con el objetivo de aplicar conceptos de Programación Orientada a Objetos (POO) y persistencia de datos en un entorno real. 
El proyecto cuenta con dos versiones: una de ejecución rápida por consola y una versión "Pro" con Interfaz Gráfica de Usuario.

## 🚀 Características Principales
* **Operaciones CRUD Completas:** Permite agregar, visualizar, actualizar y eliminar productos del inventario.
* **Persistencia de Datos Automática:** Almacenamiento local seguro utilizando archivos `.json` (`inventario.json`). El sistema carga los datos al iniciar y guarda los cambios automáticamente tras cada operación (en la versión GUI).
* **Manejo de Excepciones robusto:** Validaciones integradas (bloques `try-except`) para evitar caídas del sistema por ingreso de datos incorrectos (ej. validación de enteros para cantidades y flotantes para precios).
* **Versatilidad de Uso:** Incluye un script base operativo desde consola (`proyecto2.py`) y una versión avanzada con Interfaz Gráfica interactiva (`mostrarp2.py`).

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Librerías (Versión GUI):** `customtkinter` (UI moderna con modo oscuro)
* **Manejo de Datos:** Módulo nativo `json`

## 💻 Instalación y Uso

1. Clonar el repositorio:
```bash
git clone https://github.com/joaquinalonso1/gestor-inventarios-python.git
```

2. Instalar la dependencia gráfica (necesaria para la versión Pro):
```bash
pip install customtkinter
```

3. Ejecutar la aplicación:
* Para la versión con Interfaz Gráfica:
```bash
python mostrarp2.py
```

* Para la versión de Consola:
```bash
python proyecto2.py
```

<img width="607" height="683" alt="image" src="https://github.com/user-attachments/assets/dfe77285-8207-476f-a7a3-fa0d35c4e4d2" />
