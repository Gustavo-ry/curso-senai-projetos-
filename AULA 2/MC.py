nome = input("digiye seu nome")
print(f'ola {nome} seja bem vindo ao sistema de calculo de massa corporal')
print(f'criado por Gustavo ryan')

peso = float(input("digite seu peso"))
altura = float(input("digite sua altura"))
imc = peso / (altura*altura)
print(f'seu imc é {imc}')

if imc < 19.1:
    print(f'voce esta abaixo do peso')
elif imc > 19.1 and imc <= 25.8:
    print(f'voce esta no peso ideal')
elif imc > 25.8 and imc <= 27.3:
    print(f'voce esta acima do peso')
elif imc > 27.3 and imc <= 32.3:
    print(f'voce esta com obesidade 1')
elif imc > 32.3:
    print(f'voce esta com obesidade')

    