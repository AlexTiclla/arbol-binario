from ArbolBinario import ArbolBinario

def main():
    # Instancia
    arbol = ArbolBinario()


    # Agregacion
    arbol.agregarIterativo(5)
    arbol.agregarIterativo(3)
    arbol.agregarIterativo(7)
    arbol.agregarIterativo(1)
    arbol.agregarIterativo(4)
    arbol.agregarIterativo(8)
    arbol.agregarIterativo(9)
    arbol.agregarIterativo(6)
    arbol.agregarIterativo(10)

    # Imprimir el árbol
    arbol.print_tree(arbol.raiz)
    
    # Recorrido
    arbol.inorden()

    print("Maxima amplitud: " + str(arbol.getMaxWidth(arbol.raiz)))
    print("Altura: " + str(arbol.altura(arbol.raiz)))
    print("Cantidad de nodos: " + str(arbol.cantidad_Nodos(arbol.raiz)))

    # Escribe una funcion para probar el metodo print_tree
    arbol.print_tree(arbol.raiz)






    
    

    # arbol.preorden()
    # arbol.postorden()
    
    # # Búsqueda
    # busqueda = input("Busca algo en el árbol: ")
    # nodo = arbol.buscar(int(busqueda))
    # if nodo is None:
    #     print(f"{busqueda} no existe")
    # else:
    #     print(f"{busqueda} sí existe")
  
    # # Prueba metodos vacio y eshoja
    # arbol2 = ArbolBinario()
    # arbol2.agregar(1)
    # print("El arbol2 esta vacio: " + str(arbol2.vacio()))
    # print("La raiz del arbol2 es hoja: " + str(arbol2.esHoja()))
  

if __name__ == '__main__':
    main()