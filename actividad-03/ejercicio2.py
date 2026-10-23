import tkinter as tk
from tkinter import messagebox, ttk
import math

# ==========================================
# JERARQUÍA DE CLASES (Lógica del Negocio)
# ==========================================

class FiguraGeometrica:
    """Clase base que almacena los resultados de los cálculos."""
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

    def get_volumen(self):
        return self.volumen

    def get_superficie(self):
        return self.superficie

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.calcular_volumen()
        self.calcular_superficie()

    def calcular_volumen(self):
        # Fórmula: π * r² * h
        self.volumen = math.pi * (self.radio ** 2) * self.altura

    def calcular_superficie(self):
        # Fórmula: 2πrh + 2πr²
        self.superficie = (2 * math.pi * self.radio * self.altura) + (2 * math.pi * (self.radio ** 2))

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.calcular_volumen()
        self.calcular_superficie()

    def calcular_volumen(self):
        # Fórmula: 4/3 * π * r³
        self.volumen = (4.0 / 3.0) * math.pi * (self.radio ** 3)

    def calcular_superficie(self):
        # Fórmula: 4 * π * r²
        self.superficie = 4.0 * math.pi * (self.radio ** 2)

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.calcular_volumen()
        self.calcular_superficie()

    def calcular_volumen(self):
        # Fórmula: (base² * altura) / 3
        self.volumen = ((self.base ** 2) * self.altura) / 3.0

    def calcular_superficie(self):
        # Fórmula: base² + 2 * base * apotema
        self.superficie = (self.base ** 2) + (2.0 * self.base * self.apotema)

