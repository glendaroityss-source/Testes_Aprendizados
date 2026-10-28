
# métodos str essenciais python
play = input('Aperte ENTER para visualizar os métodos de str.')
apresentacao = 'Qual é o seu nome? '.upper()
frase_pergunta = 'Qual é o seu nome?'
senha = 'Agosto270819'
print()
#upper
print(f'seu nome é {apresentacao}')
print('com .upper() ele fica todo maísculo')
print()

#lower
print(f'Seu nome é {apresentacao.lower()}')
print(f'Com .lower() ele fica todo minúsculo')
print()

#strip = tira
print(f'O .strip() tira os espaços do começo e do final ({apresentacao.strip()})')
#aqui ele está ficando em maísculo porque eu coloqeui o .upper() na própia variável
print()

#replace
#para conseguir mudar as palavras da variável apresentação eu tive que criar uma variável com a frase que aparece na tela,
#porque aprendi que, o input não guarda a frase que eu faço aparecer na tela, somente o que o usuário digita, com isso,
#ele não achou nada que eu tinha pedido para ele trocar porque só tinha o nome que a pessoa digitou
idade = frase_pergunta.replace('nome', 'Idade').replace('seu', 'sua' ).replace('o','a')
print(idade)
print('com o .replace() eu posso mudar as palavras de um texto, mudei nome para Idade, seu para sua e o para a')
print()

#split = separar
lista = frase_pergunta.split()
print(lista)
print('com o .split() eu posso fazer uma lista, e cada item da mesma é feito a partir dos espaços')
print()

#count
print(f' Quantas vezes o (e) aparece na fase: Qual é o seu nome? {frase_pergunta.count('e')}')
print('o .count() conta quantas vezes um termo aparece no texto')
print()

#find = encontrar
print(frase_pergunta.find('Qual'))
print(f'O .find() mostra em qual índice começa o termo que você colocou nas aspas, o Qual começa na índice[0]')
print()

#startswith = começa com
print(senha.startswith('Ago'))
print('o .estarswith() analisa se o prefixo colocado dentro das aspas é igual ao começo da frase do texto, aí em cima \n '
      'ele retornou verdadeiro por eu coloquei Ago e a senha é Agosto270819')
print()

#join = juntar/agrupar
print(' '.join(lista))
print('Aqui eu usei o .join(), com ele é possível transformar um lista em um só texto,\n'
      'eu peguei a lista que havia feio com .split() e transformei em uma frase novamente')

