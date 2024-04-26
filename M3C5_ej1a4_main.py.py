#Ejercicio 1: Cree un bucle For de Python.

nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

for i in lista_nombre:
  if i == nombre:
    print('El nombre está en la lista de nombres')
    break
else:
  print('Lo siento, el nombre no está en la lista de nombres')


#Ejercicio 2: Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3

def suma(a,b,c):
  x = a+b+c
  return x

print(suma(2,5,3))  


#Ejercicio 3: Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

suma = lambda a,b,c : a + b + c
print(suma(3,7,9))  


#Ejercicio 4: -Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.

nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

if nombre in lista_nombre:
  print('El nombre está en la lista de nombres')
else:
  print('Lo siento, el nombre no está en la lista de nombres')