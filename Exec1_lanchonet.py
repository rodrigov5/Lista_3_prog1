lanches = ['Cachorro Quente', 'Bauru Simples', 'Bauru com ovo', 'Hambúrger', 'Cheeseburger', 'Refrigerante']
precos = [1.20, 1.30, 1.50, 1.20, 1.30, 1]

print('opçoes')
for i in range(len(lanches)):
    print(f'''{lanches[i].capitalize()} \t\t 10{i} \t\t R${precos[i]: .2f}''')

pedidos = []
valor = []
quantidade = []


while True:
    user = int(input('Digite o lache que voce deseja: 10'))
    pedidos.append(lanches[user])
    valor.append(precos[user])
    quant = int(input('Agora digite a quantidade: '))
    quantidade.append(quant)

    continua = int(input('Voce que adicionar mais pedidos? [1 = sim, 2 não]'))

    if continua == 1:
        continue
    elif continua == 2:
        break

valorT = 0
print('\n')
print("\t\t\tNOTA FISCAL")
print('-='*30)
for i in range(len(pedidos)):
    valorT = valorT + (valor[i] * quantidade[i])
    print(f'Lanche: {pedidos[i]} \t Quantidade: {quantidade[i]} \t Valor a ser pago: {valor[i]* quantidade[i]}')
    
print(f'Valor Total {valorT}')      