from character import Character                                       # importing the character object from character file

hero = Character(name="Hero", health=100)
enemy = Character(name="Enemy", health=100)

while True:                                                          # invoking the attack method for hero and enemy.
    hero.attack(enemy)
    enemy.attack(hero)
    
    print(f"Health of Hero {hero.health} and Health of Enemy {enemy.health} ")
    
    input()