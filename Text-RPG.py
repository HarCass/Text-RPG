import sys
import random
import math
from os import system

#Defining a clear screen function
system('')
def clear():
    input('Press enter to continue')
    print('\n'*10)

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

def roll(number, dice):
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

#Combat Function start
def combat(pc,*npc):
    npc_count = len(npc)
    if npc_count == 1:
        choice = None
        while npc[0].hp > 0 and pc.hp > 0:
            print(f'\nCurrent HP: {pc.hp}/{pc.hpmax}')
            print(f'\nCurrent Stamina: {pc.stam}/{pc.stam_max}')
            print(f'You are faced by one {npc[0].name}')
            print('''
            1 - Attack
            2 - Defend
            3 - Use Ability
            4 - Use Item
            ''')
            choice = input('What will you do?: ')

            if choice == '1':
                pc.atk()
                print(f'You make an attack against the {npc[0].name} with your {pc.wpn_equip}.')
                if pc.hit >= npc[0].ac or pc.crit:
                    if pc.crit:
                        print(f'Critical hit! Your attack hits the {npc[0].name}! Dealing {pc.dmg} damage.')
                    else:
                        print(f'Your attack hits the {npc[0].name}! ({pc.hit} vs {npc[0].ac}). Dealing {pc.dmg} damage.')
                    if npc[0].hp - pc.dmg <= 0:
                        npc[0].hp = 0
                        print(f'Your blow deals lethal damage, the {npc[0].name} bloodied, collapses to the ground with a thud.')
                    else:
                        npc[0].hp -= pc.dmg
                elif pc.hit < npc[0].ac:
                        print(f'Your attack misses! ({pc.hit} vs {npc[0].ac}). The {npc[0].name} prepares for a strike!')

            elif choice == '2':
                choice = None
                while choice == None:
                    choice = input('Are you sure you want to defend? (1-Y/2-N): ')
                    choice = choice.upper()
                    if choice == '':
                        print('Invalid input.')
                        choice = None
                        continue
                    elif choice[0] == 'N' or choice == '2':
                        choice = None
                        break
                    elif choice[0] == 'Y' or choice == '1':
                        pc.ac += 2
                        print(f'You raise your weapon into a defensive stance(AC raised by 2 ({pc.ac}!).')
                        break
                    else:
                        print('Invalid input.')
                        choice = None
                        continue

            elif choice == '3':
                if pc.stam <= 0:
                    print('You have no stamina left.')
                    choice = None
                    continue
                else:
                    choice = pc.cability()

                if choice  == '':
                    pc.atk()
                    print(f'You make an attack against the {npc[0].name} with your {pc.wpn_equip}.')
                    if pc.hit >= npc[0].ac or pc.crit:
                        if pc.crit:
                            print(f'Critical hit! Your attack hits the {npc[0].name}! Dealing {pc.dmg} damage.')
                        else:
                            print(f'Your attack hits the {npc[0].name}! ({pc.hit} vs {npc[0].ac}). Dealing {pc.dmg} damage.')
                        if npc[0].hp - pc.dmg <= 0:
                            npc[0].hp = 0
                            print(f'Your blow deals lethal damage, the {npc[0].name} bloodied, collapses to the ground with a thud.')
                        else:
                            npc[0].hp -= pc.dmg
                    elif pc.hit < npc[0].ac:
                        print(f'Your attack misses! ({pc.hit} vs {npc[0].ac}). The {npc[0].name} prepares for a strike!')

            elif choice == '4':
                if len(pc.invtry) == 0:
                    print('You have no items.')
                    choice = None
                    continue
                else:
                    choice = pc.useitem()

            else:
                print('invalid input')
                continue

            if choice == None:
                continue
            else:
                pass
            
            if npc[0].hp <= 0:
                pass
            else:
                npc[0].atk()
                print(f'\nThe {npc[0].name} swings at you with their {npc[0].wpn_equip}.')

                if npc[0].hit >= pc.ac or npc[0].crit:
                    if npc[0].crit:
                        print(f'The {npc[0].name} hits a critical hit! Dealing {npc[0].dmg} damage.')
                    else:
                        print(f"The {npc[0].name}'s attack hits! ({npc[0].hit} vs {pc.ac}) Dealing {npc[0].dmg} damage.")
                    if pc.hp - npc[0].dmg <= 0:
                        print(f"The {npc[0].name}'s blow deals lethal damage! Your lifeless body collapes to the ground.")
                        pc.hp = 0
                        break
                    else:
                        pc.hp -= npc[0].dmg
                elif npc[0].hit < pc.ac:
                    print(f"The {npc[0].name}'s attack misses!({npc[0].hit} vs {pc.ac}). They huff in annoyance.")

            if pc.ac != (10+pc.agi_bonus):
                pc.ac = 10+pc.agi_bonus
                print(f'You leave your defensive stance (AC returned to normal ({pc.ac})).')
        

    elif npc_count > 1:
        choice = None
        atk_trgt = None
        trgt_count = npc_count

        while trgt_count > 0 and pc.hp > 0:
            print(f'\nCurrent HP: {pc.hp}/{pc.hpmax}')
            print(f'\nCurrent Stamina: {pc.stam}/{pc.stam_max}')
            if trgt_count == 1:
                for x in range(0,npc_count):
                    if npc[x].hp == 0:
                        pass
                    else:
                        print(f'Only one foe remains, you are faced by one {npc[x].name}.')
            elif trgt_count < npc_count:
                print(f'You have slain {npc_count - trgt_count} enemies, {trgt_count} enemies remain.')
            else:
                print(f'You are faced by {trgt_count} enemies.')
            print('''
            1 - Attack
            2 - Defend
            3 - Use Ability
            4 - Use Item
            ''')
            choice = input('What will you do?: ')

            if choice == '1':
                pc.atk()
                if trgt_count == 1:
                    for x in range(0,npc_count):
                        if npc[x].hp == 0:
                            pass
                        else:
                            print(f'You make an attack against the last enemy, a {npc[x].name}, with your {pc.wpn_equip}.')
                            if pc.hit >= npc[x].ac or pc.crit:
                                if pc.crit:
                                    print(f'Critical hit! Your attack hits the {npc[x].name}! Dealing {pc.dmg} damage.')
                                else:
                                    print(f'Your attack hits the {npc[x].name}! ({pc.hit} vs {npc[x].ac}) Dealing {pc.dmg} damage.')
                                if npc[x].hp - pc.dmg <= 0:
                                    npc[x].hp = 0
                                    trgt_count -= 1
                                    print(f'Your blow deals lethal damage, the {npc[x].name}s blood splatters across the floor and its body drops limp and lifeless to the floor.')
                                else:
                                    npc[x].hp -= pc.dmg
                            elif pc.hit < npc[x].ac:
                                print(f'Your attack misses! ({pc.hit} vs {npc[x].ac}) The {npc[x].name} laughs at your attempt.')

                else:
                    atk_trgt = None
                    print('''
                    Current Available Targets:
                    ''')
                    for x in range(0,npc_count):
                        if npc[x].hp > 0:
                            print(f'''
                    {x+1} - {npc[x].name} {x+1}
                    ''')
                    print('''
                    0 - Back
                    ''')
                    while atk_trgt == None:
                        atk_trgt = input('Which enemy would you like to attack?: ')
                        try:
                            atk_trgt = int(atk_trgt)
                        except:
                            print('Invalid choice.')
                            atk_trgt = None
                            continue
                        if atk_trgt == 0:
                            choice = None
                            break
                        elif 1 > atk_trgt or atk_trgt > npc_count:
                            print('Invalid choice.')
                            atk_trgt = None
                            continue
                        else:
                            atk_trgt -= 1
                        if npc[atk_trgt].hp == 0:
                            print('Invalid choice.')
                            atk_trgt = None
                            continue
                        print(f'You make an attack against enemy {atk_trgt+1}, a {npc[atk_trgt].name}, with your {pc.wpn_equip}.')
                        if pc.hit >= npc[atk_trgt].ac or pc.crit:
                            if pc.crit:
                                print(f'Critical hit! Your attack hits the {npc[atk_trgt].name}! Dealing {pc.dmg} damage.')
                            else:
                                print(f'Your attack hits the {npc[atk_trgt].name}! ({pc.hit} vs {npc[atk_trgt].ac}) Dealing {pc.dmg} damage.')
                            if npc[atk_trgt].hp - pc.dmg <= 0:
                                npc[atk_trgt].hp = 0
                                trgt_count -= 1
                                print(f'Your blow deals lethal damage, the {npc[atk_trgt].name}s blood splatters across the floor and its body drops limp and lifeless to the floor.')
                            else:
                                npc[atk_trgt].hp -= pc.dmg
                        elif pc.hit < npc[atk_trgt].ac:
                            print(f'Your attack misses! ({pc.hit} vs {npc[atk_trgt].ac}) The {npc[atk_trgt].name} laughs at your attempt.')


            elif choice == '2':
                choice = None
                while choice == None:
                    choice = input('Are you sure you want to defend? (1-Y/2-N): ')
                    choice = choice.upper()
                    if choice == '':
                        print('Invalid input.')
                        choice = None
                        continue
                    elif choice[0] == 'N' or choice == '2':
                        choice = None
                        break
                    elif choice[0] == 'Y' or choice == '1':
                        pc.ac += 2
                        print(f'You raise your weapon into a defensive stance(AC raised by 2 ({pc.ac}!).')
                        break
                    else:
                        print('Invalid input.')
                        choice = None
                        continue

            elif choice == '3':
                if pc.stam <= 0:
                    print('You have no stamina left.')
                    choice = None
                    continue
                else:
                    choice = pc.cability()

                if choice == '':
                    pc.atk()
                    if trgt_count == 1:
                        for x in range(0,npc_count):
                            if npc[x].hp == 0:
                                pass
                            else:
                                print(f'You make an attack against the last enemy, a {npc[x].name}, with your {pc.wpn_equip}.')
                                if pc.hit >= npc[x].ac or pc.crit:
                                    if pc.crit:
                                        print(f'Critical hit! Your attack hits the {npc[x].name}! Dealing {pc.dmg} damage.')
                                    else:
                                        print(f'Your attack hits the {npc[x].name}! ({pc.hit} vs {npc[x].ac}) Dealing {pc.dmg} damage.')
                                    if npc[x].hp - pc.dmg <= 0:
                                        npc[x].hp = 0
                                        trgt_count -= 1
                                        print(f'Your blow deals lethal damage, the {npc[x].name}s blood splatters across the floor and its body drops limp and lifeless to the floor.')
                                    else:
                                        npc[x].hp -= pc.dmg
                                elif pc.hit < npc[x].ac:
                                    print(f'Your attack misses! ({pc.hit} vs {npc[x].ac}) The {npc[x].name} laughs at your attempt.')

                    else:
                        atk_trgt = None
                        print('''
                        Current Available Targets:
                        ''')
                        for x in range(0,npc_count):
                            if npc[x].hp > 0:
                                print(f'''
                        {x+1} - {npc[x].name} {x+1}
                        ''')
                        print('''
                        0 - Back
                        ''')
                        while atk_trgt == None:
                            atk_trgt = input('Which enemy would you like to attack?: ')
                            try:
                                atk_trgt = int(atk_trgt)
                            except:
                                print('Invalid choice.')
                                atk_trgt = None
                                continue
                            if atk_trgt == 0:
                                choice = None
                                break
                            elif 1 > atk_trgt or atk_trgt > npc_count:
                                print('Invalid choice.')
                                atk_trgt = None
                                continue
                            else:
                                atk_trgt -= 1
                            if npc[atk_trgt].hp == 0:
                                print('Invalid choice.')
                                atk_trgt = None
                                continue
                            print(f'You make an attack against enemy {atk_trgt+1}, a {npc[atk_trgt].name}, with your {pc.wpn_equip}.')
                            if pc.hit >= npc[atk_trgt].ac or pc.crit:
                                if pc.crit:
                                    print(f'Critical hit! Your attack hits the {npc[atk_trgt].name}! Dealing {pc.dmg} damage.')
                                else:
                                    print(f'Your attack hits the {npc[atk_trgt].name}! ({pc.hit} vs {npc[atk_trgt].ac}) Dealing {pc.dmg} damage.')
                                if npc[atk_trgt].hp - pc.dmg <= 0:
                                    npc[atk_trgt].hp = 0
                                    trgt_count -= 1
                                    print(f'Your blow deals lethal damage, the {npc[atk_trgt].name}s blood splatters across the floor and its body drops limp and lifeless to the floor.')
                                else:
                                    npc[atk_trgt].hp -= pc.dmg
                            elif pc.hit < npc[atk_trgt].ac:
                                print(f'Your attack misses! ({pc.hit} vs {npc[atk_trgt].ac}) The {npc[atk_trgt].name} laughs at your attempt.')

            elif choice == '4':
                if len(pc.invtry) == 0:
                    print('You have no items.')
                    choice = None
                    continue
                else:
                    choice = pc.useitem()

            else:
                print('invalid input')
                continue

            if choice == None:
                continue
            else:
                pass

            for x in range(0,npc_count):
                if npc[x].hp <= 0:
                    pass
                else:
                    npc[x].atk()
                    print(f'\nEnemy {x+1}, a {npc[x].name}, swings at you with their {npc[x].wpn_equip}.')
        
                    if npc[x].hit >= pc.ac or npc[x].crit:
                        if npc[x].crit:
                            print(f'The {npc[x].name} hits a critical hit! Dealing {npc[x].dmg} damage.')
                        else:
                            print(f"The {npc[x].name}'s attack hits! ({npc[x].hit} vs {pc.ac}) Dealing {npc[x].dmg} damage.")
                        if pc.hp - npc[x].dmg <= 0:
                            print(f"The {npc[x].name}'s blow deals lethal damage! They chuckle as you fall to the ground dead.")
                            pc.hp = 0
                            break
                        else:
                            pc.hp -= npc[x].dmg
                    elif npc[x].hit < pc.ac:
                        print(f"The {npc[x].name}'s attack misses!({npc[x].hit} vs {pc.ac}) They yell in frustration.")
                        
            if pc.hp == 0:
                pass
            elif pc.ac != (10+pc.agi_bonus):
                pc.ac = 10+pc.agi_bonus
                print(f'You leave your defensive stance (AC returned to normal ({pc.ac})).')

