# 1. Definición de la función
def eliminar_duplicados(array):
    """
    Toma un array (lista), elimina los elementos duplicados
    y devuelve una nueva lista con elementos únicos.
    """
    return list(set(array))


# =========================================================
# 2. Pruebas y Casos Límite
# =========================================================

# Caso 1: Tu lista original
lista_usuario = [1,1,1,2,3,4,5,5,5,5,5,8,8,9,0,11,15,16,17,18,19,20,20]
print("--- Caso 1: Lista Original ---")
print("Antes: ", lista_usuario)
print("Después:", eliminar_duplicados(lista_usuario))

# Caso 2: Lista vacía (Caso límite común)
lista_vacia = []
print("\n--- Caso 2: Lista Vacía ---")
print("Antes: ", lista_vacia)
print("Después:", eliminar_duplicados(lista_vacia))

# Caso 3: Lista sin duplicados (No debería alterar nada)
lista_sin_duplicados = [1, 2, 3, 4, 5]
print("\n--- Caso 3: Sin Duplicados ---")
print("Antes: ", lista_sin_duplicados)
print("Después:", eliminar_duplicados(lista_sin_duplicados))

# Caso 4: Todos los elementos son iguales
lista_identicos = [7, 7, 7, 7, 7]
print("\n--- Caso 4: Todos Identificados ---")
print("Antes: ", lista_identicos)
print("Después:", eliminar_duplicados(lista_identicos))

# Caso 5: Tipos de datos mixtos (Números, cadenas y booleanos)
lista_mixta = [1, "hola", 1, True, "hola", 2, False, 0]
print("\n--- Caso 5: Tipos Mixtos ---")
print("Antes: ", lista_mixta)
print("Después:", eliminar_duplicados(lista_mixta))
