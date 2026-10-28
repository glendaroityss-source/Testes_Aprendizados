#funções função(variável)
#variáveis de teste

frase = 'Curso em Video Python'
print('frase = Curso em Video Python')
lista_compras = ['macarrão', 'molho de tomate', 'cebola', 'alho']
lista_valores = [50.0, 270.0, 27.0, 157.0, -78, 8.56984]
diferença = 20 - 70
print()

#type retornará o tipo primitivo ou classe que a variável se enquadra
print(f'type(frase) = {type(frase)}')
print()

#isinstance = instancia quando colocado a variável, vírgula e um tipo, ele retorna verdadeiro ou falso para saber se é ou não
print(f'isinstance(frase, str) = {isinstance(frase, str)}')
print()

# o id retorna um número único, que identifica aquela variável no computador
print(f' id(frase) = {id(frase)}')
print()

#len conta quantos caracteres há em uma variável (contando com seus espaços)
print(f'len(frase) = {len(frase)}')
print()
print('lista_valores = [50.0, 270.0, 27.0, 157.0, -78, 8.56984]')

# sum SOMA VALORES de uma LISTA, SOMENTE NÚMEROS
print(f'sum(lista_valores) = {sum(lista_valores)}')
print()

#min() e max() da o valor menor e maior da lista/sequência
print(f'min(lista_valores) = {min(lista_valores)}')
print(f'max(lista_valores) = {max(lista_valores)}')
print()

# round() arredonda um número para o mais próximo
# math.ceil(x)	Sempre para cima (teto) e math.floor(x)	Sempre para baixo (chão)
print(f'round(lista_valores[5]) = {round(lista_valores[5])}')
print()

print('diferença = 20 - 70')
#abs(): Retorna a distância absoluta de um número até o zero (remove o sinal negativo).
print(f'abs(diferença) = {abs(diferença)}')
print()

print('lista_compras = [macarrão, molho de tomate, cebola, alho]')
print()

#FOR pelo o que eu entendi, o for passa em cada item de uma lista, modificando
# cada um desses itens, criando uma nova variável temporária com essas modificações
print('for comida in lista_compras: \n print(comida) =')
for comida in lista_compras:
    print(comida)

''' precos = [100, 200, 300]
 O 'for' entrega cada valor na variável temporária 'preco'
for preco in precos:
    # Aqui você faz o novo que pediu:
    preco_com_desconto = preco * 0.90
    print(f"Valor com desconto: R$ {preco_com_desconto:.2f}")'''


# range() Quando você chama range(), você está apenas dizendo ao Python para produzir números dentro de um intervalo.
#sozinho ele não vai mostrar contando, você precisa de outra função para fazer isso
de_um_até_cem = list(range(1,101))
print(f'DE UM ATÉ CEM:\n {de_um_até_cem}')
print()
numeros_pares = list(range(2, 101, 2))
print(f'NUMEROS PARES:\n {numeros_pares}')
print()
numeros_impares = list(range(1,101,2))
print(numeros_impares)
