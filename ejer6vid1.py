# "kaconcha@espol.edu.ec-zaastudillo@espol.edu.ec-luanvill@espol.edu.ec"
#  kaconcha
#  zaastudillo
#  luanvill

#INDEXACION

correos="kaconcha@espol.edu.ec-zaastudillo@espol.edu.ec-luanvill@espol.edu.ec"
posGuion=correos.index("-")
correo1=correos[:posGuion]
posGuion2=correos.index("-",posGuion+1)
correo2=correos[posGuion+1:posGuion2]
correo3=correos[posGuion2+1:]
posArro1=correo1.index("@")
posArro2=correo2.index("@")
posArro3=correo3.index("@")
usuario1=correo1[:posArro1]
usuario2=correo2[:posArro2]
usuario3=correo3[:posArro3]
print(usuario1)
print(usuario2)
print(usuario3)