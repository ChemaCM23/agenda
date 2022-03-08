agenda = {}
#Definición de la función menú#
def mostrarmenu():
    print("|----------------------------|")
    print("|  : : AGENDA DE CHEMA : :   |")
    print("|----------------------------|")
    print("|                            |")
    print("|  1. Añadir o modificar     |")
    print("|  2. Buscar                 |")
    print("|  3. Borrar                 |")
    print("|  4. Listar                 |")
    print("|  5. Salir                  |")
    print("|____________________________|")
    print("")
    x = input ("Dime la función a realizar: : ")
    opc = int (x)
    return (opc)

###Parte realizada por Chema###
###Añadir y modificar###

#Función añadir o modificar#
def añadirModificarJcaballero():
    nombre = input("Nombre del contacto: ")
    if nombre in agenda:
        print("%s es un contacto que ya existe, su número de teléfono es %s" % (nombre,agenda[nombre]))
        selec = input("Pulsa la tecla 's' si quiere modificarlo. Cualquier otra tecla para continuar.")
        if selec == "s":
            telefono = input("Dime el nuevo número de teléfono: ")
            agenda[nombre]=telefono
    else:
        telefono = input("Dime el número de teléfono: ")
        agenda[nombre]=telefono

###Programa###
selec = mostrarmenu() #Función para que llame el menu cada vez que se le llame#
if (selec<0 or selec>4):
    print ("La opción es incorrecta. Inicia de nuevo la agenda y elige una correcta.")

while (selec>0 and selec<5):
    if (selec==1):
        añadirModificarJcaballero()

    #elif (selec==2):
        ###

    #elif (selec==3):
        ###
    
    #elif (selec==4):
        ###

    #elif (selec==5):
        #print("Hasta luego.")
        #break

    selec =mostrarmenu()


