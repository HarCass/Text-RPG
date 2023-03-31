import random

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