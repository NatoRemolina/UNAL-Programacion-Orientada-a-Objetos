import tkinter as tk
from tkinter import messagebox, ttk

# ==========================================
# CLASE LÓGICA (Modelo)
# ==========================================
class Vendedor:
    """Modela un vendedor y valida su edad antes de crear el objeto."""

    def __init__(self, nombre, apellidos, edad):
        # La edad se verifica primero: si no es válida, el objeto no se crea
        self.verificar_edad(edad)
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def verificar_edad(self, edad):
        """Lanza una excepción si la edad no cumple los requisitos."""
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120")
        if edad <= 18:
            raise ValueError("El vendedor debe ser mayor de 18 años")

    def imprimir(self):
        """Retorna los valores de los atributos del vendedor."""
        return (f"Nombre: {self.nombre}\n"
                f"Apellidos: {self.apellidos}\n"
                f"Edad: {self.edad} años")

# ==========================================
# CLASE INTERFAZ GRÁFICA (Vista/Controlador)
# ==========================================
class VentanaVendedor(tk.Tk):
    """Ventana que solicita los datos del vendedor y muestra el resultado."""

    def __init__(self):
        super().__init__()

        # Paleta de colores azul
        self.color_fondo = "#e3f2fd"
        self.color_texto = "#0d47a1"

        self.title("Registro de Vendedor")
        self.geometry("320x330")
        self.resizable(False, False)
        self.configure(bg=self.color_fondo)

        self._crear_componentes()
        self.eval('tk::PlaceWindow . center')

    def _crear_componentes(self):
        etiquetas = ["Nombre:", "Apellidos:", "Edad:"]
        self.entradas = []

        for i, texto in enumerate(etiquetas):
            tk.Label(self, text=texto, anchor="w", bg=self.color_fondo,
                     fg=self.color_texto, font=("Arial", 10, "bold")
                     ).place(x=20, y=25 + (i * 35), width=80, height=25)

            txt_entry = tk.Entry(self, bd=1, relief="solid")
            txt_entry.place(x=110, y=25 + (i * 35), width=180, height=25)
            self.entradas.append(txt_entry)

        # Botones con estilo azul.
        # Se usa ttk con el tema "clam" porque los botones tk no admiten
        # colores de fondo en macOS y quedarían ilegibles.
        estilo = ttk.Style(self)
        estilo.theme_use("clam")
        estilo.configure("Registrar.TButton", background="#2196f3", foreground="white",
                         font=("Arial", 9, "bold"), borderwidth=0, focuscolor="#2196f3")
        estilo.map("Registrar.TButton", background=[("active", "#1565c0")])
        estilo.configure("Limpiar.TButton", background="#1976d2", foreground="white",
                         font=("Arial", 9, "bold"), borderwidth=0, focuscolor="#1976d2")
        estilo.map("Limpiar.TButton", background=[("active", "#0d47a1")])

        ttk.Button(self, text="Registrar", command=self.action_registrar,
                   style="Registrar.TButton").place(x=20, y=145, width=130, height=30)
        ttk.Button(self, text="Limpiar", command=self.action_limpiar,
                   style="Limpiar.TButton").place(x=160, y=145, width=130, height=30)

        self.lbl_resultado = tk.Label(self, text="", bg=self.color_fondo,
                                      fg=self.color_texto, justify="left", anchor="nw")
        self.lbl_resultado.place(x=20, y=195, width=270, height=110)

    def action_registrar(self):
        """Crea el vendedor y muestra sus datos, o la excepción generada."""
        nombre, apellidos, edad_texto = [e.get().strip() for e in self.entradas]

        if not nombre or not apellidos or not edad_texto:
            messagebox.showwarning("Datos incompletos",
                                   "Debe diligenciar los tres campos.")
            return

        try:
            # La edad debe ser un número entero
            edad = int(edad_texto)
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número entero.")
            return

        try:
            vendedor = Vendedor(nombre, apellidos, edad)
            self.lbl_resultado.config(text="Vendedor registrado\n\n" + vendedor.imprimir())
        except ValueError as excepcion:
            # Se captura la excepción lanzada por verificar_edad
            self.lbl_resultado.config(text="")
            messagebox.showerror("Edad no válida", str(excepcion))

    def action_limpiar(self):
        """Deja la ventana en su estado inicial."""
        for entrada in self.entradas:
            entrada.delete(0, tk.END)
        self.lbl_resultado.config(text="")

# ==========================================
# BLOQUE PRINCIPAL
# ==========================================
if __name__ == "__main__":
    app = VentanaVendedor()
    app.mainloop()
