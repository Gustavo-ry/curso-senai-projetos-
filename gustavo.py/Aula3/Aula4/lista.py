frutas = ['maça', 'pera', 'uva', 'abacate', 'gato']

print('Qtde itens: ', len(frutas))

print(frutas[0])
print(frutas[2])
print(frutas[4])


frutas.append('carambola')
frutas.append('jaca')
print('Qtde itens: ', len(frutas))


print(frutas[5])
print(frutas[6])


frutas.pop(4)
print('Qtde itens: ', len(frutas))


print(frutas[4])

frutas.remove('jaca')
print('Qtde itens: ', len(frutas))

frutas[2] = 'melancia'
print(frutas[2])
print('Qtde itens: ', len(frutas))

for fruta in frutas:
    print('suco de ', fruta)
    
print(frutas) 



