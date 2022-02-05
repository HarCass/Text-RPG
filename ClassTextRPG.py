import sys
import random
from os import system

#Defining a clear screen function
system('')
def clear():
    input('Press enter to continue')
    _=system('cls')

#Import system, random and define dice rollers
def d4():
    roll = random.randint(1,4)
    return roll

def d6():
    roll = random.randint(1,6)
    return roll

def d8():
    roll = random.randint(1,8)
    return roll

def d10():
    roll = random.randint(1,10)
    return roll

def d12():
    roll = random.randint(1,12)
    return roll

def d20():
    roll = random.randint(1,20)
    return roll

def roll(dice,number=1):
    dicelst = ['d4','d6','d8','d10','d12','d20']
    total = 0
    if dice in dicelst:
        if dice == 'd4':
            for x in range(0,number):
                total += d4()
            return total
        elif dice == 'd6':
            for x in range(0,number):
                total += d6()
            return total
        elif dice == 'd8':
            for x in range(0,number):
                total += d8()
            return total
        elif dice == 'd10':
            for x in range(0,number):
                total += d10()
            return total
        elif dice == 'd12':
            for x in range(0,number):
                total += d12()
            return total
        elif dice == 'd20':
            for x in range(0,number):
                total += d20()
            return total
    else:
        return 1

