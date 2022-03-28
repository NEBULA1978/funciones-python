import math

radio = int(input(" radio -> "))
area = int(input(" area -> "))
if radio>0:
    print("El numero es positivo")
elif radio ==0:
    print("El numero es cero")
else:
    print("El numero es negativo")


radio = float(input("radio -> "))
area = math.pi * radio**2
longitud = 2 * math.pi * radio

if area>0:
    print("El numero es positivo")
elif area ==0:
    print("El numero es cero")
else:
    print("El numero es negativo")



print(f"El area es: {area:.2f}")
print(f"La longitud de la circunferencia es: {longitud:.2f}")

radio = input(" radio ->= ")
area = input(" area ->= ")

radio , area = area , radio
print(f"La longitud de la circunferencia es: {longitud:.2f}")
print(f"El nuevo valor de a es: {radio}")
print(f"El nuevo valor de b es: {area}")
print(f"La longitud de la circunferencia es: {longitud:.2f}")