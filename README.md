# Graphy Recommendation Algorithm

## Descripción

Este repositorio contiene la implementación del algoritmo de recomendación de productos para la aplicación Graphy. Utiliza una versión modificada del algoritmo de Prim y técnicas de análisis de grafos para generar recomendaciones personalizadas basadas en las características de los productos y el historial de compras.

## Características principales

- Implementación del algoritmo de Prim modificado para recomendaciones
- Análisis de grafos para determinar relaciones entre productos
- Recomendaciones basadas en atributos de productos (categoría, subcategoría, marca, tipo)
- Recomendaciones adicionales basadas en la marca del producto seleccionado

## Tecnologías utilizadas

- Python 3.x
- Bibliotecas: pandas, networkx, matplotlib

## Instalación

1. Clona el repositorio:
   ```
   git clone https://github.com/tu-usuario/graphy-recommendation-algorithm.git
   ```

2. Instala las dependencias:
   ```
   pip install networkx
   pip install -U matplotlib
   ```

## Uso

1. Asegúrate de tener los archivos `productos.csv` y `conexiones.csv` en el mismo directorio que `graph.py`.

2. Ejecuta el script:
   ```
   python graph.py
   ```

3. El script generará visualizaciones de los grafos y mostrará las recomendaciones en la consola.

## Funcionamiento del algoritmo

1. **Carga de datos**: Lee los datos de productos y conexiones desde archivos CSV.

2. **Construcción del grafo**: Crea un grafo donde los nodos son productos y las aristas representan la similitud entre productos.

3. **Cálculo de pesos**: Determina el peso de las aristas basándose en la similitud de atributos entre productos.

4. **Delimitación del grafo**: Crea un subgrafo centrado en el producto seleccionado.

5. **Algoritmo de Prim modificado**: Implementa una versión modificada del algoritmo de Prim para encontrar el árbol de expansión máxima.

6. **Recomendaciones por marca**: Genera recomendaciones adicionales basadas en productos de la misma marca.

7. **Visualización**: Genera visualizaciones de los grafos resultantes.

## Personalización

Para modificar el producto de inicio para las recomendaciones, cambia el valor de `start_node` en el script.

## Visualizaciones

El script genera tres visualizaciones:
1. Grafo de conexiones de productos con pesos
2. Grafo de recomendaciones (resultado del algoritmo de Prim modificado)
3. Grafo de recomendaciones por marca

## Contribución

Si deseas contribuir al proyecto, por favor:

1. Haz un fork del repositorio
2. Crea una nueva rama (`git checkout -b feature/NuevaCaracteristica`)
3. Haz commit de tus cambios (`git commit -m 'Añade alguna NuevaCaracteristica'`)
4. Haz push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
