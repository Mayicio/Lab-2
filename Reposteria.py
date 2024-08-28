class Reposteria:
    def __init__(self):
        # Constructor que solicita al usuario los detalles del pedido y los guarda como atributos.
        self.tipo_producto = input("¿Qué desea comprar? (Brownie/Galleta/Café): ").capitalize()
        self.sabor = input("Ingrese el sabor del producto (Chocolate/Vainilla/Café): ").capitalize()
        self.cantidad = int(input("Ingrese la cantidad que desea comprar: "))
        self.precio_unitario = self.definir_precio()  # Precio unitario según el tipo de producto
        self.precio_total = self.calcular_precio_total()  # Precio total basado en la cantidad
        self.envase = self.seleccionar_envase()  # Selección de envase dependiendo del producto
        self.servicio_a_domicilio = self.opcion_servicio_domicilio()  # Si se agrega servicio a domicilio

    def definir_precio(self):
        # Método que define el precio unitario según el tipo de producto.
        if self.tipo_producto == "Brownie":
            return 2.50
        elif self.tipo_producto == "Galleta":
            return 1.50
        elif self.tipo_producto == "Café":
            return 3.00
        else:
            print("Producto no disponible.")
            return 0

    def calcular_precio_total(self):
        # Método que calcula el precio total multiplicando la cantidad por el precio unitario.
        return self.cantidad * self.precio_unitario

    def seleccionar_envase(self):
        # Método para seleccionar el tipo de envase según el producto.
        if self.tipo_producto == "Brownie" or self.tipo_producto == "Galleta":
            return "Caja"
        elif self.tipo_producto == "Café":
            return "Vaso desechable"
        else:
            return "Sin envase"

    def opcion_servicio_domicilio(self):
        # Método para agregar servicio a domicilio si el usuario lo desea.
        opcion = input("¿Desea servicio a domicilio? (Si/No): ").lower()
        if opcion == "si":
            print("Se ha agregado un costo adicional de $5.00 por servicio a domicilio.")
            return 5.00
        else:
            return 0.00

    def mostrar_detalles(self):
        # Método que muestra todos los detalles del pedido.
        print("\nDetalles de su pedido:")
        print(f"Producto: {self.tipo_producto}")
        print(f"Sabor: {self.sabor}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Envase: {self.envase}")
        print(f"Precio Unitario: ${self.precio_unitario:.2f}")
        print(f"Servicio a Domicilio: ${self.servicio_a_domicilio:.2f}")
        print(f"Precio Total: ${(self.precio_total + self.servicio_a_domicilio):.2f}")


# Registro y presentación del primer pedido.
print("Registro del primer pedido:")
pedido1 = Reposteria()
pedido1.mostrar_detalles()

# Registro y presentación del segundo pedido.
print("\nRegistro del segundo pedido:")
pedido2 = Reposteria()
pedido2.mostrar_detalles()
