'''
Title: ArbolBinario
Author: Alex Ticlla Choque
Created: 03/27/24
Version: 1.0
'''
from Nodo import Nodo
from collections import deque


class ArbolBinario:
    """
    Clase ArbolBinario representa la estructura de un arbol binario
    """
    def __init__(self, dato=None):
        """
        Constructor de la clase ArbolBinario si se le proporciona un dato
        entonces la raiz del arbol contiene el dato, sino la raiz es nula. 
        """
        if dato is not None:
            self.raiz = Nodo(dato)
        else:
            self.raiz = None

    
 
    # Metodos Privados 

    def __agregar_recursivo(self, current_nodo, dato):
        # Metodo auxiliar para el metodo 'agregar'
        if dato < current_nodo.dato:
            if current_nodo.izquierda is None:
                current_nodo.izquierda = current_nodo(dato)
            else:
                self.__agregar_recursivo(current_nodo.izquierda, dato)
        elif dato > current_nodo.dato:
            if current_nodo.derecha is None:
                current_nodo.derecha = current_nodo(dato)
            else:
                self.__agregar_recursivo(current_nodo.derecha, dato)
        else:
            print("El dato a ingresar ya existe en el arbol")

    def __inorden_recursivo(self, current_nodo):
        # Metodo recursivo imprime el contenido de un arbol en inorden
    
        # Caso base
                
        if current_nodo is not None:
            self.__inorden_recursivo(current_nodo.izquierda)
            print(current_nodo.dato, end=", ")
            self.__inorden_recursivo(current_nodo.derecha)

    def __preorden_recursivo(self, current_nodo):
        # Metodo recursivo imprime el contenido de un arbol en preorden

        if current_nodo is not None:
            print(current_nodo.dato, end=", ")
            self.__preorden_recursivo(current_nodo.izquierda)
            self.__preorden_recursivo(current_nodo.derecha)

    def __postorden_recursivo(self, current_nodo):
        # Metodo recursivo imprime el contenido de un arbol en postorden

        if current_nodo is not None:
            self.__postorden_recursivo(current_nodo.izquierda)
            self.__postorden_recursivo(current_nodo.derecha)
            print(current_nodo.dato, end=", ")

    def __buscar(self, current_nodo, busqueda):
        # Metodo recursivo para buscar un valor 'busqueda'
        if current_nodo is None:
            return None
        if current_nodo.dato == busqueda:
            return current_nodo
        if busqueda < current_nodo.dato:
            return self.__buscar(current_nodo.izquierda, busqueda)
        else:
            return self.__buscar(current_nodo.derecha, busqueda)

    # Funciones públicas

    def agregar(self, dato):
        # Metodo para agregar un 'dato' de cualquier tipo al Arbol
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self.__agregar_recursivo(self.raiz, dato)

    def inorden(self):
        # Metodo para imprimir el contenido de un arbol de manera inorden
        print("Imprimiendo árbol inorden recursivamente: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        # Metodo para imprimir el contenido de un arbol de manera preorden
        print("Imprimiendo árbol preorden recursivamente: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):

        # Metodo para imprimir el contenido de un arbol de manera postorden
        print("Imprimiendo árbol postorden recursivamente: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        # Funcion de busqueda
        return self.__buscar(self.raiz, busqueda)
    
    def vacio(self):
        return self.raiz == None
    
    def esHoja(self, node):
        # Solo funciona para arboles con un nodo
        if node is None:
            return False
        
        if (node.derecha is None) and (node.izquierda is None):
            return True
        
        return False
        
    # Funciones iterativas
    def agregarIterativo(self, value):
        '''Metodo iterativo para agregar un valor al arbol.
        Parametros: self.raiz, dato'''
        previous_node = None
        current_node = self.raiz
        if current_node is None:
            self.raiz = Nodo(value)
        else:
            while current_node is not None:
                previous_node = current_node

                if value > current_node.dato:
                    current_node = current_node.derecha
                elif value < current_node.dato:
                    current_node = current_node.izquierda
                else:
                    return
                
            new_node = Nodo(value)
            if value > previous_node.dato:
                previous_node.setHijoDerecha(new_node)
            else:
                previous_node.setHijoIzquierda(new_node)
            return
        
    def iterativeInorder(self, current_node):
        '''
        Metodo de recorrido inorder traversal iterativo
        toma como parametro a un nodo actual, que en primera instancia
        es la raiz del arbol
        '''
        if current_node is None:
            print('El arbol se encuentra vacio')
            return
        
        print('Imprimiendo el arbol iterativamente inorder traversal: ')
        pila = []
        while current_node or pila:
            while current_node:
                pila.append(current_node)
                current_node = current_node.izquierda
            current_node = pila.pop()
            print(str(current_node.dato) + ', ', end='')
            current_node = current_node.derecha
        print()
        return
    
    def inorderTraversal(self):
        self.iterativeInorder(self.raiz)
    

        

    def deleteNode(self, root, key):
            # Base case
        if root is None:
            return root

        # If the key to be deleted is smaller than the root's key, then it lies in the left subtree
        if key < root.dato:
            root.izquierda = self.deleteNode(root.izquierda, key)
        # If the key to be deleted is greater than the root's key, then it lies in the right subtree
        elif key > root.dato:
            root.derecha = self.deleteNode(root.derecha, key)
        # If key is same as root's key, then this is the node to be deleted
        else:
            # Node with only one child or no child
            if root.izquierda is None:
                return root.derecha
            elif root.derecha is None:
                return root.izquierda

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            root.dato = self.minValue(root.derecha)

            # Delete the inorder successor
            root.derecha = self.deleteNode(root.derecha, root.dato)

        return root
    

    def minValue(self, root):
        minv = root.dato
        while root.izquierda:
            minv = root.izquierda.key
            root = root.izquierda
        return minv  

    def altura(self, current_node):
        """
        Encuentra la altura maxima del nodo, desde el nodo raiz, hasta el nodo hoja mas lejano 
        parametros: tipo de dato Nodo
        """
        if current_node is None:
            return 0
        else:
            altura_izq = self.altura(current_node.izquierda)
            altura_der = self.altura(current_node.derecha)

            if altura_izq > altura_der:
                return altura_izq + 1
            else:
                return altura_der + 1
    
    def getMaxWidth(self, root):
        """
        Encuentra la amplitud maxima de un arbol binario
        par: root de tipo Nodo
        """
        maxWidth = 0
        h = self.altura(root)
        # Get width of each level and compare the
        # width with maximum width so far
        for i in range(1, h+1):
            width = self.getWidth(root, i)
            if (width > maxWidth):
                maxWidth = width
        return maxWidth
    # Get width of a given level
    def getWidth(self, root, level):
        if root is None:
            return 0
        if level == 1:
            return 1
        elif level > 1:
            return (self.getWidth(root.izquierda, level-1) +
                    self.getWidth(root.derecha, level-1))
    
    def cantidad_Nodos(self, current_node):
        """Retorna la cantidad de nodos en un arbol
        par: current_node type Nodo"""
        if current_node is None:
            return 0
        else:
            cantidad_izq = self.cantidad_Nodos(current_node.izquierda)
            cantidad_der = self.cantidad_Nodos(current_node.derecha)
            return cantidad_der + cantidad_izq + 1
    
    def cantidad_Hojas(self, current_node):
        """Retorna la cantidad de hojas en un arbol
        par: current_node type Nodo"""
        if current_node is None:
            return 0
        if current_node.izquierda is None and current_node.derecha is None:
            return 1
        else:
            return self.cantidad_Hojas(current_node.izquierda) + self.cantidad_Hojas(current_node.derecha)
        
    # Funciones para recorrer el arbol en anchura
    def anchura(self):
        if self.raiz is None:
            return
        queue = []
        queue.append(self.raiz)
        while(len(queue) > 0):
            print(queue[0].dato, end = ' ')
            node = queue.pop(0)
            if node.izquierda is not None:
                queue.append(node.izquierda)
            if node.derecha is not None:
                queue.append(node.derecha)
        print()
    # Metodo para imprimir un arbol en consola de manera bonita
    def print_tree(self, current_node, indent='', last=True):
        # Metodo recursivo para imprimir un arbol de manera bonita
        if current_node is not None:
            print(indent, end='')
            if last:
                print('R----', end='')
                indent += '     '
            else:
                print('L----', end='')
                indent += '|    '

            print(current_node.dato)
            self.print_tree(current_node.izquierda, indent, False)
            self.print_tree(current_node.derecha, indent, True)
    

        


        
        





    
