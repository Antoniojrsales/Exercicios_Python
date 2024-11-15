#5. Contador de vogais
#Peça uma frase ao usuário e conte quantas vogais (a, e, i, o, u) existem nela.

frase = input('Digite uma frase: ').strip().lower()
vogais = 'a', 'e', 'i', 'o', 'u'
contador_frases = ''

if len(frase) < 2 or frase == '':
    print('Vc nao digitou nada ou digitou um nome invalido')
else:
    for i in frase:
        if i in vogais:
            contador_frases += i
    print(f'As vogais selecionadas foram {contador_frases} e a quantidade da soma e {len(contador_frases)}')        


''' Sugestoes de melhorias

-Melhorar a validação da entrada:
A verificação tamanho_frase < 2 pode ser simplificada para apenas verificar se a entrada está vazia.

-Eficácia no uso de strings:
Armazenar as vogais em uma lista ou string é suficiente.
Você pode contar diretamente as vogais sem concatenar a string contador_frases, o que é mais eficiente.

-Separar a lógica:
Encapsular o código em uma função facilita a leitura e reutilização.

----------------------------------------------------------------------------------------------
def contar_vogais():
    frase = input('Digite uma frase: ').strip().lower()
    vogais = 'aeiou'  # Lista de vogais
    contador = 0
    encontradas = []

    if not frase:
        print('Você não digitou nada ou digitou uma frase inválida.')
        return

    for letra in frase:
        if letra in vogais:
            contador += 1
            encontradas.append(letra)

    print(f"As vogais encontradas foram: {''.join(encontradas)}")
    print(f"A quantidade total de vogais é: {contador}")

# Chamar a função
contar_vogais()


'''


