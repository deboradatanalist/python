#quiz
#Dicionario com perguntas e respostas

from unidecode import unidecode
quiz={
    
    "Quanto é 7 + 5?" : "12",
    "Qual é a metade de 100?" : "50",
    "Qual o valor de 9 x 6?" : "54",
    "Quanto é 81 dividido por 9?" : "9",
    "Qual planeta é conhecido como planeta vermelho?" : "Marte",
    "A água ferve a quantos graus Celsius?" : "100°C",
    "Qual é o estado da água em temperatura ambiente?":"Líquido",
    "Qual é o plural de pão?": "Pães",
    "Qual a sílaba tônica da palavra janela?" : "Ne",
    }

#criar a logica do quiz

acertos = 0

for pergunta, resposta in quiz.items():
    resposta_usuario = input(pergunta + " ")
    
    if resposta_usuario.strip().lower() == unidecode(resposta.lower()):
        print("Resposta Correta")
        acertos +=1
    else:
        print(f"Resposta Errada! A resposta correta é : {resposta}")

percen = round(((acertos/len(quiz))*100),2)
print(f"Você Acertou {percen}% das perguntas.")
