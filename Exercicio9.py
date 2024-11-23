'''9. Palíndromo
Escreva um programa que peça uma palavra ao usuário e verifique se ela é um palíndromo (lê-se igual de trás para frente).'''

while True:
    frase = input('Digite [S]air ou uma Frase: ').strip().upper()
    frase_invertido = frase[::-1]

    if frase == 'S':
        print('Programa finalizado pelo usuario. Ate logo!')
        break

    if not frase or frase.isnumeric() or len(frase) < 2:
        print('Você não digitou nada ou digitou uma frase inválida.')
        print()
        continue

    condicao = frase == frase_invertido

    resultado = 'SIM' if condicao else 'NÃO'

    print(f'A palavra {frase}, {resultado} é um Palindromo ')

'''Sugestoes de melhorias

-Ignorar espaços e caracteres especiais:
Um palíndromo deve ser analisado apenas com letras (e números, se permitido).

-Adicionar mais clareza ao resultado:
Incluir a versão invertida na saída pode ser interessante para o usuário entender a verificação.

-Organizar lógica em uma função:
Deixar o programa modular e mais legível.

def verificar_palindromo():
    while True:
        frase = input('Digite [S]air ou uma palavra/frase: ').strip()
        if frase.lower() == 's':  # Permite "s" em maiúsculo ou minúsculo
            print('Programa finalizado pelo usuário. Até logo!')
            break

        # Filtrar apenas letras e números
        frase_filtrada = ''.join(c for c in frase if c.isalnum()).lower()
        frase_invertida = frase_filtrada[::-1]

        if not frase_filtrada or len(frase_filtrada) < 2:
            print('Você não digitou nada ou digitou uma palavra/frase inválida.')
            continue

        if frase_filtrada == frase_invertida:
            print(f'A palavra/frase "{frase}" é um PALÍNDROMO! (Inverso: {frase_invertida})')
        else:
            print(f'A palavra/frase "{frase}" NÃO é um palíndromo. (Inverso: {frase_invertida})')

# Chamar a função
verificar_palindromo()

    '''
