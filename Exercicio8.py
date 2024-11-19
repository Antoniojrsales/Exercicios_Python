#8. Lista crescente
#Peça ao usuário para inserir 5 números inteiros e exiba os números ordenados em ordem #crescente.

lista_numeros = []

for i in range(5):
    while True:
        entrada = input(f'Digite [S]air ou o numero {i + 1}: ').strip()
        try:
            lista = int(entrada)
            lista_numeros.append(lista)
            break
        except ValueError:
            print('Por favor, digite um número válido (inteiro)')     

lista_ordenada = sorted(lista_numeros)
print(f'Os números digitados em ordem crescente são: {lista_ordenada}')

'''Sugestoes de melhorias

-Clareza na mensagem:
As mensagens ao usuário podem ser um pouco mais descritivas.

-Possibilidade de reuso:
Encapsular a lógica em uma função para maior organização e reutilização.

-Adicionar feedback:
Informar ao usuário o número inserido ou a lista final de números.

def coletar_e_ordenar_numeros(quantidade):
    lista_numeros = []
    print('Digite os números ou digite "sair" para finalizar o programa.')
    
    for i in range(quantidade):
        while True:
            entrada = input(f'Digite o número {i + 1} de {quantidade}: ').strip()
            if entrada.lower() == "sair":
                print("Programa finalizado pelo usuário.")
                return  # Sai da função e encerra o programa
            try:
                numero = int(entrada)
                lista_numeros.append(numero)
                break
            except ValueError:
                print('Por favor, digite um número válido (inteiro).')
    
    lista_ordenada = sorted(lista_numeros)
    print(f'Os números digitados em ordem crescente são: {lista_ordenada}')

# Chamar a função
coletar_e_ordenar_numeros(5)

'''