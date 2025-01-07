'''1. Operações com Listas
Crie um programa em Python que:

Solicite ao usuário que insira 5 números.
Adicione esses números a uma lista.
Exiba o maior e o menor número da lista.
Calcule e exiba a média dos números inseridos.'''

lista = []

def sep_lista():
    while True:
        entrada = input('Digite 5 numeros con forme seu gosto: ').strip()

        if entrada.isdigit() and len(entrada) == 5:
            for i in entrada:
                lista.append(i)
            print(f'A lista original é: {lista}')
            break
        else:
            return f'Entrada inválida. Por favor, digite 5 números.'

def maior_menor():
    maior = max(lista)
    menor = min(lista)
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")

def media_list():
    valores = [int(val) for val in lista]
    soma = sum(valores)
    media = soma / len(lista)
    print(f"A soma da lista é: {soma}")
    print(f"A média dos números da lista é: {media:.2f}")

def main():
    sep_lista()
    maior_menor()
    media_list()

main()

'''
# Lista global para armazenar os números
lista = []

def sep_lista():
    global lista
    lista = []  # Reinicia a lista para evitar duplicações
    print("Por favor, insira 5 números:")
    for _ in range(5):
        while True:
            try:
                num = int(input("Digite um número: "))
                lista.append(num)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
    print(f'A lista original é: {lista}')

def maior_menor():
    maior = max(lista)
    menor = min(lista)
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")

def media_list():
    soma = sum(lista)
    media = soma / len(lista)
    print(f"A soma da lista é: {soma}")
    print(f"A média dos números da lista é: {media:.2f}")

def main():
    sep_lista()
    maior_menor()
    media_list()

main()

'''