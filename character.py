                                                                # This video was used as a tutorial for me to understand Object orientated programming using python. 
                                                                # https://www.youtube.com/watch?v=cM_ocyOrs_k
                                                                # This is used for educational purposes only.



from weapon import fists

                                                                # Assigning the values of name, health and damage to the object itself using the self method.
class Character:
                                                                #race = "Human" class level variable - shared across all instances of the object
    def __init__(self, name: str, health: int) -> None:
        self.name = name                                        # object level variables - they will be unique to the created objects
        self.health = health
        self.health_max = health
        
        self.weapon = fists                                     # All characters will now have fists as a weapon
        
    def attack(self, target) -> None:                           # this will only take one object in this case the target we want to attack
        target.health -= self.weapon.damage                            # this will reduce the health of target by the damage of the attacker(object)
        target.health = max(target.health, 0)                   # this avoids going below zero