#PC START
class PC():
    #Starting Classes available to player
    __classes = ['FIGHTER', 'ROGUE', 'BARBARIAN']
    #All weapons
    __wpns = {'Dagger':['d4', 'dex'], 'Shortsword':['d6', 'str'], 'Mace':['d6', 'str'], 'Arming Sword':['d8', 'str'], 'Battle Axe':['d8', 'str'], 'Rapier':['d8', 'dex'], 'Warhammer':['d8', 'str'], 'Longsword':['d10', 'str'], 'Greataxe':['d12', 'str'], 'Greatsword':['d12', 'str'], 'Maul':['d12', 'str']}
    #Progress flag
    pflag = 1
    
    #Function which allows user to pick the class of the character
    def __char_build(self):
        choice = None
        while choice == None:
            print('''
Class Select

Fighter: Average stats, starts with a shortsword.
Rogue: Dex based attacks, high AC and accuracy but low hp, starts with a dagger.
Barbarian: High Str and Con but low AC and accuracy, starts with a battle axe.

        ''')
            choice = input('\nWhich Class would you like to play as?: ')
            choice = choice.upper()
            if choice in PC.__classes:
                if choice == 'FIGHTER':
                    self.cclass = 'FIGHTER'
                    self.clvl = 1
                    self.wpn_equip = 'Shortsword'
                    self.atrb['STR'] = 6
                    self.atrb['AGI'] = 5
                    self.atrb['DEX'] = 4
                    self.atrb['CON'] = 9
                    self.str_bonus = round(self.atrb['STR']/2)
                    self.agi_bonus = round(self.atrb['AGI']/2)
                    self.dex_bonus = round(self.atrb['DEX']/2)
                    self.con_bonus = round(self.atrb['CON']/2)
                    self.hpmax = self.atrb['CON']*4
                    self.hp = self.hpmax
                    self.ac = 9+self.atrb['AGI']

                elif choice == 'ROGUE':
                    self.cclass = 'ROGUE'
                    self.clvl = 1
                    self.wpn_equip = 'Dagger'
                    self.atrb['STR'] = 1
                    self.atrb['AGI'] = 8
                    self.atrb['DEX'] = 8
                    self.atrb['CON'] = 7
                    self.str_bonus = round(self.atrb['STR']/2)
                    self.agi_bonus = round(self.atrb['AGI']/2)
                    self.dex_bonus = round(self.atrb['DEX']/2)
                    self.con_bonus = round(self.atrb['CON']/2)
                    self.hpmax = self.atrb['CON']*4
                    self.hp = self.hpmax
                    self.ac = 9+self.atrb['AGI']

                elif choice == 'BARBARIAN':
                    self.cclass = 'BARBARIAN'
                    self.clvl = 1
                    self.wpn_equip = 'Battle Axe'
                    self.atrb['STR'] = 8
                    self.atrb['AGI'] = 1
                    self.atrb['DEX'] = 2
                    self.atrb['CON'] = 13
                    self.str_bonus = round(self.atrb['STR']/2)
                    self.agi_bonus = round(self.atrb['AGI']/2)
                    self.dex_bonus = round(self.atrb['DEX']/2)
                    self.con_bonus = round(self.atrb['CON']/2)
                    self.hpmax = self.atrb['CON']*4
                    self.hp = self.hpmax
                    self.ac = 9+self.atrb['AGI']

            else:
                print('\nThis class does not exist. Please Choose a Class from the list.')
                choice = None
                continue

            print('\n'+self.name+"'s Current Stats are: ", ', '.join("{}: {}".format(k, v) for k, v in self.atrb.items()))
            print(self.name+"'s", 'current HP is', self.hp)
            print(self.name+"'s", 'current AC is', self.ac)
            print(self.name, 'is wielding a', self.wpn_equip)
            choice = input('Are you ready to venture forth? (Y/N): ')
            choice = choice.upper()
            if choice == 'N':
                choice = None
                continue
            elif choice == 'Y':
                print('Exiting Stat Builder')
                break
            
            else:
                print('Invalid input. Returning to start')
                choice = None
                continue
            

    def __init__(self):
        print('A new adventurer steps forward.')
        self.name = input('Please choose a name: ')
        if self.name == '':
            while self.name == '':
                self.name = input('Please choose a name: ')
        self.name = self.name.title()
        print('Prepare for a gruelling journey', self.name)
        self.atrb = {'STR':1, 'AGI':1, 'DEX':1, 'CON':1}
        self.__char_build()

    def lvlup(self):
        print('\nCongratulations you have levelled up!')
        self.clvl += 1
        
        if self.cclass == 'FIGHTER':
            self.atrb['STR'] += 1
            self.atrb['AGI'] += 1
            self.atrb['DEX'] += 1
            self.atrb['CON'] += 1
            self.str_bonus = round(self.atrb['STR']/2)
            self.agi_bonus = round(self.atrb['AGI']/2)
            self.dex_bonus = round(self.atrb['DEX']/2)
            self.con_bonus = round(self.atrb['CON']/2)
            self.hpmax = self.atrb['CON']*4
            self.hp = self.hpmax
            self.ac = 9+self.atrb['AGI']
            print('\n'+self.name+" is a level", self.clvl, self.cclass,'Whose current Stats are: ', ', '.join("{}: {}".format(k, v) for k, v in self.atrb.items()))
            print(self.name+"'s", 'current HP is', self.hp)
            print(self.name+"'s", 'current AC is', self.ac)
            clear()
            
        elif self.cclass == 'ROGUE':
            self.atrb['STR'] += 1
            self.atrb['AGI'] += 1
            self.atrb['DEX'] += 1
            self.atrb['CON'] += 1
            self.str_bonus = round(self.atrb['STR']/2)
            self.agi_bonus = round(self.atrb['AGI']/2)
            self.dex_bonus = round(self.atrb['DEX']/2)
            self.con_bonus = round(self.atrb['CON']/2)
            self.hpmax = self.atrb['CON']*4
            self.hp = self.hpmax
            self.ac = 9+self.atrb['AGI']
            print('\n'+self.name+" is a level", self.clvl, self.cclass,'Whose current Stats are: ', ', '.join("{}: {}".format(k, v) for k, v in self.atrb.items()))
            print(self.name+"'s", 'current HP is', self.hp)
            print(self.name+"'s", 'current AC is', self.ac)
            clear()
            
        elif self.cclass == 'BARBARIAN':
            self.atrb['STR'] += 1
            self.atrb['AGI'] += 1
            self.atrb['DEX'] += 1
            self.atrb['CON'] += 1
            self.str_bonus = round(self.atrb['STR']/2)
            self.agi_bonus = round(self.atrb['AGI']/2)
            self.dex_bonus = round(self.atrb['DEX']/2)
            self.con_bonus = round(self.atrb['CON']/2)
            self.hpmax = self.atrb['CON']*4
            self.hp = self.hpmax
            self.ac = 9+self.atrb['AGI']
            print('\n'+self.name+" is a level", self.clvl, self.cclass,'Whose current Stats are: ', ', '.join("{}: {}".format(k, v) for k, v in self.atrb.items()))
            print(self.name+"'s", 'current HP is', self.hp)
            print(self.name+"'s", 'current AC is', self.ac)
            clear()
                
    def __hit(self):
        self.crit = False
        hit = d20()
        if hit == 20:
            self.crit = True
        return hit + self.dex_bonus
    
    def __dmg(self):
        if self.wpn_equip in PC.__wpns:
            if PC.__wpns[self.wpn_equip][1] == 'dex':
                if self.dex_bonus > self.str_bonus:
                    damage = roll(PC.__wpns[self.wpn_equip][0]) + self.dex_bonus
                else:
                    damage = roll(PC.__wpns[self.wpn_equip][0]) + self.str_bonus
            else:
                damage = roll(PC.__wpns[self.wpn_equip][0]) + self.str_bonus

        else:
            damage = 1 + self.str_bonus
            
        return damage

    def atk(self):
        self.hit = self.__hit()
        if self.crit:
            if PC.__wpns[self.wpn_equip][1] == 'dex' and self.dex_bonus > self.str_bonus:
                self.dmg = (self.__dmg()*2)-self.dex_bonus
            else:
                self.dmg = (self.__dmg()*2)-self.str_bonus
        else:
            self.dmg = self.__dmg()

