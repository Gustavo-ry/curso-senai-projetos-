print('|' * 50)
print('|',' ' * 46, '|')
print('|',' ' * 46, '|')
print('|',' ' * 46, '|')
print('|',' ' * 46, '|')
print('|',' ' * 46, '|')
print('#' * 50)

contador  = 1
for i in range(20):
    print('#' * contador)
    contador += 1 


contador = 2
espaço = 18
for i in range(20):
    print(' ' * espaço,contador * '#')
    contador = contador + 2
    espaço = espaço - 1