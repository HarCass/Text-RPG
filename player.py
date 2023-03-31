import math
from os import system
from dice import d4, d8, d20, roll

system('')
def clear():
    input('Press enter to continue')
    print('\n'*10)

#PC START
class PC():
    #All weapons
    __wpns = {'Dagger':[1,'d4','dex'], 'Falchion':[1,'d6','dex'], 'Shortsword':[1,'d6','str'], 'Mace':[1,'d6','str'], 'Arming Sword':[1,'d8','str'], 'Battle Axe':[1,'d8','str'],
              'Rapier':[1,'d8','dex'], 'Warhammer':[1,'d10','str'], 'Longsword':[1,'d10','str'], 'Estoc':[1,'d10','dex'], 'Greataxe':[1,'d12','str'], 'Greatsword':[1,'d12','str'], 'Maul':[1,'d12','str']}
    #Progress flag
    pflag = 1
    
    #Setup for character lets user choose name and class and sets intitial values            
    def __init__(self):
        print('A new adventurer steps forward.')
        self.name = input('Please choose a name: ')
        if self.name == '':
            while self.name == '':
                self.name = input('Please choose a name: ')
        self.name = self.name.title()
        print(f'Prepare for a gruelling journey {self.name}.')
        self.atrb = {'STR':1, 'AGI':1, 'DEX':1, 'CON':1}
        self.advantage = False
        self.useab = False
        choice = None
        while choice == None:
            print('''
Class Select

    1 - Barbarian: High Str and Con but low AC and accuracy, starts with a battle axe.
    2 - Fighter: Average stats, starts with a shortsword.
    3 - Rogue: Dex based attacks, high AC and accuracy but low hp, starts with a dagger.

        ''')
            choice = input('\nWhich Class would you like to play as?: ')
            choice = choice.upper()
            
            if choice == '1' or choice == 'BARBARIAN':
                self.cclass = 'Barbarian'
                self.clvl = 1
                self.stam_max = 1
                self.stam = self.stam_max
                self.wpn_equip = 'Battle Axe'
                self.atrb['STR'] = 8
                self.atrb['AGI'] = 1
                self.atrb['DEX'] = 2
                self.atrb['CON'] = 11
                self.str_bonus = math.ceil(self.atrb['STR']/2)
                self.agi_bonus = math.ceil(self.atrb['AGI']/2)
                self.dex_bonus = math.ceil(self.atrb['DEX']/2)
                self.con_bonus = math.ceil(self.atrb['CON']/2)
                self.hpmax = self.atrb['CON']*4
                self.hp = self.hpmax
                self.ac = 10+self.agi_bonus
                self.gold = 2
                self.invtry = {'Healing Potion': 4}
                
            elif choice == '2' or choice == 'FIGHTER':
                self.cclass = 'Fighter'
                self.clvl = 1
                self.stam_max = 2
                self.stam = self.stam_max
                self.wpn_equip = 'Shortsword'
                self.atrb['STR'] = 6
                self.atrb['AGI'] = 4
                self.atrb['DEX'] = 4
                self.atrb['CON'] = 8
                self.str_bonus = math.ceil(self.atrb['STR']/2)
                self.agi_bonus = math.ceil(self.atrb['AGI']/2)
                self.dex_bonus = math.ceil(self.atrb['DEX']/2)
                self.con_bonus = math.ceil(self.atrb['CON']/2)
                self.hpmax = self.atrb['CON']*4
                self.hp = self.hpmax
                self.ac = 10+self.agi_bonus
                self.gold = 10
                self.invtry = {'Healing Potion': 2}

            elif choice == '3' or choice == 'ROGUE':
                self.cclass = 'Rogue'
                self.clvl = 1
                self.stam_max = 1
                self.stam = self.stam_max
                self.wpn_equip = 'Dagger'
                self.atrb['STR'] = 1
                self.atrb['AGI'] = 7
                self.atrb['DEX'] = 8
                self.atrb['CON'] = 6
                self.str_bonus = math.ceil(self.atrb['STR']/2)
                self.agi_bonus = math.ceil(self.atrb['AGI']/2)
                self.dex_bonus = math.ceil(self.atrb['DEX']/2)
                self.con_bonus = math.ceil(self.atrb['CON']/2)
                self.hpmax = self.atrb['CON']*4
                self.hp = self.hpmax
                self.ac = 10+self.agi_bonus
                self.gold = 6
                self.invtry = {'Healing Potion': 1}

            else:
                print('\nPlease Choose a Class from the list.')
                choice = None
                continue

            print(f"\n{self.name}'s Current Stats are: ", ', '.join("{}: {}".format(k, v) for k, v in self.atrb.items()))
            print(f"{self.name}'s current HP is {self.hp}")
            print(f"{self.name}'s current AC is {self.ac}")
            print(f"{self.name} is wielding a {self.wpn_equip}")
            print(f"{self.name} has {self.gold} gold and has {self.invtry['Healing Potion']} healing Potions.")
            choice = None
            while choice == None:
                choice = input('Are you ready to venture forth? (1-Y/2-N): ')
                choice = choice.upper()
                if choice == '':
                    print('Invalid input.')
                    choice = None
                    continue
                elif choice[0] == 'N' or choice == '2':
                    print('Returning to start.')
                    choice = None
                    break
                elif choice[0] == 'Y' or choice == '1':
                    print('Exiting Stat Builder')
                    break
            
                else:
                    print('Invalid input.')
                    choice = None
                    continue

    def lvlup(self):
        print('\nCongratulations you have levelled up!')
        self.clvl += 1
        self.stam_max += 1
        self.stam = self.stam_max
        self.atrb['STR'] += 1
        self.atrb['AGI'] += 1
        self.atrb['DEX'] += 1
        self.atrb['CON'] += 1
        self.str_bonus = math.ceil(self.atrb['STR']/2)
        self.agi_bonus = math.ceil(self.atrb['AGI']/2)
        self.dex_bonus = math.ceil(self.atrb['DEX']/2)
        self.con_bonus = math.ceil(self.atrb['CON']/2)
        self.hpmax = self.atrb['CON']*4
        self.hp = self.hpmax
        self.ac = 10+self.agi_bonus
        print(f'\n{self.name} is a level {self.clvl} {self.cclass}. Whose current Stats are: ', ', '.join("{}: {}".format(k, v) for k, v in self.atrb.items()))
        print(f"{self.name}'s current HP is {self.hp}")
        print(f"{self.name}'s current AC is {self.ac}")
        clear()
                
    def __hit(self):
        self.crit = False
        if self.advantage:
            a = d20()
            b = d20()
            if a >= b:
                hit = a
            else:
                hit = b
        else:
            hit = d20()
        if hit == 20:
            self.crit = True
        if self.useab and self.cclass == 'Fighter':
            return hit + self.dex_bonus + d8()
        else:
            return hit + self.dex_bonus
    
    def __dmg(self):
        if self.wpn_equip in PC.__wpns:
            if PC.__wpns[self.wpn_equip][2] == 'dex' and self.dex_bonus > self.str_bonus:
                damage = roll(PC.__wpns[self.wpn_equip][0], PC.__wpns[self.wpn_equip][1]) + self.dex_bonus
            else:
                damage = roll(PC.__wpns[self.wpn_equip][0], PC.__wpns[self.wpn_equip][1]) + self.str_bonus

        else:
            damage = 1 + self.str_bonus
            
        return damage

    def useitem(self):
        x = 1
        items = []
        choice = None
        for item in self.invtry:
            print(f'\t\t{x} - {item} ({self.invtry[item]})')
            print('\t\t0 - Back')
            items.append(item)
            x +=1
        while choice == None:
            choice = input('Choose an item you wish to use: ')
            try:
                choice = int(choice)-1
            except:
                print('Invalid choice.')
                choice = None
                continue
            if choice+1 == 0:
                return None
            try:
                use = items[choice]
            except:
                print('Invalid choice.')
                choice = None
                continue
            if use == 'Healing Potion':
                self.invtry[use]-= 1
                if self.invtry[use] == 0:
                    del self.invtry[use]
                heal = (d4() + d4() + d4() + 3)
                self.hp += heal
                if self.hp > self.hpmax:
                    self.hp = self.hpmax
                print(f'You chug the potion and heal {heal} HP from the potion! You now have {self.hp} HP.')
                return ''
            else:
                print('This item is unusable.')
                choice = None
                continue

    def cability(self):
        self.useab = False
        choice = None
        if self.cclass == 'Barbarian':
            print(f'''
Current Stamina - {self.stam}/{self.stam_max}
    1 - Reckless Attack (Costs 1 Stamina)
        Makes an attack at advantage.
        Deals +7 damage on a hit.

    0 - Quit''')
            while choice == None:
                choice = input('Choose an ability you wish to use: ')
                if choice == '0':
                    return None
                elif choice == '1':
                    self.useab = True
                    self.stam -= 1
                    self.advantage = True
                    return ''
                else:
                    print('Invalid Choice')
                    choice = None
                    continue

        elif self.cclass == 'Fighter':
            print(f'''
Current Stamina - {self.stam}/{self.stam_max}
    1 - Precision Attack (Costs 1 Stamina)
        Makes an attack with a +d8 to hit.
        Deals +d8 damage on a hit.

    0 - Quit''')
            while choice == None:
                choice = input('Choose an ability you wish to use: ')
                if choice == '0':
                    return None
                elif choice == '1':
                    self.useab = True
                    self.stam -= 1
                    return ''
                else:
                    print('Invalid Choice')
                    choice = None
                    continue

        elif self.cclass == 'Rogue':
            print(f'''
Current Stamina - {self.stam}/{self.stam_max}
    1 - Sneak Attack (Costs 1 Stamina)
        Makes a normal attack.
        Deals +{self.clvl}d6 damage on a hit.

    0 - Quit''')
            while choice == None:
                choice = input('Choose an ability you wish to use: ')
                if choice == '0':
                    return None
                elif choice == '1':
                    self.useab = True
                    self.stam -= 1
                    return ''
                else:
                    print('Invalid Choice')
                    choice = None
                    continue

    

    def atk(self):
        self.hit = self.__hit()
        if self.crit:
            if PC.__wpns[self.wpn_equip][1] == 'dex' and self.dex_bonus > self.str_bonus:
                if self.useab:
                    if self.cclass == 'Barbarian':
                        self.dmg = (self.__dmg()*2)-self.dex_bonus+7
                    elif self.cclass == 'Fighter':
                        self.dmg = self.dmg = (self.__dmg()*2)-self.dex_bonus+d8()
                    elif self.cclass == 'Rogue':
                        self.dmg = (self.__dmg()*2)-self.dex_bonus+roll(self.clvl,'d6')
                else:
                    self.dmg = (self.__dmg()*2)-self.dex_bonus
            else:
                if self.useab:
                    if self.cclass == 'Barbarian':
                        self.dmg = (self.__dmg()*2)-self.str_bonus+7
                    elif self.cclass == 'Fighter':
                        self.dmg = self.dmg = (self.__dmg()*2)-self.str_bonus+d8()
                    elif self.cclass == 'Rogue':
                        self.dmg = (self.__dmg()*2)-self.str_bonus+roll(self.clvl,'d6')
                else:
                    self.dmg = (self.__dmg()*2)-self.str_bonus
        else:
            if self.useab:
                if self.cclass == 'Barbarian':
                    self.dmg = self.__dmg()+7
                elif self.cclass == 'Fighter':
                    self.dmg = self.dmg = self.__dmg()+d8()
                elif self.cclass == 'Rogue':
                    self.dmg = self.__dmg()+roll(self.clvl,'d6')
            else:
                self.dmg = self.__dmg()
        self.useab = False
        self.advantage = False

#PC END