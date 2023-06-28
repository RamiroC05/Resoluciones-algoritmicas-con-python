lista = []
contador = 0

num = int(input('Digite un numero: '))
if num  > 0 :
    contador+=1
    lista.append(num)

print ('Si desea salir del progamar digite el numero 0 ')

while num != 0 :
    num = int(input('Digite un número: '))
    if num  > 0 :
        contador+=1
        lista.append(num)

print(f'la sumatoria de todos los numeros ingresados es igual a {sum(lista)}')
print(f'y su promedio es igual a {sum(lista) / contador}')
