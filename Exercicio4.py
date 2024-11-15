#4. Média de três números
#Crie um programa que peça três números ao usuário e exiba a média deles.

numeros = []
for i in range(3):
    while True:
        entrada = input(f'Digite o numero {i + 1}: ').strip()
        if entrada.isdigit() or (entrada.startswith('-') and entrada[-1].isdigit()):
            numeros.append(int(entrada))
            break
        else:
            print("Por favor, digite um número inteiro válido.")
soma = sum(numeros[:])

print(f'A media dos numeros {numeros[0]}, {numeros[1]}, {numeros[2]} = {soma / len(numeros)}')

''' Melhorias sugeridas:

-Melhoria na validação:
Seu método de validação já é robusto, mas a verificação de entrada[-1].isdigit() pode ser simplificada.
Considere também números de ponto flutuante se o objetivo for ampliar a funcionalidade.

-Exibição de resultados:
Para maior clareza, formate a média com duas casas decimais.

-Organização do código:
Encapsular a lógica em uma função pode facilitar a reutilização.
------------------------------------------------------------------------------------
def calcular_media():
    numeros = []
    for i in range(3):
        while True:
            entrada = input(f'Digite o número {i + 1}: ').strip()
            try:
                numero = float(entrada)  # Aceita inteiros e números decimais
                numeros.append(numero)
                break
            except ValueError:
                print("Por favor, digite um número válido (inteiro ou decimal).")
    
    media = sum(numeros) / len(numeros)
    print(f'A média dos números {numeros[0]}, {numeros[1]} e {numeros[2]} é {media:.2f}.')

# Chamar a função
calcular_media()


'''
