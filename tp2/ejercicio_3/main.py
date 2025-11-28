
def next_fit(lista_objetos, capacidad_max=1):
    # Si no hay objetos, se necesitan 0 recipientes
    if not lista_objetos:
        return 0
    
    # Inicializamos el primer recipiente
    contenedores_usados = 1
    espacio_disponible = capacidad_max  # Capacidad inicial de los contenedores
    
    for objeto in lista_objetos:
        if objeto <= espacio_disponible:
            espacio_disponible -= objeto
        else:
            # El objeto no entra, pasamos al siguiente recipiente
            contenedores_usados += 1
            # El nuevo recipiente contiene el objeto actual
            espacio_disponible = capacidad_max - objeto
    
    return contenedores_usados


