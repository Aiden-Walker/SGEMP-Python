# -*- coding: utf-8 -*-
class Pieza():
    idPieza = ""
    peso = 0
    precio = 0.0
    urlFabricante = ""
    def __init__(self, idPiezaVALUE, pesoVALUE, precioVALUE, urlFabricanteVALUE):
        self.__idPieza = idPiezaVALUE
        self.__peso = pesoVALUE
        self.__precio = precioVALUE
        self.__urlFabricante = urlFabricanteVALUE
    def __str__(self):
        return "Hello"
    @property
    def idPieza(self):
        return self._idPieza
    @idPieza.setter
    def idPieza(self,idPiezaVALUE):
        self._idPieza = idPiezaVALUE
    @property
    def peso(self):
        return self._peso
    @peso.setter
    def peso(self,pesoVALUE):
        self._peso = pesoVALUE
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self,precioVALUE):
        self._precio = precioVALUE
    @property
    def urlFabricante(self):
        return self._urlFabricante
    @idPieza.setter
    def urlFabricante(self,urlFabricanteVALUE):
        self._urlFabricante = urlFabricanteVALUE