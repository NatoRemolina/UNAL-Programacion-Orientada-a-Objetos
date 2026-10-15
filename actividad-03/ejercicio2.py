import tkinter as tk
from tkinter import messagebox
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


# ==========================================
# INTERFAZ GRÁFICA (Tkinter)
# ==========================================

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas")
        self.geometry("300x250")
        self.configure(bg="#e3f2fd") # Fondo azul claro
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')

        # Estilo para botones
        btn_style = {"width": 15, "bg": "#1976d2", "fg": "white", "font": ("Arial", 10, "bold")}

        tk.Label(self, text="Seleccione una figura:", font=("Arial", 12, "bold"), 
                 bg="#e3f2fd", fg="#0d47a1").pack(pady=20)

        tk.Button(self, text="Cilindro", command=self.abrir_cilindro, **btn_style).pack(pady=5)
        tk.Button(self, text="Esfera", command=self.abrir_esfera, **btn_style).pack(pady=5)
        tk.Button(self, text="Pirámide", command=self.abrir_piramide, **btn_style).pack(pady=5)

    def abrir_cilindro(self): VentanaCilindro(self)
    def abrir_esfera(self): VentanaEsfera(self)
    def abrir_piramide(self): VentanaPiramide(self)

class VentanaCilindro(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Cilindro")
        self.geometry("280x250")
        self.configure(bg="#e3f2fd")
        
        tk.Label(self, text="Radio (cm):", bg="#e3f2fd").pack(pady=5)
        self.txt_radio = tk.Entry(self)
        self.txt_radio.pack()

        tk.Label(self, text="Altura (cm):", bg="#e3f2fd").pack(pady=5)
        self.txt_altura = tk.Entry(self)
        self.txt_altura.pack()

        tk.Button(self, text="Calcular", command=self.calcular, bg="#2196f3", fg="white").pack(pady=15)

        self.lbl_volumen = tk.Label(self, text="Volumen: ", bg="#e3f2fd")
        self.lbl_volumen.pack()
        self.lbl_superficie = tk.Label(self, text="Superficie: ", bg="#e3f2fd")
        self.lbl_superficie.pack()

    def calcular(self):
        try:
            cilindro = Cilindro(float(self.txt_radio.get()), float(self.txt_altura.get()))
            self.lbl_volumen.config(text=f"Volumen: {cilindro.get_volumen():.2f} cm³")
            self.lbl_superficie.config(text=f"Superficie: {cilindro.get_superficie():.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

class VentanaEsfera(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Esfera")
        self.geometry("280x200")
        self.configure(bg="#e3f2fd")

        tk.Label(self, text="Radio (cm):", bg="#e3f2fd").pack(pady=5)
        self.txt_radio = tk.Entry(self)
        self.txt_radio.pack()

        tk.Button(self, text="Calcular", command=self.calcular, bg="#2196f3", fg="white").pack(pady=15)

        self.lbl_volumen = tk.Label(self, text="Volumen: ", bg="#e3f2fd")
        self.lbl_volumen.pack()
        self.lbl_superficie = tk.Label(self, text="Superficie: ", bg="#e3f2fd")
        self.lbl_superficie.pack()

    def calcular(self):
        try:
            esfera = Esfera(float(self.txt_radio.get()))
            self.lbl_volumen.config(text=f"Volumen: {esfera.get_volumen():.2f} cm³")
            self.lbl_superficie.config(text=f"Superficie: {esfera.get_superficie():.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

class VentanaPiramide(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Pirámide")
        self.geometry("280x300")
        self.configure(bg="#e3f2fd")

        tk.Label(self, text="Base (cm):", bg="#e3f2fd").pack(pady=5)
        self.txt_base = tk.Entry(self)
        self.txt_base.pack()

        tk.Label(self, text="Altura (cm):", bg="#e3f2fd").pack(pady=5)
        self.txt_altura = tk.Entry(self)
        self.txt_altura.pack()

        tk.Label(self, text="Apotema (cm):", bg="#e3f2fd").pack(pady=5)
        self.txt_apotema = tk.Entry(self)
        self.txt_apotema.pack()

        tk.Button(self, text="Calcular", command=self.calcular, bg="#2196f3", fg="white").pack(pady=15)

        self.lbl_volumen = tk.Label(self, text="Volumen: ", bg="#e3f2fd")
        self.lbl_volumen.pack()
        self.lbl_superficie = tk.Label(self, text="Superficie: ", bg="#e3f2fd")
        self.lbl_superficie.pack()

    def calcular(self):
        try:
            piramide = Piramide(float(self.txt_base.get()), float(self.txt_altura.get()), float(self.txt_apotema.get()))
            self.lbl_volumen.config(text=f"Volumen: {piramide.get_volumen():.2f} cm³")
            self.lbl_superficie.config(text=f"Superficie: {piramide.get_superficie():.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()