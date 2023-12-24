import random

class Enemy():
    __NAMES = ['Dragon','Skeleton','Mage','Goblin']
    
    def __init__(self,health=100) -> None:
        self.name = random.choice(self.__NAMES)
        self.health = health


class Player():
    
    def __init__(self,name,health=100) -> None:
            
        self.name = self.__varify_input(name)
        self.health = health 

    @classmethod
    def __varify_input(cls,name):
        if len(name) < 1:
            print('Имя вашего очень короткое(Минимальная длинна имени - 1 буква).')
            while len(name) <= 0:
                name = input("Имя: ")
        return name
        
        
def healing():
    point_heal = random.randint(1,20)
    return point_heal  

    
def attack():
        point_attack = random.randint(1,10)
        return point_attack
