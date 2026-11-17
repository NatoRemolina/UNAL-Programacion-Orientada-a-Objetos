import tkinter as tk
from tkinter import messagebox, ttk
import math

# ==========================================
# CLASE LÓGICA (Modelo)
# ==========================================
class CalculosNumericos:
    """Realiza dos cálculos matemáticos con métodos estáticos.
    Si el valor recibido no es positivo se genera una excepción aritmética."""

    @staticmethod
    def logaritmo_neperiano(valor):
        if valor <= 0:
            raise ArithmeticError("El logaritmo solo existe para valores positivos")
        return math.log(valor)

    @staticmethod
    def raiz_cuadrada(valor):
        if valor <= 0:
            raise ArithmeticError("La raíz cuadrada solo se calcula para valores positivos")
        return math.sqrt(valor)

# ==========================================
# CLASE INTERFAZ GRÁFICA (Vista/Controlador)
# ==========================================
class VentanaCalculos(tk.Tk):
    """Ventana que solicita un valor y muestra sus dos cálculos."""

    def __init__(self):
        super().__init__()

        # Paleta de colores azul
        self.color_fondo = "#e3f2fd"
        self.color_texto = "#0d47a1"

        self.title("Cálculos Numéricos")
        self.geometry("330x250")
        self.resizable(False, False)
        self.configure(bg=self.color_fondo)

        self._crear_componentes()
        self.eval('tk::PlaceWindow . center')

    def _crear_componentes(self):
        tk.Label(self, text="Valor:", anchor="w", bg=self.color_fondo,
                 fg=self.color_texto, font=("Arial", 10, "bold")
                 ).place(x=20, y=30, width=60, height=25)

        self.txt_valor = tk.Entry(self, bd=1, relief="solid")
        self.txt_valor.place(x=90, y=30, width=210, height=25)

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

        ttk.Button(self, text="Calcular", command=self.action_calcular,
                   style="Calcular.TButton").place(x=20, y=80, width=135, height=30)
        ttk.Button(self, text="Limpiar", command=self.action_limpiar,
                   style="Limpiar.TButton").place(x=165, y=80, width=135, height=30)

        resultado_style = {"bg": self.color_fondo, "fg": self.color_texto, "anchor": "w"}

        self.lbl_logaritmo = tk.Label(self, text="Logaritmo neperiano: ", **resultado_style)
        self.lbl_logaritmo.place(x=20, y=140, width=280, height=25)

        self.lbl_raiz = tk.Label(self, text="Raíz cuadrada: ", **resultado_style)
        self.lbl_raiz.place(x=20, y=175, width=280, height=25)

    def action_calcular(self):
        """Calcula ambos resultados y gestiona las excepciones posibles."""
        try:
            # Si el texto no es numérico se genera una excepción de conversión
            valor = float(self.txt_valor.get())
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un valor numérico.")
            return

        try:
            logaritmo = CalculosNumericos.logaritmo_neperiano(valor)
            raiz = CalculosNumericos.raiz_cuadrada(valor)
            self.lbl_logaritmo.config(text=f"Logaritmo neperiano: {logaritmo:.4f}")
            self.lbl_raiz.config(text=f"Raíz cuadrada: {raiz:.4f}")
        except ArithmeticError as excepcion:
            # Se captura la excepción aritmética lanzada por la clase
            self.action_limpiar(conservar_valor=True)
            messagebox.showerror("Excepción aritmética", str(excepcion))

    def action_limpiar(self, conservar_valor=False):
        """Deja la ventana en su estado inicial."""
        if not conservar_valor:
            self.txt_valor.delete(0, tk.END)
        self.lbl_logaritmo.config(text="Logaritmo neperiano: ")
        self.lbl_raiz.config(text="Raíz cuadrada: ")

# ==========================================
# BLOQUE PRINCIPAL
# ==========================================
if __name__ == "__main__":
    app = VentanaCalculos()
    app.mainloop()
