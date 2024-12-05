'''Exercício 2: Números primos
Peça ao usuário um número inteiro positivo e verifique se ele é um número primo.
Exemplo:
Entrada: 7
Saída: 7 é um número primo.
Entrada: 8
Saída: 8 não é um número primo.'''

import math

while True:
    entrada = input("Digite um número inteiro positivo (ou 'S' para sair): ").strip()
    if entrada.upper() == 'S':
        print("Programa finalizado.")
        break

    if entrada.isdigit():
        numero = int(entrada)
        if numero > 1:
            if numero == 2:
                print(f"{numero} é um número primo.")
                continue

            eh_primo = True
            for i in range(2, int(math.sqrt(numero)) + 1):
                if numero % i == 0:
                    eh_primo = False
                    break

            if eh_primo:
                print(f"{numero} é um número primo.")
            else:
                print(f"{numero} não é um número primo.")
        else:
            print("Por favor, digite um número maior que 1.")
    else:
        print("Entrada inválida. Digite um número inteiro positivo.")
