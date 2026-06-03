from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"

class Planeta:
    def __init__(self, nombre, cantidad_satelites, masa, volumen, diametro, distancia_sol, tipo, es_observable):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable

    def imprimir(self):
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidad_satelites}")
        print(f"Masa del planeta = {self.masa}")
        print(f"Volumen del planeta = {self.volumen}")
        print(f"Diámetro del planeta = {self.diametro}")
        print(f"Distancia al sol = {self.distancia_sol}")
        print(f"Tipo de planeta = {self.tipo.name}")
        print(f"Es observable = {self.es_observable}")

    def calcular_densidad(self):
        # Evita división por cero
        return self.masa / self.volumen if self.volumen != 0 else 0

    def es_planeta_exterior(self):
        # 149597870 * 3.4
        limite = 508632758.0
        return self.distancia_sol > limite


print("Ingrese el nombre : ")
nombre = input()
print("Ingrese cantidad de satélites : ")
cantidad_satelites = int(input())
print("Ingrese la masa : ")
masa = float(input())
print("Ingrese el volumen : ")
volumen = float(input())

print("Ingrese el diámetro : ")
diametro = int(input())
print("Ingrese la distancia al sol : ")
distancia_sol = float(input())
p1 = Planeta(nombre, cantidad_satelites, masa, volumen, diametro,
             distancia_sol, TipoPlaneta.TERRESTRE, True)
print("********************************")
p1.imprimir()
print(f"Densidad del planeta = {p1.calcular_densidad()}")
print(f"Es planeta exterior = {p1.es_planeta_exterior()}")
print("********************************")
