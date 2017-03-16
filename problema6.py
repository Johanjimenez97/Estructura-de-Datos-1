cad="12389sdklasdkl23412389sdfkf23819"
x=int
z=0
for i in cad:
    try:
        x = int(i)
        if (x/2)*2 == x:
            z=z+1    
    except:
        x
print "la cadena de texto tiene",z,"numeros pares"