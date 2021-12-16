import random
craps = [2,12,3]
points = [7,11]
def turn():
    """method that will take one roll of the dice
    and returns an array of the two numbers rolled from the dice"""
    #roll method
    dice = [1,2,3,4,5,6]
    # dicerollnumber = 0
    
    schema = []
    for i in range(2):
        fizz = random.choice(dice)
        # print(f'rolling {fizz}')
        schema.append(fizz)
        # dicerollnumber += fizz
    #check the output of the two dice
    # print( schema)
    return schema
# turn()  

def opencraps(schema):
    """method to check for dupicates
    PARAMS: schema : List 
    RETURNS : Bool """
    if schema[0] == schema[1]:
        ck = schema[0] + schema[1]
        if ck == craps[0] or ck == craps[1] or ck == craps[2]:
            return True
    else:return False      
opencraps(turn()) 

def addDice(arrLen2Int):
    """function that adds the values of two dice
    _____________________________________________________________________
    SYNTAX : sum = addDice(listWithALengthOfTwoIntegers)
    _____________________________________________________________________
    PARAMS (1): arrLen2Int : literally an array with a length of two integers
    _____________________________________________________________________
    
    RETURN : sum : the added value of both dice
    """
    sum = 0
    for i in arrLen2Int:
        sum += i
    return sum  


