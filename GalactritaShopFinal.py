import time
# HashTableLinkedList==========================================
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setNext(self, next_node):
        self.next = next_node

    def setValue(self, value):
        self.value = value


class LinkedList:
    def __init__(self):
        self.head, self.tail, self.len = None, None, 0

    def __len__(self):
        return self.len

    def append(self, value):
        new_node = Node(value)
        if len(self) == 0:
            self.head = new_node
            self.setTail(new_node)
        else:
            current_tail = self.tail
            current_tail.setNext(new_node)
            self.setTail(new_node)
        self.len += 1

    def search(self, key):
        current = self.head
        while current is not None and current.getValue()[0] != key:
            current = current.getNext()
        return current

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def setTail(self, new_tail):
        if new_tail is not None:
            new_tail.setNext(None)
            self.tail = new_tail
        else:
            self.tail = None

    def delete(self, key):
        prev = None
        current = self.head
        while current is not None:
            if current.getValue()[0] == key:
                if prev is None:
                    self.head = current.getNext()
                else:
                    prev.setNext(current.getNext())
                if current == self.tail:
                    self.setTail(prev)
                self.len -= 1
                return True
            prev = current
            current = current.getNext()
        return False


class HashTable:
    def __init__(self, size):
        self.elements = [LinkedList() for _ in range(size)]

    def hash(self, key):
        return hash(key) % len(self.elements)

    def insert(self, key, value):
        index = self.hash(key)
        value.precio = value.calc_precio
        self.elements[index].append((key, value))

    def search(self, key):
        index = self.hash(key)
        node = self.elements[index].search(key)
        return node.getValue()[1] if node else None

    def update(self, key, new_value):
        index = self.hash(key)
        node = self.elements[index].search(key)
        if node:
            node.setValue((key, new_value))

    def delete(self, key):
        index = self.hash(key)
        return self.elements[index].delete(key)

    def __str__(self):
        result = ""
        for i, bucket in enumerate(self.elements):
            result += f"{i} : "
            node = bucket.getHead()
            while node:
                key, value = node.getValue()
                result += f"({key}, {value}) -> "
                node = node.getNext()
            result += "None\n"
        return result


# Grafos para conexiones =============================================
import math
import heapq

# Constantes para grafos
WHITE = "white"
BLACK = "black"
GRAY = "gray"


class Graph:
    def _buildAdjMatrix(self):
        self.adjMat = [[0 for v in range(len(self.vertexes))] for v in range(len(self.vertexes))]
        for relation in self.relations:
            row, col = self.encoder[relation[0]], self.encoder[relation[1]]
            self.adjMat[row][col] = 1

    def _buildEncoding(self):
        self.encoder, self.decoder = {}, {}
        index = 0
        for v in self.vertexes:
            self.encoder[v] = index
            self.decoder[index] = v
            index = index + 1

    def _buildAdjList(self):
        self.adjList = {}
        for v in self.vertexes:
            self.adjList[v] = []
        for relation in self.relations:
            self.adjList[relation[0]].append(relation[1])

    def _buildRelation(self, e):
        if self.directed:
            self.relations = e
        else:
            self.relations = set()
            for el in e:
                self.relations.add(el)
                if len(el) == 2:
                    self.relations.add((el[1], el[0]))
                else:
                    self.relations.add((el[1], el[0], e[2]))

    def _buildWeight(self):
        self._weight = {}  # (a,b) --> w
        for e in self.relations:
            if len(e) == 2:
                self._weight[e] = 1
            else:
                self._weight[(e[0], e[1])] = e[2]

    def __init__(self, v, e, directed=True, view=True):
        self.directed = directed
        self.view = view
        self.vertexes = v
        self._buildRelation(e)
        self._buildAdjList()
        self._buildEncoding()
        self._buildAdjMatrix()
        self._buildWeight()

    def dijkstra(self, s):
        self._buildVProps(s)
        Q = [v for v in self.vertexes]
        S = set([])  # Mínimos locales
        while len(Q) > 0:
            minimo_local = self.extract_min(S, Q)
            S.add(minimo_local)
            for neighbors in self.getNeighbors(minimo_local):
                self.relax((minimo_local, neighbors, self._weight[(minimo_local, neighbors)]))
        return self.v_props

    def extract_min(self, S, Q):
        min_vertex, min_distance = None, math.inf
        for v in self.vertexes:
            if v not in S and min_distance > self.v_props[v]['distance']:
                min_vertex, min_distance = v, self.v_props[v]['distance']
        Q.remove(min_vertex)
        return min_vertex

    def relax(self, e):
        source, destination, weight = e[0], e[1], e[2]
        if self.v_props[destination]['distance'] > self.v_props[source]['distance'] + weight:
            self.v_props[destination]['distance'] = self.v_props[source]['distance'] + weight
            self.v_props[destination]['parent'] = source
            return True
        return False

    def _buildVProps(self, source=None):
        self.v_props = {}
        for v in self.vertexes:
            self.v_props[v] = {
                'color': WHITE,
                'distance': math.inf,
                'parent': None
            }
        if source is not None:
            self.v_props[source] = {
                'color': GRAY,
                'distance': 0,
                'parent': None
            }

    def getNeighbors(self, vertex):
        return self.adjList.get(vertex, [])


