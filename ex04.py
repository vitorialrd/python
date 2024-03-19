num = []

while True:
    n = int(input('Enter a number: '))
    num.append(n)
    r = str(input('Do you want to continue? [Y/N]')).upper()
    if r == 'N':
        break
num.sort(reverse = True)
print(f'The list have {len(num)} itens.')
print(f'The list in descending order {num}')
if 5 in num:
    print(f'The list has the value 5 in position {num.index(5) + 1}')
else:
    print('The list does not have value 5')
