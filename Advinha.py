import random

print ("Jogo de adivinhação")
print ("Tente adivinhar o número que estou pensando entre 1 a 100")
print ("Você tem 7 tentativas")

numerosecreto = random.randint (1,100)

Contador = 7
Acertou = False

while Contador > 0:
    Tentativa = int ( input ("digite sua Tentativa "))
    if Tentativa == numerosecreto:
        print ("Parabéns, você conseguiu!")
    Acertou = True
    break
    elif Tentativa < numerosecreto:
    print("O número é maior que seu palpite ", numerosecreto)
    else:
    print("O número é menor que seu palpite ", numerosecreto)

if not Acertou:
    print ("Que pena, você  errou. O número secreto era,: ", numerosecreto)
else:
    print ("Você acertou o número secreto em", 7 - Contador + 1, "tentativas")