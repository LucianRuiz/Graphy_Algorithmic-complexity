import pandas as pd
import networkx as nx
import ast
import matplotlib.pyplot as plt

productos_df = pd.read_csv('productos.csv')
conexiones_df = pd.read_csv('conexiones.csv')

G = nx.Graph()

# Limita el número de filas procesadas
num_filas = 20  # Limite de filas a procesasr

# Crea una función para calcular el peso basado en la igualdad de valores de atributos
def calculate_weight(node1, node2):
    attributes1 = set(productos_df[productos_df['id'] == node1][['category', 'sub_category', 'brand', 'type']].values.flatten())
    attributes2 = set(productos_df[productos_df['id'] == node2][['category', 'sub_category', 'brand', 'type']].values.flatten())

    # Calcula la cantidad de valores iguales entre los conjuntos de atributos
    common_values = len(attributes1.intersection(attributes2))

    return common_values + 1 

def gen_edge(Graph,productos): #1 Implementar esta funcion en el github GraphyLi
    n = len(productos)
    if n > 1:
        for i in range(n - 1):
            source = productos[i]
            target = productos[i + 1]
            weight = calculate_weight(source, target)
            Graph.add_edge(source, target, weight=weight)
        source = productos[-1]
        target = productos[0]
        weight = calculate_weight(source, target)
        Graph.add_edge(source, target, weight=weight)

for idx, row in conexiones_df.iterrows():
    #if idx >= num_filas:
    #    break
    
    list_products_str = row['list_products']
    
    if pd.notna(list_products_str):  # Verifica si la cadena no es 'nan(invalida)'
        productos = ast.literal_eval(list_products_str)
        gen_edge(G,productos)





#Delimitacion el grafo y generacion del grafo delimitado

start_node = 89


def new_Graph(first_node):
    x = list(G[first_node].items())
    graph = []
    for i in x:
        edge = (first_node,i[0],i[1].get("weight"))
        graph.append(edge)
    for i in x:
        newfirst_node = i[0]
        newlist = list(G[newfirst_node].items())
        for j in newlist:
            edge = (newfirst_node,j[0],j[1].get("weight"))
            graph.append(edge)    
    return graph

nuevo = nx.Graph()

delimitado = new_Graph(start_node)

for i in delimitado:
    node1, node2, weight = i
    nuevo.add_edge(node1, node2, weight=weight)




#Aplicacion del algoritmo 




def Prim(G, start_node):
    mst = nx.Graph()
    visited = set([start_node])
    edges = []
    selected = []


    while len(visited) < len(G.nodes):
        min_edge = None

        for node in visited:
            for neighbor, data in G[node].items():
                if neighbor not in visited:
                    edges.append((node, neighbor, data['weight']))

        edges.sort(key=lambda x: x[2],reverse=True)
        for edge in edges:
            node1, node2, weight = edge
            if node1 in visited and node2 not in visited:
                min_edge = edge
                break

        if min_edge:
            node1, node2, weight = min_edge
            visited.add(node2)
            mst.add_edge(node1, node2, weight=weight)
            selected.append(node2)
        edges = []
      
    selected = selected[:10]
    return mst, selected


mst, seleccionados = Prim(nuevo, start_node)


print(seleccionados)

#Recomendacion por marca

# Obtiene la marca del producto seleccionado
marca_seleccionada = productos_df.loc[productos_df['id'] == start_node, 'brand'].values[0]

# Filtra los productos con la misma marca que el producto seleccionado
productos_misma_marca = productos_df[productos_df['brand'] == marca_seleccionada]

# Obtiene las IDs de los productos con la misma marca
ids_productos_misma_marca = productos_misma_marca['id'].convert_dtypes(int).tolist()

marcas = nx.Graph()

gen_edge(marcas,ids_productos_misma_marca)


print(f"Productos con la misma marca ({marca_seleccionada}): {ids_productos_misma_marca}")




# Dibuja el grafo con los pesos en las aristas
#plt.figure(figsize=(10, 10))
#pos = nx.shell_layout(G)  # Layout para la visualización
#edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
#nx.draw(G, pos, with_labels=True, node_size=300, node_color='skyblue', font_size=10, font_color='black')
#nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
#plt.title("Grafo de Conexiones de Productos con Pesos (Contando Valores Iguales de Atributos)")
#plt.show()


plt.figure(figsize=(8, 8))
pos = nx.spring_layout(nuevo)  # Layout para la visualización
edge_labels = {(u, v): d['weight'] for u, v, d in nuevo.edges(data=True)}
nx.draw(nuevo, pos, with_labels=True, node_size=300, node_color='skyblue', font_size=10, font_color='black')
nx.draw_networkx_edge_labels(nuevo, pos, edge_labels=edge_labels, font_size=8)
plt.title("Grafo de Conexiones de Productos con Pesos (Contando Valores Iguales de Atributos)")
plt.show()

plt.figure(figsize=(8, 8))
pos = nx.spring_layout(mst)  # Layout para la visualización
edge_labels = {(u, v): d['weight'] for u, v, d in mst.edges(data=True)}
nx.draw(mst, pos, with_labels=True, node_size=300, node_color='skyblue', font_size=10, font_color='black')
nx.draw_networkx_edge_labels(mst, pos, edge_labels=edge_labels, font_size=8)
plt.title("Grafo de Recomendaciones")
plt.show()

plt.figure(figsize=(8, 8))
pos = nx.spring_layout(marcas)  # Layout para la visualización
edge_labels = {(u, v): d['weight'] for u, v, d in marcas.edges(data=True)}
nx.draw(marcas, pos, with_labels=True, node_size=300, node_color='skyblue', font_size=10, font_color='black')
nx.draw_networkx_edge_labels(marcas, pos, edge_labels=edge_labels, font_size=8)
plt.title("Grafo de Recomendaciones por marca")
plt.show()
