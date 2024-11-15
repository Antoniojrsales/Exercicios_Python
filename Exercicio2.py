#2. Soma de dois números
#Peça ao usuário dois números inteiros e exiba a soma deles.

num1 = input('Digite o primeiro numero desejado: ') # # Solicitando uma entrada do usuario
num2 = input('Digite o segundo numero desejado: ')

try:    
    num1_inteiro = int(num1) # Convertendo para inteiro se for digitado um numero
    num2_inteiro = int(num2)          
    print(f'A soma do numero {num1_inteiro} + {num2_inteiro} = {num1_inteiro + num2_inteiro}') # Msg com o resultado
except ValueError:  
    print('Vc nao digitou nada ou digitou um valor invalido!') # Msg caso tenha algum erro


'''Melhorias sugeridas

-for e range(2):
O laço for é usado para iterar duas vezes, uma para cada número solicitado.
O valor de i varia entre 0 e 1 para gerar mensagens apropriadas (número 1, número 2).

-Lista numeros:
Os números convertidos para inteiro são armazenados na lista, que facilita o cálculo da soma com sum(numeros).

-Validação com while True:
O while dentro do for garante que o programa continue pedindo um número válido até que o usuário insira corretamente.
----------------------------------------------------------------------------------------------
numeros = []  # Lista para armazenar os números

# Pedindo ao usuário dois números (pode ser ajustado para mais)
for i in range(2):  # Itera duas vezes, uma para cada número
    while True:
        entrada = input(f'Digite o número {i + 1}: ').strip()
        if entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit()):
            numeros.append(int(entrada))  # Adiciona o número à lista
            break
        print("Por favor, digite um número inteiro válido.")  # Mensagem para entrada inválida

# Calculando e exibindo a soma
print(f'A soma dos números {numeros[0]} + {numeros[1]} = {sum(numeros)}')'''