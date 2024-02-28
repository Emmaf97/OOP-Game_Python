                                                                # This video was used as a tutorial for me to better understand Object orientated programming using python. 
                                                                # https://www.youtube.com/watch?v=cM_ocyOrs_k



from weapon import fists
from health_bar import HealthBar

                                                                # Assigning the values of name, health and damage to the object itself using the self method.
class Character:
                                                                #race = "Human" class level variable - shared across all instances of the object.
    def __init__(self, 
                 name: str, 
                 health: int) -> None:
        self.name = name                                        # object level variables - they will be unique to the created objects.
        self.health = health
        self.health_max = health
        
        self.weapon = fists                                     # All characters will now have fists as a weapon.
        
    def attack(self, target) -> None:                           # this will only take one object in this case the target we want to attack
        target.health -= self.weapon.damage                     # this will reduce the health of target by the damage of the attacker(object)
        target.health = max(target.health, 0)                   # this avoids going below zero
        target.health_bar.update()
        print(f"{self.name} dealt {self.weapon.damage} damage to "
              f"{target.name} with {self.weapon.name}")
        
        
class Hero(Character):                                          # refering to the parent class will inherit from character class/
    def __init__(self, 
                 name: str, 
                 health: int) -> None:
        super().__init__(name=name, health=health)
        
        self.default_weapon = self.weapon
        
        self.health_bar = HealthBar(self, color="green")
        
    def equip(self, weapon) -> None:
        self.weapon = weapon                                    # this method overwrites the current weapon for the hero with a new one.
        print(f"{self.name} equipped a(n) {self.weapon.name}!")
        
    def drop(self):
        print(f"{self.name} dropped the {self.weapon.name}!")
        self.weapon = self.default_weapon                       # this method allows the hero to drop a weapon.
        
class Enemy(Character):                                         # refering to the parent class will inherit from character class.
    def __init__(self, 
                 name: str, 
                 health: int,
                 weapon,) -> None:
        super().__init__(name=name, health=health)
        
        self.weapon = weapon
        
        self.health_bar = HealthBar(self, color="red")