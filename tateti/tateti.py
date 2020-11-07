tateti = {1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}

def imprimirtablero():
    print( "|" +str(tateti[1]) + "|" + str(tateti[2]) + "|" + str(tateti[3])+ "|" )
    print( "|" +str(tateti[4]) + "|" + str(tateti[5]) + "|" + str(tateti[6])+ "|" )
    print( "|" +str(tateti[7]) + "|" + str(tateti[8]) + "|" + str(tateti[9])+ "|" )


def esvacio(valor):
    return tateti[valor]==" "


def instertarx(valor):
    tateti[valor]="X"

def insertaro(valor):
    tateti[valor]="O"

for i in range(99):
    imprimirtablero()
    if i%2==0:
       instertarx(int(input("ingrese valor de x")))
    else:
        insertaro(int(input("ingrese valor de o")))
        