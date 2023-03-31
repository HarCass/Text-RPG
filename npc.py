import random
from dice import d20, roll

#NPC START
class NPC():
    name = ''
    weps = []
    weps_dmg = {}
    ac_list = []
    hit_die = []
    hp_bonus = 1
    hit_bonus = 1
    dmg_bonus = 1
    
    def __init__(self):
        self.hpmax = roll(self.hit_die[0],self.hit_die[1]) + self.hp_bonus
        self.hp = self.hpmax
        self.ac = random.choice(self.ac_list)
        self.wpn_equip = random.choice(self.weps)

    def __hit(self):
        self.crit = False
        roll = d20()
        if roll == 20:
            self.crit = True
        return roll + self.hit_bonus
    
    def __dmg(self):
        if self.wpn_equip in self.weps_dmg:
            damage = roll(self.weps_dmg[self.wpn_equip][0],self.weps_dmg[self.wpn_equip][1]) + self.dmg_bonus

        else:
            damage = 1 + self.dmg_bonus
            
        return damage

    def atk(self):
        self.hit = self.__hit()
        if self.crit:
            self.dmg = (self.__dmg()*2)-self.dmg_bonus
        else:
            self.dmg = self.__dmg()
#NPC END

#GOBLIN START
class GOBLIN(NPC):
    name = 'Goblin'
    weps = ['Dagger', 'Shortsword', 'Spiked Club']
    weps_dmg = {'Dagger':[1,'d4'], 'Shortsword':[1,'d6'], 'Spiked Club':[1,'d8']}
    ac_list = [10, 12, 14, 16]
    hit_die = [2,'d6']
    hp_bonus = 2
    hit_bonus = 2
    dmg_bonus = 2
#GOBLIN END

#OGRE START
class OGRE(NPC):
    name = 'Ogre'
    weps = ['Fists', 'Club', 'Spiked Club']
    weps_dmg = {'Fists':[2,'d4'], 'Club':[2,'d6'], 'Spiked Club':[2,'d8']}
    ac_list = [9, 11, 12, 14]
    hp_bonus = 9
    hit_die = [3,'d10']
    hit_bonus = 4
    dmg_bonus = 4
#OGRE END

#THUG START
class THUG(NPC):
    name = 'Thug'
    weps = ['Dagger', 'Mace', 'Arming Sword']
    weps_dmg = {'Dagger':[1,'d4'], 'Mace':[1,'d6'], 'Arming Sword':[1,'d8']}
    ac_list = [10, 12, 14, 16]
    hit_die = [2,'d8']
    hp_bonus = 2
    hit_bonus = 2
    dmg_bonus = 2
#THUG END