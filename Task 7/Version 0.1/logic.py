import json


def get_all_record(counts=0):
    with open('collection.json', 'r') as read_file:
        info_file = json.load(read_file)
    for item in info_file['item']:
        for key,value in item.items():
            print(f"    {key}: {value}")
        print()
    return "the end"
        
        

def search_title(name):pass


def search_artist(producer):pass


def search_year(year):pass


def search_genre(genre):pass


def add_film(name_film,producer,year,genre):
    data = {
        'Title' : name_film,
        'Producer' : producer,
        'Years': year,
        'Genre' : genre
    }

    with open('collection.json', 'r') as read_file:
        info_file = json.load(read_file)
        info_file["item"].append(data)

        with open('collection.json', 'w') as out_file:
            json.dump(info_file,out_file,ensure_ascii=False,indent=4)
        
    return 'The record has been added to the collection'




if __name__ == "__main__":
    print(get_all_record())