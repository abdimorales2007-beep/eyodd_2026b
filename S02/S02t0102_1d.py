#importando el modulo Arrays de
# la biblioteca array y renombrandolo como arr
from array import array as arr

def print_array(input_array):
   print("[",end=" ")
   for element in input_array:
      print(element,end=",",)
   print("]")   

my_array = arr('i',[2,10,15,20])
print_array(my_array)

#buscar el elemento 15
number_to_search = 100
counter = 0
print(f"Buscando el numero {number_to_search} en el arreglo.")
for integer in my_array:
   if integer == number_to_search:
      print(" 🥳 Numero encontrado!!")
      #sirve para terminar siclo break
      break
   counter += 1
   if counter == len(my_array):
      print("🔍Numero no encontrado!!")