'''Exercício 11: Soma dos dígitos
Peça ao usuário para digitar um número inteiro positivo e calcule a soma de todos os dígitos desse número.
Exemplo:
Entrada: 1234
Saída: A soma dos dígitos é 10 (1 + 2 + 3 + 4).'''

lista_num = []

while True:
    try:
        print('Digite os números ou digite [S]air para finalizar o programa.')
        entrada = input('Digite um valor inteiro positivo: ').strip()
        
        if entrada.upper() == 'S':
            print("Programa finalizado pelo usuário.")
            break
        
        if len(entrada) <= 1 or int(entrada) < 0:
            print('Error')
            print('Vc digitou um valor negativo ou somente um valor.')
            print()
        else:
            for i in entrada:
                lista_num.append(int(i))            
                lista_ordenada = sorted(lista_num)
                result = sum(lista_num)
        print(f'A soma dos dígitos é {result} ({lista_ordenada})')
                
    except ValueError:
        print('Por favor, digite um número válido (inteiro).')

'''Sugestoes de melhorias

-Problemas identificados:
Acúmulo na lista:
A lista lista_num acumula os dígitos de todas as entradas, porque você não está limpando-a após cada execução.

-Validação incorreta:
O programa aceita números com apenas um dígito, mas você o trata como um erro.

-Mensagem de erro confusa:
A mensagem de erro diz "somente um valor", mas um número de um único dígito é válido.
Saída de lista ordenada desnecessária:
Ordenar os dígitos para exibição não parece fazer sentido no contexto do exercício.

-Solução ajustada:

-Limpeza da lista:
Limpe a lista a cada iteração para evitar acúmulo de dígitos de entradas anteriores.

-Permitir números de um dígito:
Números de um dígito devem ser tratados como válidos.

-Mensagem clara e feedback direto:
Ajuste a mensagem para informar diretamente o que está errado.

-Evitar uso desnecessário de sorted:
Para este caso, basta exibir a soma.

while True:
    try:
        print('Digite os números ou digite [S]air para finalizar o programa.')
        entrada = input('Digite um número inteiro positivo: ').strip()
        
        if entrada.upper() == 'S':
            print("Programa finalizado pelo usuário.")
            break

        if not entrada.isdigit() or int(entrada) < 0:
            print('Erro! Por favor, digite apenas números inteiros positivos.')
            print()
            continue
        
        # Somar os dígitos
        soma_digitos = sum(int(digito) for digito in entrada)
        
        print(f'A soma dos dígitos do número {entrada} é {soma_digitos}.')
        print()
        
    except ValueError:
        print('Erro inesperado! Tente novamente.')

'''



