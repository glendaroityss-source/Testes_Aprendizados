lista_frutas = ['maça', 'banana', 'pera', 'mexerica', 'abacaxi', 'tomate']
lista_compras = ['macarrão', 'farinha', 'queijo']
print(''' lista Original: lista_frutas = ['maça', 'banana', 'pera', 'mexerica', 'abacaxi', 'tomate']''')
print(''' Lista Original: lista_compras = ['macarrão', 'farinha', 'queijo']''')
print()

#append = acrescentar
lista_frutas.append('pitaya')
print(f'1 - {lista_frutas}')
print('O append() adiciona itens no final da sua lista, minha lista não tinha pitaya')
print()

#extend = estender/ expandir
lista_frutas.extend(lista_compras)
print(f'2 - {lista_frutas}')
print('Aqui eu usei o .extend() com ele eu posso colocar todos os itens de outras listas na minha lista atual')
print()

#insert = inserir
lista_frutas.insert(1, 'morango')
print(f'3 - {lista_frutas}')
print('Aqui eu usei o .insert(), que ao invés de adicionar itens no final da lista, adiciona na índice que você quiser\n'
      'eu coloquei "morango" na índice 1')
print()

#remove = remover
lista_frutas.remove('banana')
print(f'4 - {lista_frutas}')
print('aqui eu removi "banana" com o metodo .remove()')
print()

#pop = estourar
fruta_escolhida = lista_frutas.pop(0)
print(f'5 - {lista_frutas}')
print(fruta_escolhida)
print('Com o .pop() eu posso remover e guardar em outra lista ou variável')
print()

#index = índice
indice = lista_frutas.index('abacaxi')
print(f'6 - {indice}')
print('Aqui eu usei o .index() para localizar em qual posição se encontra "abacaxi"')
print()

#sort = ordenar/classificar (Para ordem decrescente / inversa, usa-se lista.sort(reverse=True))
lista_compras.sort()
print(f'7- {lista_compras}')
lista_frutas.sort()
print(lista_frutas)
print('Aqui eu usei o .sort() para ordenar a lista, como só há texto, ele fará em ordem alfabética')
print()

#reverse = reverter ()
lista_frutas.reverse()
print(f'8 - {lista_frutas}')
print('Com o .reverse() eu posso reverter o que eu fiz a cima')
print()

#copy
copia = lista_frutas.copy()
print(f'9 - {copia}')
print('Aqui eu copiei minha lista original com .copy() \n'
      'serve para caso eu queira fazer uma  alteração sem modificar a original')
print()

#clear = limpar
lista_frutas.clear()
print(f'10 - {lista_frutas}')
print('E por fim, usei o .clear() para limpar a lista')




