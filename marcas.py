import pandas as pd

# Especifica la ID del producto seleccionado
producto_seleccionado_id = 1  # Cambia 1 a la ID del producto que deseas seleccionar

# Carga tu archivo CSV en un DataFrame de pandas
productos_df = pd.read_csv('productos.csv')

# Obtiene la marca del producto seleccionado
marca_seleccionada = productos_df.loc[productos_df['id'] == producto_seleccionado_id, 'brand'].values[0]

# Filtra los productos con la misma marca que el producto seleccionado
productos_misma_marca = productos_df[productos_df['brand'] == marca_seleccionada]

# Obtiene las IDs de los productos con la misma marca
ids_productos_misma_marca = productos_misma_marca['id'].convert_dtypes(int).tolist()


print(f"Productos con la misma marca ({marca_seleccionada}): {ids_productos_misma_marca}")