#PC END

#NPC START
class NPC():
    weps = []
    weps_dmg = {}
    ac = []
    hit_die = []
    hp_bonus = 1
    hit_bonus = 1
    dmg_bonus = 1
    
    def __init__(self):
        self.hpmax = roll(self.hit_die[0],self.hit_die[1]) + self.hp_bonus
        self.hp = self.hpmax
        self.ac = random.choice(self.ac)
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
    weps = ['Dagger', 'Shortsword', 'Spiked Club']
    weps_dmg = {'Dagger':['d4',1], 'Shortsword':['d6',1], 'Spiked Club':['d8',1]}
    ac = [10, 12, 14, 16]
    hit_die = ['d6',2]
    hp_bonus = 2
    hit_bonus = 2
    dmg_bonus = 3
#GOBLIN END

#OGRE START
class OGRE(NPC):
    weps = ['Fists', 'Club', 'Spiked Club']
    weps_dmg = {'Fists':['d4',2], 'Club':['d6',2], 'Spiked Club':['d8',2]}
    ac = [9, 11, 12, 14]
    hp_bonus = 9
    hit_die = ['d10',3]
    hit_bonus = 4
    dmg_bonus = 5
#OGRE END

#THUG START
class THUG(NPC):
    weps = ['Dagger', 'Mace', 'Arming Sword']
    weps_dmg = {'Dagger':['d4',1], 'Mace':['d6',1], 'Arming Sword':['d8',1]}
    ac = [10, 12, 14, 16]
    hit_die = ['d8',2]
    hp_bonus = 2
    hit_bonus = 2
    dmg_bonus = 3
#THUG END

