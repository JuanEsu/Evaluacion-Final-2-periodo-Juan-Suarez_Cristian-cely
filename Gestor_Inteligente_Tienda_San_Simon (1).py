
# ==========================================
# Gestor Inteligente de la Tienda San Simón
# ==========================================

inventario = [
    "empanada", "jugo", "papas", "galletas", "chocolatina",
    "gaseosa", "agua", "arepa", "sandwich", "ponque",
    "chicle", "gomitas", "yogur", "helado", "manzana",
    "banano", "pera", "salchipapa", "pizza", "brownie"
]

pedidos_pendientes = []

print("=== BIENVENIDO AL GESTOR DE LA TIENDA SAN SIMÓN ===")

while True:
    print("\n------ MENÚ PRINCIPAL ------")
    print("1. Ver inventario disponible")
    print("2. Tomar un nuevo pedido")
    print("3. Entregar todos los pedidos pendientes")
    print("4. Salir del sistema")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        print("\nProductos disponibles:")
        for producto in inventario:
            print("- " + producto.title())

    elif opcion == "2":
        nombre = input("Nombre del estudiante: ").strip().title()
        producto = input("Producto que desea: ").strip().lower()

        if producto in inventario:
            pedido = f"{nombre} - {producto.title()}"
            pedidos_pendientes.append(pedido)
            print("Pedido registrado correctamente.")
        else:
            print("Error: ese producto no existe en el inventario.")

    elif opcion == "3":
        if len(pedidos_pendientes) == 0:
            print("\nNo hay pedidos pendientes.")
        else:
            print("\nEntregando pedidos...")
            for pedido in pedidos_pendientes:
                print("➡ Entregando pedido a:", pedido)

            pedidos_pendientes.clear()
            print("Todos los pedidos fueron entregados.")

    elif opcion == "4":
        print("\nCerrando el sistema. ¡Que tengas un buen día!")
        break

    else:
        print("\nOpción no válida. Por favor, intenta de nuevo.")
