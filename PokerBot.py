import time
import random

suits = ['C', 'D', 'H', 'S' ]
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'] 
values = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13}



T = 10

def deck(): #builds deck
    full_deck = []
    
    for r in ranks:
        for s in suits:
            full_deck.append(r+s)
    

    return full_deck

def draw(deck, num): #deck already shuffled
    drawn_cards = []
    for _ in range(num):
        drawn_cards.append(deck[-1])
        del deck[-1]
    return deck, drawn_cards



    
def ranking(hole, comm): #returns a number based on what the win condition is 
    cards = hole + comm
    royal_flush1 = {"AC", "KC", "QC", "JC", "TC"}
    royal_flush2 = {"AH", "KH", "QH", "JH", "TH"}
    royal_flush3 = {"AD", "KD", "QD", "JD", "TD"}
    royal_flush4 = {"AS", "KS", "QS", "JS", "TS"}
    straight_flush = {"A", "2", "3", "4", "5"}
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
    
 

    if royal_flush1.issubset(set(cards)) or royal_flush2.issubset(set(cards)) or royal_flush3.issubset(set(cards)) or royal_flush4.issubset(set(cards)): 
        return 10
        
    elif r_vals == [1, 1, 1, 4] :
        return 8
    
    elif r_vals == [1, 1, 2, 3]:
        return 7
    
    elif s['C'] == 5 or s['H'] == 5 or s['D'] == 5 or s['S'] == 5:
        count = 0
        for ind in sorted(r):
            if count == 0:
                old = values[ind]
                count += 1
            else:
                if values[ind] != old + 1:
                    break
            old = values[ind]
            count += 1
        
        if count == 5 or straight_flush.issubset(r):
            return 9
        else:
            return 6
        
    elif r_vals == [1, 1, 1, 1, 3]:
        return 4
        
    elif r_vals == [1, 1, 1, 2, 2]:
        return 3
    
    elif r_vals == [1, 1, 1, 1, 1, 2]:
        return 2
        
    else:
        count = 0
        for ind in sorted(r):
            if count == 0:
                old = values[ind]
                count += 1
            else:
                if values[ind] != old + 1:
                    break
            old = values[ind]
            count += 1
            
        if count > 5 or straight_flush.issubset(r): 
            return 5
        else:
            return 1


def simulate(my_cards, community):
    #start timer
    start_time = time.time()
    win = 0
    tie = 0
    all_games = 0
    

    if community == []:
        known = set(my_cards)
    else:
        known = set(my_cards + community)
    

    
    while(time.time()-start_time < 10):
        sim_deck = deck()
        
        random.shuffle(sim_deck)

        
        for k in known:
            sim_deck.remove(k)
        
        sim_deck, opp_cards = draw(sim_deck, 2)
        sim_deck, comm_cards = draw(sim_deck, 5-len(community))
        all_comm_cards = community + comm_cards
        
        
        opp_rank = ranking(opp_cards, all_comm_cards)
        my_rank = ranking(my_cards, all_comm_cards)
        
        if my_rank>opp_rank:
            win += 1
        elif my_rank == opp_rank:
            tie += 1
        all_games += 1
    
    return ((win + (0.5 * tie))/all_games)
        
  



def main():
    the_deck = deck()
    random.shuffle(the_deck)
    community = []

    the_deck, my_hole = draw(the_deck, 2)
    
    print(f"game starts! your cards are {my_hole}")
    if simulate(my_hole, community) >= 0.5:
        print("stay")
    else:
        print("fold, you lost :(")
        exit()

    the_deck, community = draw(the_deck, 3)
    if simulate(my_hole, community) >= 0.5:
        print("stay")
    else:
        print("fold, you lost :(")
        exit()

    the_deck, new = draw(the_deck, 1)
    community = community + new

    if simulate(my_hole, community) >= 0.5:
        print("stay")
    else:
        print("fold, you lost :(")
        exit()

    the_deck, new = draw(the_deck, 1)
    community = community + new
    
    
    the_deck, opp_hole = draw(the_deck, 2)
    
    opp_rank = ranking(opp_hole, community)
    my_rank = ranking(my_hole, community)
    
    if opp_rank > my_rank:
        print("opponent wins :( )")
    else:
        print("you won! :D")
    


    
main()