def e1(pc):
    print('\nYou journey along a lonesome road, the town you seek is just over the horizon.')
    print('You come to a slight bend in the road, the road ahead is blocked by a copse of trees.')
    print('Wary you continue down the road, as you pass the trees a strange smell fills your nostrils and something bursts forth from the thicket.')
    print('Two Goblins! Weapons bared and ready to kill, you prepare for a fight to the death.')
    clear()

    gob1 = GOBLIN()
    gob2 = GOBLIN()
    choice = None
    atk_trgt = None

    while gob1.hp > 0 or gob2.hp > 0 or pc.hp > 0:
        print('\nCurrent HP: ', pc.hp, '/', pc.hpmax)
        if gob1.hp == 0 or gob2.hp == 0:
            print('You have slain one Goblin, one more remains.')
        else:
            print('You are faced by two frenzied Goblins')
        print('''
        1 - Attack
        2 - Defend
        ''')
        choice = input('What will you do?: ')

        if choice == '1':
            pc.atk()
            if gob2.hp == 0:
                print('You make an attack against the first Goblin with your', pc.wpn_equip, '.')
                if pc.hit >= gob1.ac:
                        if pc.crit:
                            print('Critical hit! Your attack hits the goblin! (', pc.hit, 'vs', gob1.ac, ') Dealing', pc.dmg, 'damage.')
                        else:
                            print('Your attack hits the goblin! (', pc.hit, 'vs', gob1.ac, ') Dealing', pc.dmg, 'damage.')
                        if gob1.hp - pc.dmg <= 0:
                            gob1.hp = 0
                            print('Your blow deals lethal damage, the Goblins blood splatters across the floor and its body drops limp and lifeless to the floor.')
                            break
                        else:
                            gob1.hp -= pc.dmg
                elif pc.hit < gob1.ac:
                        print('Your attack misses! (', pc.hit, 'vs', gob1.ac, ') The Goblin laughs at your attempt.')
            elif gob1.hp == 0:
                print('You make an attack against the second Goblin with your', pc.wpn_equip, '.')
                if pc.hit >= gob2.ac:
                    if pc.crit:
                            print('Critical hit! Your attack hits the goblin! (', pc.hit, 'vs', gob1.ac, ') Dealing', pc.dmg, 'damage.')
                    else:
                            print('Your attack hits the goblin! (', pc.hit, 'vs', gob1.ac, ') Dealing', pc.dmg, 'damage.')
                    if gob2.hp - pc.dmg <= 0:
                        gob2.hp = 0
                        print('Your blow deals lethal damage, the Goblins head rolls from its shoulders and its body drops limp and lifeless to the floor.')
                        break
                    else:
                        gob2.hp -= pc.dmg
                elif pc.hit < gob2.ac:
                    print('Your attack misses! (', pc.hit, 'vs', gob2.ac, ') The Goblin cackles in glee.')
            else:
                while atk_trgt == None:
                    print('''
                    Current Available Targets
                    Goblin 1 - 1
                    Goblin 2 - 2
                    ''')
                    atk_trgt = input('Which enemy would you like to attack?: ')
                    if atk_trgt == '1':
                        print('You make an attack against the first Goblin with your', pc.wpn_equip, '.')
                        if pc.hit >= gob1.ac:
                            if pc.crit:
                                print('Critical hit! Your attack hits the goblin! (', pc.hit, 'vs', gob1.ac, ') Dealing', pc.dmg, 'damage.')
                            else:
                                print('Your attack hits the goblin! (', pc.hit, 'vs', gob1.ac, ') Dealing', pc.dmg, 'damage.')
                            if gob1.hp - pc.dmg <= 0:
                                gob1.hp = 0
                                print('Your blow deals lethal damage, the Goblins blood splatters across the floor and its body drops limp and lifeless to the floor.')
                            else:
                                gob1.hp -= pc.dmg
                        elif pc.hit < gob1.ac:
                            print('Your attack misses! (', pc.hit, 'vs', gob1.ac, ') The Goblin laughs at your attempt.')
                        atk_trgt = None
                        break
                    elif atk_trgt == '2':
                        print('You make an attack against the second Goblin with your', pc.wpn_equip, '.')
                        if pc.hit >= gob2.ac:
                            if pc.crit:
                                print('Critical hit! Your attack hits the goblin! (', pc.hit, 'vs', gob1.ac, ') Dealing', pc.dmg, 'damage.')
                            else:
                                print('Your attack hits the goblin! (', pc.hit, 'vs', gob1.ac, ') Dealing', pc.dmg, 'damage.')
                            if gob2.hp - pc.dmg <= 0:
                                gob2.hp = 0
                                print('Your blow deals lethal damage, the Goblins head rolls from its shoulders and its body drops limp and lifeless to the floor.')
                            else:
                                gob2.hp -= pc.dmg
                        elif pc.hit < gob2.ac:
                            print('Your attack misses! (', pc.hit, 'vs', gob2.ac, ') The Goblin cackles in glee.')
                        atk_trgt = None
                        break
                    else:
                        print('Inavlid Target')
                        atk_trgt = None
                        continue

        elif choice == '2':
            pc.ac += 2
            print('You raise your weapon into a defensive stance(AC raised by 2 (',pc.ac, ')!).')

        else:
            print('invalid input')
            continue

        if gob1.hp <= 0:
            pass
        else:
            gob1.atk()
            print('The first Goblin swings at you with its', gob1.wpn_equip, '.')
    
            if gob1.hit >= pc.ac:
                if gob1.crit:
                    print('The Goblin hits a critical hit!(', gob1.hit, 'vs', pc.ac, ') Dealing', gob1.dmg, 'damage.')
                else:
                    print("The Goblin's attack hits! (", gob1.hit, 'vs', pc.ac, ') Dealing', gob1.dmg, 'damage.')
                if pc.hp - gob1.dmg <= 0:
                    print("The Goblin's blow deals lethal damage! It chuckles as you fall to the ground dead.")
                    pc.hp = 0
                    break
                else:
                    pc.hp -= gob1.dmg
            elif gob1.hit < pc.ac:
                print("The Goblin's attack misses!(", gob1.hit, 'vs', pc.ac, ') It snarls in frustration.')

        if gob2.hp <= 0:
            pass
        else:
            gob2.atk()
            print('The second Goblin slashes at you with its', gob2.wpn_equip, '.')

            if gob2.hit >= pc.ac:
                if gob2.crit:
                    print('The Goblin hits a critical hit!(', gob2.hit, 'vs', pc.ac, ') Dealing', gob2.dmg, 'damage.')
                else:
                    print("The Goblin's attack hits! (", gob2.hit, 'vs', pc.ac, ') Dealing', gob2.dmg, 'damage.')
                if pc.hp - gob2.dmg <= 0:
                    print("The Goblin's blow deals lethal damage! It chortles as you fall to the ground dead.")
                    pc.hp = 0
                    break
                else:
                    pc.hp -= gob2.dmg
            elif gob2.hit < pc.ac:
                print("The Goblin's attack misses!(", gob2.hit, 'vs', pc.ac, ') It screeches in frustration.')

        if choice == '2':
            pc.ac -= 2
            print('You leave your defensive stance (AC returned to normal (', pc.ac, ')).')

    if gob1.hp <= 0 and gob2.hp <= 0:
        print('You walk away from the Goblins corpses and continue on your journey.')
        pc.lvlup()

    if pc.hp <= 0:
        print('GAME OVER')
        pc.pflag = 0
        sys.exit

