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

def aMayus(cad):
    acum=""
    for i in range(0,len(cad)):
        sim=cad[i]
        if sim>="a"and sim<="z":
         cod=ord(sim)-32
         sim=chr(cod)
         acum+=sim
        elif sim=="á":
            acum+="A"
        elif  sim=="é":
            acum+="E"
        elif  sim=="í":
            acum+="I"
        elif sim=="ó":
            acum+=""
        elif sim=="ú":
            acum+="U"
        elif sim=="ñ":
            acum+="Ñ"
    
        else:
            acum+=sim
    return acum

def VALIDARADN(cad):
    cad=aMayus(cad)
    floag=True
    for i in range(len(cad)):
        if cad[i]!="A"and  cad[i]!="C" and cad[i]!="G"and  cad[i]!="T" :
            floag=False
        else:
            floag=True
    return floag
def   invertido(c):
   n=len(c)
   s=""
   for i in range(0,n):
     si=c[i]
     s=si+s
   return s
