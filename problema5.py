# ploblema 5
cad="asdfasarboldfasfasarboldabarbololasdfasdfasd"
x=0
c=0
for i in cad: 
    if i=="a":
        if cad[x+1]=="r":
            if cad[x+2]=="b":
                if cad[x+3]=="o":
                    if cad[x+4]=="l":
                        c=c+1                   
    x=x+1
print "la palabra arbol esta",c,"veces dentro de la cadena de texto"
