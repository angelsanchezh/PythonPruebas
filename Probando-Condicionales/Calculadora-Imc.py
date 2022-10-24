#Calculdora  IMC
#IMC  = peso/(altura x altura)
# < 19  = Delgadez
# entre 20 y 25 normal
# ebtre 26 y 30 , esta con sobrepeso
# mayor  30 esta con obesidad

def CalcularImc():

    peso= float(input('cual es tu peso? '))
    altura= float( input('cual es tu altura ? '))

    alturaenmetros= altura/100

    imc = peso / ( alturaenmetros * alturaenmetros )

    if imc < 20:
        print('te encuentras delgado')

    if imc >= 20 and imc < 26:
        print('te encuentras e tu peso normal')

    if imc >= 26 and imc < 30:
        print('estas con sobre peso')

    if imc >30:
        print('estas con obesidad')

CalcularImc()

