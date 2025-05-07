import time
import random

suits = ['C', 'D', 'H', 'S' ]
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'] 

def deck(): #builds deck
    full_deck = []
    
    for r in ranks:
        for s in suits:
            full_deck.append(s + r)
    
    return full_deck

def draw(deck, num): #deck already shuffled
    for _ in range(num):
        del deck[-1]
        
    return deck

def shuffle(deck):
    d = random.shuffle(deck)
    return d
    
def ranking(cards):
    royal_flush1 = {"AC", "KC", "QC", "JC", "TC"}
    royal_flush2 = {"AH", "KH", "QH", "JH", "TH"}
    royal_flush3 = {"AD", "KD", "QD", "JD", "TD"}
    royal_flush4 = {"AS", "KS", "QS", "JS", "TS"}
    s = set()
    r = set()
    '''
    r = {}
    r['C'] = 0
    r['S'] = 0
    r['H'] = 0 
    r['D'] = 0
    '''
    

    
    for c in cards:
        r.add(c[0])
        s.add(c[1])
        

    if royal_flush1.issubset(set(cards)) or royal_flush2.issubset(set(cards)) or royal_flush3.issubset(set(cards)) or royal_flush4.issubset(set(cards)): 
        print("yuh")
    
    
    
    print(cards)
    print(f"s : {s}")
    print(f"r: {r}")

'''
d = deck()

print(len(d))

d_new = draw(d, 2)

print(d_new)
print(len(d_new))
            
    
if ["a", "k"] in ["k", "a"]:

    print("yuh")
    
'''

ranking(["AC", "JC", "TC", "7S", "KC", "QC", "8S"])
