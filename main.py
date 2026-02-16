import math

def calcular_volumen_esfera(radio):
    """
    Calcula el volumen de una esfera dado su radio.
    Fórmula: V = (4/3) * π * r³
    """
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    volumen = (4/3) * math.pi * (radio ** 3)
    return volumen

# Solicitar el radio al usuario
try:
    radio = float(input("Introduce el radio de la esfera: "))
    volumen = calcular_volumen_esfera(radio)
    print(f"El volumen de la esfera con radio {radio} es: {volumen:.2f}")
    print(f"El perímetro de la esfera con radio {radio} es: {2 * math.pi * radio:.2f}")
except ValueError as e:
    print(f"Error: {e}")