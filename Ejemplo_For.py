# Marco Antonio Morales González

# ESTE CODIGO IMPRIME LOS ELEMENTOS DE UNA LISTA JUNTO CON SU POSICION

# 07 / 03 / 2025 - V. 1. 0. 0 - EJEMPLO FOR

lista = ["manzana", 873, "UV"] #Creamos la lista 
i=1  #Definimos la variable que nos ayudara a saber que posicion de la lista estamos imprimiendo

for elemento in lista:  #Definimos la estructura del for
    print(f'El elemento numero {i} de la lista es {elemento}') #Imprimimos el numero de elemento y el elemento mismo
    i+=1 #Sumamos 1
