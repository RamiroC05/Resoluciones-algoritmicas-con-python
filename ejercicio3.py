num=input('Digite un numero: ')

lista=[]

for i in num:
    lista.append(int(i))

print(f'La suma de los digitos ingresados es igual a {sum(lista)}')