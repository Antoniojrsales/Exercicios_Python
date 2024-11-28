'''Passo a passo: Fibonacci
Entender a sequência de Fibonacci:

Cada número da sequência é a soma dos dois números anteriores.
Exemplo: 0, 1, 1, 2, 3, 5, 8, 13...
O 3º número é 0 + 1 = 1
O 4º número é 1 + 1 = 2
O 5º número é 1 + 2 = 3
Pedir um número inteiro positivo ao usuário:

Use input() para obter o número desejado.
Certifique-se de que o usuário insira um valor válido (número inteiro positivo).
Trabalhar com condições iniciais:

A sequência começa com 0 e 1.
Se n == 1, exiba apenas [0].
Se n == 2, exiba [0, 1].
Calcular os números restantes da sequência:

Para n > 2, use um loop para calcular os números da sequência:
Comece com uma lista contendo [0, 1].
Em cada iteração, some os dois últimos números da lista e adicione o resultado à lista.
Exibir o resultado final:

Depois que o loop terminar, exiba a lista completa da sequência de Fibonacci.'''

#10. Fibonacci
#Peça ao usuário um número inteiro n e exiba os primeiros n números da sequência de Fibonacci.

lista_n = []
while True:    
    entrada = input('Digite um numero ou digite [S]air: ').strip().upper()
    if entrada == 'S':
        print('Muito obrigado por usar nosso app.')
        print('Finalizando Programa.')
        break
    try:
        numero = int(entrada)
        if numero == 1:
            lista_n = [0]
        elif numero == 2:
            lista_n = [0, 1]
        elif numero > 2:
            lista_n = [0,1]
            while len(lista_n) < numero:
                proximo_numero = lista_n[-1] + lista_n[-2]
                lista_n.append(proximo_numero)
        print(f'A sequencia Fibonacci: {lista_n}')        
    except ValueError:
        print('Por favor, digite um número válido (inteiro).')

'''Sugestoes de melhorias

-Separar a lógica em uma função:
Isso tornará o código mais modular e reutilizável.

-Adicionar mais informações sobre a sequência:
Por exemplo, exibir o número total de termos gerados.

-Formatar a saída para sequências longas:
Caso o usuário insira números muito grandes, você pode exibir os resultados de forma mais amigável (como limitar a quantidade exibida ou mostrar em múltiplas linhas).

def gerar_fibonacci(n):
    """Gera os primeiros n números da sequência de Fibonacci."""
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        lista_n = [0, 1]
        while len(lista_n) < n:
            lista_n.append(lista_n[-1] + lista_n[-2])
        return lista_n

while True:
    entrada = input('Digite um número ou digite [S]air: ').strip().upper()
    if entrada == 'S':
        print('Muito obrigado por usar nosso app.')
        print('Finalizando Programa.')
        break
    try:
        numero = int(entrada)
        if numero <= 0:
            print('Por favor, insira um número inteiro positivo.')
            continue
        sequencia = gerar_fibonacci(numero)
        print(f'A sequência de Fibonacci com {numero} termos: {sequencia}')
    except ValueError:
        print('Por favor, digite um número válido (inteiro).')


'''
   
    


    