class Cubo(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado
        self.calcular_volumen()
        self.calcular_superficie()

    def calcular_volumen(self):
        # Fórmula: lado³
        self.volumen = self.lado ** 3

    def calcular_superficie(self):
        # Fórmula: 6 * lado²
        self.superficie = 6.0 * (self.lado ** 2)

class Prisma(FiguraGeometrica):
    """Prisma rectangular definido por su largo, ancho y altura."""
    def __init__(self, largo, ancho, altura):
        super().__init__()
        self.largo = largo
        self.ancho = ancho
        self.altura = altura
        self.calcular_volumen()
        self.calcular_superficie()

    def calcular_volumen(self):
        # Fórmula: largo * ancho * altura
        self.volumen = self.largo * self.ancho * self.altura

    def calcular_superficie(self):
        # Fórmula: 2 * (largo*ancho + largo*altura + ancho*altura)
        self.superficie = 2.0 * ((self.largo * self.ancho) +
                                 (self.largo * self.altura) +
                                 (self.ancho * self.altura))


# ==========================================
# IMÁGENES DE LAS FIGURAS (dibujadas con Canvas)
# ==========================================

COLOR_FONDO = "#e3f2fd"
COLOR_BORDE = "#0d47a1"
COLOR_RELLENO = "#90caf9"

def configurar_estilos(ventana):
    """Define el estilo azul de los botones.

    Se usa ttk con el tema "clam" porque los botones tk no admiten colores
    de fondo en macOS y el texto blanco quedaría ilegible.
    """
    estilo = ttk.Style(ventana)
    estilo.theme_use("clam")
    estilo.configure("Menu.TButton", background="#1976d2", foreground="white",
                     font=("Arial", 10, "bold"), borderwidth=0, focuscolor="#1976d2")
    estilo.map("Menu.TButton", background=[("active", "#0d47a1")])
    estilo.configure("Calcular.TButton", background="#2196f3", foreground="white",
                     font=("Arial", 10, "bold"), borderwidth=0, focuscolor="#2196f3")
    estilo.map("Calcular.TButton", background=[("active", "#1565c0")])

def dibujar_figura(canvas, tipo):
    """Dibuja sobre el canvas la imagen de la figura geométrica indicada."""
    estilo = {"outline": COLOR_BORDE, "fill": COLOR_RELLENO, "width": 2}

    if tipo == "cilindro":
        canvas.create_oval(40, 85, 120, 105, **estilo)
        canvas.create_rectangle(40, 25, 120, 95, outline="", fill=COLOR_RELLENO)
        canvas.create_line(40, 25, 40, 95, fill=COLOR_BORDE, width=2)
        canvas.create_line(120, 25, 120, 95, fill=COLOR_BORDE, width=2)
        canvas.create_oval(40, 15, 120, 35, **estilo)

    elif tipo == "esfera":
        canvas.create_oval(40, 20, 120, 100, **estilo)
        canvas.create_oval(40, 50, 120, 70, outline=COLOR_BORDE, width=1)

    elif tipo == "piramide":
        canvas.create_polygon(80, 15, 35, 85, 125, 85,
                              outline=COLOR_BORDE, fill=COLOR_RELLENO, width=2)
        canvas.create_oval(35, 75, 125, 95, outline=COLOR_BORDE, fill=COLOR_RELLENO, width=2)
        canvas.create_line(80, 15, 80, 85, fill=COLOR_BORDE, width=1, dash=(3, 2))

    elif tipo == "cubo":
        canvas.create_polygon(45, 40, 70, 20, 130, 20, 105, 40,
                              outline=COLOR_BORDE, fill=COLOR_RELLENO, width=2)
        canvas.create_polygon(105, 40, 130, 20, 130, 80, 105, 100,
                              outline=COLOR_BORDE, fill=COLOR_RELLENO, width=2)
        canvas.create_rectangle(45, 40, 105, 100, **estilo)

    elif tipo == "prisma":
        canvas.create_polygon(35, 45, 60, 25, 140, 25, 115, 45,
                              outline=COLOR_BORDE, fill=COLOR_RELLENO, width=2)
        canvas.create_polygon(115, 45, 140, 25, 140, 75, 115, 95,
                              outline=COLOR_BORDE, fill=COLOR_RELLENO, width=2)
        canvas.create_rectangle(35, 45, 115, 95, **estilo)


# ==========================================
# INTERFAZ GRÁFICA (Tkinter)
# ==========================================

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas")
        self.geometry("300x340")
        self.configure(bg=COLOR_FONDO) # Fondo azul claro
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')

        # Estilo para botones
        configurar_estilos(self)
        btn_style = {"width": 15, "style": "Menu.TButton"}

        tk.Label(self, text="Seleccione una figura:", font=("Arial", 12, "bold"),
                 bg=COLOR_FONDO, fg=COLOR_BORDE).pack(pady=20)

        ttk.Button(self, text="Cilindro", command=self.abrir_cilindro, **btn_style).pack(pady=5)
        ttk.Button(self, text="Esfera", command=self.abrir_esfera, **btn_style).pack(pady=5)
        ttk.Button(self, text="Pirámide", command=self.abrir_piramide, **btn_style).pack(pady=5)
        ttk.Button(self, text="Cubo", command=self.abrir_cubo, **btn_style).pack(pady=5)
        ttk.Button(self, text="Prisma", command=self.abrir_prisma, **btn_style).pack(pady=5)

    def abrir_cilindro(self): VentanaCilindro(self)
    def abrir_esfera(self): VentanaEsfera(self)
    def abrir_piramide(self): VentanaPiramide(self)
    def abrir_cubo(self): VentanaCubo(self)
    def abrir_prisma(self): VentanaPrisma(self)

class VentanaFigura(tk.Toplevel):
    """Ventana base: muestra la imagen de la figura y sus campos de entrada."""
    def __init__(self, parent, titulo, tipo, etiquetas, alto):
        super().__init__(parent)
        self.title(titulo)
        self.geometry(f"280x{alto}")
        self.configure(bg=COLOR_FONDO)

        # Imagen de la figura geométrica
        canvas = tk.Canvas(self, width=160, height=120, bg=COLOR_FONDO, highlightthickness=0)
        canvas.pack(pady=5)
        dibujar_figura(canvas, tipo)

        # Un campo de entrada por cada dato solicitado
        self.entradas = []
        for etiqueta in etiquetas:
            tk.Label(self, text=etiqueta, bg=COLOR_FONDO).pack(pady=2)
            txt_entry = tk.Entry(self)
            txt_entry.pack()
            self.entradas.append(txt_entry)

        ttk.Button(self, text="Calcular", command=self.calcular,
                   style="Calcular.TButton").pack(pady=10)

        self.lbl_volumen = tk.Label(self, text="Volumen: ", bg=COLOR_FONDO)
        self.lbl_volumen.pack()
        self.lbl_superficie = tk.Label(self, text="Superficie: ", bg=COLOR_FONDO)
        self.lbl_superficie.pack()

    def crear_figura(self, valores):
        """Cada ventana construye su propia figura con los valores ingresados."""
        raise NotImplementedError

    def calcular(self):
        try:
            valores = [float(entrada.get()) for entrada in self.entradas]
            figura = self.crear_figura(valores)
            self.lbl_volumen.config(text=f"Volumen: {figura.get_volumen():.2f} cm³")
            self.lbl_superficie.config(text=f"Superficie: {figura.get_superficie():.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

class VentanaCilindro(VentanaFigura):
    def __init__(self, parent):
        super().__init__(parent, "Cilindro", "cilindro",
                         ["Radio (cm):", "Altura (cm):"], 370)

    def crear_figura(self, valores):
        return Cilindro(valores[0], valores[1])

class VentanaEsfera(VentanaFigura):
    def __init__(self, parent):
        super().__init__(parent, "Esfera", "esfera",
                         ["Radio (cm):"], 320)

    def crear_figura(self, valores):
        return Esfera(valores[0])

class VentanaPiramide(VentanaFigura):
    def __init__(self, parent):
        super().__init__(parent, "Pirámide", "piramide",
                         ["Base (cm):", "Altura (cm):", "Apotema (cm):"], 420)

    def crear_figura(self, valores):
        return Piramide(valores[0], valores[1], valores[2])

class VentanaCubo(VentanaFigura):
    def __init__(self, parent):
        super().__init__(parent, "Cubo", "cubo",
                         ["Lado (cm):"], 320)

    def crear_figura(self, valores):
        return Cubo(valores[0])

class VentanaPrisma(VentanaFigura):
    def __init__(self, parent):
        super().__init__(parent, "Prisma", "prisma",
                         ["Largo (cm):", "Ancho (cm):", "Altura (cm):"], 420)

    def crear_figura(self, valores):
        return Prisma(valores[0], valores[1], valores[2])

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
