import pandas as pd
import networkx as nx
import ast
import matplotlib.pyplot as plt

productos_df = pd.read_csv('productos.csv')
conexiones_df = pd.read_csv('conexiones.csv')

G = nx.Graph()

# Limita el número de filas procesadas
num_filas = 10  # Limite de filas a procesasr

# Crea una función para calcular el peso basado en la igualdad de valores de atributos
def calculate_weight(node1, node2):
    attributes1 = set(productos_df[productos_df['id'] == node1][['category', 'sub_category', 'brand', 'type']].values.flatten())
    attributes2 = set(productos_df[productos_df['id'] == node2][['category', 'sub_category', 'brand', 'type']].values.flatten())

    # Calcula la cantidad de valores iguales entre los conjuntos de atributos
    common_values = len(attributes1.intersection(attributes2))

    return common_values

for idx, row in conexiones_df.iterrows():
    if idx >= num_filas:
        break
    
    list_products_str = row['list_products']
    
    if pd.notna(list_products_str):  # Verifica si la cadena no es 'nan(invalida)'
        productos = ast.literal_eval(list_products_str)
        n = len(productos)
        
        if n > 1:
            for i in range(n - 1):
                source = productos[i]
                target = productos[i + 1]
                weight = calculate_weight(source, target)
                G.add_edge(source, target, weight=weight)
            source = productos[-1]
            target = productos[0]
            weight = calculate_weight(source, target)
            G.add_edge(source, target, weight=weight)

# Dibuja el grafo con los pesos en las aristas
plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G)  # Layout para la visualización
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw(G, pos, with_labels=True, node_size=300, node_color='skyblue', font_size=10, font_color='black')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
plt.title("Grafo de Conexiones de Productos con Pesos (Contando Valores Iguales de Atributos)")
plt.show()

