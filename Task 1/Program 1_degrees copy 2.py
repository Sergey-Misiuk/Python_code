print('Введите градусы Цельсия, которые будут переведены в градусы по Фаренгейту.')
celsius = int(input('Ввод: '))
print(celsius, 'по Цельсию =', round((celsius * 9/5) + 32, 1), "по Фаренгейту")