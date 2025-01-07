'''Exercício 2: Soma dos quadrados
Peça ao usuário para digitar um número inteiro positivo n e calcule a soma dos quadrados de todos os números de 1 até n.
Exemplo:
Entrada: 3
Saída: "A soma dos quadrados de 1 até 3 é 14 (1² + 2² + 3²)."'''

while True:
    entrada = input('Digite [S]air ou um numero inteiro positivo: ').strip()

    if entrada.upper() == 'S':
        print('Muito obrigado por usar nosso app')
        print('Programa finalizado.')
        break 
    
    if entrada.isdigit():
        numero = int(entrada)
        lista_quadrada = [indice ** 2 for indice in range(1, numero +1)]
        print(f'A soma dos quadrados de {lista_quadrada[0]} até {entrada[-1]} é {sum(lista_quadrada)} (1² + 2² + 3²).')        
    
    else:
        print("Entrada inválida. Por favor, digite uma numero inteiro positivo.")

'''Sugestoes de melhorias
-Uso de numero:
Substituí o uso de entrada[-1] por numero para evitar confusão.

-Formato Dinâmico da Fórmula:
Adicionei uma lista de strings gerada dinamicamente para exibir todos os quadrados calculados na mensagem final (quadrados_formatados).

-Melhoria na Mensagem Final:
A mensagem agora explica que a soma é feita de 1 até numero e exibe claramente o cálculo.

while True:
    entrada = input('Digite [S]air ou um número inteiro positivo: ').strip()

    if entrada.upper() == 'S':
        print('Muito obrigado por usar nosso app!')
        print('Programa finalizado.')
        break 

    if entrada.isdigit():
        numero = int(entrada)
        lista_quadrada = [indice ** 2 for indice in range(1, numero + 1)]
        quadrados_formatados = ' + '.join(f'{i}²' for i in range(1, numero + 1))
        print(f'A soma dos quadrados de 1 até {numero} é {sum(lista_quadrada)} ({quadrados_formatados}).')
    else:
        print("Entrada inválida. Por favor, digite um número inteiro positivo.")


'''