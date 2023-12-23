import test_game_logic

def attack_point():
    return test_game_logic.attack()

def healing_point():
    return test_game_logic.healing()

def create_player(name_player):
    hero = test_game_logic.Player(name_player)
    return hero

def game(player1,enemy):
    try:
        while enemy.health >= 1 and player1.health >=1:
            print(f'\n{player1.name} {player1.health} ед. здоровья ----------- {enemy.name} {enemy.health} ед. здоровья')
            player_choice = int(input("""Ваши ход:
                1. Атакавать (нанести урон на 1-10 ед.)
                2. Вылечить раны (вы восполните свое здоровье на 1-20 ед., но не больше 100)\n"""))
            if player_choice == 1:
                attack_player = attack_point()
                print(f'\nВы нанесли - {attack_player} ед. урона')
                enemy.health -= attack_player
                print(f'У {enemy.name} - {enemy.health} ед. здоровья')
            elif player_choice == 2:
                player_healing = healing_point()
                print(f"\nВы выпили зелье. Ваше здоровье востановленно на {player_healing} ед.")
                player1.health += player_healing
                if player1.health >= 100:
                    player1.health = 100
                    print('Вы полностью востановили здоровье.')
                print(f'У вас {player1.health} ед. здоровья\n')
            else:
                print('\nВыбирите действие из меню!!!')
                game(player1,enemy)
            
            if enemy.health <= 0:
                print("Поздравляем!!! Вы победили противника, вы выйграли!\n")
                break
            attack_enemy = attack_point()
            print('Ход врага. Противник атакует!!!')
            print(f'{enemy.name} нанёс вам {attack_enemy} ед. урона')
            player1.health -= attack_enemy
                
            if player1.health <= 0:
                print("Вы проиграли!!!! Ваш персонаж погиб!\n")
                break
            
    except:
        print('\nВыбирите действие из меню!!!')
        game(player1,enemy)



def main():
    while True:
        choice = input("""Вы попали в игру "Битва с драконом", выберити пункт из меню:
           1. Начать игру
           0. Выход\n""")
        if choice == '0':
            break
        elif choice == '1':
            new_player = input('Введите имя персонажа:\n')
            player1 = create_player(new_player)
            # player1 = test_game_logic.Player(new_player)
            enemy = test_game_logic.Enemy('Dragon')
            game(player1,enemy)
        
            


if __name__ == '__main__':
    main()