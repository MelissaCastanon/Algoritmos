# Este programa calcula la cantidad de litros de agua que Nathan beberá en función del tiempo transcurrido,
# asumiendo que bebe 0.5 litros de agua por cada hora. El resultado se redondea hacia abajo utilizando 'math.floor'.
# El programa solicita al usuario que ingrese el tiempo en horas y valida la entrada para asegurarse de que sea un número.

import math
def litros_de_agua(tiempo):
    # Calcular la cantidad de litros
    litros = tiempo * 0.5

    # Redondear hacia abajo
    litros_redondeados = math.floor(litros)

    return litros_redondeados
def main():
    try:
        # Solicitar al usuario que ingrese el tiempo
        tiempo = float(input("Ingrese el tiempo en horas: "))

        # Calcular y mostrar la cantidad de litros
        litros = litros_de_agua(tiempo)
        print(f"Nathan beberá {litros} litros de agua.")

    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")


if __name__ == "__main__":
    main()
