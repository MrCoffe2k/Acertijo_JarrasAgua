import random

# Esta función genera una regla aleatoria del acertijo.
def generar_regla_azar():
    return random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Esta función aplica la regla seleccionada al estado actual de las jarras.
def aplicar_regla(jarra_3, jarra_4, regla):
    if regla == 1:
        jarra_4 = 4
    elif regla == 2:
        jarra_3 = 3
    elif regla == 3 and jarra_4 > 0:
        jarra_4 -= 1
    elif regla == 4 and jarra_3 > 0:
        jarra_3 -= 1
    elif regla == 5:
        jarra_4 = 0
    elif regla == 6:
        jarra_3 = 0
    elif regla == 7 and jarra_4 > 0 and jarra_3 < 3:
        espacio_disponible = 3 - jarra_3
        jarra_3 += min(jarra_4, espacio_disponible)
        jarra_4 -= min(jarra_4, espacio_disponible)
    elif regla == 8 and jarra_3 > 0 and jarra_4 < 4:
        espacio_disponible = 4 - jarra_4
        jarra_4 += min(jarra_3, espacio_disponible)
        jarra_3 -= min(jarra_3, espacio_disponible)
    elif regla == 9 and jarra_4 > 0 and jarra_3 < 3:
        espacio_disponible = 3 - jarra_3
        jarra_3 += jarra_4 if jarra_4 < espacio_disponible else espacio_disponible
        jarra_4 -= jarra_4 if jarra_4 < espacio_disponible else espacio_disponible
    elif regla == 10 and jarra_3 > 0 and jarra_4 < 4:
        espacio_disponible = 4 - jarra_4
        jarra_4 += jarra_3 if jarra_3 < espacio_disponible else espacio_disponible
        jarra_3 -= jarra_3 if jarra_3 < espacio_disponible else espacio_disponible
    
    return jarra_3, jarra_4

# Esta función resuelve el acertijo de las jarras de agua utilizando las funciones anteriores.
def resolver_acertijo():
    jarra_3 = 0
    jarra_4 = 0
    movimientos = 0
    
    while jarra_4 != 2:
        regla = generar_regla_azar()
        jarra_3, jarra_4 = aplicar_regla(jarra_3, jarra_4, regla)
        movimientos += 1
        print(f"Regla {regla}: ({jarra_3}, {jarra_4})")
    
    print(f"\nAcertijo resuelto en {movimientos} movimientos")

resolver_acertijo()

