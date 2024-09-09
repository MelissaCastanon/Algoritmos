def nba_extrap(ppg, mpg):
    # Si mpg es 0, retornamos 0
    if mpg == 0:
        return 0

    # Calcular los puntos extrapolados para 48 minutos
    ppg_extrapolado = (ppg / mpg) * 48

    # Redondear el resultado a la décima más cercana
    return round(ppg_extrapolado, 1)


def main():
    # Solicitar al usuario los valores
    ppg = float(input("Ingresa el promedio de puntos por juego (ppg): "))
    mpg = float(input("Ingresa el promedio de minutos jugados por juego (mpg): "))

    # Calcular la extrapolación
    result = nba_extrap(ppg, mpg)

    # Mostrar el resultado
    print(f"Puntos extrapolados para 48 minutos: {result}")


# Ejecutar la función principal
if __name__ == "__main__":
    main()
