#3. Verificação de número par ou ímpar
#Peça ao usuário um número inteiro e informe se ele é par ou ímpar.

numero = input('Digite o numero desejdo: ').strip()

try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print(f'O número {numero_int} é PAR.')
    else:
        print(f'O número {numero_int} é ÍMPAR.')
except ValueError:
    print('O valor digite e invalido!')

''' Melhorias sugeridas:

-Remover espaços na entrada: Usar .strip() no input para lidar com espaços extras.

-Tornar mensagens mais amigáveis: Acrescentar o número digitado nas mensagens de saída pode deixar o programa mais interativo.

-Modularizar: Você pode encapsular o código em uma função para maior organização e reutilização.
-----------------------------------------------------------------------------------------------
numero = input('Digite o número desejado: ').strip()

try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print(f'O número {numero_int} é PAR.')
    else:
        print(f'O número {numero_int} é ÍMPAR.')
except ValueError:
    print('O valor digitado é inválido!')

'''

'''Usando Funcoes

def par_impar(num):   
    if num % 2 == 0:
        return 'PAR'
    else:
        return 'IMPAR'
    
while True:
    entrada = input('Digite [S]air ou um numero inteiro: ')  
    if entrada.upper() == 'S':
        print('Muito obrigado por usar nosso app')
        print('Programa finalizado com sucesso')
        break
    
    if entrada.isdigit():
        numero = int(entrada)
        valor = par_impar(numero)
        print(f'O valor {entrada} digitado e {valor}')
        print()
    else:
        print('Erro! Por favor, digite apenas números inteiros.')
        print()
    
-Sugestoes de melhorias

-Aceitar números negativos:
Atualmente, a validação isdigit() não aceita números negativos. Você pode corrigir isso com lstrip('-').isdigit().

-Melhor feedback de erro:
Quando a entrada for inválida, explique exatamente o problema ao usuário.

-Simplificação do if no loop:
Combine condições e torne o fluxo do código mais enxuto.

def par_impar(num):   
    return 'PAR' if num % 2 == 0 else 'IMPAR'

while True:
    entrada = input('Digite um número inteiro ou [S]air: ').strip()
    
    if entrada.upper() == 'S':
        print('Muito obrigado por usar nosso app.')
        print('Programa finalizado com sucesso.')
        break
    
    # Validar números inteiros, incluindo negativos
    if entrada.lstrip('-').isdigit():
        numero = int(entrada)
        resultado = par_impar(numero)
        print(f'O valor {numero} digitado é {resultado}.')
    else:
        print('Erro! Por favor, digite um número inteiro válido.')
    print()  # Adicionar uma linha em branco para organização


'''
