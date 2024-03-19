num = []

for c in range(0, 5):
    n = int(input('Enter a number: '))
    for c, v in enumerate(num):
        if n < v:
            num.insert(c, n)
            break
    else:
        num.append(n)
    print(num)
