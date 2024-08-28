class Papeleria:
    def __init__(self, cuadernos=0, lapices=0, precio_compra=0):
        # Constructor que inicializa los atributos del objeto Papeleria.
        # Se establecen valores predeterminados para cuadernos, lápices y precio de compra.
        self.cuadernos = cuadernos  # Tipo de cuadernos (50 hojas o 100 hojas)
        self.lapices = lapices  # Tipo de lápices (grafito o color)
        self.marca_cuadernos = "Hojitas"  # Marca predeterminada de cuadernos
        self.marca_lapices = "Rayas"  # Marca predeterminada de lápices
        self.precio_compra = precio_compra  # Precio de compra del artículo
        self.precio_venta = self.calcular_precio_venta()  # Precio de venta calculado

    def calcular_precio_venta(self):
        # Método que calcula el precio de venta como un 30% más del precio de compra.
        return self.precio_compra * 1.30

    def recibir_datos(self):
        # Método para solicitar al usuario que ingrese los detalles del artículo.
        # El tipo de cuaderno y lápiz se selecciona mediante input.
        tipo_cuaderno = int(input("Seleccione el tipo de cuaderno (1: 50 Hojas, 2: 100 Hojas): "))
        if tipo_cuaderno == 1:
            self.cuadernos = "50 Hojas"
        elif tipo_cuaderno == 2:
            self.cuadernos = "100 Hojas"
        else:
            print("Opción no válida.")  # Mensaje de error si la opción es inválida
        
        tipo_lapiz = input("Seleccione el tipo de lápiz (grafito o color): ").lower()
        if tipo_lapiz == "grafito":
            self.lapices = "Lápiz de Grafito"
        elif tipo_lapiz == "color":
            self.lapices = "Lápiz de Color"
        else:
            print("Opción no válida.")  # Mensaje de error si la opción es inválida
        
        # Solicita el precio de compra y recalcula el precio de venta en base al nuevo valor.
        self.precio_compra = float(input("Ingrese el precio de compra: "))
        self.precio_venta = self.calcular_precio_venta()

    def mostrar_datos(self):
        # Método para mostrar los detalles del artículo registrado.
        print("\nDetalles del artículo registrado:")
        print(f"Marca de Cuadernos: {self.marca_cuadernos}")
        print(f"Tipo de Cuaderno: {self.cuadernos}")
        print(f"Marca de Lápices: {self.marca_lapices}")
        print(f"Tipo de Lápiz: {self.lapices}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")


# Creación de la primera instancia de la clase Papeleria.
articulo1 = Papeleria()
articulo1.recibir_datos()  # Solicita los datos al usuario.
articulo1.mostrar_datos()  # Muestra los datos ingresados.

# Creación de una segunda instancia de la clase Papeleria.
articulo2 = Papeleria()
articulo2.recibir_datos()  # Solicita los datos al usuario.
articulo2.mostrar_datos()  # Muestra los datos ingresados.
