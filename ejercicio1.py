num = int(input('Digite un número: '))
if num > 0 :
        print(f'El numero ingresado {num} es positivo')
elif num == 0: 
        print (f'el numero es igual a cero')
elif num < 0 :
        print(f'El numero ingresado {num} es negativo')
print ('Si desea salir del progamar digite el asterisco * ')
while num != '*':
    num = input('Digite un número: ')
    if num > "0" :
        print(f'El numero ingresado {num} es positivo')
    elif num == "0" : 
        print (f'el numero es igual a cero')
    elif num < "0" :
        print(f'El numero ingresado {num} es negativo')
print ('Adios, que se encuentre bien')