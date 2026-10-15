class Automovil:
    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil, color, velocidad_maxima, numero_puertas, numero_asientos):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.velocidad_maxima = velocidad_maxima
        self.numero_puertas = numero_puertas
        self.numero_asientos = numero_asientos

        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.color = color

        self._velocidad_actual = 0

    @property
    def tipo_combustible(self):
        return self._tipo_combustible

    @tipo_combustible.setter
    def tipo_combustible(self, valor):
        self._tipo_combustible = valor

    @property
    def tipo_automovil(self):
        return self._tipo_automovil

    @tipo_automovil.setter
    def tipo_automovil(self, valor):
        self._tipo_automovil = valor

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, valor):
        self._color = valor

    @property
    def velocidad_actual(self):
        return self._velocidad_actual

    def acelerar(self, incremento):
        if incremento < 0:
            print("Error: valor no valido")
            return

        if self._velocidad_actual + incremento <= self.velocidad_maxima:
            self._velocidad_actual += incremento
        else:
            self._velocidad_actual = self.velocidad_maxima
            print(f"Se ha alcanzado la velocidad máxima de {self.velocidad_maxima}")

        print(f"La velocidad actual es {self._velocidad_actual} km/h")

    def desacelerar(self, decremento):
        if decremento < 0:
            print("Error: valor no valido")
            return

        if self._velocidad_actual - decremento >= 0:
            self._velocidad_actual -= decremento
        else:
            self._velocidad_actual = 0
            print("El automóvil se ha detenido por completo.")

        print(f"Velocidad actual: {self._velocidad_actual} km/h")

    def frenar(self):
        self._velocidad_actual = 0
        print("Freno activado. Velocidad: 0 km/h")

    def tiempo_de_llegada(self, distancia):
        if self._velocidad_actual == 0:
            print("No se puede calcular el tiempo de llegada porque el automovil esta detenido.")
            return None

        return distancia / self._velocidad_actual

    def mostrar_atributos(self):
        print("\n--- ESPECIFICACIONES DEL VEHÍCULO ---")
        print(f"Marca: {self.marca} | Modelo: {self.modelo}")
        print(f"Motor: {self.motor}L | Velocidad Máx: {self.velocidad_maxima} km/h")
        print(f"Combustible: {self.tipo_combustible.title()}")
        print(f"Tipo de Auto: {self.tipo_automovil.title()}")
        print(f"Color: {self.color.title()}")
        print(f"Puertas: {self.numero_puertas} | Asientos: {self.numero_asientos}")
        print(f"ESTADO ACTUAL: {self._velocidad_actual} km/h")

def main():
    print("CONFIGURACIÓN DE AUTOMÓVIL\n")

    marca = input("Marca: ")
    modelo = input("Modelo (Año): ")
    motor = float(input("Motor (Litros): "))
    velocidad_maxima = float(input("Velocidad Máxima: "))
    numero_puertas = int(input("Puertas: "))
    numero_asientos = int(input("Asientos: "))

    while True:
        print("\n--- TIPO DE COMBUSTIBLE ---")
        print("1. Gasolina\n2. Bioetanol\n3. Diésel\n4. Biodiésel\n5. Gas Natural")
        opcion_combustible = input("Seleccione (1-5): ")
        if opcion_combustible == "1":
            tipo_combustible_seleccionado = "Gasolina"; break
        elif opcion_combustible == "2":
            tipo_combustible_seleccionado = "Bioetanol"; break
        elif opcion_combustible == "3":
            tipo_combustible_seleccionado = "Diésel"; break
        elif opcion_combustible == "4":
            tipo_combustible_seleccionado = "Biodiésel"; break
        elif opcion_combustible == "5":
            tipo_combustible_seleccionado = "Gas Natural"; break
        else:
            print("Opción inválida.")

    while True:
        print("\n--- TIPO DE AUTO ---")
        print("1. Ciudad\n2. Subcompacto\n3. Compacto\n4. Familiar\n5. Ejecutivo\n6. SUV")
        opcion_tipo = input("Seleccione (1-6): ")
        if opcion_tipo == "1":
            tipo_automovil_seleccionado = "Carro de ciudad"; break
        elif opcion_tipo == "2":
            tipo_automovil_seleccionado = "Subcompacto"; break
        elif opcion_tipo == "3":
            tipo_automovil_seleccionado = "Compacto"; break
        elif opcion_tipo == "4":
            tipo_automovil_seleccionado = "Familiar"; break
        elif opcion_tipo == "5":
            tipo_automovil_seleccionado = "Ejecutivo"; break
        elif opcion_tipo == "6":
            tipo_automovil_seleccionado = "SUV"; break
        else:
            print("Opción inválida.")

    while True:
        print("\n--- COLOR ---")
        print("1. Blanco\n2. Negro\n3. Rojo\n4. Naranja\n5. Amarillo\n6. Verde\n7. Azul\n8. Violeta")
        opcion_color = input("Seleccione (1-8): ")
        if opcion_color == "1":
            color_seleccionado = "Blanco"; break
        elif opcion_color == "2":
            color_seleccionado = "Negro"; break
        elif opcion_color == "3":
            color_seleccionado = "Rojo"; break
        elif opcion_color == "4":
            color_seleccionado = "Naranja"; break
        elif opcion_color == "5":
            color_seleccionado = "Amarillo"; break
        elif opcion_color == "6":
            color_seleccionado = "Verde"; break
        elif opcion_color == "7":
            color_seleccionado = "Azul"; break
        elif opcion_color == "8":
            color_seleccionado = "Violeta"; break
        else:
            print("Opción inválida.")

    mi_auto = Automovil(
        marca,
        modelo,
        motor,
        tipo_combustible_seleccionado,
        tipo_automovil_seleccionado,
        color_seleccionado,
        velocidad_maxima,
        numero_puertas,
        numero_asientos
    )

    while True:
        print("\n--- MENÚ DE CONDUCCIÓN ---")
        print("1. Acelerar")
        print("2. Desacelerar")
        print("3. Frenar")
        print("4. Calcular tiempo de llegada")
        print("5. Ver Ficha Técnica (Atributos)")
        print("6. Salir del programa")

        opcion_menu = input("\nElija una opción: ")

        if opcion_menu == "1":
            cantidad_acelerar = float(input("¿Cuánto desea acelerar? (km/h): "))
            mi_auto.acelerar(cantidad_acelerar)

        elif opcion_menu == "2":
            cantidad_desacelerar = float(input("¿Cuánto desea desacelerar? (km/h): "))
            mi_auto.desacelerar(cantidad_desacelerar)

        elif opcion_menu == "3":
            mi_auto.frenar()

        elif opcion_menu == "4":
            distancia_viaje = float(input("Distancia a recorrer (km): "))
            tiempo_resultado = mi_auto.tiempo_de_llegada(distancia_viaje)
            if tiempo_resultado is not None:
                print(f"Tiempo estimado: {tiempo_resultado:.2f} horas.")

        elif opcion_menu == "5":
            mi_auto.mostrar_atributos()

        elif opcion_menu == "6":
            print("Saliendo del sistema")
            break

        else:
            print("Opción no válida.")


main()
