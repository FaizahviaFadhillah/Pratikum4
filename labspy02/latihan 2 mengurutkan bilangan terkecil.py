print('faizah via fadhillah')
print(312210460)
a = int(input('Banyaknya bilangan : '))
bil = []
for i in range(1,a+1):
    x = int (input(f'bilangan ke-{i}: '))
    bil.append(x)
list.sort(bil)
print('Urutan bilangan: ',bil)