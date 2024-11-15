#6. Sequência de números
#Peça ao usuário um número inteiro positivo n e imprima todos os números de 1 até n.

entrada = input('Digite um numero inteiro: ')
lista = []

if entrada.isdigit():
    entrada_int = int(entrada)
    for i in range(1, entrada_int):
        if i < entrada_int:        
            contador = i
            lista.append(contador)     
    print(f'A sequência de números de 1 até {entrada_int} é: {lista}')          
else:         
    print('Vc digitou um valor invalido')


'''Melhorias sugeridas:

-Simplificar o loop:
Você não precisa do if i < entrada_int, já que o range(1, entrada_int) já lida com o limite.

-Incluir o número final n na sequência:
Se o objetivo é imprimir até n, o range deve ser range(1, entrada_int + 1).

-Usar list(range(...)):
Para gerar a lista de números diretamente, você pode usar a função list(range(...)), eliminando a necessidade do for.

-Mensagem para o usuário:
Informar ao usuário o resultado de forma mais descritiva pode deixar o programa mais interativo.
----------------------------------------------------------------------------------------------
entrada = input('Digite um número inteiro positivo: ').strip()

if entrada.isdigit():  # Verifica se é um número inteiro positivo
    entrada_int = int(entrada)
    if entrada_int > 0:
        lista = list(range(1, entrada_int + 1))  # Gera a lista diretamente
        print(f'A sequência de números de 1 até {entrada_int} é: {lista}')
    else:
        print('Por favor, digite um número maior que zero.')
else:
    print('Você digitou um valor inválido!')'''



 