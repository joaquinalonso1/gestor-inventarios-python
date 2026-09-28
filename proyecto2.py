#Vamos con el segundo proyecto: GESTOR DE INVENTARIO
#uso libreria json para guardar los datos en el disco duro
#uso try-except para iniciar un sistema que ya este guardado, y si no lo esta, que lo cree
#por primera vez

import json

print("Iniciando sistema...")

try:
    with open("inventario.json", "r") as archivo:
        inventario = json.load(archivo)
    print("Inventario cargado correctamente.")

except FileNotFoundError:
    print("No se encontró el archivo de inventario. Se creará uno nuevo.")
    inventario = {}

while True:
    print("--GESTOR DE INVENTARIO--")
    print("1) AGREGAR PRODUCTO")
    print("2)MOSTRAR INVENTARIO")
    print("3) ACTUALIZAR PRODUCTO")
    print("4) ELIMINAR PRODUCTO")
    print("5) SALIR")   
    
    #elijo lo que va a capturar la opcion que de el usuario
    #y le pongo un int porq solo tiene que analizar el numero de las opciones
    opcion = int(input("elige una opcion: "))

    if opcion ==1:
        producto= input("agregar el nombre del producto: ")
        cantidad= int(input("agregar la cantidad del producto: "))
        precio= float(input("agregar el precio del producto: "))
        #meto los datos en el innventario general y luego un print al mismo para ver que se guarden
        inventario[producto]= {"cantidad": cantidad , "precio": precio}
        
        
    elif opcion == 2: #es mostrar inventario
        print("INVENTARIO ACTUAL") 
        if not inventario:
            print("El inventario está vacío.")
        else:
            for producto, detalles in inventario.items():
                print(f"producto: {producto}, cantidad: {detalles['cantidad']}, precio: {detalles['precio']}")
        
    elif opcion==3:#actualizar el producto
        nom_produ= input("elegi el nombre del producot a actualizar: ")
        if nom_produ in inventario:
            ncantidad= int(input("ingresa la nueva cantidad: "))
            nprecio=float(input("ingresa el nuevo precio: "))
            #actualizo los datos, y luego aplasto los datos anteriores con el siguiente paso
            inventario[nom_produ]["cantidad"]= ncantidad
            inventario[nom_produ]["precio"]= nprecio
            print(f"Producto {nom_produ} se actualizo de manera correcta")
        else:
            print("no se encontro el producto en el inventario")
            
    
    elif opcion==4:
        nombreprodu=input("ingresar el producot a eliminar: ")
        if nombreprodu in inventario:
            del inventario[nombreprodu]
            print(f"Producto {nombreprodu} eliminado correctamente")
        else:
            print("no se encontro el producto en el inventario")
    
    elif opcion==5:
        print("guardando datos del inventario")
        with open("inventario.json", "w") as archivo:
            # Volcamos el diccionario al archivo. indent=4 lo hace fácil de leer para un humano.
            json.dump(inventario, archivo, indent=4)
        
        print("saliendo del sistema")
        break #termina el while si elije la opcion de salir
    
    else:
        print("no elegiste opcion correcta, vuelve a intentarlo")