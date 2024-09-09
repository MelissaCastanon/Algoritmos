def calcular_costo_mango(cantidad, precio_por_mango):
    # Calcular cuántos grupos de 3 mangoes hay
    grupos = cantidad // 3
    # Calcular el número de mangoes restantes
    restantes = cantidad % 3

    # Calcular el costo total
    costo_total = (grupos * 2 * precio_por_mango) + (restantes * precio_por_mango)

    return costo_total


def main():
    try:
        # Solicitar al usuario que ingrese la cantidad y el precio por mango
        cantidad = int(input("Ingrese la cantidad de mangos: "))
        precio_por_mango = float(input("Ingrese el precio por mango: "))

        # Calcular y mostrar el costo total
        costo = calcular_costo_mango(cantidad, precio_por_mango)
        print(f"El costo total de los mangos es: ${costo:.2f}")

    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")


if __name__ == "__main__":
    main()
