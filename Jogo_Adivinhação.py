from time import sleep
import random 
import os

numero_secreto = random.randint(0, 10)
tentativas = 0

print('-' * 20)
print('JOGO DA ADIVINHAÇÃO')
print('-' * 20)
sleep(1.0)

while True:
    tentativas += 1

    try:
        resposta = input('Digite um valor entre 0 à 10: ')
        resposta = int(resposta)
        sleep(1)

        if resposta == numero_secreto:
            os.system('cls')
            print('Parabéns. Você acertou!!')
            print(f'O número secreto era: {numero_secreto}')
            print(f'Número de tentativas: {tentativas}')
            break

        if resposta > numero_secreto:
            print(f'Tente colocar um número menor que {resposta}')
            continue 
        if resposta < numero_secreto:
            print(f'Tente colocar um número maior que {resposta}')
            continue 
    except ValueError:
        print('Digite apenas números entre 0 e 10')
        continue