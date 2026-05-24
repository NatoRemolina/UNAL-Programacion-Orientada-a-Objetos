class PruebaEscritorio:
    """
    Clase diseñada para simular paso a paso la prueba de escritorio 
    del algoritmo propuesto, mostrando el estado de las variables en memoria.
    """
    def __init__(self):
        # Inicializamos las variables que se utilizarán en el algoritmo
        self.suma = 0
        self.x = 0
        self.y = 0

    def ejecutar_algoritmo(self):
        """
        Ejecuta secuencialmente las instrucciones del seudocódigo
        e imprime el valor de las variables para evidenciar el seguimiento.
        """
        # Paso 1: Inicializar la variable acumuladora SUMA en 0
        self.suma = 0
        print(f"Paso 1 -> Inicio: SUMA = {self.suma}")

        # Paso 2: Asignar el valor 20 a la variable X
        self.x = 20
        print(f"Paso 2 -> X asignado: {self.x}")

        # Paso 3: Acumular el valor actual de X en SUMA (0 + 20)
        self.suma = self.suma + self.x
        print(f"Paso 3 -> SUMA = SUMA + X: {self.suma}")

        # Paso 4: Asignar el valor 40 a la variable Y
        self.y = 40
        print(f"Paso 4 -> Y asignado: {self.y}")

        # Paso 5: Actualizar X sumándole el cuadrado de Y (20 + 40^2)
        # Nota: En Python, el operador de potenciación es **
        self.x = self.x + (self.y ** 2)
        print(f"Paso 5 -> X = X + Y^2: {self.x}")

        # Paso 6: Acumular en SUMA el resultado de la división X / Y
        self.suma = self.suma + (self.x / self.y)
        print(f"Paso 6 -> SUMA = SUMA + X/Y: {self.suma}")

        # Salida final exigida por el algoritmo
        print("\n--- Resultado ---")
        print(f"EL VALOR DE LA SUMA ES: {self.suma}")

# ==========================================
# BLOQUE PRINCIPAL
# ==========================================
if __name__ == "__main__":
    # Instanciamos la clase y ejecutamos la simulación del algoritmo
    prueba = PruebaEscritorio()
    prueba.ejecutar_algoritmo()