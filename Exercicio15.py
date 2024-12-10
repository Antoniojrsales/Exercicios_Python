'''Exercício 15: Soma dos múltiplos
Peça ao usuário um número inteiro positivo n e calcule a soma de todos os múltiplos de 3 e 5 menores que n.
Exemplo:
Entrada: 10
Saída: A soma dos múltiplos de 3 e 5 menores que 10 é 23 (3 + 5 + 6 + 9).'''

while True:
    entrada = input('Digite [S]air ou um numero inteiro positivo: ').strip()

    if entrada.lower() == 's':
        print('Muito obrigado por usar nosso app')
        print('Programa finalizado.')
        break 

    if entrada.isdigit():
        numero = int(entrada)
        lista = [i for i in range(1, numero) if i % 3 == 0 or i % 5 == 0]
        resultado = sum(lista)
        print(f'A soma dos múltiplos de 3 e 5 menores que {entrada} é {resultado} ({lista})')
        print()
    else:
        print("Entrada inválida. Digite um número inteiro positivo.")

'''Sugestoes de melhorias

-Uso de or: A condição i % 3 == 0 or i % 5 == 0 garante que cada número só será adicionado à lista uma vez.

-Comprehension List: A criação da lista lista com compreensão reduz o número de linhas e mantém o código mais limpo.

-Evita Duplicatas: Não há necessidade de adicionar duas vezes números que são múltiplos tanto de 3 quanto de 5 (como 15).

'''