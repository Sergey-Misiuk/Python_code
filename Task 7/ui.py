import logic


def add_film():
    name_film = input('Enter name Film:\n')
    director = input('Enter director Film:\n')
    year = input('Enter year Film:\n')
    genre = input('Enter genre Film:\n')
    print(logic.add_film(name_film,director,year,genre))


def get_all_record():
    print(logic.get_all_record())


def search_title(name):
    logic.search_title(name)


def search_artist(Director):
    logic.search_artist(Director)


def search_year(year):
    logic.search_year(year)


def search_genre(genre):
    logic.search_genre(genre) 


def main():
    while True:
        choice = input("""
        Select the desired item in the menu:
        0.Exit
        1.Get all records
        2.Search record
        3.Add new record
        """).strip()
        if choice == '0':
            break
        elif choice == '1':
            get_all_record()
        elif choice == '2':
            next_choice = input("""
            Find an entry by:
            0.Exit
            1.Name
            2.Director
            3.Years
            4.Genre
            """)
            if next_choice == '0':
                break
            elif next_choice == '1':
                search_input = input('Enter movie title to search:\n')
                search_title(search_input)
            elif next_choice == '2':
                search_input = input("Enter director's name to search:\n")
                search_artist(search_input)
            elif next_choice == '3':
                search_input = input('Enter year to search:\n')
                search_year(search_input)
            elif next_choice == '4':
                search_input = input('Enter genre to search:\n')
                search_genre(search_input)
        elif choice == '3':
            add_film()
        else:
            print('Select a number from from the menu')
        
        
        
        
main()