class Persona:
    def __init__(self, nombre, apellido, numero_documento, año_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_documento = numero_documento
        self.año_nacimiento = año_nacimiento

    def mostrar_datos_personales(self):
        print(f"Nombre = {self.nombre}")
        print(f"Apellido = {self.apellido}")
        print(f"Número de documento de identidad = {self.numero_documento}")
        print(f"Año de nacimiento = {self.año_nacimiento}")

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
numero_documento = input("Ingrese el número de documento de identidad: ")
año_nacimiento = int(input("Ingrese el año de nacimiento: "))

persona1 = Persona(nombre, apellido, numero_documento, año_nacimiento)
persona1.mostrar_datos_personales()
