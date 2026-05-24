class Empleado:
    """
    Clase que modela la información laboral de un empleado y calcula 
    su estructura salarial (bruto, retenciones y neto) aplicando
    conceptos de Programación Orientada a Objetos.
    """
    def __init__(self):
        # Inicialización de atributos base del empleado
        self.horas_trabajadas = 0
        self.valor_hora = 0
        self.porcentaje_retencion = 0.0
        
        # Inicialización de atributos que almacenarán los resultados calculados
        self.salario_bruto = 0.0
        self.retencion = 0.0
        self.salario_neto = 0.0

    def ingresar_datos(self):
        """
        Asigna los valores iniciales y constantes definidos por el 
        enunciado del problema.
        """
        self.horas_trabajadas = 48
        self.valor_hora = 5000
        self.porcentaje_retencion = 12.5  # Representa el 12.5% de retención en la fuente

    def calcular_salario(self):
        """
        Ejecuta las operaciones matemáticas para determinar el salario 
        bruto, el monto de descuento y el salario líquido final.
        """
        # Salario bruto: Total ganado sin aplicar ningún descuento
        self.salario_bruto = self.horas_trabajadas * self.valor_hora
        
        # Retención: Se obtiene multiplicando el bruto por el porcentaje dividido entre 100
        self.retencion = self.salario_bruto * (self.porcentaje_retencion / 100)
        
        # Salario neto: La diferencia entre el devengado (bruto) y lo deducido (retención)
        self.salario_neto = self.salario_bruto - self.retencion

    def mostrar_info(self):
        """
        Imprime el desglose salarial en consola, utilizando f-strings 
        para formatear las salidas financieras con separadores de miles y decimales.
        """
        print("--- Información Salarial del Trabajador ---")
        print(f"Horas trabajadas en la semana: {self.horas_trabajadas}")
        print(f"Valor por hora: ${self.valor_hora}")
        print(f"Porcentaje de retención: {self.porcentaje_retencion}%")
        print("-" * 41)
        
        # El formato :,.2f añade comas para miles y muestra exactamente dos decimales
        print(f"Salario Bruto:           ${self.salario_bruto:,.2f}")
        print(f"Retención en la fuente:  ${self.retencion:,.2f}")
        print(f"Salario Neto a pagar:    ${self.salario_neto:,.2f}")

# ==========================================
# BLOQUE PRINCIPAL
# ==========================================
if __name__ == "__main__":
    # Instanciamos el objeto empleado y ejecutamos el flujo de cálculo salarial
    empleado = Empleado()
    empleado.ingresar_datos()
    empleado.calcular_salario()
    empleado.mostrar_info()