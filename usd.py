def usdcny(usd):
    conversion_rate = 6.75
    cny = usd * conversion_rate
    return f"{usd} USD -> {cny:.2f} Chinese Yuan"

# Solicitar la entrada del usuario
usd_input = int(input("Ingrese la cantidad en dólares (USD): "))

# Imprimir el resultado
print(usdcny(usd_input))
