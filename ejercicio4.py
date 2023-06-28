print("MENU DE OPCIONES")
print("1. Ingresar números y determinar si es positivo o negativo")
print("2. Ingresar números y determinar la suma y su promedio")
print("3. Ingresar números y determinar la suma de sus dígitos")
print("4. Salir")

while True:
    opc = input("Ingrese una opción: ")

    if opc == "1":
        num = int(input("Digite un número: "))

        if num > 0:
            print("El número ingresado es positivo")
        elif num == 0:
            print("El número es igual a cero")
        else:
            print("El número ingresado es negativo")

    elif opc == "2":
        contador = 0
        lista = []
        num = int(input("Digite un número: "))

        if num > 0:
            contador += 1
            lista.append(num)

        while num != 0:
            num = int(input("Digite un número: "))

            if num > 0:
                contador += 1
                lista.append(num)

        print(f"La sumatoria de todos los números ingresados es igual a {sum(lista)}")
        print(f"Y su promedio es igual a {sum(lista) / contador}")

    elif opc == "3":
        num = input("Digite un número: ")
        lista = []

        for i in num:
            lista.append(int(i))

        print(f"La suma de los dígitos ingresados es igual a {sum(lista)}")

    elif opc == "4":
        break

print("Programa finalizado.")