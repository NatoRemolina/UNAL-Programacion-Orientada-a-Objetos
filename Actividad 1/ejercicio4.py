import sys

class Familia:
    """
    Clase encargada de calcular y almacenar las edades de los miembros 
    de la familia en función de la edad de Juan.
    """
    def __init__(self):
        # Inicializamos los atributos de las edades en cero
        self.edad_juan = 0
        self.edad_alberto = 0.0
        self.edad_ana = 0.0
        self.edad_mama = 0.0

    def solicitar_datos(self):
        """
        Solicita la edad de Juan por consola. 
        Incluye un manejo de excepciones para asegurar que la entrada sea numérica.
        """
        try:
            print("Ingrese la edad de Juan: ")
            # Lectura de datos desde la entrada estándar
            input_data = sys.stdin.readline()
            
            # Si la entrada está vacía (útil para pruebas automatizadas), asignamos un valor por defecto
            if not input_data.strip():
                self.edad_juan = 9 
                print(f"Usando valor por defecto: {self.edad_juan}")
            else:
                # Convertimos la entrada a un número entero
                self.edad_juan = int(input_data)
                
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    def calcular_edades(self):
        """
        Aplica las proporciones matemáticas dadas para calcular 
        las edades de Alberto, Ana y la madre en base a la edad de Juan.
        """
        # Edad de Alberto: 2/3 de la edad de Juan
        self.edad_alberto = (2 / 3) * self.edad_juan
        
        # Edad de Ana: 4/3 de la edad de Juan
        self.edad_ana = (4 / 3) * self.edad_juan
        
        # Edad de la mamá: suma de las edades de sus tres hijos
        self.edad_mama = self.edad_juan + self.edad_alberto + self.edad_ana

    def mostrar_resultados(self):
        """
        Imprime en consola las edades calculadas, formateando 
        los números para no mostrar decimales (.0f).
        """
        print(f"La edad de Juan es: {self.edad_juan}")
        print(f"La edad de Alberto es: {self.edad_alberto:.0f}")
        print(f"La edad de Ana es: {self.edad_ana:.0f}")
        print(f"La edad de la Mamá es: {self.edad_mama:.0f}")

# ==========================================
# BLOQUE PRINCIPAL
# ==========================================
if __name__ == "__main__":
    # Instanciamos la clase Familia y ejecutamos los métodos secuencialmente
    familia = Familia()
    familia.solicitar_datos()
    familia.calcular_edades()
    familia.mostrar_resultados()