# Programación Orientada a Objetos · UNAL

Ejercicios y actividades del curso de Programación Orientada a Objetos en Python, Universidad Nacional de Colombia.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-2C5D8F)
![LaTeX](https://img.shields.io/badge/Informes-LaTeX-008080?logo=latex&logoColor=white)
[![Licencia: MIT](https://img.shields.io/badge/Licencia-MIT-green.svg)](LICENSE)

🇪🇸 Español · 🇬🇧 English (próximamente)

---

## Descripción

| | |
|---|---|
| **Curso** | Programación Orientada a Objetos |
| **Universidad** | Universidad Nacional de Colombia · Facultad de Minas, sede Medellín |
| **Periodo** | 2026-2 |
| **Docente** | Walter Hugo Arboleda Mazo |

Cada actividad contiene los ejercicios resueltos en Python y un informe en LaTeX con el código fuente y el diagrama de clases de cada ejercicio. El curso avanza desde clases simples con atributos y métodos hasta encapsulamiento, herencia e interfaces gráficas.

## Conceptos por actividad

| Actividad | Conceptos de POO |
|---|---|
| [Actividad 1](actividad-01/) | Clases, atributos de instancia, métodos, validación de entradas con excepciones |
| [Actividad 2](actividad-02/) | Constructores con parámetros, enumeraciones (`Enum`), encapsulamiento con `@property`, varias clases en un mismo módulo |
| [Actividad 3](actividad-03/) | Herencia, separación entre lógica y vista, interfaces gráficas con Tkinter |

## Actividad 1 · Clases y métodos

| Ejercicio | Archivo | Clase | Descripción |
|---|---|---|---|
| 1.4 | [`ejercicio4.py`](actividad-01/ejercicio4.py) | `Familia` | Calcula las edades de los miembros de una familia a partir de la edad de Juan. |
| 1.5 | [`ejercicio5.py`](actividad-01/ejercicio5.py) | `PruebaEscritorio` | Simula paso a paso la prueba de escritorio de un algoritmo y muestra el estado de cada variable. |
| 1.12 | [`ejercicio12.py`](actividad-01/ejercicio12.py) | `Empleado` | Calcula el salario bruto, la retención y el salario neto a partir de las horas trabajadas. |
| 1.14 | [`ejercicio14.py`](actividad-01/ejercicio14.py) | `Calculadora` | Calcula el cuadrado y el cubo de un número. |
| 1.17 | [`ejercicio17.py`](actividad-01/ejercicio17.py) | `Circulo` | Calcula el área y la longitud de la circunferencia a partir del radio. |

📄 Informe: [`actividad-01/informe.tex`](actividad-01/informe.tex)

## Actividad 2 · Modelado de objetos

| Ejercicio | Archivo | Clases | Descripción |
|---|---|---|---|
| 2.1 | [`ejercicio1.py`](actividad-02/ejercicio1.py) | `Persona` | Registra y muestra los datos personales de una persona. |
| 2.2 | [`ejercicio2.py`](actividad-02/ejercicio2.py) | `Planeta`, `TipoPlaneta` | Modela un planeta, calcula su densidad y determina si es exterior al cinturón de asteroides. |
| 2.3 | [`ejercicio3.py`](actividad-02/ejercicio3.py) | `Automovil` | Acelera, desacelera, frena y estima el tiempo de llegada, con atributos encapsulados y un menú interactivo. |
| 2.4 | [`ejercicio4.py`](actividad-02/ejercicio4.py) | `Circulo`, `Rectangulo`, `Cuadrado`, `Triangulo` | Calcula el área y el perímetro de cada figura y clasifica el triángulo. |
| 2.5 | [`ejercicio5.py`](actividad-02/ejercicio5.py) | `CuentaBancaria` | Permite consignar, retirar y consultar el saldo, validando fondos suficientes. |

📄 Informe: [`actividad-02/informe.tex`](actividad-02/informe.tex)

## Actividad 3 · Herencia e interfaces gráficas

| Ejercicio | Archivo | Clases | Descripción |
|---|---|---|---|
| 3.1 | [`ejercicio1.py`](actividad-03/ejercicio1.py) | `Notas`, `VentanaNotas` | Calculadora de notas con interfaz gráfica: promedio, desviación estándar, nota mínima y máxima. |
| 3.2 | [`ejercicio2.py`](actividad-03/ejercicio2.py) | `FiguraGeometrica` → `Cilindro`, `Esfera`, `Piramide` | Jerarquía de figuras 3D que calcula volumen y área superficial, con una ventana por figura. |

📄 Informe: [`actividad-03/informe.tex`](actividad-03/informe.tex)

## Estructura

```text
.
├── actividad-01/   Ejercicios 1.4 a 1.17 + informe.tex
├── actividad-02/   Ejercicios 2.1 a 2.5 + informe.tex
└── actividad-03/   Ejercicios 3.1 y 3.2 (Tkinter) + informe.tex
```

## Cómo ejecutar

Requiere Python 3 sin dependencias externas (Tkinter viene incluido con Python).

```bash
git clone https://github.com/NatoRemolina/UNAL-Programacion-Orientada-a-Objetos.git
cd UNAL-Programacion-Orientada-a-Objetos
python3 actividad-01/ejercicio4.py
```

Los ejercicios de la Actividad 3 abren una ventana, así que necesitan un entorno gráfico.

Para compilar un informe (requiere una distribución de LaTeX):

```bash
cd actividad-01
pdflatex informe.tex
```

## Licencia

Código publicado bajo [licencia MIT](LICENSE). Los enunciados de los ejercicios pertenecen al curso.

## Autora

**Natalia Patricia Remolina Rodríguez**
Ingeniería Física · Universidad Nacional de Colombia

[![GitHub](https://img.shields.io/badge/GitHub-NatoRemolina-181717?logo=github)](https://github.com/NatoRemolina)
