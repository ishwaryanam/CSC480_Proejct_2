import time
import random

suits = ['C', 'D', 'H', 'S' ]
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'] 

print(sorted(ranks))

T = 10

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
    
    r_dict = {}
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
        r_dict[c[0]] = r_dict.get(c[0], 0) + 1
    
    r_vals = r_dict.values()
    
    r_vals = sorted(r_vals)
    
    print(f"rv: {r_vals}")

    if royal_flush1.issubset(set(cards)) or royal_flush2.issubset(set(cards)) or royal_flush3.issubset(set(cards)) or royal_flush4.issubset(set(cards)): 
        print("royal flush")
        
    #STRAIGHT FLUSH
    elif r_vals == [1, 1, 1, 4] :
        print("four of a kind")
    
    elif r_vals == [1, 1, 2, 3]:
        print("full house")
    
    #FLUSH
    
    #STRAIGHT FLUSH
        
    elif r_vals == [1, 1, 1, 1, 3]:
        print("three of a kind")
        
    elif r_vals == [1, 1, 1, 2, 2]:
        print("2 pairs")
    
    elif r_vals == [1, 1, 1, 1, 1, 2]:
        print("1 pair")
        
    else:
        print("high card")
    
    
        
        
        
   
    
    
    
    print(cards)
    print(f"s : {s}")
    print(f"r: {sorted(r)}")
    print(f"r_dict: {r_dict}")

'''
d = deck()

print(len(d))

d_new = draw(d, 2)

print(d_new)
print(len(d_new))
            
    
if ["a", "k"] in ["k", "a"]:

    print("yuh")
    
'''

ranking(["1C", "1S", "1H", "2D", "2C", "QC", "8S"])