def e2(pc):
    choice = None
    print('\nA grueling battle completed, you decide to see if the Goblins have anything of value and take a short rest.')
    print('\nLooking through the Goblins belongings you find a map that seems to have a camp marked nearby. Perhaps a chance for treasure?')
    print('\nOr maybe it is safer to continue to the town.')
    print('''
    1 - Head to goblin camp.
    2 - Continue to nearby town.
    ''')
    while choice == None:
        choice = input('\nWhat will you do?: ')
        if choice == '1':
            print('\nYou head through the forest towards the marked location, eventually you come to see a small clearing ahead of you a fire lit at its centre. Surrounding it are two tents one of medium size the other quite large.')
            print('\nAs you approach the camp the smell of burning flesh fills your nostrils as you see a humanoid creature roasting on a spit above the fire. Quiet, too quiet you think. All of a sudden a load crack sounds behind you!')
            print('\nTurning you see a large ogre. "Another one for the fire, yum yummy yum" it says in a booming voice. It looks like you are in for a fight!')
            clear()
            ogre1 = OGRE()
            choice = None
            while ogre1.hp > 0 or pc.hp > 0:
                print('\nCurrent HP: ', pc.hp, '/', pc.hpmax)
                print('You are faced by a hungry Ogre')
                print('''
                1 - Attack
                2 - Defend
                ''')
                choice = input('What will you do?: ')

                if choice == '1':
                    pc.atk()
                    print('You make an attack against the Ogre with your', pc.wpn_equip, '.')
                    if pc.hit >= ogre1.ac:
                        if pc.crit:
                            print('Critical hit! Your attack hits the Ogre! (', pc.hit, 'vs', ogre1.ac, ') Dealing', pc.dmg, 'damage.')
                        else:
                            print('Your attack hits the Ogre! (', pc.hit, 'vs', ogre1.ac, ') Dealing', pc.dmg, 'damage.')
                        if ogre1.hp - pc.dmg <= 0:
                            ogre1.hp = 0
                            print('Your blow deals lethal damage, the Ogre bloodied and bruised, collapses to the ground with a loud thud.')
                            break
                        else:
                            ogre1.hp -= pc.dmg
                    elif pc.hit < ogre1.ac:
                            print('Your attack misses! (', pc.hit, 'vs', ogre1.ac, ') The Ogre licks its lips in anticipation.')

                elif choice == '2':
                    pc.ac += 2
                    print('You raise your weapon into a defensive stance(AC raised by 2 (',pc.ac, ')!).')
                else:
                    print('invalid input')
                    continue
                
                if ogre1.hp <= 0:
                    pass
                else:
                    ogre1.atk()
                    print('The Ogre swings at you with its', ogre1.wpn_equip, '.')
    
                    if ogre1.hit >= pc.ac:
                        if ogre1.crit:
                            print("The Ogre hits a critical hit! (", ogre1.hit, 'vs', pc.ac, ') Dealing', ogre1.dmg, 'damage.')
                        else:
                            print("The Ogre's attack hits! (", ogre1.hit, 'vs', pc.ac, ') Dealing', ogre1.dmg, 'damage.')
                        if pc.hp - ogre1.dmg <= 0:
                            print("The Ogre's blow deals lethal damage! It lifts your lifeless body off the ground and throws it onto the fire, 'Yummy yum yum' it cackles.")
                            pc.hp = 0
                            break
                        else:
                            pc.hp -= ogre1.dmg
                    elif ogre1.hit < pc.ac:
                        print("The Ogre's attack misses!(", ogre1.hit, 'vs', pc.ac, ') It huffs and puffs in annoyance.')

                if choice == '2':
                              pc.ac -= 2
                              print('You leave your defensive stance (AC returned to normal (', pc.ac, ')).')

            if ogre1.hp <= 0:
                print('\nYou collapse exhausted from the fight, the Ogres body lying next to you, your eyelids feel heavy and you fall unconcious.')
                print('After a few hours of rest you awaken to the foul stench of the dead ogre and the burnt flesh of the corpse over the now dwindling fire.')
                pc.hp = pc.hpmax
                print('Despite the uncomfortable nature of your rest you find your wounds no longer trouble you. Current HP: ', pc.hp, '/', pc.hpmax)
                print('\nFeeling refreshed and emboldened from your recent victory you decide to search the camp. After some time you find little of worth and curse the Ogre in frustration.')
                print('Eventually you decide to leave the forest and head down the path that will lead you to the nearby town.')
            if pc.hp <= 0:
                print('GAME OVER')
                pc.pflag = 0
                sys.exit
            

        elif choice == '2':
            print('\nYou think better of heading into the forest and continue on the road to the town.')

        else:
            print('Invalid choice please select 1 or 2.')
            choice = None
            continue

