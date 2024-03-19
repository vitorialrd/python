num = []
par = []
impar = []

for c in range (0, 7):
    n = int(input('Numeros: '))

    if n % 2 == 0:
        par.append(n)
    if n % 2 == 1:
        impar.append(n)

    
par.sort()
impar.sort()
num.append(par[:])
num.append(impar[:])


print(num)