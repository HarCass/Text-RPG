import random
from os import system
from combat import combat
from player import PC
from npc import OGRE, GOBLIN, THUG

#Defining a clear screen function
system('')
def clear():
    input('Press enter to continue')
    print('\n'*10)

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
