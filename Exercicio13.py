'''Exercício 13: Palavras com mais de 5 caracteres
Peça ao usuário uma frase e mostre todas as palavras da frase que possuem mais de 5 caracteres.
Exemplo:
Entrada: "A programação é maravilhosa e desafiadora"
Saída: As palavras com mais de 5 caracteres são: ['programação', 'maravilhosa', 'desafiadora']'''


while True:
    frase = input('Digite uma frase ou [S]air: ').strip()
    dividir_frase = frase.split()

    if frase.upper() == 'S':
        print('Muito obrigado por usar nosso app')
        print('Programa finalizado.')
        break

    if not frase or frase.isnumeric():
        print('Error. Você não digitou nada ou digitou uma frase inválida.')
    
    elif len(dividir_frase) >= 1:
        lista_frase = []
        for i in dividir_frase:
            if len(i) > 5:
                lista_frase.append(i)
            if lista_frase:    
                msg = f'As palavras com mais de 5 caracteres sao: {lista_frase}'
            else:
                msg = f'Na frase {dividir_frase} nao a palavras com 5 caracteres '  
        print(msg)  
    else:
        print('Por favor digitar uma frase valida')

'''Sugestões de melhoria:
-Use a lista lista_frase fora do loop para acumular palavras maiores que 5 caracteres.

-Valide a entrada antes de dividir a frase e processar palavras.

-Se a lista lista_frase estiver vazia ao final da análise, exiba a mensagem apropriada.

while True:
    frase = input('Digite uma frase ou [S]air: ').strip()

    if frase.upper() == 'S':
        print('Muito obrigado por usar nosso app')
        print('Programa finalizado.')
        break

    if not frase or frase.isnumeric():
        print('Error. Você não digitou nada ou digitou uma frase inválida.')
        continue

    dividir_frase = frase.split()
    
    if len(dividir_frase) >= 2:
        lista_frase = [palavra for palavra in dividir_frase if len(palavra) > 5]

        if lista_frase:
            print(f'As palavras com mais de 5 caracteres são: {lista_frase}')
        else:
            print(f'Na frase "{frase}" não há palavras com mais de 5 caracteres.')
    else:
        print('Por favor, digite uma frase válida.')

'''

