import time
import random

suits = ['C', 'D', 'H', 'S' ]
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'] 

values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

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


def simulate(my_cards, community):
    #start timer
    
    known = set(my_cards + community)
    
    #timer
    
    #create and shuffle a deck, check that deck doesn't have duplicates
    
    #opponent draws cards
    #do we need more community cards? - draw and create community
    
    #rank your hand (call ranking)
    #rank opponents hand (call ranking)
    
    #evaluate who wins, update wins, ties, and total games
    
    
    
    
    
def ranking(cards): #returns a number based on what the win condition is 
    royal_flush1 = {"AC", "KC", "QC", "JC", "TC"}
    royal_flush2 = {"AH", "KH", "QH", "JH", "TH"}
    royal_flush3 = {"AD", "KD", "QD", "JD", "TD"}
    royal_flush4 = {"AS", "KS", "QS", "JS", "TS"}
    s = {}
    s['H'] = 0
    s['D'] = 0
    s['S'] = 0
    s['C'] = 0
    
    r = set()
    
    r_dict = {}
    
    
    for c in cards:
        r.add(c[0])
        s[c[1]] += 1
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
    
    elif s['C'] == 5 or s['H'] == 5 or s['D'] == 5 or s['S'] == 5:
        
        print("flush")
  
    
    #STRAIGHT
        
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



ranking(["1C", "2C", "3C", "4C", "5C", "QD", "8S"])

# in main
# create a deck
# pull two cards as your hole 
# pull two cards as their hole

# after each simulation 
# simulate - keep going if stay
# pull 3 community cards - flop
# simulate - keep going if stay
# pull 1 community card - turn
#simulate - keep going if stay
# pull 1 community card - river

# if you're still in at the end, who ever actually has a higher hand wins
# if you ever fold, you lose
