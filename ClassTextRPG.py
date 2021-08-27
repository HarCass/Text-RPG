import sys
import random
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

#PC START
class PC():
    #Starting Classes available to player
    __classes = ['FIGHTER', 'ROGUE', 'BARBARIAN']
    #All weapons
    __wpns = ['Dagger', 'Shortsword', 'Mace', 'Arming Sword', 'Rapier', 'Warhammer', 'Longsword', 'Greatsword', 'Maul']
    #Progress flag
    pflag = 1
    
    #Function which allows user to pick the class of the character
    def __char_build(self):
        choice = None
        while choice == None:
            print('''
Class Select

Fighter: Average stats, uses a Longsword.
Rogue: Dex based attacks, high AC and accuracy but low hp, uses a Rapier.
Barbarian: High Str and Con but low AC and accuracy, uses a Maul.

        ''')
            choice = input('\nWhich Class would you like to play as?: ')
            choice = choice.upper()
            if choice in PC.__classes:
                if choice == 'FIGHTER':
                    self.cclass = 'FIGHTER'
                    self.clvl = 1
                    self.wpn_equip = 'Longsword'
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
                    self.wpn_equip = 'Rapier'
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
                    self.wpn_equip = 'Maul'
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
        print('Congratulations you have levelled up!')
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
            input('Press enter to continue.')
            
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
            input('Press enter to continue.')
            
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
            input('Press enter to continue.')
                
    def __hit(self):
        hit = d20() + self.dex_bonus
        return hit
    
    def __dmg(self):
        if self.wpn_equip == 'Dagger':
            if self.dex_bonus > self.str_bonus:
                damage = d4() + self.dex_bonus
            else:
                damage = d4() + self.str_bonus

        elif self.wpn_equip in ('Shortsword', 'Mace'):
            damage = d6() + self.str_bonus

        elif self.wpn_equip in ('Arming Sword', 'warhammer'):
            damage = d8() + self.str_bonus

        elif self.wpn_equip == 'Rapier':
            if self.dex_bonus > self.str_bonus:
                damage = d8() + self.dex_bonus
            else:
                damage = d8() + self.str_bonus

        elif self.wpn_equip == 'Longsword':
            damage = d10() + self.str_bonus

        elif self.wpn_equip in ('Greatsword', 'Maul'):
            damage = d12() + self.str_bonus

        else:
            damage = 1 + self.str_bonus
            
        return damage

    def atk(self):
        self.crit = False
        self.hit = self.__hit()
        self.dmg = self.__dmg()
        if (self.hit - self.dex_bonus) == 20:
            self.crit = True
            self.dmg = (self.dmg * 2)

#PC END

#GOBLIN START
class GOBLIN():
    gobweps = ['Dagger', 'Scimitar', 'Spiked Club']
    gobac = [11, 13, 15, 17]
    hit_bonus = 2
    dmg_bonus = 3
    
    def __init__(self):
        self.hpmax = d6() + d6() + 2
        self.hp = self.hpmax
        self.ac = random.choice(GOBLIN.gobac)
        self.wpn_equip = random.choice(GOBLIN.gobweps)

    def __hit(self):
        roll = d20() + GOBLIN.hit_bonus
        return roll
    
    def __dmg(self):
        if self.wpn_equip == '':
            damage = 1 + GOBLIN.dmg_bonus

        elif self.wpn_equip == 'Dagger':
            damage = d4() + GOBLIN.dmg_bonus

        elif self.wpn_equip == 'Scimitar':
            damage = d6() + GOBLIN.dmg_bonus

        elif self.wpn_equip == 'Spiked Club':
            damage = d8() + GOBLIN.dmg_bonus
        return damage

    def atk(self):
        self.hit = self.__hit()
        self.dmg = self.__dmg()
        

#GOBLIN END

