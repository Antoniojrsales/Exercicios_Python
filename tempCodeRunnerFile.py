def soma_numeros(msg):
    entrada = input(msg).strip()
    if entrada.isdigit():
        return int(entrada)
    else:
        print("Por favor, digite um número inteiro válido.")

num1 = soma_numeros('Digite o primeiro numero: ')
num2 = soma_numeros('Digite o segundo numero: ')
print(f'A soma do número {num1} + {num2} = {num1 + num2}')