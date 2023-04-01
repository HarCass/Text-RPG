from player import PC
from encounters import e1, e2, e3, e4

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
