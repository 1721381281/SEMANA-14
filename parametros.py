def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Esta función calcula el monto del descuento aplicado al monto total de la compra.
    
    Parámetros:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (float): El porcentaje de descuento a aplicar (por defecto 10%).
    
    Retorna:
    float: El monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Programa principal
if __name__ == "__main__":
    # Primera llamada a la función: solo monto total
    monto_compra1 = 200.0  # Monto total de la compra
    descuento1 = calcular_descuento(monto_compra1)
    monto_final1 = monto_compra1 - descuento1

    print(f"Monto de la compra: ${monto_compra1:.2f}")
    print(f"Descuento aplicado (10%): ${descuento1:.2f}")
    print(f"Monto final a pagar: ${monto_final1:.2f}\n")

    # Segunda llamada a la función: monto total y porcentaje de descuento
    monto_compra2 = 150.0  # Monto total de la compra
    porcentaje_descuento2 = 20  # Porcentaje de descuento
    descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
    monto_final2 = monto_compra2 - descuento2

    print(f"Monto de la compra: ${monto_compra2:.2f}")
    print(f"Descuento aplicado (20%): ${descuento2:.2f}")
    print(f"Monto final a pagar: ${monto_final2:.2f}")
    