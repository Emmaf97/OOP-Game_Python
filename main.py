import os
from character import Hero, Enemy                                    # importing the Hero and Enemy object from character file
from weapon import short_bow, iron_sword, fists

hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

while True:                                                          # invoking the attack method for hero and enemy.
    os.system("clear")
    hero.attack(enemy)
    enemy.attack(hero)
    
    hero.health_bar.draw()
    enemy.health_bar.draw()
    
    if hero.weapon != fists:
        hero.drop()
    input()