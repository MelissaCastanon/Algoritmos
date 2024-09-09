def round_to_two_decimal_places(number):
    # Redondear el número a dos decimales
    return round(number, 2)


def main():
    # Solicitar al usuario que ingrese un número
    number = float(input("Ingresa un número: "))

    # Redondear el número
    rounded_number = round_to_two_decimal_places(number)

    # Mostrar el resultado con dos decimales
    print(f"Número redondeado: {rounded_number:.2f}")


# Ejecutar la función principal
if __name__ == "__main__":
    main()
