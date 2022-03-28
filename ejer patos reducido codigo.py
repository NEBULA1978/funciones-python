"""
USTED ELABORARA UNA SIMULACION DE UN JUEGO DE DISPAROS DE TIRO AL BLANCO CON PATOS.

EL JUGADOR CUENTA CON 30 MUNICIONES PARA REALIZAR LOS DISPAROS Y CADA PATO TIENE UN NIVEL DE VIDA.

PARA REALIZAR ESTA SIMULACION USTED CREARA UNA LISTA CON 6 NUMEROS ALEATORIOS DIFERENTES ENTRE 1Y6.
CADA UNO DE LOS ELEMENTOS DE LA LISTA REPRESENTA A UN PATO CON SU NIVEL DE VIDA.

  [3,5,4,2,1,6]

EL JUGADOR DEBERA INGRESAR POR TECLADO LA POSICION DEL PATO AL QUE VA A DISPARAR.

EL DISPARAR UN PATO SIGNIFICA QUE DEBE REDUCIR SU NIVEL DE VIDA .

CUANDO EL NIVEL DE VIDA DEL PATO ESTE EN 0 SIGNIFICA QUE EL PATO HA SIDO ELIMINADO DEL JUEGO.
(NOTA.-VALIDAR QUE EL JUGADOR INGRESE UNA POSICION VALIDA Y QUE NO LE DISPARE AL PATO QUE YA A SIDO ELIMINADO).

"""



from random import *
#patos=list(range(1,7)) ai tambien es valido crear una lista o como abajo
patos=[1,2,3,4,5,6]
shuffle(patos)
print("Patos:")
municion=30
while(municion >0 and sum(patos)!=0):#patos.count(0)!=0
    print(patos)
    pos=int(input("Ingrese la posicion a la que va a disparar; "))
    if pos>=0 and pos<=5:
        vida=patos[pos]
        municion -= 1
    if vida > 0:
        patos[pos]-=1
    else:
        print("Ese pato ya ha sio eliminado!!")
    print("Tiros restantes: ", municion)


    else:
        print("Tiro Fallido")
        municion-=1


