import random
class Victor():
    eleccion: int
    se_efectuo_cambio: bool

    def eleccion_y_primera_muestra_de_esfera(self) -> int:
        self.eleccion = random.randint(0,1)
        self.se_efectuo_cambio = False
        return self.eleccion
        

    def eleccion_potencial_de_cambio(self):
        cambio = random.randint(0,1)
        if cambio == 1:
            if self.eleccion == 0:
                self.eleccion = 1
            else:
                self.eleccion = 0
            self.se_efectuo_cambio = True
        else:
            self.se_efectuo_cambio == False

    def segunda_muestra_de_esfera(self) -> int:
        return self.eleccion

    def verificar_prueba(self, hipotesis) -> bool:
        return hipotesis == self.se_efectuo_cambio
        