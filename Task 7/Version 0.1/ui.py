import logic


def add_film():
    name_film = input('Enter name Film:\n')
    producer = input('Enter producer Film:\n')
    year = input('Enter year Film:\n')
    genre = input('Enter genre Film:\n')
    print(logic.add_film(name_film,producer,year,genre))


def get_all_record():
    print(logic.get_all_record())

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
            2.Producer
            3.Years
            4.Genre
            """)
            pass
        elif choice == '3':
            add_film()
        else:
            print('Select a number from from the menu')
        
        
        
        
main()