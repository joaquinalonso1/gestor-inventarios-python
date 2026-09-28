import json
import customtkinter as ctk

# --- LÓGICA DE BACKEND (CRUD) ---

def agregar_producto():
    nombre = entrada_nombre.get().strip()
    if not nombre:
        etiqueta_estado.configure(text="Error: El nombre no puede estar vacío.", text_color="red")
        return

    try:
        cantidad = int(entrada_cantidad.get())
        precio = float(entrada_precio.get())
    except ValueError:
        etiqueta_estado.configure(text="Error: Cantidad (entero) y Precio (decimal).", text_color="red")
        return

    try:
        with open("inventario.json", "r") as archivo:
            inventario = json.load(archivo)
    except FileNotFoundError:
        inventario = {}

    inventario[nombre] = {"cantidad": cantidad, "precio": precio}

    with open("inventario.json", "w") as archivo:
        json.dump(inventario, archivo, indent=4)
    
    etiqueta_estado.configure(text=f"Éxito: '{nombre}' guardado correctamente.", text_color="green")
    
    # Limpiar inputs
    entrada_nombre.delete(0, 'end')
    entrada_cantidad.delete(0, 'end')
    entrada_precio.delete(0, 'end')
    actualizar_lista()

def actualizar_producto():
    nombre = entrada_nombre.get().strip()
    if not nombre:
        etiqueta_estado.configure(text="Escribí el nombre del producto a actualizar.", text_color="red")
        return

    try:
        with open("inventario.json", "r") as archivo:
            inventario = json.load(archivo)
    except FileNotFoundError:
        inventario = {}

    if nombre in inventario:
        try:
            cantidad = int(entrada_cantidad.get())
            precio = float(entrada_precio.get())
        except ValueError:
            etiqueta_estado.configure(text="Error: Ingesá nuevos valores numéricos válidos.", text_color="red")
            return

        inventario[nombre] = {"cantidad": cantidad, "precio": precio}
        with open("inventario.json", "w") as archivo:
            json.dump(inventario, archivo, indent=4)
        
        etiqueta_estado.configure(text=f"Éxito: '{nombre}' actualizado.", text_color="green")
        actualizar_lista()
    else:
        etiqueta_estado.configure(text=f"Error: '{nombre}' no existe en el inventario.", text_color="red")

def eliminar_producto():
    nombre = entrada_nombre.get().strip()
    if not nombre:
        etiqueta_estado.configure(text="Escribí el nombre del producto a eliminar.", text_color="red")
        return

    try:
        with open("inventario.json", "r") as archivo:
            inventario = json.load(archivo)
    except FileNotFoundError:
        inventario = {}

    if nombre in inventario:
        del inventario[nombre]
        with open("inventario.json", "w") as archivo:
            json.dump(inventario, archivo, indent=4)
        
        etiqueta_estado.configure(text=f"Éxito: '{nombre}' eliminado.", text_color="orange")
        entrada_nombre.delete(0, 'end')
        actualizar_lista()
    else:
        etiqueta_estado.configure(text=f"Error: '{nombre}' no se encontró.", text_color="red")

def actualizar_lista():
    # Limpiamos y rellenamos la caja de texto visual (Read)
    caja_texto.configure(state="normal")
    caja_texto.delete("1.0", "end")
    
    try:
        with open("inventario.json", "r") as archivo:
            inventario = json.load(archivo)
            if not inventario:
                caja_texto.insert("end", "El inventario está vacío.")
            else:
                for prod, datos in inventario.items():
                    texto_linea = f"• {prod.upper()} | Cantidad: {datos['cantidad']} | Precio: ${datos['precio']}\n"
                    caja_texto.insert("end", texto_linea)
    except FileNotFoundError:
        caja_texto.insert("end", "No hay base de datos registrada aún.")
    
    caja_texto.configure(state="disabled")


# --- CONFIGURACIÓN DE LA VISTA (FRONTEND) ---

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.geometry("600x650")
ventana.title("Gestor de Inventario - Pro")

# Título principal
titulo = ctk.CTkLabel(ventana, text="SISTEMA DE GESTIÓN DE INVENTARIO", font=("Arial", 18, "bold"))
titulo.pack(pady=15)

# Marco para el formulario de entradas
marco_inputs = ctk.CTkFrame(ventana)
marco_inputs.pack(pady=10, padx=20, fill="x")

entrada_nombre = ctk.CTkEntry(marco_inputs, placeholder_text="Nombre del producto", width=350)
entrada_nombre.pack(pady=8)

entrada_cantidad = ctk.CTkEntry(marco_inputs, placeholder_text="Cantidad (Ej: 10)", width=350)
entrada_cantidad.pack(pady=8)

entrada_precio = ctk.CTkEntry(marco_inputs, placeholder_text="Precio (Ej: 1500.50)", width=350)
entrada_precio.pack(pady=8)

# Botonera de Acciones CRUD
marco_botones = ctk.CTkFrame(ventana, fg_color="transparent")
marco_botones.pack(pady=10)

btn_agregar = ctk.CTkButton(marco_botones, text="Agregar", fg_color="green", hover_color="darkgreen", width=110, command=agregar_producto)
btn_agregar.grid(row=0, column=0, padx=5)

btn_actualizar = ctk.CTkButton(marco_botones, text="Actualizar", fg_color="orange", hover_color="darkorange", width=110, command=actualizar_producto)
btn_actualizar.grid(row=0, column=1, padx=5)

btn_eliminar = ctk.CTkButton(marco_botones, text="Eliminar", fg_color="red", hover_color="darkred", width=110, command=eliminar_producto)
btn_eliminar.grid(row=0, column=2, padx=5)

# Etiqueta de estado / feedback visual para el usuario
etiqueta_estado = ctk.CTkLabel(ventana, text="Sistema listo.", font=("Arial", 12))
etiqueta_estado.pack(pady=5)

# Sección de Visualización (Read / Inventario Actual en pantalla)
lbl_inventario = ctk.CTkLabel(ventana, text="Inventario en Tiempo Real:", font=("Arial", 14, "bold"))
lbl_inventario.pack(anchor="w", padx=30, pady=(10, 0))

caja_texto = ctk.CTkTextbox(ventana, width=540, height=200, font=("Consolas", 12))
caja_texto.pack(pady=10)
caja_texto.configure(state="disabled") # Bloqueado para escritura manual, solo lectura

# Cargar los datos iniciales al arrancar la ventana
actualizar_lista()

ventana.mainloop()