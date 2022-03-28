# condicionales

#altura = int(input("¿Cual es tu altura?: "))

#if altura >= 180:
 #   print(("Eres una persona alta!!: "))
#else:
#    print("Eres Bajito!!")

# funciones

var_altura = int(input("¿Cual es tu altura?: "))

def mostrarAltura(altura):
    resultado = ""

    if altura >= 180:
       resultado= "Eres una persona alta!!"
    else:
        resultado = "Eres Bajito!!"
    return resultado

print(mostrarAltura(var_altura))
print(mostrarAltura(var_altura))
print(mostrarAltura(var_altura))