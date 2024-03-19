num = []
odd = []
even = []

while True:
    n = int(input('Enter a number: '))
    num.append(n)
    if n % 2 == 0:
        even.append(n)
    elif n % 2 == 1:
        odd.append(n)
    r = str(input('Do you wanto to continue? [Y/N]')).upper()
    if r == 'N':
        break
even.sort()
odd.sort()
print(num)
print(even)
print(odd)
    
    