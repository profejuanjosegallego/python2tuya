#Creando una lista de datos en python
# LAS LISTAS SE NOMBRAN EN PLURAL
jugadores=["Juan","Laura","Raul","Isabel","Tuya"]

#Agregando elementos a una lista
jugadores.append(input("Digita un nombre de usuario: "))

#Mostrando los datos de una lista
print(jugadores)






#Creando diccionarios en PYTHON
#EL NOMBRE DEL DICCIONARIO VA EN SINGULAR
jugador={
    "id":45,
    "nombre":"Edwin Cardona",
    "edad":40,
    "posicion":"Medio campista",
    "salarioMensual":200000000,
    "estaLesionado":True
} #CLAVE:VALOR

#Agrego un nuevo elemento a mi diccionario
jugador["golesEnTemporada"]=6

#Mostrando los datos de un diccionario
print(jugador)