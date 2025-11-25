from peggy import Peggy
from victor import Victor


def main():
    esferas = ["Roja", "Verde"]
    victor = Victor()
    peggy = Peggy()

    eleccion_de_esfera = victor.eleccion_y_primera_muestra_de_esfera()
    esfera = esferas[eleccion_de_esfera]
    peggy.primera_vision_de_esfera(esfera)
    victor.eleccion_potencial_de_cambio()
    eleccion_de_esfera = victor.segunda_muestra_de_esfera()
    esfera = esferas[eleccion_de_esfera]
    peggy.segunda_vision_de_esfera(esfera)
    hipotesis = peggy.probar_cambio_de_esfera()
    resultado_de_la_prueba = victor.verificar_prueba(hipotesis)
    print(resultado_de_la_prueba)


main()