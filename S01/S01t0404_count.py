# Creamos una lista de estudiantes 
student_list_01 = ['Jordan','kobe','kyrie','Shack','luka']  

def random_function(students): 
 first = students[0] # O(1) 
 total = 0 # O(1) 
 new_list = [] # O(1)

 for student in students: #O(n)
   print("se le suma 1 a total")
   total += 1 #O(n) 
   new_list.append(student) #O(n)  
#agregar estudiante -> append 
#si el print esta fuera significa que no repite lo de arriba en este caso del for
 
 print(new_list) # O(1)      
 return total # O(1) 

print(f"Tamaño de lista: {len(student_list_01)}")
print(random_function(student_list_01)) 

# Calcular O(?)
# 0(2n) +0(5) = 0(2n+5) = 0(n)
