import tkinter as tk
from tkinter import ttk

# ==========================================
# CLASE LÓGICA (Modelo)
# ==========================================
class PruebaExcepciones:
    """Reproduce los dos bloques try del ejercicio y guarda, en orden,
    los mensajes que el programa va imprimiendo."""

    def __init__(self):
        self.mensajes = []

    def ejecutar(self):
        self.mensajes = []

        # Primer bloque try: se provoca una división por cero
        try:
            self.mensajes.append("Ingresando al primer try")
            cociente = 10000 / 0
            # Esta instrucción nunca se ejecuta
            self.mensajes.append("Después de la división")
        except ZeroDivisionError:
            self.mensajes.append("División por cero")
        finally:
            # El bloque finally siempre se ejecuta, ocurra o no la excepción
            self.mensajes.append("Ingresando al primer finally")

        # Segundo bloque try: se usa un objeto nulo
        try:
            self.mensajes.append("Ingresando al segundo try")
            objeto = None
            objeto.upper()
            # Esta instrucción nunca se ejecuta
            self.mensajes.append("Imprimiendo objeto")
        except ZeroDivisionError:
            # La excepción lanzada no es de este tipo, así que no entra aquí
            self.mensajes.append("División por cero")
        except Exception:
            self.mensajes.append("Ocurrió una excepción")
        finally:
            self.mensajes.append("Ingresando al segundo finally")

        return self.mensajes

# ==========================================
# CLASE INTERFAZ GRÁFICA (Vista/Controlador)
# ==========================================
class VentanaPrueba(tk.Tk):
    """Ventana que ejecuta el programa y muestra su salida en pantalla."""

    def __init__(self):
        super().__init__()

        # Paleta de colores azul
        self.color_fondo = "#e3f2fd"
        self.color_texto = "#0d47a1"

        self.title("Prueba de Excepciones")
        self.geometry("420x320")
        self.resizable(False, False)
        self.configure(bg=self.color_fondo)

        self._crear_componentes()
        self.eval('tk::PlaceWindow . center')

    def _crear_componentes(self):
        tk.Label(self, text="Resultado de la ejecución del programa:",
                 bg=self.color_fondo, fg=self.color_texto,
                 font=("Arial", 11, "bold")).pack(pady=10)

        # Área donde se muestran los mensajes, en el orden en que se imprimen
        self.txt_salida = tk.Text(self, height=9, width=46, bd=1, relief="solid")
        self.txt_salida.pack(padx=20)
        self.txt_salida.config(state="disabled")

        # Botones con estilo azul.
        # Se usa ttk con el tema "clam" porque los botones tk no admiten
        # colores de fondo en macOS y quedarían ilegibles.
        estilo = ttk.Style(self)
        estilo.theme_use("clam")
        estilo.configure("Ejecutar.TButton", background="#2196f3", foreground="white",
                         font=("Arial", 9, "bold"), borderwidth=0, focuscolor="#2196f3")
        estilo.map("Ejecutar.TButton", background=[("active", "#1565c0")])
        estilo.configure("Limpiar.TButton", background="#1976d2", foreground="white",
                         font=("Arial", 9, "bold"), borderwidth=0, focuscolor="#1976d2")
        estilo.map("Limpiar.TButton", background=[("active", "#0d47a1")])

        marco = tk.Frame(self, bg=self.color_fondo)
        marco.pack(pady=15)
        ttk.Button(marco, text="Ejecutar", command=self.action_ejecutar,
                   style="Ejecutar.TButton", width=14).pack(side="left", padx=5)
        ttk.Button(marco, text="Limpiar", command=self.action_limpiar,
                   style="Limpiar.TButton", width=14).pack(side="left", padx=5)

    def action_ejecutar(self):
        """Ejecuta el programa y escribe sus mensajes en la ventana."""
        prueba = PruebaExcepciones()
        mensajes = prueba.ejecutar()

        self.txt_salida.config(state="normal")
        self.txt_salida.delete("1.0", tk.END)
        for mensaje in mensajes:
            self.txt_salida.insert(tk.END, mensaje + "\n")
        self.txt_salida.config(state="disabled")

    def action_limpiar(self):
        """Deja la ventana en su estado inicial."""
        self.txt_salida.config(state="normal")
        self.txt_salida.delete("1.0", tk.END)
        self.txt_salida.config(state="disabled")

# ==========================================
# BLOQUE PRINCIPAL
# ==========================================
if __name__ == "__main__":
    app = VentanaPrueba()
    app.mainloop()
