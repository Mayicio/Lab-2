class Veterinaria:
    def __init__(self, peso=0, nombre="", clase="", color="", edad=0, genero=""):
        # Constructor que inicializa los atributos del objeto Veterinaria.
        # Se establecen valores predeterminados en caso de que no se proporcionen al crear la instancia.
        self.Estado = "NO ATENDIDO"  # Estado inicial del perro
        self.peso = peso  # Peso del perro
        self.tamano = self.determinar_tamano()  # Se determina el tamaño según el peso
        self.Nombre = nombre  # Nombre del perro
        self.Clase = clase  # Raza del perro
        self.Color = color  # Color del perro
        self.Edad = edad  # Edad del perro
        self.Genero = genero  # Género del perro

    def determinar_tamano(self):
        # Método para determinar el tamaño del perro según su peso.
        # Si el peso es de 10 kg o menos, se considera un perro pequeño; si es mayor, un perro grande.
        if self.peso <= 10:
            return "Perro Pequeño"
        else:
            return "Perro Grande"

    def cambiar_estado(self):
        # Método para cambiar el estado del perro a "ATENDIDO".
        self.Estado = "ATENDIDO"
        return self.Estado

    def entrada_datos(self):
        # Método para solicitar y almacenar los datos del perro ingresados por el usuario.
        self.Nombre = input("Nombre del Perro: ")
        self.Clase = input("Ingrese qué raza es su mascota: ")
        self.Color = input("Ingrese el color de su mascota: ")
        self.Edad = int(input("Ingrese la edad de su mascota: "))
        self.peso = int(input("Ingrese el peso de su mascota en kg: "))
        self.Genero = input("Ingrese el género de su mascota: ")
        self.tamano = self.determinar_tamano()  # Se recalcula el tamaño basado en el peso ingresado

    def muestra_datos(self):
        # Método para mostrar todos los datos del perro.
        print(f"Nombre: {self.Nombre}")
        print(f"Raza: {self.Clase}")
        print(f"Color: {self.Color}")
        print(f"Edad: {self.Edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Tamaño: {self.tamano}")
        print(f"Género: {self.Genero}")
        print(f"Estado: {self.Estado}")

# Creación de una instancia de la clase Veterinaria sin pasar valores iniciales.
perro = Veterinaria()

# Llamada al método para solicitar datos al usuario.
perro.entrada_datos()

# Cambio del estado del perro a "ATENDIDO".
perro.cambiar_estado()

# Muestra los datos ingresados y el estado actual del perro.
perro.muestra_datos()
