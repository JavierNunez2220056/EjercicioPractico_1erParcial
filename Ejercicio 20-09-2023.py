
print("Vamos a trabajar la secuencia de Collatz")
print("Ingrese 9 dígitos preferiblemente menores a 258")
sumNum = 0
for k in range(0,9):
    numIng = int(input())
    sumNum = sumNum+numIng
numSec = int((sumNum/9))
if numSec < 258:
    print ("Vamos a trabajar la secuencia de Collatz con", numSec ,"\n")
    print (numSec)
    while numSec != 1:
        if numSec%2 == 0:
            numSec = numSec/2
        else:
            numSec = (numSec*3)+1
        print (numSec)
    print ("La secuencia a llegado a 1")
else:
    print("El numero promedio es", numSec ,", este es mayor o igual a 258, por ende no se puede llevar a cabo la secuencia de Collatz")
