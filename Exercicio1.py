#1. Saudação personalizada
'''Escreva um programa que peça o nome do usuário e o cumprimente com uma mensagem personalizada.'''

usuario = input('Digite o seu nome: ') # Solicitando uma entrada do usuario

if len(usuario) < 2 or usuario == '': # Condicao que limite se o nome e valido ou nao
    print('Vc nao digitou nada ou digitou um nome invalido.')
else:
    print(f'Ola muito prazer em lhe conhecer {usuario}') # Msg de saudacao


'''Melhorias sugeridas

-Evitar nomes compostos como inválidos: Se o usuário digitar algo como "Jo", ele será considerado válido, mas você pode melhorar a verificação considerando espaços vazios ou garantindo apenas letras.

-Usar .strip(): Esse método remove espaços extras no início e no final da string.

-Normalizar letras maiúsculas/minúsculas: Transformar a entrada do usuário para o formato "Título" pode deixar a saudação mais elegante.
---------------------------------------------------------------------------------------------------------------
usuario = input('Digite o seu nome: ').strip()

if len(usuario) < 2 or not usuario.isalpha():
    print('Você não digitou um nome válido.')
else:
    print(f'Olá, muito prazer em lhe conhecer, {usuario.title()}!')'''
