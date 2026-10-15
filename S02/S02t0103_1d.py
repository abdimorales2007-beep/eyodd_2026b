from array import array as arr
#Importando funcion Array
#del modulo array y renombrar
#como arr 

#impotando una funcion de otro
#archivo

from S02t0102_1d import print_array

my_array = arr('i',[2,10,15,20,10])

print("---ANTES DE INSERCIÓN---")
print_array(my_array)

#Elimación
try:
    my_array.remove(100)
except:
    print("🔍Numero no encontrado!!")
print("---DESPUÉS DE ELIMINACIÓN---")
print_array(my_array) 

  

print("---DESPUES DEL APPEND---")
my_array.append(1000)
print_array(my_array)

print("---SIMILAR UN APPEND CON UN INSERT---")
my_array.insert(len(my_array), 90000)
print_array(my_array)