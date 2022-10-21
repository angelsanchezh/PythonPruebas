Nombre = input('como te llamas ')
print('Hola ' + Nombre )

edad = int(input('cuantos años tienes '))
masDe12 = edad >= 12

respuesDelHijoDelDueño = input('eres hijo del dueño')
esHijoDelDueño= respuesDelHijoDelDueño == 'si'

puedesPasar = masDe12 or esHijoDelDueño


if puedesPasar:
    print('usted puede pasar')
else:
    print('no puedes ingresar por ser menor de edad')