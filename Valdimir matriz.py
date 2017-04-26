f1=[1,1,1]
f2=[0,1,0]
f3=[0,1,1]
c1=[1,0,0]
c2=[1,1,1]
c3=[1,0,1]
matriz=[f1,f2,f3,c1,c2,c3]
filas= int (input("Numero de filas: "))
columnas= int (input("Numero de columnas: "))
for i in range (filas):
    matriz.append( [0]*columnas)
for f in range (filas,colomnas):
     for c in range (columnas):
        matriz.append( [0]*matriz)
print(matriz)
print(len(matriz))

