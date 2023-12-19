import os
dict_output = {}
signs = [',', '.', '!', '?', ':', ';', '"',
         "'", '#', '%', '@', '$', '^', '*', '<', '>']


def main():
    [find_words(x) for x in os.listdir('.') if x.endswith(('.txt'))]
    if dict_output:
        for key, elem in dict_output.items():
            print(f'Слова найденные в файлах "{key}" - количество {elem}')
    else:
        print('Файлов для чтения не найдено!!!!\nИспользуйте файлы с расширением .txt')


def find_words(name):
    with open(name, 'r') as file:
        for item in file:
            for i in signs:
                item = item.lower().replace(i, ' ')
            for word in item.split():
                if word in dict_output:
                    dict_output[word] += 1
                else:
                    dict_output[word] = 1
    return dict_output


main()
