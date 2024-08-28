class DispositivoElectronico:
    def __init__(self):
        # Constructor que solicita al usuario los detalles del dispositivo y los guarda como atributos.
        self.tipo = input("Ingrese el tipo de dispositivo (Celular/Tablet/Portátil): ")  # Tipo de dispositivo
        self.modelo = input("Ingrese el modelo del dispositivo: ")  # Modelo del dispositivo
        self.capacidad = input("Ingrese la capacidad del dispositivo (e.g., 128GB, 8GB RAM): ")  # Capacidad del dispositivo
        self.color = input("Ingrese el color del dispositivo: ")  # Color del dispositivo
        self.pantalla = input("Ingrese el tamaño de la pantalla (e.g., 6.5 pulgadas): ")  # Tamaño de la pantalla
        self.bateria = input("Ingrese la capacidad de la batería (e.g., 4000mAh): ")  # Capacidad de la batería
        self.precio_compra = float(input("Ingrese el precio de compra del dispositivo: "))  # Precio de compra
        self.marca = "PHR"  # Marca predeterminada del dispositivo
        self.origen = "Importado"  # Origen predeterminado del dispositivo
        self.precio_venta = self.calcular_precio_venta()  # Precio de venta calculado

    def calcular_precio_venta(self):
        # Método que calcula el precio de venta, que es un 70% mayor al precio de compra.
        return self.precio_compra * 1.7

    def mostrar_datos(self):
        # Método que muestra todos los detalles del dispositivo.
        print("\nCaracterísticas del dispositivo:")
        print(f"Tipo: {self.tipo}")
        print(f"Modelo: {self.modelo}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Color: {self.color}")
        print(f"Tamaño de Pantalla: {self.pantalla}")
        print(f"Capacidad de Batería: {self.bateria}")
        print(f"Marca: {self.marca}")
        print(f"Origen: {self.origen}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")

# Registro y presentación del primer dispositivo electrónico.
print("Registro del primer dispositivo:")
dispositivo1 = DispositivoElectronico()
dispositivo1.mostrar_datos()

# Registro y presentación del segundo dispositivo electrónico.
print("\nRegistro del segundo dispositivo:")
dispositivo2 = DispositivoElectronico()
dispositivo2.mostrar_datos()
