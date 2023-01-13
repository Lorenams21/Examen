# libraries
import numpy as np
import sys


def Suma(a, b):
    return np.sum(a + b)


def Restar(a, b):
    return a - b


def Multiplicar(a, b):
    return a * b


def Dividir(a, b):
    return a / b


def Raiz(a, b):
    return pow(a, 1 / b)


def Exponencial(a, b):
    return np.power(a, b)


def Seno(a):
    return np.sin(a)


def Coseno(a):
    return np.cos(a)


def Tangente(a):
    return np.tan(a)


def Calculadora():
    print("Este es tu menu de opraciones que puedes realizar; ")
    print("1 Sumar")
    print("2 Restar")
    print("3 Multiplicar")
    print("4 Dividir")
    print("5 Exponente")
    print("6 Raíz n")
    print("7 Seno")
    print("8 Coseno")
    print("9 Tangente")
    print("10 Apagar Calculadora")

    while True:
        num1 = 0
        num2 = 0
        num3 = 0
        choice = input("¿Que deseas realizar? (1\t2\t3\t4\t5\t6\t7\t8\t9\t10)")
        if choice in ('1', '2', '3', '4', '5', '6'):
            num1 = float(input("Escribe tu primer valor: "))
            num2 = float(input("Escribe tu segundo valor: "))
        elif choice in ('7', '8', '9'):
            num3 = float(input("Ingresa un valor: "))
        if choice == '1':
            print(f"{num1} + {num2} = ", Suma(num1, num2))
        elif choice == '2':
            print(f"{num1} - {num2} = ", Restar(num1, num2))
        elif choice == '3':
            print(f"{num1} * {num2} = ", Multiplicar(num1, num2))
        elif choice == '4':
            print(f"{num1} / {num2} = ", Dividir(num1, num2))
        elif choice == '5':
            print("El exponente es:  ", Exponencial(num1, num2))
        elif choice == '6':
            print("La raiz n del valor es: ", Raiz(num1, num2))
        elif choice == '7':
            print("El seno es: ", Seno(num3))
        elif choice == '8':
            print("El Coseno es", Coseno(num3))
        elif choice == '9':
            print("La tangente es", Tangente(num3))
        elif choice == '10':
            print("La calculadora se cerrará", Close())
        else:
            print("Su seleccion no es valida")
            break


Calculadora()
