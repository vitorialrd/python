peoples = []
data = []

thin = fat = 0

while True:
    data.append(str(input('Name: ')))
    data.append(float(input('Weigth: ')))

    if len(peoples) == 0:
        thin = fat = data[1]
    else:
        if data[1] < thin:
            thin = data[1]
        if data[1] > fat:
            fat = data[1]

    peoples.append(data[:])
    data.clear()

    r = str(input('Do you want to continue? [Y/N]')).upper()
    if r == 'N':
        break   

print(len(peoples))
print(f'Fat peoples: {fat} ', end='')
for p in peoples:
    if p[1] == fat:
        print(f'[{p[0]}] ', end='')
print(f'\nThin peoples: {thin} ', end='')
for p in peoples:
    if p[1] == thin:
        print(f'[{p[0]}] ', end='')