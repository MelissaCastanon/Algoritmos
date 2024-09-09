import math
def aspect_ratio_conversion(x, y, constant):
    aspect_ratio = 16 / 9

    if constant == "height":
        # Mantiene constante la altura
        new_x = math.ceil(y * aspect_ratio)
        new_y = y
    elif constant == "width":
        # Mantiene constante el ancho
        new_x = x
        new_y = math.ceil(x / aspect_ratio)
    elif constant == "diagonal":
        # Mantiene constante la diagonal
        original_diagonal = math.sqrt(x ** 2 + y ** 2)
        new_y = math.ceil(math.sqrt(original_diagonal ** 2 / (aspect_ratio ** 2 + 1)))
        new_x = math.ceil(new_y * aspect_ratio)
    elif constant == "area":
        # Mantiene constante el área
        original_area = x * y
        new_y = math.ceil(math.sqrt(original_area / aspect_ratio))
        new_x = math.ceil(new_y * aspect_ratio)
    else:
        raise ValueError("La constante debe ser 'height', 'width', 'diagonal' o 'area'.")

    return new_x, new_y


# Ejemplo de uso
x = 1440
y = 1080
constant = "height"

new_resolution = aspect_ratio_conversion(x, y, constant)
print(f"La nueva resolución es: {new_resolution[0]}x{new_resolution[1]}")
