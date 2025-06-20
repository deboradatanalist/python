
while True:
    numero = int(input("Digite um número: "))
    if numero >0:
        print(f"TABUADA do numero {numero}: ")
        for i in range(1,11):
            print(f"{numero} x {i} = {numero*i}")
    elif numero == 0:
        print("Tabuada de  ZERO é ZERO")
        continue
    else:
        print("Programa encerrado")
        break
    
    
             
