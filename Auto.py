
class Auto:
    def __init__(self):
        # Constructor que solicita al usuario los detalles del automóvil y los guarda como atributos.
        self.marca = input("Ingrese la marca del auto: ")  # Marca del auto
        self.modelo = input("Ingrese el modelo del auto: ")  # Modelo del auto
        self.año = input("Ingrese el año del auto: ")  # Año del auto
        self.color = input("Ingrese el color del auto: ")  # Color del auto
        self.tipo_combustible = input("Ingrese el tipo de combustible (Gasolina/Diesel/Eléctrico): ")  # Tipo de combustible
        self.transmision = input("Ingrese el tipo de transmisión (Automática/Manual): ")  # Tipo de transmisión
        self.motor = input("Ingrese el tipo de motor (e.g., 1.8L): ")  # Tipo de motor
        self.origen = input("Ingrese el origen del auto (Nacional/Importado): ")  # Origen del auto
        self.precio_compra = float(input("Ingrese el precio de compra del auto: "))  # Precio de compra
        self.precio_venta = self.calcular_precio_venta()  # Precio de venta calculado
        self.ruedas = 4  # Número de ruedas del auto, establecido en 4 de forma predeterminada
        self.capacidad = 5  # Capacidad de pasajeros, establecida en 5 de forma predeterminada

    def calcular_precio_venta(self):
        # Método que calcula el precio de venta, que es un 40% mayor al precio de compra.
        return self.precio_compra * 1.4

    def mostrar_datos(self):
        # Método que muestra todos los detalles del auto.
        print("\nCaracterísticas del vehículo:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Tipo de Combustible: {self.tipo_combustible}")
        print(f"Transmisión: {self.transmision}")
        print(f"Motor: {self.motor}")
        print(f"Origen: {self.origen}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Capacidad de pasajeros: {self.capacidad}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")

# Registro y presentación del primer auto.
print("Registro del primer auto:")
auto1 = Auto()
auto1.mostrar_datos()

# Registro y presentación del segundo auto.
print("\nRegistro del segundo auto:")
auto2 = Auto()
auto2.mostrar_datos()
