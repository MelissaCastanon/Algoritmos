def encontrar_tercer_angulo(angulo1, angulo2):
    # Asegurarse de que los ángulos sean enteros positivos
    if angulo1 <= 0 or angulo2 <= 0:
        raise ValueError("Los ángulos deben ser enteros positivos.")

    # Calcular el tercer ángulo
    tercer_angulo = 180 - (angulo1 + angulo2)

    # Asegurarse de que el tercer ángulo sea positivo
    if tercer_angulo <= 0:
        raise ValueError("Ángulos inválidos proporcionados; la suma de los ángulos dados excede 180 grados.")

    return tercer_angulo


def main():
    try:
        # Solicitar al usuario que ingrese los ángulos
        angulo1 = int(input("Ingrese el primer ángulo (en grados): "))
        angulo2 = int(input("Ingrese el segundo ángulo (en grados): "))

        # Encontrar y mostrar el tercer ángulo
        tercer_angulo = encontrar_tercer_angulo(angulo1, angulo2)
        print(f"El tercer ángulo del triángulo es: {tercer_angulo} grados")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
