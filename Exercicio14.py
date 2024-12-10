'''Exercício 14: Inverter números
Peça ao usuário um número inteiro positivo e exiba o número invertido.
Exemplo:
Entrada: 12345
Saída: O número invertido é 54321.'''

def num_invertido():
    sequencia = ''

    while True:
        entrada = input('Digite um número inteiro positivo ou [S]air: ').strip()

        if entrada.lower() == 's':
            print('Muito obrigado por usar nosso app')
            print('Programa finalizado.')
            break 

        if entrada.isdigit():
            numero = int(entrada)
            while numero > 0:
                digito_invertido = numero % 10
                numero //= 10
                sequencia += str(digito_invertido)
            print(f'O número invertido é: {sequencia}')

        else:
            print("Entrada inválida. Digite um número inteiro positivo.")

num_invertido()

'''Sugestoes de melhorias
-Sequência desnecessária: Você cria a sequência como uma string e retorna após completar o loop, mas há maneiras mais simples de manipular isso.

-Saída após sair do programa: O programa imprime um resultado mesmo se o usuário escolheu sair (return sequencia antes de terminar o programa).

-Uso de strings: Manipular números diretamente pode ser simplificado utilizando recursos do Python, como slicing de strings.

def num_invertido():
    while True:
        entrada = input('Digite um número inteiro positivo ou [S]air: ').strip()

        if entrada.lower() == 's':
            print('Muito obrigado por usar nosso app!')
            print('Programa finalizado.')
            break

        if entrada.isdigit():
            # Inverter usando strings
            numero_invertido = entrada[::-1]
            print(f'O número invertido é: {numero_invertido}')
        else:
            print("Entrada inválida. Digite um número inteiro positivo.")

num_invertido()'''


    