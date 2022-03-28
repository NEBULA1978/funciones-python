"""
Escribir un programa en python que recibe por
teclado una direccion web de instituciones educativas
del ecuador. Por ejemplo : www.espol.edu.ec y debe presentar
por pantalla el nombre de la institucion a la cual le
pertenece la direccion web,para el ejemplo la
institucion de Espol

"""

url=input("Ingrese direccion web: ")#"www.ug.edu.ec"
posPunto1=url.index(".")
posPunto2=url.index(".",posPunto1+1)
nombreWeb= url[posPunto1+1:posPunto2].upper()
print(nombreWeb)