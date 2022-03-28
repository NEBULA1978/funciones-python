# join: primero se hicieron listas y despues de eso se transformaron
# de nuevo a stream y vuelven a como ingreso el usuario
monedas=input("Ingrese monedas: ")
listaMon=monedas.split(",") #["10","10","50","100"]
print(listaMon)
cad="-".join(listaMon)
print(cad)