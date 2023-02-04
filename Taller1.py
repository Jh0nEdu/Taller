import random
def primerPunto():
  mat = [[11, 23, 76, 34, 11],[14, 30, 92, 30, 101],[12, 45, 58, 92, 22],[74, 56, 49, 56, 100],[99, 5, 28, 47, 99]]
  dPrincipal = 0
  dSecundaria = len(mat) - 1
  flag = 0
  for i in range(len(mat)):
    dPrincipal += i
    dSecundaria -= i
    if mat[i][dPrincipal] == mat[i][dSecundaria]:
      flag += 1
    dPrincipal = 0
    dSecundaria = len(mat) - 1
    if flag == len(mat):
      print(True)
#primerPunto()

#segundo punto
def esCapicua(a):
  izq = len(a) - 1
  cont = 0
  for i in range(len(a)):
    izq -= i
    if a[i] == a[izq]:
      cont += 1
    izq = len(a) - 1
  if cont == len(a):
    print(True)
  else:
    print(False)
  
def diferenciarListas(a, b):
  diferencia = []
  cont = 0
  for i in range(len(a)):
    for t in b:
      if a[i] != t:
        cont += 1
      else:
        b.remove(t)  
    if cont == len(b):
      diferencia.append(a[i])
    cont = 0
  print(diferencia)
def tercerPunto():
  ejecuciones = int(input())
  lista = []
  for i in range(ejecuciones):
    linea1 = int(input())
    linea2 = int(input())
    list1 = [linea1]
    for t in range(linea1):
      dato = random.randint(1,9)
      list1.append(dato)
    lista.append(list1)
    print(list1)
    list2 = [linea2]
    for m in range(linea2):
      dato = random.randint(1,9)
      list2.append(dato)
    print(list2)
    lista.append(list2)
    diferenciarListas(list1,list2)
#tercerPunto()
