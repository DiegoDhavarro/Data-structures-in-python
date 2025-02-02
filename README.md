# Galactrita Shop - Sistema de Gestión de Inventario y Ventas Interplanetario

Galactrita Shop es un sistema de gestión de inventario y ventas diseñado para una tienda interplanetaria que vende productos como armas, consumibles, municiones, herramientas y compañeros robóticos. El sistema permite gestionar inventarios, realizar ventas, transferir productos entre sucursales en diferentes planetas, y calcular rutas óptimas para envíos interplanetarios.

---

## Características Principales

- **Gestión de Inventario**: Añadir, modificar y eliminar productos.
- **Ventas**: Registrar ventas de productos y actualizar el balance de la tienda.
- **Transferencias entre Sucursales**: Enviar productos entre sucursales en diferentes planetas.
- **Cálculo de Rutas Óptimas**: Usa el algoritmo de Dijkstra para calcular la ruta más corta entre sucursales.
- **Alertas de Stock**: Identifica productos con bajo stock.
- **Agrupación por Tipo**: Organiza y muestra productos por categorías (armas, consumibles, municiones, etc.).
- **Sucursales Interconectadas**: Conexiones entre sucursales con costos de envío y distancias.

---

## Uso

El programa es interactivo y ofrece un menú con las siguientes opciones:

1. **Mostrar inventario**: Muestra todos los productos en el inventario.
2. **Vender producto**: Registra una venta y actualiza el balance.
3. **Adicionar stock**: Añade más unidades de un producto al inventario.
4. **Modificar precio**: Cambia el precio de un producto.
5. **Agregar nuevo producto**: Añade un nuevo producto al inventario.
6. **Mostrar balance**: Muestra el balance actual de la tienda.
7. **Modificar características**: Cambia las características de un producto.
8. **Envíos Sucursales**:
   - Mostrar la red de envíos.
   - Realizar un envío entre sucursales.
9. **Inventario por tipo**: Muestra productos agrupados por tipo (armas, consumibles, etc.).
10. **Producto con menor stock**: Muestra una alerta del producto con menor stock.
11. **Salir**: Cierra el programa.

---

## Ejemplo de Funcionamiento

### Transferencia entre Sucursales
1. Selecciona la opción **8. Envíos Sucursales**.
2. Elige **2. Realizar envío**.
3. Ingresa la sucursal de destino, el producto y la cantidad.
4. El sistema calculará la ruta más corta y el costo de envío, y actualizará los inventarios.

### Agrupación por Tipo
1. Selecciona la opción **9. Inventario por tipo**.
2. Ingresa el tipo de producto (por ejemplo, "arma").
3. El sistema mostrará todos los productos de ese tipo.

### Alerta de Stock
1. Selecciona la opción **10. Producto con menor stock**.
2. El sistema mostrará el producto con la menor cantidad en stock.

---

## Estructura de Archivos

- **`GalactritaShopFinal.py`**: Archivo principal que contiene todo el código del proyecto.
- **`README.md`**: Este archivo, que proporciona una descripción del proyecto.

---

## Créditos

- **Desarrollado por**: Diego F. Chavarro
- **Herramientas utilizadas**:
  - **Python**: Lenguaje de programación utilizado.

---

## Estado del Proyecto

🛠️ **En desarrollo**: El proyecto está en fase de desarrollo. Se están implementando nuevas funcionalidades y mejorando la estructura actual.

---

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE). Siéntete libre de usarlo y modificarlo según tus necesidades.

---

## Contacto

Si tienes preguntas o sugerencias, no dudes en contactarme:  
📧 [chavarrodiegofernando3@gmail.com]  
🌐 [(https://github.com/DiegoDhavarro)]

