class Fraccion:
    __numerador=0
    __denominador=1
    def __init__(self,numerador=0,denominador=1):
        self.__numerador=numerador
        self.__denominador=denominador
    def getNumerador(self):
        return self.__numerador
    def getDenominador(self):
        return self.__denominador
    def __add__(self,otroValor):
        if not isinstance(otroValor,Fraccion):
            otroValor=Fraccion(otroValor,1)
        denominador=self.__denominador*otroValor.getDenominador()
        nuevaFraccion=Fraccion(((denominador/self.__denominador)*self.__numerador)+((denominador/otroValor.getDenominador())*otroValor.getNumerador()),denominador)
        nuevaFraccion.simplificar()
        return nuevaFraccion
    def __radd__(self,otroValor):
        if not isinstance(otroValor,Fraccion):
            otroValor=Fraccion(otroValor,1)
        denominador=self.__denominador*otroValor.getDenominador()
        nuevaFraccion=Fraccion(((denominador/self.__denominador)*self.__numerador)+((denominador/otroValor.getDenominador())*otroValor.getNumerador()),denominador)
        nuevaFraccion.simplificar()
        return nuevaFraccion
    def __sub__(self,otroValor):
        if not isinstance(otroValor,Fraccion):
            otroValor=Fraccion(otroValor,1)
        denominador=self.__denominador*otroValor.getDenominador()
        nuevaFraccion=Fraccion(((denominador/self.__denominador)*self.__numerador)-((denominador/otroValor.getDenominador())*otroValor.getNumerador()),denominador)
        nuevaFraccion.simplificar()
        return nuevaFraccion
    def __rsub__(self,otroValor):
        print(otroValor)
        if not isinstance(otroValor,Fraccion):
            otroValor=Fraccion(otroValor,1)
        denominador=self.__denominador*otroValor.getDenominador()
        nuevaFraccion=Fraccion(((denominador/self.__denominador)*self.__numerador)-((denominador/otroValor.getDenominador())*otroValor.getNumerador()),denominador)
        nuevaFraccion.simplificar()
        return nuevaFraccion
    def __mul__(self,otroValor):
        if not isinstance(otroValor,Fraccion):
            otroValor=Fraccion(otroValor,1)
        nuevaFraccion=Fraccion(otroValor.getNumerador()*self.__numerador,otroValor.getDenominador()*self.__denominador)
        nuevaFraccion.simplificar()
        return nuevaFraccion
    def __rmul__(self,otroValor):
        if not isinstance(otroValor,Fraccion):
            otroValor=Fraccion(otroValor,1)
        nuevaFraccion=Fraccion(otroValor.getNumerador()*self.__numerador,otroValor.getDenominador()*self.__denominador)
        nuevaFraccion.simplificar()
        return nuevaFraccion
    def __truediv__(self,otroValor):
        if not isinstance(otroValor,Fraccion):
            otroValor=Fraccion(otroValor,1)
        nuevaFraccion=Fraccion(self.__numerador*otroValor.getDenominador(),self.__denominador*otroValor.getNumerador())
        nuevaFraccion.simplificar()
        return nuevaFraccion
    def __rtruediv__(self,otroValor):
        if not isinstance(otroValor,Fraccion):
            otroValor=Fraccion(otroValor,1)
        nuevaFraccion=Fraccion(otroValor.getNumerador()*self.__denominador,otroValor.getDenominador()*self.__numerador)
        nuevaFraccion.simplificar()
        return nuevaFraccion
    def simplificar(self):
        dividendo=0
        divisor=0
        resto=0
        if abs(self.__numerador)>abs(self.__denominador):
            resto=abs(self.__numerador)%abs(self.__denominador)
            divisor=abs(self.__denominador)
        else:
            resto=abs(self.__denominador)%abs(self.__numerador)
            divisor=abs(self.__numerador)
        while resto!=0:
            dividendo=divisor
            divisor=resto
            resto=dividendo%divisor
        self.__numerador=round(self.__numerador/divisor)
        self.__denominador=round(self.__denominador/divisor)
    def __str__(self):
        cadena=''
        if self.__denominador==1:
            cadena=str(self.__numerador)
        else:
            cadena='{}/{}'.format(self.__numerador,self.__denominador)
        return cadena