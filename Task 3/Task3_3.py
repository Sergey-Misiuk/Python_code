input_string = input('Enter: ').lower().replace(
    ',', ' ').replace('.', ' ').split()

str_dict = {}
count = 1
for i in input_string:
    if not i in str_dict:
        str_dict[i] = count
    else:
        str_dict[i] += 1

for key, elem in str_dict.items():
    print(f'Word "{key}" - count {elem}')
