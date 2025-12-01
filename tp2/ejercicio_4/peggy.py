class Peggy():
    esfera_inicial: str
    esfera_final: str

    def primera_vision_de_esfera(self, esfera: str):
        self.esfera_inicial = esfera
    
    def segunda_vision_de_esfera(self, esfera: str):
        self.esfera_final = esfera

    def probar_cambio_de_esfera(self):
        return self.esfera_inicial != self.esfera_final