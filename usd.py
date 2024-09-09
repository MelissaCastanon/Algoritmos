# Este programa convierte una cantidad en dólares estadounidenses (USD) a yuanes chinos (CNY) utilizando una tasa de
# conversión fija de 1 USD = 6.75 CNY. El usuario ingresa la cantidad en dólares, y el programa devuelve el equivalente
# en yuanes chinos formateado a dos decimales.

def usdcny(usd):
    conversion_rate = 6.75
    cny = usd * conversion_rate
    return f"{usd} USD -> {cny:.2f} Chinese Yuan"

# Solicitar la entrada del usuario
usd_input = int(input("Ingrese la cantidad en dólares (USD): "))

# Imprimir el resultado
print(usdcny(usd_input))
