print("=======================")
print("     MI CALCULADORA")
print("=======================")
while True:
    print("")
    print("opciones")
    print("a. sumar")
    print("b. restar")
    print("c. multiplicación")
    print("d. división")
    print("e. salir")
    print("-----------------------")

    opción = input("Elige una opción:")

    if opción == "a":
        num1 = input("ingrea el primer número:")
        num1 = int(num1)
        num2 = input("ingresa el segundo número:")
        num2 = int(num2)
        print(" El resultado de la suma es:",num1 + num2)

    elif opción == "b":
        num1 = input("ingresa el primer número:")
        num1 = int(num1)
        num2 = input("ingresa el segundo numero:")
        num2 = int("num2")
        print("el resultado de la resta es:",num1 - num2)

    elif opción == "c":
        num1 = input("ingresa el primer numero:")
        num1 = int (num1)
        num2  = input("ingresa el segundo numero:") 
        num2 = int(num2)
        print("el resultado de la multiplicacion es:",num1*num2)

    elif opción == "d":
        num1 = input("ingresa el primer numero:")
        num1 = int(num1)
        num2 = input("ingresa el segundo numero:")
        num2 = int(num2)
        print("el resultado de la division es:",num1/num2)
    elif opción == "e":
        print("gracias por usar mi calculadora")

        print("")




        


        

