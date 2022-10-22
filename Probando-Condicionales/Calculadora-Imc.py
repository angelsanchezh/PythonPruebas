#Calculdora  IMC
#IMC  = peso/(altura x altura)
# < 19  = Delgadez
# entre 20 y 25 normal
# ebtre 26 y 30 , esta con sobrepeso
# mayor  30 esta con obesidad

peso= int(input('cual es tu peso? '))
altura= int( input('cual es tu altura ? '))

imc = peso / (altura * altura)

print (str(imc))


