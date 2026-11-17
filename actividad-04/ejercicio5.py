import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os

# ==========================================
# CLASE LÓGICA (Modelo)
# ==========================================
class LeerArchivo:
    """Lee un archivo de texto y entrega su contenido.
    Gestiona los errores de entrada y salida."""

    def __init__(self, ruta):
        self.ruta = ruta

    def leer(self):
        """Retorna el contenido del archivo.
        Lanza una excepción si no existe o no se puede leer."""
        archivo = None
        try:
            archivo = open(self.ruta, "r", encoding="utf-8")
            return archivo.read()
        except FileNotFoundError:
            raise IOError(f"No se encontró el archivo: {self.ruta}")
        except OSError:
            raise IOError(f"No se pudo leer el archivo: {self.ruta}")
        finally:
            # El archivo se cierra siempre, ocurra o no una excepción
            if archivo is not None:
                archivo.close()

# ==========================================
# CLASE INTERFAZ GRÁFICA (Vista/Controlador)
# ==========================================
class VentanaLector(tk.Tk):
    """Ventana que permite escoger un archivo de texto y ver su contenido."""

    ARCHIVO_POR_DEFECTO = "prueba.txt"

    def __init__(self):
        super().__init__()

        # Paleta de colores azul
        self.color_fondo = "#e3f2fd"
        self.color_texto = "#0d47a1"

        self.title("Lector de Archivos")
        self.geometry("460x370")
        self.resizable(False, False)
        self.configure(bg=self.color_fondo)

        self._crear_componentes()
        self.eval('tk::PlaceWindow . center')

    def _crear_componentes(self):
        self.lbl_ruta = tk.Label(self, text="Ningún archivo abierto",
                                 bg=self.color_fondo, fg=self.color_texto,
                                 anchor="w", font=("Arial", 10, "bold"))
        self.lbl_ruta.place(x=20, y=15, width=420, height=25)

        # Área donde se muestra el contenido del archivo
        self.txt_contenido = tk.Text(self, bd=1, relief="solid")
        self.txt_contenido.place(x=20, y=50, width=420, height=230)
        self.txt_contenido.config(state="disabled")

        # Botones con estilo azul.
        # Se usa ttk con el tema "clam" porque los botones tk no admiten
        # colores de fondo en macOS y quedarían ilegibles.
        estilo = ttk.Style(self)
        estilo.theme_use("clam")
        estilo.configure("Abrir.TButton", background="#2196f3", foreground="white",
                         font=("Arial", 9, "bold"), borderwidth=0, focuscolor="#2196f3")
        estilo.map("Abrir.TButton", background=[("active", "#1565c0")])
        estilo.configure("Prueba.TButton", background="#1976d2", foreground="white",
                         font=("Arial", 9, "bold"), borderwidth=0, focuscolor="#1976d2")
        estilo.map("Prueba.TButton", background=[("active", "#0d47a1")])

        ttk.Button(self, text="Abrir archivo", command=self.action_abrir,
                   style="Abrir.TButton").place(x=20, y=300, width=200, height=30)
        ttk.Button(self, text="Leer prueba.txt", command=self.action_leer_prueba,
                   style="Prueba.TButton").place(x=240, y=300, width=200, height=30)

    def action_abrir(self):
        """Permite escoger un archivo de texto del sistema de archivos."""
        ruta = filedialog.askopenfilename(
            title="Seleccione un archivo de texto",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        if ruta:
            self.mostrar_archivo(ruta)

    def action_leer_prueba(self):
        """Lee el archivo prueba.txt que acompaña al ejercicio."""
        carpeta = os.path.dirname(os.path.abspath(__file__))
        self.mostrar_archivo(os.path.join(carpeta, self.ARCHIVO_POR_DEFECTO))

    def mostrar_archivo(self, ruta):
        """Muestra el contenido del archivo o la excepción generada."""
        lector = LeerArchivo(ruta)
        try:
            contenido = lector.leer()
        except IOError as excepcion:
            self.lbl_ruta.config(text="Ningún archivo abierto")
            self.escribir("")
            messagebox.showerror("Error de lectura", str(excepcion))
            return

        self.lbl_ruta.config(text="Archivo: " + os.path.basename(ruta))
        self.escribir(contenido)

    def escribir(self, texto):
        """Vuelca un texto en el área de contenido."""
        self.txt_contenido.config(state="normal")
        self.txt_contenido.delete("1.0", tk.END)
        self.txt_contenido.insert(tk.END, texto)
        self.txt_contenido.config(state="disabled")

# ==========================================
# BLOQUE PRINCIPAL
# ==========================================
if __name__ == "__main__":
    app = VentanaLector()
    app.mainloop()
