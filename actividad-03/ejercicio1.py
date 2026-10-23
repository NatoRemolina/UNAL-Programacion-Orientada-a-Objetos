import tkinter as tk
from tkinter import messagebox, ttk
import math

# ==========================================
# CLASE LÓGICA (Modelo)
# ==========================================
class Notas:
    """Clase encargada de realizar los cálculos matemáticos de las notas."""
    def __init__(self, lista_notas):
        self.notas = lista_notas

    def calcular_promedio(self):
        # Retorna el promedio simple de la lista
        return sum(self.notas) / len(self.notas)

    def calcular_desviacion_estandar(self):
        promedio = self.calcular_promedio()
        # Varianza poblacional: suma de (nota - promedio)^2 / N
        varianza = sum(math.pow(nota - promedio, 2) for nota in self.notas) / len(self.notas)
        # Retorna la raíz cuadrada de la varianza
        return math.sqrt(varianza)

    def calcular_mayor(self):
        # Retorna el valor máximo de la lista
        return max(self.notas)

    def calcular_menor(self):
        # Retorna el valor mínimo de la lista
        return min(self.notas)

# ==========================================
# CLASE INTERFAZ GRÁFICA (Vista/Controlador)
# ==========================================
class VentanaNotas(tk.Tk):
    """Clase que representa la ventana principal con una paleta de colores azules."""
    def __init__(self):
        super().__init__()
        
        # Paleta de colores azul
        self.color_fondo = "#e3f2fd" # Azul muy claro
        self.color_texto = "#0d47a1" # Azul oscuro para etiquetas
        
        # Configuración básica
        self.title("Calculadora de Notas")
        self.geometry("280x380")
        self.resizable(False, False)
        # Aplicamos el color de fondo a toda la ventana
        self.configure(bg=self.color_fondo)
        
        self.entradas_notas = []
        
        # Inicializar componentes
        self._crear_componentes()
        
        self.eval('tk::PlaceWindow . center')

    def _crear_componentes(self):
        # Crear los campos de entrada
        for i in range(5):
            lbl = tk.Label(self, text=f"Nota {i+1}:", anchor="w", 
                           bg=self.color_fondo, fg=self.color_texto, font=("Arial", 10, "bold"))
            lbl.place(x=20, y=20 + (i * 30), width=60, height=25)
            
            txt_entry = tk.Entry(self, bd=1, relief="solid")
            txt_entry.place(x=100, y=20 + (i * 30), width=150, height=25)
            self.entradas_notas.append(txt_entry)

        # Botones con estilo azul.
        # Se usa ttk con el tema "clam" porque los botones tk no admiten
        # colores de fondo en macOS y quedarían ilegibles.
        estilo = ttk.Style(self)
        estilo.theme_use("clam")
        estilo.configure("Calcular.TButton", background="#2196f3", foreground="white",
                         font=("Arial", 9, "bold"), borderwidth=0, focuscolor="#2196f3")
        estilo.map("Calcular.TButton", background=[("active", "#1565c0")])
        estilo.configure("Limpiar.TButton", background="#1976d2", foreground="white",
                         font=("Arial", 9, "bold"), borderwidth=0, focuscolor="#1976d2")
        estilo.map("Limpiar.TButton", background=[("active", "#0d47a1")])

        btn_calcular = ttk.Button(self, text="Calcular", command=self.action_calcular,
                                  style="Calcular.TButton")
        btn_calcular.place(x=20, y=180, width=110, height=30)

        btn_limpiar = ttk.Button(self, text="Limpiar", command=self.action_limpiar,
                                 style="Limpiar.TButton")
        btn_limpiar.place(x=140, y=180, width=110, height=30)

        # Labels de resultados con estilo azul
        resultado_style = {"bg": self.color_fondo, "fg": self.color_texto, "anchor": "w"}
        
        self.lbl_promedio = tk.Label(self, text="Promedio: ", **resultado_style)
        self.lbl_promedio.place(x=20, y=230, width=240, height=25)
        
        self.lbl_desviacion = tk.Label(self, text="Desviación estándar: ", **resultado_style)
        self.lbl_desviacion.place(x=20, y=260, width=240, height=25)
        
        self.lbl_mayor = tk.Label(self, text="Mayor nota: ", **resultado_style)
        self.lbl_mayor.place(x=20, y=290, width=240, height=25)
        
        self.lbl_menor = tk.Label(self, text="Menor nota: ", **resultado_style)
        self.lbl_menor.place(x=20, y=320, width=240, height=25)

    def action_calcular(self):
        """Procesa las entradas y muestra resultados."""
        # Es obligatorio ingresar las cinco notas: se avisa cuáles faltan
        faltantes = [i + 1 for i, entry in enumerate(self.entradas_notas)
                     if not entry.get().strip()]
        if faltantes:
            notas_faltantes = ", ".join(str(numero) for numero in faltantes)
            messagebox.showwarning(
                "Datos incompletos",
                f"Es obligatorio ingresar las cinco notas.\nFalta la nota: {notas_faltantes}."
            )
            return

        try:
            valores = [float(entry.get()) for entry in self.entradas_notas]
            calculadora = Notas(valores)
            
            # Actualizamos textos con los cálculos
            self.lbl_promedio.config(text=f"Promedio: {calculadora.calcular_promedio():.2f}")
            self.lbl_desviacion.config(text=f"Desviación estándar: {calculadora.calcular_desviacion_estandar():.2f}")
            self.lbl_mayor.config(text=f"Mayor nota: {calculadora.calcular_mayor():.2f}")
            self.lbl_menor.config(text=f"Menor nota: {calculadora.calcular_menor():.2f}")
            
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")

    def action_limpiar(self):
        """Limpia la interfaz."""
        for entry in self.entradas_notas:
            entry.delete(0, tk.END)
        self.lbl_promedio.config(text="Promedio: ")
        self.lbl_desviacion.config(text="Desviación estándar: ")
        self.lbl_mayor.config(text="Mayor nota: ")
        self.lbl_menor.config(text="Menor nota: ")

# ==========================================
# BLOQUE PRINCIPAL
# ==========================================
if __name__ == "__main__":
    app = VentanaNotas()
    app.mainloop()