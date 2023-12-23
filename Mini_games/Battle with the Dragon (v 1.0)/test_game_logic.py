import random

class Enemy():
    
    def __init__(self,name,health=100) -> None:
        self.name = name
        self.health = health


class Player():
    def __init__(self,name,health=100) -> None:
        self.name = name
        self.health = health 

        
def healing():
    point_heal = random.randint(1,20)
    return point_heal  

    
def attack():
        point_attack = random.randint(1,10)
        return point_attack


