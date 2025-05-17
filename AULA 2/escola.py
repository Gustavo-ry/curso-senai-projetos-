# sistemas para calcular medias de notas
# entrada de dados

print("sistemas para calcular a média de notas")
print("desenvolvido por gustavo")
nome = input("digite o seu nome")
print(f'ola boa tarde {nome}')
print(f'seja bem vindo ao sistema de calcular media de notas bimestrais')

continuar = 'Sim' # o comando .lower() transforma a string em minusculo
while continuar.lower().strip() == 'sim':  # cria um loop infinito # o comando stri () remove os espaços em branco

    # dados
    bimestre1 = float(input("digite a nota do primeiro bimestre"))
    while bimestre1 > 10:
        bimestre1 = float(input("Erro, digite a nota do primeiro bimestre"))
             
    bimestre2 = float(input("digite a nota do segundo bimestre"))
    while bimestre2 > 10:
       bimestre2 = float(input("Erro, diginete a nota do segundo bimestre"))

    bimestre3 = float(input("digite a nota do terceiro bimestre"))
    while bimestre3 > 10:
       bimestre3 = float(input("Erro, digite a nota do terceiro bimestre"))

    bimestre4 = float(input("digite a nota do quarto bimestre"))
    while bimestre4 > 10:
       bimestre4 = float(input("Erro, diginete a nota do quarto bimestre"))

    # processamento
    media = (bimestre1 + bimestre2 + bimestre3 + bimestre4) / 4

    #saida de dados
    print(f' a media do aluno é {media}') 
    if media >= 5:
       print(f'O aluno {nome} foi aprovado')
    elif media >=3:
       print(f'O aluno {nome} foi para o conselho de classe')
    else :
       print(f'O aluno {nome} foi reprovado')
    continuar = input('continuar? (sim/nao)')
    if continuar == 'nao':
       break # se a resposta for nao, o loop e interronpido
    
       

    
