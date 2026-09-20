def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total


precio_producto = float(input("Ingrese el precio del producto: "))
cantidad_productos = int(input("Ingrese la cantidad de productos: "))

total_compra = calcular_total(precio_producto, cantidad_productos)

print("El precio total de la compra es:", total_compra)