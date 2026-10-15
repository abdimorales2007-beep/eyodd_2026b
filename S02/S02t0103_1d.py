from array import array as arr
#Importando funcion Array
#del modulo array y renombrar
#como arr 

#impotando una funcion de otro
#archivo

from S02t0102_1d import print_array

my_array = arr('i',[2,10,15,20])

print("---ANTES DE INSERCIÓN---")
print_array(my_array)

#Inserción 
my_array.insert(1, 90)
print("---DESPUÉS DE INSERCIÓN---")
print_array(my_array)   

print("---DESPUES DEL APPEND---")
my_array.append(1000)
print_array(my_array)

print("---SIMILAR UN APPEND CON UN INSERT---")
my_array.insert(len(my_array), 90000)
print_array(my_array)