#importando el modulo Arrays
from array import array as arr
#creando un arreglo
array_01 =arr('i', [3,8,5,1,6])

#iterando automaticamente 
for data in array_01:
    print(data,end=",")
print()


#Array
# Fro, array of import 
import array as arr

#creacion de un arreglo
#i: Entero con un signo 
#I: Entero sin signo
#f: Numero decimal
#d: Numero decimal de doble 
#u: Carácteres unicode
my_array = arr.array('i',[11, 22, 333,33,77, 44, 55, 88, 777, 666,888])

#Interación automatica
for num in my_array:
    print(num)

#Acceso invidual a los elementos del arreglo
print(my_array[0]) #primero elemento
print(my_array[1]) #segundo elemento
print(my_array[1]) #tercer elemento   

#Tamaño del arreglo
#Length
print(len(my_array)) #tamaño del arreglo

#Iteración con indices
for i in range(len(my_array)):
    print(f"Elemento {i+1}: {my_array[i]}")

#print(f"Elemento Num {i+1}: {my_array[i]}") para imprimir solo los pares
    