def e3(pc):
    clear()
    print('\nThe setting sun lies low in the distance, its red light giving a gloomy feel to the evening as you approach the town.')
    print('The high buildings and its wooden walls come into view and you hurry along the path to the towns gates')
    print('As you approach a burly guard raises his hand, "Halt traveller. What brings you to the town of Arnhollen so late in the eve?"')
    choice = None
    while choice == None:
        print(f'''
        1 - "My business is my own but know that I come with no ill intent, I seek only a place to rest."

        2 - "My name is {pc.name} and I have journeyed far and been assailed by goblins on the road, I seek somewhere to retire for the night."

        3 - "I am the great hero {pc.name} and I have come to help this town in any way I can. but first I require food and board if you would be so kind."
        ''')
        choice = input('How do you respond?: ')

        if choice == '1':
            print('\n"All right all right, it is my job to ask. There has been talk of strange folk abroad and you can never be too careful." The guard responds')
            print('"Well you look trustworthy enough, as long you as promise to stay out of trouble head on in."')
            print('"Oh, and I would recommend the Crow'+"'s"+' head if you want some rest and good food."')
            print('"Be seeing you now and watch yourself the streets can be dangerous at night."')

        elif choice == '2':
            print('\n"Goblins you say? Dark times, dark times indeed if they are so close now. Come on in quick." Says the guard with a furrowed brow.')
            print('"Worry not, the walls of Arnhollen will keep those goblins out. Head to the Crow'+"'s"+' head if you want some rest and good food."')
            print('"Be seeing you now and watch yourself it is not just goblins to be careful of."')

        elif choice == '3':
            print('\n"Oh? Great hero is it? Never heard of you! Well, you look well armed and capable and there are troubles aplenty in Arnhollen ever since the Lord went to fight the King'+"s"+' war". The guard looks troubled as he talks.')
            print('"Hmm come on in. But stay out of trouble ya hear! And if you need a place to stay head to the Crow'+"'s"+' head if you want some rest and good food."')
            print('"Be seeing you now and watch out for thugs, they like to cause trouble at night."')

        else:
            print('Invalid choice.')
            choice = None
            continue

    print('\nYou ask directions to the inn and head on your way through the dark streets of Arnhollen.')
    
    
        
def main():
    end = False
    choice = None
    while not end:
        pc = PC()
        while pc.pflag >= 1:
            e1(pc)
            if pc.pflag == 0:
                break
            e2(pc)
            if pc.pflag == 0:
                break
            e3(pc)
            if pc.pflag == 0:
                break
            print('\nThanks for playing this is the end of current content')
            break
        while choice == None:
            choice = input('\nDo you want to retry? (Y/N):')
            choice = choice.upper()
            if choice == 'Y':
                choice = None
                break
            elif choice =='N':
                end = True
                input('\nThanks for playing! Press enter to exit.')
            else:
                print('Invalid input.')
                choice = None
                continue
main()