def getPath(vertex, v_props):
    path = [vertex]
    current = vertex
    while (v_props[current]['parent'] is not None):
        path.insert(0, v_props[current]['parent'])
        current = v_props[current]['parent']
    return path

# nuevo code
class SucursalGalactrita:
    def __init__(self, nombre, planeta, inventario_inicial=None):
        self.nombre = nombre
        self.planeta = planeta
        self.inventario = inventario_inicial or {}
        self.conexiones = []
        self.balance = 0

class RedSucursales:
    def __init__(self):
        self.sucursales = {}
        self.grafo_conexiones = None

    def agregar_sucursal(self, sucursal):
        self.sucursales[sucursal.nombre] = sucursal

    def establecer_conexion(self, sucursal_origen, sucursal_destino, distancia, costo_envio):
        if sucursal_origen in self.sucursales and sucursal_destino in self.sucursales:
            self.sucursales[sucursal_origen].conexiones.append((sucursal_destino, distancia, costo_envio))
            self.sucursales[sucursal_destino].conexiones.append((sucursal_origen, distancia, costo_envio))

    def construir_grafo_conexiones(self):
        vertices = list(self.sucursales.keys())
        aristas = []

        for sucursal_nombre, sucursal in self.sucursales.items():
            for conexion in sucursal.conexiones:
                aristas.append((sucursal_nombre, conexion[0], conexion[1]))

        self.grafo_conexiones = Graph(vertices, aristas)

    def transferir_inventario(self, origen, destino, producto, cantidad):
        if (origen in self.sucursales and destino in self.sucursales and
                producto in self.sucursales[origen].inventario):

            # Verificar si hay suficiente stock
            if self.sucursales[origen].inventario[producto] >= cantidad:
                # Reducir stock en origen
                self.sucursales[origen].inventario[producto] -= cantidad

                # Aumentar stock en destino
                if producto not in self.sucursales[destino].inventario:
                    self.sucursales[destino].inventario[producto] = 0
                self.sucursales[destino].inventario[producto] += cantidad

                # Calcular costo de envío
                costo_envio,ruta = self.calcular_costo_transferencia(origen, destino)
                self.sucursales[origen].balance -= costo_envio

                print(f"Envío exitoso. Costo de envío: {costo_envio}. "
                      f"Nuevo balance de {origen}: {self.sucursales[origen].balance}")

                return True

            else:
                print("Inventario insuficiente para realizar el envío.")
        else:
            print("Datos inválidos: producto no encontrado o sucursales inexistentes.")
        return False

    def calcular_costo_transferencia(self, origen, destino):
        ruta = self.ruta_mas_corta(origen, destino)
        costo_total = 0

        for i in range(len(ruta) - 1):
            for conexion in self.sucursales[ruta[i]].conexiones:
                if conexion[0] == ruta[i + 1]:
                    costo_total += conexion[2]
                    break

        return costo_total,ruta

    def ruta_mas_corta(self, origen, destino):
        if not self.grafo_conexiones:
            self.construir_grafo_conexiones()

        propiedades = self.grafo_conexiones.dijkstra(origen)

        camino = getPath(destino, propiedades)
        return camino


