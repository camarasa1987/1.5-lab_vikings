# Soldier

import random


class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health=self.health-damage


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name=name
        self.health=health
        self.strength=strength

    def attack(self):
        return self.strength 
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health=self.health-damage
        if self.health > 0:
            return self.name + " has received " + str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"
    
    def battleCry(self):
            return "Odin Owns You All!"
    
# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage=damage
        self.health=self.health-damage
        if self.health > 0:
            return  "A Saxon has received " + str(damage) + " points of damage" 
        else:
            return "A Saxon has died in combat"


# War

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):

        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        saxon.receiveDamage(viking.strength) 
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
            return "A Saxon has died in combat"
        else:
            return  "A Saxon has received " + str(viking.strength) + " points of damage" 
    
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
            return viking.name + " has died in act of combat"
        else:    
            return viking.name + " has received " + str(saxon.strength) + " points of damage"
    
    def showStatus(self):
        if not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        elif not self.saxonArmy:
            return "Vikings have won the war of the century!"
        else:
            return "Vikings and Saxons are still in the thick of battle."
        


    

        
