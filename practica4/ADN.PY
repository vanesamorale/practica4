import random
def ADN(z):
    s=""
    while z<20 or z>1000:
        print("¡ERROR!, el tamaño debe de estar entre 20 y 1000")
        z=int(input("Ingrese la longitud de la cadena [20, 1000]:"))
    for i in range(z):
        c=random.randint(1,4)
        if c==1:
            s+="A"
        else:
            if c==2:
                s+="C"
            else:
              if c==3:
                 s+="G"
              else:
                s+="T"
    return s
            
     
        
    
X=int(input("Ingrese la longitud de la cadena [20, 1000]:"))

print("la cadena ADN es:",ADN(X))
from modulo import *
def VALIDARADN(cad):
    cad=aMayus(cad)
    floag=True
    for i in range(len(cad)):
        if cad[i]!="A"and  cad[i]!="C" and cad[i]!="G"and  cad[i]!="T" :
            floag=False
        else:
            floag=True
    return floag
from modulo import *
n=int(input("Ingrese la longitud de la cadena [20, 1000]:"))
cad=ADN(n)
fla1=VALIDARADN(cad)

while fla1==False:
    print("error,no  es una cadema")
    cad=ADN(n)
    fla=VALIDARADN(cad)
print("la cadena ADN;          ",cad)
print("la cadena invertida ADN:",invertido(cad))
       
        





    
c=input("ingrese:")
print(VALIDARADN(c))
