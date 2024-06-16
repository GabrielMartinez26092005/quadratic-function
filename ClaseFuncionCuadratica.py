import math

class FuncionCuadratica():
    __coeficientes = []
    __discriminante = 0
    __valores_calculados = []


    def ingreso_dato(self):
        self.__coeficientes.append(0)
        while self.__coeficientes[0] == 0:
            self.__coeficientes[0] = int(input('Ingrese el valor del coeficiente a '))
        self.__coeficientes.append(int(input('Ingrese el valor del coeficiente b ')))
        self.__coeficientes.append(int(input('Ingrese el valor del coeficiente c ')))            
        return
    

    def calcular_discriminante(self):
        self.__discriminante = self.__coeficientes[1]**2 - 4 * self.__coeficientes[0] * self.__coeficientes[2]
        return
    

    def evaluar_discriminante(self):
        if self.__discriminante == 0:
            self.__valores_calculados.append(self.__coeficientes[1] / 2 * self.__coeficientes[0])
        elif self.__discriminante > 0:
            self.__valores_calculados.append((-self.__coeficientes[1] + math.sqrt(self.__discriminante)) / (2 * self.__coeficientes[0]))
            self.__valores_calculados.append((-self.__coeficientes[1] - math.sqrt(self.__discriminante)) / (2 * self.__coeficientes[0]))
        else:
            pass
        return
    

    def mostrar_resultado(self):
        if len(self.__valores_calculados) == 0:
            print('La ecuación no tiene solución real')
        elif len(self.__valores_calculados) == 1:
            print(f'Valor 1: {self.__valores_calculados[0]}')
        else: 
            print(f'Valor 1: {self.__valores_calculados[0]}\nValor 2: {self.__valores_calculados[1]}')
        return

    
primer_funcion = FuncionCuadratica()
primer_funcion.ingreso_dato()
primer_funcion.calcular_discriminante()
primer_funcion.evaluar_discriminante()
primer_funcion.mostrar_resultado()




