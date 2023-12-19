import json


def read_file_collection():
    with open('collection.json', 'r') as read_file:
        info_file = json.load(read_file)
    return info_file



def get_all_record():
    info_file = read_file_collection()
    for item in info_file['item']:
        for key,value in item.items():
            print(f"    {key}: {value}")
        print()
    return 'the end'
        
        

def search_title(name):
    info_file = read_file_collection()
    gener = ( elem for elem in info_file['item'] if elem['Title'] == name)
    for elem in gener:
        print()
        for k,j in elem.items():
            print(f'{k}: {j}')
    return 'the end'


def search_artist(director):
    info_file = read_file_collection()
    gener = ( elem for elem in info_file['item'] if elem['Director'] == director)
    for elem in gener:
        print()
        for k,j in elem.items():
            print(f'{k}: {j}')
    return 'the end'


def search_year(year):
    info_file = read_file_collection()
    gener = ( elem for elem in info_file['item'] if elem['Years'] == year)
    for elem in gener:
        print()
        for k,j in elem.items():
            print(f'{k}: {j}')
    return 'the end'


def search_genre(genre):
    info_file = read_file_collection()
    gener = ( elem for elem in info_file['item'] if elem['Genre'] == genre)
    for elem in gener:
        print()
        for k,j in elem.items():
            print(f'{k}: {j}')
    return 'the end'


def add_film(name_film,director,year,genre):
    data = {
        'Title' : name_film,
        'Director' : director,
        'Years': year,
        'Genre' : genre
    }

    info_file = read_file_collection()

    if data not in info_file['item']: 
        info_file['item'].append(data)

        with open('collection.json', 'w') as out_file:
            json.dump(info_file,out_file,ensure_ascii=False,indent=4)

        return 'This record has been added to the database'

    else:  
        return 'This record is already in the database'



if __name__ == "__main__":
    pass