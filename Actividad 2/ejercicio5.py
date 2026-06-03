class CuentaBancaria:
    def __init__(self, nombre, apellido, id, tipo_de_cuenta):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.tipo_de_cuenta = tipo_de_cuenta
        self.saldo = 0

    def consignar(self, valor_consignado):
        self.saldo = self.saldo + valor_consignado
        print(f"Consignación exitosa. Nuevo saldo: {self.saldo}")

    def retirar(self, valor_retirado):
        if self.saldo >= valor_retirado:
            self.saldo = self.saldo - valor_retirado
            print(f"Retiro exitoso. Saldo actual: {self.saldo}")
        else:
            print("Saldo insuficiente")

    def imprimir_datos(self):
        print(f"Nombre del titular: {self.nombre}")
        print(f"Apellido del titular: {self.apellido}")
        print(f"Identificación: {self.id}")
        print(f"Tipo de cuenta: {self.tipo_de_cuenta}")
        print(f"Saldo de la cuenta: {self.saldo}")

def main():
    print("--- Ingrese los datos ---")
    nombre = input("Nombres del titular: \n")
    apellido = input("Apellidos del titular: \n")
    id = input("Número de cuenta: \n")

    while True:
        tipo_de_cuenta = input("Tipo de cuenta: \n").lower()
        if tipo_de_cuenta == "ahorro" or tipo_de_cuenta == "corriente":
            break
        else:
            print("Tipo de cuenta no valido.")

    cuenta = CuentaBancaria(nombre, apellido, id, tipo_de_cuenta)

    while True:
        print("--- menu ---")

        print("--- 1. consignar valor ---")
        print("--- 2. retirar valor ---")
        print("--- 3. consultar datos y saldo ---")
        print("--- 4. salir ---")

        opcion = input("Ingrese la opcion: \n")

        if opcion == "1":
            valor_consignar = float(input("Ingrese el valor a consignar: \n"))
            cuenta.consignar(valor_consignar)
        elif opcion == "2":
            valor_retirar = float(input("Ingrese valor a retirar: \n"))
            cuenta.retirar(valor_retirar)
        elif opcion == "3":
            cuenta.imprimir_datos()
        elif opcion == "4":
            print("Finalizado exitosamente")
            break
        else:
            print("Opcion no valida")

main()
