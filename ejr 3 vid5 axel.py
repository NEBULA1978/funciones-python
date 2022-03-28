resultado = "Resultado de Laboratorio 'Su Salud' Nombre del paciente: Jose Aimas E-maildel paciente: jose.aimas@gmail.com Resultados del laboratorio: INR 1.25 segundos BGT 140.12 mmol/dl HGB 13 g/dl ESR 3.2mm/hora"
palabras=resultado.split(" ")
print("INFORME DE LABORATORIO")
print("*"*22)
entro=False
for pal in palabras:
    if pal.isupper(): #pal = "INR"
        pos=palabras.index(pal)
        decimal=palabras[pos+1]
        unidades=palabras[pos+2]
        if pal=="BGT" and float(decimal) >150 :
            unidades+=" **"
            entro=True
        print("{:^10} {:^10} {:^10}".format(pal,decimal,unidades))

if "Dr." in palabras:
    posDr=palabras.index("Dr.")

else:
    posDr=palabras.index("Dra.")
nombe = " ".join(palabras[posDr+1:])
print("Medico:",nombre)

if entro:
    print("** Su nivelde azucar es alto ,se recomienda ir al endocrinologo")
