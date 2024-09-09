#Programa que
# Calcula la edad del perro y el gato en años
def calculate_pet_ages(human_years):
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4
        dog_years = 15 + 9 + (human_years - 2) * 5
# Devuelve una lista con los años humanos, gato y perro.
    return [human_years, cat_years, dog_years]

# Preguntar al usuario por los años humanos
human_years = int(input("Ingresa la cantidad de años humanos: "))


# Ejemplo de uso
ages = calculate_pet_ages(human_years)

# Imprimir la salida en el formato deseado
print(f"Años humanos = {ages[0]}")
print(f"Años del gato = {ages[1]}")
print(f"Años del perro = {ages[2]}")

print(type(ages))