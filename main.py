def max_paneles(panel_a: int, panel_b: int, techo_x: int, techo_y: int) -> int:
    # Chequeo inicial
    if (panel_a > techo_x and panel_a > techo_y)\
        or (panel_b > techo_x and panel_b > techo_y)\
        or (techo_x < panel_a and techo_x < panel_b)\
        or (techo_y < panel_a and techo_y < panel_b):
        return 0

    if panel_a <= panel_b:
        panel_corto = panel_a
        panel_largo = panel_b
    else:
        panel_corto = panel_b
        panel_largo = panel_a

    # Definimos una heurística
    max_paneles = (techo_x*techo_y)//(panel_a*panel_b)

    # --- Configuración inicial ---
    n_parados_x = techo_x//panel_corto
    n_acostados_x = 0

    max_parados_y = techo_y//panel_largo
    max_acostados_y = techo_y//panel_corto

    # Partimos solo con paneles "parados"
    n_paneles = n_parados_x * max_parados_y

    if n_paneles == max_paneles:
        return n_paneles
    
    mayor_paneles_logrado = n_paneles
    
    while n_parados_x > 0:
        n_parados_x -= 1

        techo_ocupado = n_parados_x*panel_corto + n_acostados_x*panel_largo
        # Vemos si cabe un panel acostado después de sacar uno parado
        if techo_x - techo_ocupado >= panel_largo:
            n_acostados_x += 1

            # Se calcula nuevo número de paneles solo si logramos añadir uno acostado
            n_paneles = n_parados_x*max_parados_y + n_acostados_x*max_acostados_y

            if n_paneles == max_paneles:
                return n_paneles
            if n_paneles > mayor_paneles_logrado:
                mayor_paneles_logrado = n_paneles
    
    return mayor_paneles_logrado

def main(a, b, x, y):
    orientación_1 = max_paneles(a, b, x, y)
    orientación_2 = max_paneles(a, b, y, x)

    return max(orientación_1, orientación_2)

if __name__ == "__main__":
    a = 2
    b = 2
    x = 1
    y = 10
    print(main(a, b, x, y))
        
