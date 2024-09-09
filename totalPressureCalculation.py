def total_pressure(M1, M2, m1, m2, V, T):
    # Convertir la temperatura de Celsius a Kelvin
    T_kelvin = T + 273.15

    # Constante de gas en dm^3·atm·K^−1·mol^−1
    R = 0.082

    # Calcular la presión total usando la fórmula
    P_total = ((m1 / M1) + (m2 / M2)) * R * T_kelvin / V

    return P_total

# Ejemplo de uso:
M1 = float(input("Ingresa la masa molar de la molécula 1 (g/mol): "))
M2 = float(input("Ingresa la masa molar de la molécula 2 (g/mol): "))
m1 = float(input("Ingresa la masa presente de la molécula 1 (g): "))
m2 = float(input("Ingresa la masa presente de la molécula 2 (g): "))
V = float(input("Ingresa el volumen de la vasija (dm^3): "))
T = float(input("Ingresa la temperatura en °C: "))

result = total_pressure(M1, M2, m1, m2, V, T)
print(f"La presión total es: {result:.2f} atm")