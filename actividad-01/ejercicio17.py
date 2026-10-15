import math
import sys

class Circulo:
    """
    Clase que modela un círculo y permite calcular sus propiedades 
    geométricas principales (área y longitud de la circunferencia) 
    a partir de la medida de su radio.
    """
    def __init__(self):
        # Inicializamos los atributos en 0.0 para trabajar con valores decimales (flotantes)
        self.radio = 0.0
        self.area = 0.0
        self.longitud = 0.0

    def leer_radio(self):
        """
        Captura el radio ingresado por el usuario a través de la consola,
        implementando un manejo de excepciones para evitar que el programa 
        falle si se ingresa texto en lugar de números.
        """
        try:
            print("Ingrese el radio del círculo: ")
            # Se usa sys.stdin.readline() para una lectura segura y compatible en distintos entornos
            input_data = sys.stdin.readline().strip()
            
            if not input_data:
                # Se asigna un valor por defecto si la entrada está vacía (útil en pruebas)
                self.radio = 10.0  
                print(f"Usando valor por defecto: {self.radio}")
            else:
                self.radio = float(input_data)
                
        except ValueError:
            print("Entrada inválida. Por favor ingrese un valor numérico. Usando 0.0 por defecto.")
            self.radio = 0.0

    def calcular_propiedades(self):
        """
        Aplica las fórmulas matemáticas estándar haciendo uso de la constante pi 
        proporcionada por la librería math de Python.
        """
        # Cálculo del área: Pi multiplicado por el radio al cuadrado (π * r^2)
        self.area = math.pi * (self.radio ** 2)
        
        # Cálculo de la longitud (perímetro): 2 multiplicado por Pi por el radio (2 * π * r)
        self.longitud = 2 * math.pi * self.radio

    def mostrar_resultados(self):
        """
        Imprime los resultados en consola. Se utiliza el formato :.4f 
        para redondear la salida a exactamente cuatro decimales.
        """
        print(f"\nResultados para el círculo de radio: {self.radio}")
        print("-" * 45)
        print(f"Área del círculo:              {self.area:.4f}")
        print(f"Longitud de la circunferencia: {self.longitud:.4f}")

# ==========================================
# BLOQUE PRINCIPAL
# ==========================================
if __name__ == "__main__":
    # Instanciamos el objeto Circulo y ejecutamos sus métodos en secuencia
    mi_circulo = Circulo()
    mi_circulo.leer_radio()
    mi_circulo.calcular_propiedades()
    mi_circulo.mostrar_resultados()