#OGRE START
class OGRE():
    ogreweps = ['Fists', 'Club', 'Spiked Club']
    ogreac = [9, 11, 13]
    hit_bonus = 4
    dmg_bonus = 5

    def __init__(self):
        self.hpmax = d10()+d10()+d10()+9
        self.hp = self.hpmax
        self.ac = random.choice(OGRE.ogreac)
        self.wpn_equip = random.choice(OGRE.ogreweps)

    def __hit(self):
        roll = d20() + OGRE.hit_bonus
        return roll

    def __dmg(self):
        if self.wpn_equip == 'Fists':
            damage = d4() + d4() + OGRE.dmg_bonus

        elif self.wpn_equip == 'Club':
            damage = d6() + d6() + OGRE.dmg_bonus

        elif self.wpn_equip == 'Spiked Club':
            damage = d8() + d8() + OGRE.dmg_bonus
        return damage

    def atk(self):
        self.hit = self.__hit()
        self.dmg = self.__dmg()

#OGRE END

#THUG START

class THUG():
    thugweps = ['Dagger', 'Mace', 'Arming Sword']
    thugac = [10, 12, 14, 16]
    hit_bonus = 2
    dmg_bonus = 3

    def __init__(self):
        self.hpmax = d8() + d8() + 2
        self.hp = self.hpmax
        self.ac = random.choice(THUG.thugac)
        self.wpn_equip = random.choice(THUG.thugweps)

    def __hit(self):
        roll = d20() + THUG.hit_bonus
        return roll

    def __dmg(self):
        if self.wpn_equip == 'Dagger':
            damage = d4() + THUG.dmg_bonus

        elif self.wpn_equip == 'Mace':
            damage = d6() + THUG.dmg_bonus

        elif self.wpn_equip == 'Arming Sword':
            damage = d8() + THUG.dmg_bonus
        return damage

    def atk(self):
        self.hit = self.__hit()
        self.dmg = self.__dmg()

#THUG END

def e1():
    print('\nYou journey along a lonesome road, the town you seek is just over the horizon.')
    print('You come to a slight bend in the road, the road ahead is blocked by a copse of trees.')
    print('Wary you continue down the road, as you pass the trees a strange smell fills your nostrils and something bursts forth from the thicket.')
    print('Two Goblins! Weapons bared and ready to kill, you prepare for a fight to the death.')
    input('\nPress enter to coninue.')

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

def e2():
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
            print('\nAs you approach the camp the smell of burning flesh fills your nostrils as you see a humanoid creature roasting ona spit above the fire. Quiet, too quiet you think. All of a sudden a load crack sounds behind you!')
            print('\nTurning you see a large ogre. "Another one for the fire, yum yummy yum" it says in a booming voice. It looks like you are in for a fight!')
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
                print('You collapse exhausted from the fight, the Ogres body lying next to you, your eyelids feel heavy and you fall unconcious.')
                print('After a few hours of rest you awaken to the foul stench of the dead ogre and the burnt flesh of the corpse over the now dwindling fire.')
                pc.hp = pc.hpmax
                print('Despite the uncomfortable nature of your rest you find your wounds no longer trouble you. Current HP: ', pc.hp, '/', pc.hpmax)
                print('Feeling refreshed and emboldened from your recent victory you decide to search the camp. After some time you find little of worth and curse the Ogre in frustration.')
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

def e3():
    print('The setting sun lies low in the distance, its red light giving a gloomy feel to the evening as you approach the town.')
    print('The high buildings and its wooden walls come into view and you hurry along the path to the towns gates')
    
        
def main():
    while pc.pflag >= 1:
        e1()
        if pc.pflag == 0:
            break
        e2()
        if pc.pflag == 0:
            break

pc = PC()
main()
exit = None
while exit == None:
    exit = input('\nDo you want to retry? (Y/N):')
    exit = exit.upper()
    if exit == 'Y':
        pc = PC()
        main()
        exit = None
        continue
    elif exit =='N':
        input('\nThanks for playing! Press enter to exit.')
        break
    else:
        print('Invalid input.')
        exit = None
        continue
        
