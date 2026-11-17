import tkinter as tk
from tkinter import messagebox, ttk

# ==========================================
# CLASES LÓGICAS (Modelo)
# ==========================================
class Programador:
    """Integrante del equipo. Valida que su nombre y apellidos sean
    solo texto y que no lleguen a 20 caracteres."""

    LONGITUD_MAXIMA = 20

    def __init__(self, nombre, apellidos):
        self.validar_campo(nombre, "nombre")
        self.validar_campo(apellidos, "apellidos")
        self.nombre = nombre
        self.apellidos = apellidos

    def validar_campo(self, texto, etiqueta):
        """Lanza una excepción si el campo tiene dígitos o es muy largo."""
        if not texto:
            raise ValueError(f"El campo {etiqueta} no puede estar vacío")
        for caracter in texto:
            if caracter.isdigit():
                raise ValueError(f"El campo {etiqueta} solo admite texto")
        if len(texto) >= self.LONGITUD_MAXIMA:
            raise ValueError(f"El campo {etiqueta} no puede tener "
                             f"{self.LONGITUD_MAXIMA} caracteres o más")

class EquipoMaratonProgramacion:
    """Equipo que participa en la maratón. Admite mínimo dos
    programadores y máximo tres."""

    MINIMO = 2
    MAXIMO = 3

    def __init__(self, nombre, universidad, lenguaje, tamano):
        if tamano < self.MINIMO or tamano > self.MAXIMO:
            raise ValueError(f"El equipo debe tener entre {self.MINIMO} "
                             f"y {self.MAXIMO} programadores")
        self.nombre = nombre
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.tamano = tamano
        self.programadores = []

    def esta_completo(self):
        """Indica si ya se alcanzó el tamaño definido para el equipo."""
        return len(self.programadores) == self.tamano

    def anadir_programador(self, programador):
        """Agrega un programador. Lanza una excepción si el equipo está lleno."""
        if self.esta_completo():
            raise ValueError("El equipo ya está completo, no admite más programadores")
        self.programadores.append(programador)

