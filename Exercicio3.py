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