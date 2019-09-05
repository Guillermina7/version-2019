from generador import generador
adivinado=False
aleatorio = generador(1,20)
while adivinado == False:
    print("Ingrese un numero entre 1 y 20")
    numero=int (input())
    if numero == aleatorio:
        print ("Adivinaste, humana :) :) ")
        adivinado=True
    if numero<aleatorio:
        print("Salame, ingresá uno más grande")
    if numero>aleatorio:
        print("You're very stupid, ahora mas chico")