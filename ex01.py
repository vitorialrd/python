num = []

bigger = 0
smaller = 0

for c in range(0, 5):
    num.append(int(input('Enter a number: ')))
    if c == 0:
        bigger = smaller = num[c]
    else:
        if num[c] > bigger:
            bigger = num[c]
        if num[c] < smaller:
            smaller = num[c]
for i, v in enumerate(num):
    if num[i] == bigger:
        print(f'The bigger num is {bigger} in position {[i]}')
    if num[i] == smaller:
        print(f'The smaller num is {smaller} in position {[i]}')