import math


class Circulo:
    def __init__(self, radio_circulo):
        self.radio = radio_circulo
        self.area = 0
        self.perimetro = 0

    def calcular_area(self):
        self.area = math.pi * math.pow(self.radio, 2)
        return self.area

    def calcular_perimetro(self):
        self.perimetro = 2 * math.pi * self.radio
        return self.perimetro

class Rectangulo:
    def __init__(self, base_rectangulo, altura_rectangulo):
        self.base = base_rectangulo
        self.altura = altura_rectangulo
        self.area = 0
        self.perimetro = 0

    def calcular_area(self):
        self.area = self.base * self.altura
        return self.area

    def calcular_perimetro(self):
        self.perimetro = (2 * self.base) + (2 * self.altura)
        return self.perimetro


class Cuadrado:
    def __init__(self, lado_cuadrado):
        self.lado = lado_cuadrado
        self.area = 0
        self.perimetro = 0

    def calcular_area(self):
        self.area = math.pow(self.lado, 2)
        return self.area

    def calcular_perimetro(self):
        self.perimetro = 4 * self.lado
        return self.perimetro

class Triangulo:
    def __init__(self, base_triangulo, altura_triangulo):
        self.base = base_triangulo
        self.altura = altura_triangulo
        self.area = 0
        self.hipotenusa = 0
        self.perimetro = 0

    def calcular_area(self):
        self.area = (self.base * self.altura)/2
        return self.area

    def calcular_hipotenusa(self):
        self.hipotenusa = math.sqrt(math.pow(self.base, 2) + math.pow(self.altura, 2))
        return self.hipotenusa

    def calcular_perimetro(self):
        self.perimetro = self.base + self.altura + self.calcular_hipotenusa()
        return self.perimetro

    def tipo_triangulo(self):
        # Aseguramos que la hipotenusa esté calculada antes de compararla
        self.calcular_hipotenusa()
        if self.base == self.altura and self.altura == self.hipotenusa:
            return "El triángulo es Equilátero"
        elif self.base == self.altura:
            return "El Triángulo es Isósceles"
        else:
            return "El Triángulo es Escaleno"


def main():
    print("--- datos del circulo ---")
    radio_circulo = float(input("Ingrese el radio del circulo en cm: \n"))
    valor_circulo = Circulo(radio_circulo)

    print("--- Datos Rectangulo ---")
    base_rectangulo = float(input("Ingrese la Base del Rectangulo: \n"))
    altura_rectangulo = float(input("Ingrese la Altura del Rectangulo: \n"))
    valores_rectangulo = Rectangulo(base_rectangulo, altura_rectangulo)

    print("--- Datos Cuadrado ---")
    lado_cuadrado = float(input("Ingrese el Lado del Cuadrado: \n"))
    valores_cuadrado = Cuadrado(lado_cuadrado)

    print("--- datos Triangulo Rectangulo ---")
    base_triangulo = float(input("Ingrese la Base del Triangulo Rectangulo: \n"))
    altura_triangulo = float(input("Ingrese la Altura del Triangulo Rectangulo: \n"))
    valores_triangulo = Triangulo(base_triangulo, altura_triangulo)

    print("--- Resultados de los calculos ---")
    print("--- Círculo ---")
    print(f"Area {valor_circulo.calcular_area():.2f} cm2")
    print(f"Perimetro {valor_circulo.calcular_perimetro():.2f} cm")

    print("--- Rectangulo ---")
    print(f"Area {valores_rectangulo.calcular_area():.2f} cm2")
    print(f"Perimetro {valores_rectangulo.calcular_perimetro():.2f} cm")

    print("--- Cuadrado ---")
    print(f"Area {valores_cuadrado.calcular_area():.2f} cm2")
    print(f"Perimetro {valores_cuadrado.calcular_perimetro():.2f} cm")

    print("--- Triángulo Rectangulo ---")
    print(f"Area {valores_triangulo.calcular_area():.2f} cm2")
    print(f"Perimetro {valores_triangulo.calcular_perimetro():.2f} cm")
    print(f"Hipotenusa {valores_triangulo.calcular_hipotenusa():.2f} cm")
    print(f"Tipo {valores_triangulo.tipo_triangulo()}")

main()