# Producto y Tienda =============================================
class Producto:
    def __init__(self, nombre, precio, cantidad, tipo, material, durabilidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.tipo = tipo
        self.material = material
        self.durabilidad = durabilidad

    @property
    def calc_precio(self):

        nuevo_precio = self.precio

        if self.tipo == "arma":
            nuevo_precio = self.precio * 1.3
            if self.material == "oro":
                nuevo_precio += 1500
            elif self.material == "plata":
                nuevo_precio += 1000
            else:
                nuevo_precio += 800

        else:
            if self.material == "oro":
                nuevo_precio += 800
            elif self.material == "plata":
                nuevo_precio += 500
            else:
                nuevo_precio += 200

        if self.durabilidad:
            if self.tipo == "arma":
                if self.durabilidad == "500":
                    nuevo_precio = nuevo_precio
                elif self.durabilidad == "1000":
                    nuevo_precio += 400
                else:
                    nuevo_precio += 700
            elif self.tipo == "consumible":
                if self.durabilidad == "Unico":
                    nuevo_precio = nuevo_precio
                elif self.durabilidad == "Pocos":
                    nuevo_precio += 15
                elif self.durabilidad == "Varios":
                    nuevo_precio += 30
                else:
                    nuevo_precio += 50
            elif self.tipo == "municion":
                if self.durabilidad == "1":
                    nuevo_precio = nuevo_precio
                elif self.durabilidad == "5":
                    nuevo_precio += 5
                elif self.durabilidad == "15":
                    nuevo_precio += 20
                else:
                    nuevo_precio += 35
            elif self.tipo == "herramienta":
                if self.durabilidad == "4 meses":
                    nuevo_precio = nuevo_precio
                elif self.durabilidad == "8 meses":
                    nuevo_precio += 100
                else:
                    nuevo_precio += 250
            else:
                if self.durabilidad == "1 año":
                    nuevo_precio = nuevo_precio
                elif self.durabilidad == "3 años":
                    nuevo_precio += 300
                else:
                    nuevo_precio += 500
        self.precio = nuevo_precio
        return nuevo_precio

    def vender(self, cantidad_vendida):
        if cantidad_vendida > self.cantidad:
            raise Exception("Cantidad insuficiente en stock")
        self.cantidad -= cantidad_vendida
        return self.calc_precio * cantidad_vendida

    def adicionar_stock(self, cantidad):
        self.cantidad += cantidad

    def modificar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        self.precio = self.calc_precio

    def modificar_caracteristicas(self, nombre, precio, cantidad, tipo, material, durabilidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.tipo = tipo
        self.material = material
        self.durabilidad = durabilidad


    def __str__(self):
        return f"Producto: {self.nombre} | Precio: {self.precio} | Cantidad: {self.cantidad}"

    def mostrar_informacion(self):
        print(str(self))


# Nueva clase de Sucursal
class Sucursal:
    def __init__(self, nombre, planeta):
        self.nombre = nombre
        self.planeta = planeta
        self.inventario = HashTable(11)
        self.conexiones = []
        self.balance = 0

    def agregar_producto(self, producto):
        self.inventario.insert(producto.nombre, producto)

    def transferir_producto(self, producto_nombre, cantidad, sucursal_destino):
        # Buscar el producto en el inventario actual
        producto = self.inventario.search(producto_nombre)

        if not producto:
            print(f"Producto {producto_nombre} no encontrado en {self.nombre}")
            return False

        if producto.cantidad < cantidad:
            print(f"Cantidad insuficiente de {producto_nombre} en {self.nombre}")
            return False

        # Reducir cantidad en el origen
        producto.cantidad -= cantidad

        # Transferir a la sucursal destino
        producto_transferido = Producto(
            producto.nombre,
            producto.precio,
            cantidad,
            producto.tipo,
            producto.material,
            producto.durabilidad
        )
        sucursal_destino.agregar_producto(producto_transferido)

        return True

    def establecer_conexion(self, sucursal_destino, distancia, costo_envio):
        self.conexiones.append((sucursal_destino, distancia, costo_envio))


class Tienda:
    def __init__(self):
        self.inventario = HashTable(11)
        self.balance = 0
        self.sucursales = []

    def crear_sucursal(self, nombre, planeta):
        nueva_sucursal = Sucursal(nombre, planeta)
        self.sucursales.append(nueva_sucursal)
        return nueva_sucursal

    def agregar_producto(self, producto):
        self.inventario.insert(producto.nombre, producto)

    def vender_producto(self, nombre_producto, cantidad):
        producto = self.inventario.search(nombre_producto)
        if not producto:
            print("Producto no encontrado")
            return
        ganancia = producto.vender(cantidad)
        self.balance += ganancia
        print(f"Se vendieron {cantidad} {nombre_producto}(s) por {ganancia}. Balance: {self.balance}")

    def mostrar_inventario(self):
        for bucket in self.inventario.elements:
            node = bucket.getHead()
            while node:
                node.getValue()[1].mostrar_informacion()
                node = node.getNext()
        #print("===" * 20, "HASHTABLE", "===" * 20)
        #print(self.inventario)

    def mostrar_balance(self):
        print(f"Balance actual: {self.balance}")

    def calcular_ruta_minima(self, origen, destino):
        # Crear vértices (nombres de sucursales)
        vertices = [sucursal.nombre for sucursal in self.sucursales]

        # Crear aristas con conexiones
        aristas = []
        for sucursal in self.sucursales:
            for conexion in sucursal.conexiones:
                aristas.append((sucursal.nombre, conexion[0].nombre, conexion[1]))

        # Crear grafo
        grafo = Graph(vertices, aristas)

        # Calcular ruta más corta
        try:
            propiedades = grafo.dijkstra(origen)
            ruta = getPath(destino, propiedades)
            return ruta
        except Exception as e:
            print(f"Error al calcular ruta: {e}")
            return None


def productos_prueba(tienda):
    productos = [
        Producto("Rifle a0 plasma", 10000, 8, "arma", "plata", "1500 disparos"),
        Producto("AK-47", 1200, 10, "arma", "oro", "1500 disparos"),
        Producto("Cubo de iones", 5000, 50, "consumible", "plata", "Varios"),
        Producto("Pared gloo",500,60,"consumible","titanio","unico"),
        Producto("Cartuchos a0", 10, 1200, "municion", "titanio", "30 cartuchos"),
        Producto("Cartuchos 5.56",50,2000,"municion","plata","15 cartuchos"),
        Producto("Generador de Energía de iones", 20000, 5, "herramienta", "titanio", "8 meses"),
        Producto("Alicates interdimensionales",1000,130,"herramienta","titanio","8 meses"),
        Producto("Dron minero", 15000, 20, "compañero", "titanio", "3 años"),
        Producto("Robot salvaje",45000,15,"compañero","oro","3 años")

    ]
    for producto in productos:
        tienda.agregar_producto(producto)
    return productos

# IMPLEMENTACION DISJOITSETS
class DisjointSets:

    def __init__(self, A):
        self.sets = [set([x]) for x in A]

    def getSets(self):
        return self.sets

    def findSet(self, x):
        for si in self.sets:
            if x in si:
                return si
        return None

    def makeSet(self, x):
        if self.findSet(x) is None:
            self.sets.append(set([x]))
            return self.sets[len(self.sets)-1]
        return self.findSet(x)

    def union(self, x, y):
        s1 = self.findSet(x)
        s2 = self.findSet(y)

        if s1 is None:
            s1 = self.makeSet(x)
        if s2 is None:
            s2 = self.makeSet(y)
        if s1 != s2:
            s3 = s1.union(s2)
            self.sets.remove(s1)
            self.sets.remove(s2)
            self.sets.append(s3)

    def connectedComponents(self, Arcs):
        for e in Arcs:
            self.union(e[0], e[1])
            print('After processing arc', e, self.sets)
        result = []
        for si in self.sets:
            if len(si) > 1:
                result.append(si)
        return result


def imprimir_conexiones(red):
    conexiones_directas = set()

    for sucursal_nombre, sucursal in red.sucursales.items():
        for conexion in sucursal.conexiones:
            # Almacenar solo conexiones directas en orden único
            conexiones_directas.add(tuple(sorted((sucursal_nombre, conexion[0]))))

    print("Conexiones directas entre sucursales:")
    for origen, destino in conexiones_directas:
        print(f"({origen}) <-> ({destino})")



# filtrar productos por tipos
def agrupar_por_tipo(inventario):
    tipos = set()
    objetos = []

    # Recolectar los tipos y objetos del inventario
    for bucket in inventario.elements:
        node = bucket.getHead()
        while node:
            producto = node.getValue()[1]
            tipos.add(producto.tipo)
            objetos.append((producto.tipo, producto))
            node = node.getNext()

    disjoint_tipos = DisjointSets(tipos)  # Crear conjuntos iniciales por tipos

    # Agrupar objetos en conjuntos por tipo
    for tipo, producto in objetos:
        disjoint_tipos.union(tipo, producto)
    #print(disjoint_tipos.sets)
    return disjoint_tipos

def mostrar_por_tipo(disjoint_tipos, tipo):
    conjunto = disjoint_tipos.findSet(tipo)
    print("\n =============================================")
    if conjunto:
        print(f"Objetos de tipo '{tipo}':")
        for obj in conjunto:
            if obj != tipo:  # Evitar mostrar el tipo como parte de los objetos
                print(f"- {obj.nombre}|| precio: {obj.precio}")
    else:
        print(f"No hay objetos de tipo '{tipo}'.")

# IMPLEMENTACION DE MONTONES BINARIOS
class Heap:
    # config : True // Max_Heap
    # config : False // Min_heap
    def __init__(self, data=[], config=False):
        self.data = []
        self.config = config
        self.build(data[:])

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * (index + 1)

    def parent(self, index):
        return (index - 1) // 2

    def height(self):
        return math.ceil(math.log(len(self.data), 2))

    def __len__(self):
        return len(self.data)

    def insert(self, new):
        self.data.append(new)
        self.build()

    def update(self, old, new):
        self.delete(old)
        self.insert(new)

    def delete(self, to_delete):
        if len(self) == 0:
            raise Exception("El montón está vacio")
        if to_delete not in self.data:
            raise Exception("El elemento no está en el montón")
        self.data.remove(to_delete)
        self.build()

    def build(self, data=[]):
        if data and len(data) > 0 and isinstance(data, list):
            self.data = data
        for index in range(len(self) // 2, -1, -1):
            self.heapify(index)

    def heapify(self, index):
        if self.config:
            self.max_heapify(index)
        else:
            self.min_heapify(index)

    def max_heapify(self, index):
        left_index, right_index, largest_index = self.left(index), self.right(index), index
        if left_index < len(self) and self.data[largest_index] < self.data[left_index]:
            largest_index = left_index
        if right_index < len(self) and self.data[largest_index] < self.data[right_index]:
            largest_index = right_index
        if largest_index != index:
            self.data[largest_index], self.data[index] = self.data[index], self.data[largest_index]
            self.max_heapify(largest_index)

    def peek(self):
        return self.data[0]

    def min_heapify(self, index):
        left_index, right_index, smallest_index = self.left(index), self.right(index), index
        if left_index < len(self) and self.data[smallest_index] > self.data[left_index]:
            smallest_index = left_index
        if right_index < len(self) and self.data[smallest_index] > self.data[right_index]:
            smallest_index = right_index
        if smallest_index != index:
            self.data[smallest_index], self.data[index] = self.data[index], self.data[smallest_index]
            self.min_heapify(smallest_index)


    def __str__(self):
        return str(self.data)


class PriorityQueue:
    def __init__(self, data=[], config=False):
        self.data = Heap(data, config)

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def enqueue(self, new):
        self.data.insert(new)

    def dequeue(self):
        if len(self) == 0:
            raise Exception("Underflow")
        to_dequeue = self.data.peek()
        self.data.delete(to_dequeue)
        return to_dequeue



def opcion_alerta_producto_menor_stock(tienda):
    heap = PriorityQueue(config=False)
    for bucket in tienda.inventario.elements:
        node = bucket.getHead()
        while node:
            producto = node.getValue()[1]
            heap.enqueue((producto.cantidad, producto))  # Usar la cantidad como prioridad
            node = node.getNext()


    # Obtener el producto con menor cantidad en stock
    if len(heap) > 0:
        cantidad, producto = heap.dequeue()
        print(f"Alerta: El producto con menor stock es '{producto.nombre}' con {cantidad} unidades.")
    else:
        print("El inventario está vacío.")




def main():
    print("============================= Bienvenido a la tienda =============================")
    tienda = Tienda()
    productos_prueba(tienda)
    print("Este es tu inventario:")
    tienda.mostrar_inventario()
    print("\nTenga en cuenta que los 3 materiales que hay son: oro, plata y titanio \n tambien tenga en cuenta que la durabilidad depende del tipo, 500,100 o 1500 para las armas. \n para consumible unico, pocos, varios o duradero que se refiere a los usos. \n para municion 1,5,15 o 30 cartuchos \n para herramienta 4,8 o 12 meses \n para compañero es 1,3 o 5 años.\n")
    time.sleep(2)
    # Crear red de sucursales
    red = RedSucursales()

    # Crear sucursales
    sucursal_tierra = SucursalGalactrita("Tierra Central", "Tierra",
                                         {"Rifle a0 plasma": 10, "Generador de Energía de iones": 5})

    # Unificar inventario de Tierra Central con el de la tienda principal
    for bucket in tienda.inventario.elements:
        node = bucket.getHead()
        while node:
            producto = node.getValue()[1]
            if producto.nombre in sucursal_tierra.inventario:
                sucursal_tierra.inventario[producto.nombre] += producto.cantidad
            else:
                sucursal_tierra.inventario[producto.nombre] = producto.cantidad
            node = node.getNext()

    sucursal_marte = SucursalGalactrita("Base Marciana", "Marte",
                                        {"Dron minero": 20, "Cubo de iones": 50})
    sucursal_jupiter = SucursalGalactrita("Estación Júpiter", "Júpiter",
                                          {"Cartuchos a0": 1200})
    sucursal_halo = SucursalGalactrita("Halo","Epsilon Eridani II",{"Cubo de iones":200})

    sucursal_asgard = SucursalGalactrita("Asgard","Asgard",{"Dron minero":30,"Rifle a0 plasma":10})

    sucursal_4546B = SucursalGalactrita("4546B","4546B")
    sucursal_Heridanus = SucursalGalactrita("Heridanus II","Heridanus II")
    sucursal_Reach = SucursalGalactrita("Reach","Reach")


    # Agregar sucursales a la red
    red.agregar_sucursal(sucursal_tierra)
    red.agregar_sucursal(sucursal_marte)
    red.agregar_sucursal(sucursal_jupiter)
    red.agregar_sucursal(sucursal_halo)
    red.agregar_sucursal(sucursal_asgard)
    red.agregar_sucursal(sucursal_4546B)
    red.agregar_sucursal(sucursal_Heridanus)
    red.agregar_sucursal(sucursal_Reach)
    # Establecer conexiones entre sucursales
    red.establecer_conexion("Tierra Central", "Base Marciana", 80, 800)
    red.establecer_conexion("Tierra Central", "Estación Júpiter", 650, 6500)
    red.establecer_conexion("Base Marciana", "Estación Júpiter", 550, 5500)
    red.establecer_conexion("Base Marciana","Halo",270,2700)
    red.establecer_conexion("Halo","Asgard",7000,70000)
    red.establecer_conexion("Halo","Reach",500,5000)
    red.establecer_conexion("Reach","Heridanus II",400,4000)
    red.establecer_conexion("Base Marciana","4546B",2000,20000)
    red.establecer_conexion("4546B","Heridanus II",5000,50000)


    while True:
        print("\n1. Mostrar inventario\n2. Vender producto\n3. Adicionar stock\n4. Modificar precio\n"
              "5. Agregar nuevo producto\n6. Mostrar balance\n7. Modificar características\n8. Envios Sucursales"
                "\n9. Inventario por tipo. \n10. Producto con menor stock. \n11. salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            tienda.mostrar_inventario()
        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            producto = tienda.inventario.search(nombre)
            if producto:
                try:
                    ganancia = producto.vender(cantidad)
                    tienda.balance += ganancia
                    print(f"Se vendieron {cantidad} {nombre}(s) por {ganancia}. Balance: {tienda.balance}")
                    if nombre in sucursal_tierra.inventario:
                        sucursal_tierra.inventario[nombre] -= cantidad
                        print(f"Inventario actualizado también en Tierra Central.")
                except Exception as e:
                    print(e)
            else:
                print("Producto no encontrado.")
        elif opcion == "3":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad a adicionar: "))
            producto = tienda.inventario.search(nombre)
            if producto:
                producto.adicionar_stock(cantidad)
                if nombre in sucursal_tierra.inventario:
                    sucursal_tierra.inventario[nombre] += cantidad
                else:
                    sucursal_tierra.inventario[nombre] = cantidad
                print(f"Inventario actualizado tanto en la tienda como en Tierra Central.")
            else:
                print("Producto no encontrado.")
        elif opcion == "4":
            nombre = input("Nombre del producto: ")
            nuevo_precio = int(input("Nuevo precio: "))
            producto = tienda.inventario.search(nombre)
            if producto:
                producto.modificar_precio(nuevo_precio)
            else:
                print("Producto no encontrado.")
        elif opcion == "5":
            nombre = input("Nombre del nuevo producto: ")
            precio = int(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            tipo = input("Tipo: ")
            material = input("Material: ")
            durabilidad = input("Durabilidad: ")
            producto = Producto(nombre, precio, cantidad, tipo, material, durabilidad)
            tienda.agregar_producto(producto)
            if nombre in sucursal_tierra.inventario:
                sucursal_tierra.inventario[nombre] += cantidad
            else:
                sucursal_tierra.inventario[nombre] = cantidad
            print(f"Producto agregado tanto en la tienda como en Tierra Central.")
        elif opcion == "6":
            tienda.mostrar_balance()
        elif opcion == "7":
            nombre = input("Nombre del producto: ")
            producto = tienda.inventario.search(nombre)
            if producto:
                nombre_nuevo = input("Nuevo nombre: ")
                precio = int(input("Nuevo precio: "))
                cantidad = int(input("Nueva cantidad: "))
                tipo = input("Nuevo tipo: ")
                material = input("Nuevo material: ")
                durabilidad = input("Nueva durabilidad: ")
                producto.modificar_caracteristicas(nombre_nuevo, precio, cantidad, tipo, material, durabilidad)

            else:
                print("Producto no encontrado.")
        elif opcion == "8":
            print("=="*10 + "ENVIOS" + "=="*10)
            opcion = int(input("Ingresa una opcion:\n1.Mostrar red de envios. \n2.Realizar envio.\n"))
            if opcion == 1:
                imprimir_conexiones(red)
            elif opcion == 2:
                sucursal_origen = "Tierra Central"
                sucursal_destino = input("Nombre de la sucursal de destino: ")
                producto = input("Producto a enviar: ")
                cantidad = int(input("Cantidad a enviar: "))

                if red.transferir_inventario(sucursal_origen, sucursal_destino, producto, cantidad):
                    if sucursal_origen == "Tierra Central":
                        producto_tienda = tienda.inventario.search(producto)
                        if producto_tienda:
                            producto_tienda.cantidad -= cantidad
                            costo_envio, ruta = red.calcular_costo_transferencia("Tierra Central", sucursal_destino)
                            tienda.balance -= costo_envio
                            print(f"-La ruta para entregar el producto fue: {ruta}")
                            print(f"-Inventario de la tienda actualizado. Nuevo balance: {tienda.balance}")
                    print("Envío realizado con éxito.")
                else:
                    print("Error en el envío.")
            else:
                print("opcion no valida")

        elif opcion == "9":
            disjoint_tipos = agrupar_por_tipo(tienda.inventario)
            tipo = input("Ingresa el tipo de objeto a mostrar: ")
            mostrar_por_tipo(disjoint_tipos, tipo)


        elif opcion == "10":
            opcion_alerta_producto_menor_stock(tienda)

        elif opcion == "11":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

main()
