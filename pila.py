import numpy as np

class pila:
    __tope=int
    __dim=int
    __arr=None
    def __init__(self, dim):
        self.__tope=-1
        self.__dim=dim
        self.__arr=np.empty(dim)

    def lleno(self):
        return self.__tope == self.__dim - 1
    
    def vacio(self):
        return self.__tope == -1

    def insertar(self, objeto):
        if self.lleno():
            print("La pila está llena. No se puede realizar la inserción.")
        else:
            self.__tope += 1
            self.__arr[self.__tope] = objeto

    def suprimir(self):
        if self.vacio():
            print("La pila está vacia. No se puede suprimir.")
        else:
            objeto = self.__arr[self.__tope]
            self.__arr[self.__tope] = None
            self.__tope -= 1
            return objeto

    def mostrar(self):
        print("Contenido de la pila:")
        for i in range(self.__tope + 1):
            print(self.__arr[i])

if __name__ == "__main__":
    p = pila(5)
    p.insertar(1)
    p.insertar(2)
    p.insertar(3)
    p.insertar(4)
    p.insertar(5)
    p.insertar(6)
    p.mostrar()
    objeto=p.suprimir()
    print(f"Elemento eliminado {objeto}")
    p.mostrar()
    

    
        