#Combat Function start
def combat(pc,*npc):
    npc_count = len(npc)
    choice = None
    atk_trgt = None
    trgt_count = npc_count

    while trgt_count > 0 and pc.hp > 0:
        print(f'\nCurrent HP: {pc.hp}/{pc.hpmax}')
        print(f'\nCurrent Stamina: {pc.stam}/{pc.stam_max}')
        if trgt_count == 1:
            for x in range(0, npc_count):
                if npc[x].hp == 0:
                    pass
                else:
                    print(f'You are faced by one {npc[x].name}.')
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
                        print(f'You make an attack against the {npc[x].name}, with your {pc.wpn_equip}.')
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
                print(f'\nThe {npc[x].name}(${x+1}), swings at you with their {npc[x].wpn_equip}.')
    
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