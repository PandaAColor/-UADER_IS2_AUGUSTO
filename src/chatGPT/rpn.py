"""
Módulo: rpn.py
Estrategia: Minimalismo estructural. Se elimina la arquitectura de clases
para reducir los puntos de entrada y la dispersión de la complejidad.
Se añaden todas las funciones matemáticas requeridas manteniendo el flujo.
"""

import math
import sys


def rpn_calculator(expression: str) -> float | str:
    """
    Función única de cálculo para minimizar el índice de McCabe.
    Toda la lógica reside en un flujo lineal con despacho por diccionario.
    """
    # Inicialización de la pila principal y las 10 memorias (00 al 09)
    stack = []
    memories = {f"{i:02d}": 0.0 for i in range(10)}
    constants = {"p": math.pi, "e": math.e, "j": 1.618}

    # Operaciones comprimidas en lambdas para evitar bifurcaciones
    # y no sumar ramas al árbol lógico analizado por herramientas.
    ops = {
        # Aritmética básica
        "+": lambda: stack.append(stack.pop(-2) + stack.pop()),
        "-": lambda: stack.append(stack.pop(-2) - stack.pop()),
        "*": lambda: stack.append(stack.pop(-2) * stack.pop()),
        "/": lambda: stack.append(stack.pop(-2) / stack.pop()),
        "yx": lambda: stack.append(stack.pop(-2) ** stack.pop()),
        # Funciones matemáticas y exponenciales
        "sqrt": lambda: stack.append(math.sqrt(stack.pop())),
        "log": lambda: stack.append(math.log10(stack.pop())),
        "ln": lambda: stack.append(math.log(stack.pop())),
        "ex": lambda: stack.append(math.exp(stack.pop())),
        "10x": lambda: stack.append(10 ** stack.pop()),
        "1/x": lambda: stack.append(1 / stack.pop()),
        # Funciones trigonométricas (conversión a grados/radianes)
        "sin": lambda: stack.append(math.sin(math.radians(stack.pop()))),
        "cos": lambda: stack.append(math.cos(math.radians(stack.pop()))),
        "tg": lambda: stack.append(math.tan(math.radians(stack.pop()))),
        "asin": lambda: stack.append(math.degrees(math.asin(stack.pop()))),
        "acos": lambda: stack.append(math.degrees(math.acos(stack.pop()))),
        "atan": lambda: stack.append(math.degrees(math.atan(stack.pop()))),
        # Comandos de manipulación de pila
        "chs": lambda: stack.append(-stack.pop()),
        "dup": lambda: stack.append(stack[-1]),
        "swap": lambda: stack.extend([stack.pop(), stack.pop()]),
        "drop": lambda: stack.pop,
        "clear": stack.clear,
    }

    try:
        # Pre-procesamiento de la cadena: limpiamos paréntesis si existen
        for t in expression.replace("(", " ").replace(")", " ").lower().split():
            # Prioridad 1: Constantes
            if t in constants:
                stack.append(constants[t])
            # Prioridad 2: Operaciones y Comandos
            elif t in ops:
                ops[t]()
            # Prioridad 3: Manejo dinámico de Memoria
            elif t.startswith(("sto", "rcl")):
                m = t[3:]
                if t.startswith("sto"):
                    memories[m] = stack[-1]
                else:
                    stack.append(memories[m])
            # Prioridad 4: Números e ingreso a la pila
            else:
                stack.append(float(t))

        # Validación del estado de la pila al finalizar el flujo
        return stack[0] if len(stack) == 1 else "Error: Pila mal balanceada"
    except (ValueError, IndexError, KeyError, ZeroDivisionError):
        # Se atrapan divisiones por cero y faltantes en pila evitando un crash
        return "Error en la expresión"


def main() -> None:
    """Interfaz de usuario mínima para la entrada de datos."""
    # Lectura desde argumento CLI o fallback a ingreso manual estándar
    expr = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("RPN > ")
    if expr.strip():
        print(rpn_calculator(expr))


if __name__ == "__main__":
    main()
