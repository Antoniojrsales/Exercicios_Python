#7. Tabuada
#Peça ao usuário um número inteiro e exiba a tabuada desse número (de 1 a 10).
    
while True:
    entrada = input('Digite o numero desejado: ')
    try:
        entrada_int = int(entrada)
        print()
        print(f'Segui a tabuada do {entrada_int}')
        for i in range(1, 11):
            print(f'{entrada_int} x {i} = {entrada_int * i}')
        break
    except ValueError:
        print("Por favor, digite um número válido (inteiro).")

'''Melhorias sugeridas:

-Organização do código:
Encapsular a lógica em uma função para maior modularidade.

-Separar mensagens e cálculos:
Colocar a mensagem de introdução antes da tabuada para maior clareza.

-Opção de continuar:
Oferecer ao usuário a possibilidade de calcular a tabuada de outro número.

while True:
    entrada = input('Digite o número desejado para a tabuada (ou "sair" para encerrar): ').strip()
    if entrada.lower() == "sair":
        print("Encerrando o programa. Até mais!")
        break
    try:
        numero = int(entrada)
        print(f'\nTabuada do {numero}:')
        for i in range(1, 11):
            print(f'{numero} x {i} = {numero * i}')
        print()  # Linha em branco para separação
    except ValueError:
        print("Por favor, digite um número válido (inteiro).")
'''