# list_input = input('Enter: ').split(',')

lis = ['14', '2.2', '2', '1.1']
lis.remove(min(lis))
lis2 = []
for i in lis:
    lis2.append(int(i))
lis2.sort()
print(lis2)
