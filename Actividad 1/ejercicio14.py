import sys

class Calculadora:
    """
    Clase diseñada para encapsular operaciones matemáticas básicas,
    permitiendo calcular dinámicamente el cuadrado y el cubo de un número.
    """
    def __init__(self):
        # Inicializamos el atributo que almacenará el número a procesar
        self.numero = 0.0

    def leer_numero(self):
        """
        Captura el número ingresado por el usuario a través de la consola.
        Implementa manejo de excepciones para garantizar que el programa
        no colapse ante entradas que no sean numéricas.
        """
        try:
            print("Ingrese un número para calcular su cuadrado y cubo: ")
            # Se utiliza sys.stdin.readline() para una lectura segura en distintos entornos
            input_data = sys.stdin.readline().strip()
            
            if not input_data:
                # Valor por defecto en caso de ejecuciones automatizadas o entradas vacías
                self.numero = 5.0  
                print(f"Usando valor por defecto: {self.numero}")
            else:
                # Convertimos la entrada a un tipo de dato flotante para admitir decimales
                self.numero = float(input_data)
                
        except ValueError:
            print("Entrada inválida. Por favor ingrese un valor numérico. Usando 0.0 por defecto.")
            self.numero = 0.0

    def calcular_potencias(self):
        """
        Calcula las potencias requeridas utilizando el operador de 
        exponenciación de Python (**) e imprime los resultados.
        """
        # El cuadrado es el número elevado a la potencia de 2
        cuadrado = self.numero ** 2
        
        # El cubo es el número elevado a la potencia de 3
        cubo = self.numero ** 3
        
        # Despliegue de los resultados en consola con un formato limpio
        print(f"\nResultados para el número: {self.numero}")
        print("-" * 35)
        print(f"El cuadrado de {self.numero} es: {cuadrado}")
        print(f"El cubo de {self.numero} es: {cubo}")

# ==========================================
# BLOQUE PRINCIPAL
# ==========================================
if __name__ == "__main__":
    # Instanciamos el objeto calculadora y ejecutamos los métodos de lectura y cálculo
    calc = Calculadora()
    calc.leer_numero()
    calc.calcular_potencias()