# ==========================================
# CLASE INTERFAZ GRÁFICA (Vista/Controlador)
# ==========================================
class VentanaEquipo(tk.Tk):
    """Ventana que crea el equipo y le añade sus programadores."""

    def __init__(self):
        super().__init__()

        # Paleta de colores azul
        self.color_fondo = "#e3f2fd"
        self.color_texto = "#0d47a1"

        self.title("Equipo Maratón de Programación")
        self.geometry("420x470")
        self.resizable(False, False)
        self.configure(bg=self.color_fondo)

        self.equipo = None

        self._crear_estilos()
        self._crear_componentes()
        self.eval('tk::PlaceWindow . center')

    def _crear_estilos(self):
        # Se usa ttk con el tema "clam" porque los botones tk no admiten
        # colores de fondo en macOS y quedarían ilegibles.
        estilo = ttk.Style(self)
        estilo.theme_use("clam")
        estilo.configure("Azul.TButton", background="#2196f3", foreground="white",
                         font=("Arial", 9, "bold"), borderwidth=0, focuscolor="#2196f3")
        estilo.map("Azul.TButton", background=[("active", "#1565c0")])
        estilo.configure("AzulOscuro.TButton", background="#1976d2", foreground="white",
                         font=("Arial", 9, "bold"), borderwidth=0, focuscolor="#1976d2")
        estilo.map("AzulOscuro.TButton", background=[("active", "#0d47a1")])

    def _crear_componentes(self):
        titulo_style = {"bg": self.color_fondo, "fg": self.color_texto,
                        "font": ("Arial", 11, "bold"), "anchor": "w"}
        campo_style = {"bg": self.color_fondo, "fg": self.color_texto, "anchor": "w"}

        # --- Datos del equipo ---
        tk.Label(self, text="Datos del equipo", **titulo_style).place(x=20, y=15, width=200, height=25)

        etiquetas_equipo = ["Nombre:", "Universidad:", "Lenguaje:", "Tamaño (2 o 3):"]
        self.entradas_equipo = []
        for i, texto in enumerate(etiquetas_equipo):
            tk.Label(self, text=texto, **campo_style).place(x=20, y=50 + (i * 32), width=110, height=25)
            txt_entry = tk.Entry(self, bd=1, relief="solid")
            txt_entry.place(x=140, y=50 + (i * 32), width=250, height=25)
            self.entradas_equipo.append(txt_entry)

        ttk.Button(self, text="Crear equipo", command=self.action_crear_equipo,
                   style="AzulOscuro.TButton").place(x=140, y=185, width=250, height=30)

        # --- Programadores ---
        tk.Label(self, text="Añadir programador", **titulo_style).place(x=20, y=230, width=220, height=25)

        etiquetas_programador = ["Nombre:", "Apellidos:"]
        self.entradas_programador = []
        for i, texto in enumerate(etiquetas_programador):
            tk.Label(self, text=texto, **campo_style).place(x=20, y=265 + (i * 32), width=110, height=25)
            txt_entry = tk.Entry(self, bd=1, relief="solid")
            txt_entry.place(x=140, y=265 + (i * 32), width=250, height=25)
            self.entradas_programador.append(txt_entry)

        ttk.Button(self, text="Añadir", command=self.action_anadir,
                   style="Azul.TButton").place(x=140, y=335, width=250, height=30)

        # --- Estado del equipo ---
        self.lbl_estado = tk.Label(self, text="Primero cree el equipo.",
                                   justify="left", **campo_style)
        self.lbl_estado.place(x=20, y=380, width=380, height=75)

    def action_crear_equipo(self):
        """Crea el equipo con los datos ingresados."""
        nombre, universidad, lenguaje, tamano_texto = [e.get().strip() for e in self.entradas_equipo]

        if not nombre or not universidad or not lenguaje or not tamano_texto:
            messagebox.showwarning("Datos incompletos",
                                   "Debe diligenciar los cuatro datos del equipo.")
            return

        try:
            tamano = int(tamano_texto)
        except ValueError:
            messagebox.showerror("Error", "El tamaño debe ser un número entero.")
            return

        try:
            self.equipo = EquipoMaratonProgramacion(nombre, universidad, lenguaje, tamano)
            self.mostrar_estado()
        except ValueError as excepcion:
            self.equipo = None
            messagebox.showerror("Tamaño no válido", str(excepcion))

    def action_anadir(self):
        """Añade un programador al equipo, validando sus datos."""
        if self.equipo is None:
            messagebox.showwarning("Sin equipo", "Primero debe crear el equipo.")
            return

        nombre, apellidos = [e.get().strip() for e in self.entradas_programador]

        try:
            programador = Programador(nombre, apellidos)
            self.equipo.anadir_programador(programador)
            for entrada in self.entradas_programador:
                entrada.delete(0, tk.END)
            self.mostrar_estado()
        except ValueError as excepcion:
            # Una misma excepción cubre los datos inválidos y el equipo lleno
            messagebox.showerror("No se pudo añadir", str(excepcion))

    def mostrar_estado(self):
        """Muestra los datos del equipo y la lista de sus programadores."""
        lineas = [f"Equipo {self.equipo.nombre} · {self.equipo.universidad}",
                  f"Lenguaje: {self.equipo.lenguaje} · "
                  f"{len(self.equipo.programadores)} de {self.equipo.tamano} programadores"]

        for programador in self.equipo.programadores:
            lineas.append(f"  - {programador.nombre} {programador.apellidos}")

        if self.equipo.esta_completo():
            lineas.append("El equipo está completo.")

        self.lbl_estado.config(text="\n".join(lineas))

# ==========================================
# BLOQUE PRINCIPAL
# ==========================================
if __name__ == "__main__":
    app = VentanaEquipo()
    app.mainloop()
