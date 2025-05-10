# sistemas para calcular medias de notas
# entrada de dados
print("sistemas para calcular a média de notas")
print("desenvolvido por gustavo")
nome = input("digite o seu nome")
print(f'ola boa tarde {nome}')
print(f'seja bem vindo ao sistema de calcular media de notas bimestrais')
# dados
bimestre1 = float(input("digite a nota do primeiro bimestre"))
bimestre2 = float(input("digite a nota do segundo bimestre"))
bimestre3 = float(input("digite a nota do terceiro bimeestre"))
bimestre4 = float(input("digite a nota do quarto bimestre"))
# processamento
media = (bimestre1 + bimestre2 + bimestre3 + bimestre4) / 4
#saida de dados
print(f' a media do aluno é {media}') 
if media >= 5:
    print(f'o aluno esta aprovado')
else:
    print(f'o aluno esta reprovado')