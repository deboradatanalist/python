#coletando dados do usuario
nome = str(input("Informe seu nome: "))
peso = float(input("informe seu peso: "))
altura = float(input("informe sua altura em metros: "))

#calculando o imc

imc = peso / altura**2

#mostrar resultado
print("Olá ", nome, "Seu peso é ", peso, "e sua altura é ", altura)
print('logo o seu IMC é ')
print(f"{imc:.2f}")
