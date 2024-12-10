'''Exercício 16: Contar vogais
Peça ao usuário para digitar uma frase e conte quantas vogais (a, e, i, o, u) existem na frase. Mostre o total e quais vogais foram encontradas.
Exemplo:
Entrada: "A programação é incrível!"
Saída: "A frase contém 7 vogais: ['a', 'o', 'a', 'ã', 'i', 'i', 'e']"'''

def vogais():
    while True:
        entrada = input('Digite [S]air ou uma frase: ').strip().lower()
        
        if entrada.upper() == 'S':
            print('Muito obrigado por usar nosso app')
            print('Programa finalizado.')
            break 
        
        if not entrada.isdigit():
            vogais = [i for i in entrada if i in 'aeiou' or i in 'áàâãéêíóõôú']
            if vogais:
                print(f'A frase contém {len(vogais)} vogais: ({vogais})')
            else:
                print(f'Vc nao digitou nada ou a sua frase nao contem vogais (lista vazia {vogais})')
        else:
            print("Entrada inválida. Digite uma frase.")
    
vogais()       

'''Sugestoes de melhorias
-Lista de Vogais Predefinida
Ao invés de repetir 'aeiouáàâãéêíóõôú' em duas condições, use uma variável para armazenar as vogais (incluindo as acentuadas).

-Mensagens Mais Diretas
Deixe as mensagens de erro ou de ausência de vogais mais claras e menos técnicas para o usuário.

-Elimine Ambiguidade na Entrada
Garanta que entradas compostas apenas de números não sejam interpretadas como inválidas para evitar mensagens confusas.

def contar_vogais():
    vogais_permitidas = 'aeiouáàâãéêíóõôú'
    while True:
        entrada = input('Digite [S]air ou uma frase: ').strip().lower()
        
        if entrada.upper() == 'S':
            print('Muito obrigado por usar nosso app')
            print('Programa finalizado.')
            break 
        
        if not entrada.isdigit() and entrada:
            vogais_encontradas = [letra for letra in entrada if letra in vogais_permitidas]
            if vogais_encontradas:
                print(f'A frase contém {len(vogais_encontradas)} vogais: {vogais_encontradas}')
            else:
                print('Sua frase não contém vogais.')
        else:
            print("Entrada inválida. Por favor, digite uma frase válida.")

contar_vogais()

'''
