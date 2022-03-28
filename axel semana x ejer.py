"""
una maquina de alimentos tiene tres productos de tres tipos ,A;B;C
que valen respectivamente €270, €340, €390. La maquina acepta y da
de vuelto monedas de €10 ,€50, €100.

Escriba un programa que pida al usuario elegir el producto y luego
 le pida ingresar las monedas hasta alcanzar el monto a pagar.Si el
 monto ingresado es mauor que el precio del producto,el programa debe
 entregar las monedas de vuelto,una por una.
 """
productos=["A", "B", "C"]
valores=[270, 340, 390]
cuantas=int(input("Cuantas monedas va a ingresar: "))
pro=input("Elija producto: ")# "A"
pos=productos.index(pro)# 0
costo=valores[pos] # 270
monedas=input("Ingrese monedas: ").split(",") # "100","10","50","100","100" = 360
entregado=0
for moneda in monedas:
    entregado+= int(moneda)
print(entregado)
vuelto=entregado - costo
listaVuelto=[]
if vuelto >0:
    while( vuelto!=0):
        if (vuelto >=100):
            vuelto-=100
            listaVuelto.append("100")
        elif(vuelto >=50):
            vuelto-=50
            listaVuelto.append("50")
        else:
            vuelto-=10
            listaVuelto.append("10")
    print("Su vuelto: ")
    unido= ",".join(listaVuelto)
    print(unido)

else:
    print("Compra Relizada")
