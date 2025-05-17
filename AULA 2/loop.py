x = 0
while x <= 10:
    print(x)
    x += 1 # e a mesma coisa que x = x + 1


for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)

for fruta in ['banana', 'maça', 'tanjerina',]:
    for estado  in ['verde', 'madura',]:
        print(fruta, estado)


frutas = ['banana', 'maça', 'tanjerina',]
estados = ['verde', 'madura',]
for fruta in frutas:
    for estado in estados:
        print(fruta, estado)