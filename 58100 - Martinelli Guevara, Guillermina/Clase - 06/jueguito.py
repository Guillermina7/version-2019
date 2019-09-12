from generador import generador, generador_mejor
buscado=generador(1,100)
adivinado= False
lista=[]
while adivinado == False:
    print ("Ingrese un numero del 1 al 100")
    numero= int (input())
    if numero == buscado:
        print ("Ganaste") 
        adivinado=True
    if numero<buscado:
        print ("Ingrese un numero mayor")
    if numero>buscado:
        print ("Ingrese un numero menor")
    if adivinado == False:
        numero2 = generador_mejor(1,100,lista)
        lista.append(numero2)
        if numero2 == adivinado:
            print ("Ganó la PC")
            adivinado=True


            



    

