class Nodo:
    __valor=int
    __siguiente=None
    def __init__(self, valor):
        self.__valor = valor
        self.__siguiente = None

    def getValor(self):
        return self.__valor
    
    def setSiguiente(self, objeto):
        self.__siguiente=objeto

    def getSiguiente(self):
        return self.__siguiente

class PilaEnlazada:
    __tope= None
    def __init__(self):
        self.__tope = None

    def vacio(self):
        return self.__tope is None

    def insertar(self, valor):
        nueva_celda = Nodo(valor)
        nueva_celda.setSiguiente(self.__tope)
        self.__tope = nueva_celda

    def eliminar(self):
        if self.vacio():
            print("La pila está vacía. No se puede realizar pop.")
            return None
        valor = self.__tope.getValor()
        self.__tope = self.__tope.getSiguiente()
        return valor

    def mostrar(self):
        if self.vacio():
            print("La pila está vacía.")
        else:
            celda_actual = self.__tope
            while celda_actual:
                print(celda_actual.getValor())
                celda_actual = celda_actual.getSiguiente()

# Ejemplo de uso
pila = PilaEnlazada()

pila.insertar(10)
pila.insertar(20)
pila.insertar(30)

"""print("Pop:", pila.eliminar())
print("Pop:", pila.eliminar())"""

print("¿Está vacía?", pila.vacio())

print("Contenido de la pila:")
pila.mostrar()
