import gamelogic as gl

def game():
    """game run function"""
    #TODO 
    roll = gl.turn()
    point = []
    #first roll only
    #TODO : abstract this function out
    def firstrollisCrap():
        """check for opening craps"""
        if gl.opencraps(roll):
            print(roll)
            print( "game - over")
            return True
        #TODO : check if they rolled a 7 or 11
        elif roll[0]+roll[1] == 7 or roll[0]+roll[1] == 11:
            print(f'you scored with a {roll[0]+roll[1]}')
            return
        
        elif roll[0]+roll[1] > 3 and roll[0]+roll[1] < 11:
            point.append(roll[0]+roll[1])
        else: return False
        # subseqent rolls if they didnt crap out at the beginning
    if not firstrollisCrap():
        print(roll)
        if len(point):print(f'your point is {point[0]}')
        bet = input('would you like to bet?\n')
        if bet.lower() == 'y':
            stake = int(input('how much would you like to bet'))
            gl.craps = 7
            while  True:
                r = input('type r to roll\n')
                if r.lower()=='r':
                    ro = gl.turn()
                    print(ro)
                    if ro[0]+ro[1] != point[0] : #and ro[0]+ro[1] !=  gl.craps   
                        print(f'{ro[0]+ro[1]} chasing {point[0]}')
                    elif ro[0]+ro[1] != point[0]:
                        print('point seen')
                        return False
                    
                    if ro[0]+ro[1] == gl.craps:
                        print('crap')
                        return False
                else: return        
game()        