#Combat function end


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

def e1(pc):
    clear()
    print('\nYou journey along a lonesome road, the town you seek is just over the horizon.')
    print('You come to a slight bend in the road, the road ahead is blocked by a copse of trees.')
    print('Wary you continue down the road, as you pass the trees a strange smell fills your nostrils and something bursts forth from the thicket.')
    print('Two Goblins! Weapons bared and ready to kill, you prepare for a fight to the death.')
    clear()

    gob1 = GOBLIN()
    gob2 = GOBLIN()
    combat(pc,gob1,gob2)

    if gob1.hp <= 0 and gob2.hp <= 0:
        print('You walk away from the Goblins corpses and continue on your journey.')
        pc.lvlup()

    if pc.hp <= 0:
        print('GAME OVER')
        pc.pflag = 0

def e2(pc):
    choice = None
    print('\nA grueling battle completed, you decide to see if the Goblins have anything of value and take a short rest.')
    gold_found = random.randint(1,5)
    pc.gold += gold_found
    print(f"\nLooking through the Goblins belongings you find {gold_found} gold ({pc.name}'s gold: {pc.gold}) and a map that seems to have a camp marked nearby. Perhaps a chance for treasure?")
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
            print('\nTurning you see a large ogre. "Another one for the fire, yum yummy yum" it says in a booming voice. You prepare to fight as it lumbers toward you!')
            clear()
            ogre1 = OGRE()
            combat(pc,ogre1)
            if ogre1.hp <= 0:
                print('\nYou collapse exhausted from the fight, the Ogres body lying next to you, your eyelids feel heavy and you fall unconcious.')
                print('After a few hours of rest you awaken to the foul stench of the dead ogre and the burnt flesh of the corpse over the now dwindling fire.')
                pc.hp = pc.hpmax
                pc.stam = pc.stam_max
                print(f'Despite the uncomfortable nature of your rest you find your wounds no longer trouble you and your stamina returned.(HP and Stamina recovered.)')
                gold_found = random.randint(1,15)
                pc.gold += gold_found
                print(f"\nFeeling refreshed and emboldened from your recent victory you decide to search the camp. After some time you find {gold_found} coins ({pc.name}'s gold: {pc.gold}) but little else of worth and curse the Ogre in frustration.")
                print('Eventually you decide to leave the forest and head down the path that will lead you to the nearby town.')
            if pc.hp <= 0:
                print('GAME OVER')
                pc.pflag = 0
            

        elif choice == '2':
            print('\nYou think better of heading into the forest and continue on the road to the town.')

        else:
            print('Invalid choice.')
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

        3 - "I am the great hero {pc.name} and I have come to help this town in any way I can, but first I require food and board if you would be so kind."
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

    clear()
    print('\nYou ask directions to the inn and head on your way through the dark streets of Arnhollen.')
    print('Few people wander the streets and those that do hide their faces beneath their hoods, hurrying to whatever is their destination, paying you little heed.')
    print('You wander along the streets taking in the dreary sight of Arnhollen'+"'s"+' buildings around you, drab, stained and dishevelled you wonder if this is the slums or if Arnhollen has seen better times.')
    print('Eventually you notice that your destination is on the street across from you on the other side of some buildings, you spot an alleyway that will lead you through and to your destination.')
    print('You could cut through the alleyway or take the long way round to your destination.')
    choice = None
    while choice == None:
        print('''
        1 - Take the long way
        
        2 - Take the alleyway
        ''')
        choice = input('Which path do you take?: ')

        if choice == '1':
            print('You head down the street and turn when it reaches the end, hoping to loop back down the adjacent street to the inn.')
            print('As you round the corner you see three cloaked figures lurking at the streets side, their chatter stops as they notice you.')
            print('They head towards you and you pause gripping your weapon ready for trouble.')
            print('Two circle around you and the other stands before you "Your money or your life" they growl and you see the glint of steel flash in their hand.')
            choice = None
            while choice == None:
                print('''
        1 - Give the thugs your gold
        2 - Fight them
        ''')
                choice = input('What do you do?: ')
                if choice == '1':
                    print('Thinking better of risking your life for some gold, you decide to pay them.')
                    print('"Fine I can pay. No need for violence lads." you say as you fish out your purse.')
                    print('"We got a smart one here, how lucky for us." the thug in front of you says as he looks to his companions.')
                    print('"Now hand it over!" the thug rasies their voice and holds out their hand to recieve your hard earned gold.')
                    gold_lost = random.randint((round(pc.gold/2)),(pc.gold-2))
                    pc.gold -= gold_lost
                    print(f'You manage to sneak {pc.gold} coins out before handing over the remaining {gold_lost} coins in the purse.')
                    if gold_lost < 10:
                        print('"That it?" the thug mumbles grumpily, "Oh well its better than nothing I suppose. Go on off you go." the thug waves you away.')
                    else:
                        print('"Haha jackpot!" the thug cries, "Pleasure doing business with you. Now piss off!" The thug gestures for you to leave.')
                elif choice == '2':
                    print(f'You unsheathe your {pc.wpn_equip} and prepare for a fight.')
                    print('"Fool!" the thug in front of you says "Fine lets bleed you good and strip your cold dead corpse!"')
                                               
                    clear()
                    thug1 = THUG()
                    thug2 = THUG()
                    thug3 = THUG()
                    combat(pc,thug1,thug2,thug3)

                    if thug1.hp <= 0 and thug2.hp <= 0:
                        print('The thugs bodies surround you as an eerie silence fills the street.')
                        gold_found = random.randint(1,25)
                        pc.gold += gold_found
                        print(f"Searching them you find {gold_found} gold, most likely looted from other poor victims, and stuff the coins in your purse ({pc.name}'s Gold: {pc.gold}).")
                        print('You walk away from the thugs corpses and continue on.')

                    if pc.hp <= 0:
                        print('GAME OVER')
                        pc.pflag = 0
                        return None
            print('Thankful to still be alive you make your way to the inn.')

        elif choice == '2':
            print('You make your way through the dark alleyway. Boxes and barrells line its side but there is plenty of space still to walk through.')
            print('Nestled betweeen two boxes you notice a dishevelled man, "Alms for the poor" the begger whimpers.')
            choice = None
            while choice == None:
                print('''
        1 - Give the beggar a coin
        2 - Ignore the poor man
        ''')
                choice = input('What would you like to do?: ')
                if choice == '1':
                    pc.gold -= 1
                    print(f"You toss a coin to the old man the gold flashing as it spins in the air. ({pc.name}'s gold: {pc.gold})")
                    print('The man skillfully snatches the coin out of the air, a smile rising on his face. Suddenly he does not look so rough.')
                    print('Where once was a pitiful beggar, now stands a well dressed man with luscious black hair and a handsome face.')
                    print('Meeting your gaze he bows, "I am Versandis, a pleasure to meet you" he proclaims. "I am a great wizard who travels this land in search of goodfolk to give fortune to"')
                    print('"You have shown the strength of your character good ser and I would grant you a boon if you allow me" he looks at you eagerly.')
                    print('"I can give you a mighty weapon or perhaps you would prefer something more... Interesting?" his grin grows wide as he finishes.')
                    choice = None
                    while choice == None:
                        print('''
        1 - "I'll take the weapon"
        2 - "Consider me intrigued, I'll take this interesting thing you speak of"
        3 - "Keep your trinkets to yourself madman!"
        ''')
                        choice = input('How do you respond?: ')
                        if choice == '1':
                            print(f'"Here my friend pass me your weapon" says verandis. You hesistantly hand over your {pc.wpn_equip}.')
                            print(f'Verandis holds the {pc.wpn_equip} in one hand and with the other makes a strange motion, all the while muttering some strange incantation.')
                            print(f"Before your eyes the {pc.wpn_equip} begins to glow, then suddenly it begins to change shape. Seems the man wasn't lying about being a wizard after all.")
                            if pc.cclass == 'Fighter':
                                pc.wpn_equip = 'Arming Sword'
                            elif pc.cclass == 'Rogue':
                                pc.wpn_equip = 'Falchion'
                            elif pc.cclass == 'Barbarian':
                                pc.wpn_equip = 'Warhammer'
                            print(f'Eventually the glow stops and versandis stops his spell."There you go friend, may it serve you well in the days to come." versandis hands you a shiny {pc.wpn_equip} instead of your old weapon.')
                            print('"And with that I must leave you! Good luck to you ser." before you can say a word he vanishes in a puff of smoke.')
                            print('Giving yourself a moment to process the strange events that just occured, you head out of the alley and make for the inn.')
                        elif choice == '2':
                            print('"Hah! Excellent choice, here take this." Versandis grabs your hand and places something into it.')
                            print('"And with that I must leave you! Good luck to you ser." before you can say a word he vanishes in a puff of smoke.')
                            print('Looking down at what he gave you, you open your hand to reveal a small orb that changes colours in the light.')
                            print('Not knowing exactly what the strange object is or what it does you pocket it for later use.')
                            pc.invtry["Versandis' Orb"] = 1
                            print('After the strange encounter you make your way out and into the street heading for the inn.')
                        elif choice == '3':
                            print('Versandis seems shocked by your outburst and looks sullen as he responds "Seems I have misjudged you." He shakes his head and with a flash disappears.')
                            print('Not knowing if what happened was real, you make your way out of the alley and on to the street, heading straight for the inn.')
                        else:
                            print('Invalid choice.')
                            choice = None
                            continue
                elif choice == '2':
                    print('You ignore the poor man and head down the alley. Eventually you make your way onto the street and make for the inn.')

                else:
                    print('Invalid choice.')
                    

        else:
            print('Invalid choice.')
            choice = None
            continue

        print("You've successfully made your way through Arnhollen's streets and now stand before your destination, The crow's head inn.")
        pc.lvlup()

def e4(pc):
    pass
        
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
            e4(pc)
            if pc.pflag == 0:
                break
            print('\nThanks for playing this is the end of current content')
            break
        while choice == None:
            choice = input('\nDo you want to retry? (1-Y/2-N):')
            choice = choice.upper()
            while choice == '':
                print('Invalid input.')
                choice = input('\nDo you want to retry? (1-Y/2-N):')
            if choice[0] == 'Y' or choice == '1':
                choice = None
                break
            elif choice[0] =='N' or choice == '2':
                end = True
                input('\nThanks for playing! Press enter to exit.')
            else:
                print('Invalid input.')
                choice = None
                continue
main()
