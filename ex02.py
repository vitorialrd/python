num = []

while True:
    n = int(input('Enter a number: '))
    if n not in num:
        num.append(n)
    r = str(input('Do you want to continue? [Y/N]')).upper()
    if r == 'N':
        break
num.sort()
print(num)