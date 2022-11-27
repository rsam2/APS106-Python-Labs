##############################
# APS106 Winter 2022 - Lab 6 #
##############################

import random
from itertools import combinations

#####################################
# HELPER FUNCTIONS TO HELP PLAY THE
# GAME - NO NEED TO EDIT THESE
#####################################

def generate_deck():
    """
    (None) -> [[suit, number],[suit,number], ...]

    Create a standard deck of cards with which to play our game.
    Suits are: spades, clubs, diamonds, hearts
    Numbers are: 1 -13 where the numbers represent the following cards:
        1  - Ace
        11 - Jack
        12 - Queen
        13 - King
        2-10 - Number cards
    """

    deck = []
    suits = ['spades','clubs','diamonds','hearts']

    for suit in suits:
        for number in range(1,14):
            deck.append([suit,number])

    return deck

def shuffle(deck):
    """
    (list) -> list

    Produce a shuffled version of a deck of cards. This should shuffle a deck
    containing any positive number of cards.

    Note, this function should return a new list containing the shuffled deck
    and not directly reorder the elements in the input list. That is, the
    list contained in 'deck' should be unchanged after the function returns.
    """

    shuffled_deck = random.sample(deck,len(deck))

    return shuffled_deck

#############################
# PART 1 - Deal card
#############################

def deal_card(deck,hand):
    """
    (list,list) -> None

    Deal a card from the first element in the deck list and add it to the list
    representing the player's hand. Both list input parameters
    are nested lists with each element in the list being a two-element
    list representing a card.
    
    Note that this function returns nothing! It modifies the two lists that 
    are passed in as parameters in place.

    """
    card = deck.pop(0)                  # pop the first card off the deck and store it in a variable
    hand.append(card)                   # append the popped card onto the end of the hand list

#############################
# PART 2 - Score Hand
#############################

def score_hand(hand):
    """
    (list) -> int

    Calculate the cribbage score for a hand of five cards. The input parameter
    is a nested list of length 5 with each element being a two-element list
    representing a card. The first element for each card is a string defining
    the suit of the card and the second element is an int representing the 
    number of the card.
    """
    
    points = 0
    list_hand_values = [] 
    
    # initialize dictionaries to keep track of number of each suit and number of each value
    num_suits = {"hearts":0, "spades":0, "clubs":0, "diamonds":0}               
    num_values = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
    
    # update dictionary with tally of each suit
    # loop through each card in the hand and compare the suit to each key in the dicitonary, if they match add 1 to the tally for that suit in the dicitonary
    for i in range(len(hand)):
        for suit in num_suits:
            if hand[i][0] == suit:
                num_suits[suit] += 1
     
    # update dictionary with tally of each value 
    # loop throgh each card in the hand and compare the value to each key in the value dicitonary, if they are the same, add 1 to the tally for that value in the dictionary            
    for j in range(len(hand)):
        for value in num_values:
            if hand[j][1] == value:
                num_values[value] += 1
                
                
                
                
                
                
    
    # add points according to the number of pairs of one value there are
    # loop through each VALUE in the values dictionary, if the number of values is 2, add 2 points, if the number of values is 3, add 6 points, if the number of values is 4, add 12 points 
    for value_count in num_values.values():
        if value_count == 2:
            points += 2
        if value_count == 3:
            points += 6
        if value_count == 4:
            points += 12  
            
            
            
            
            
            
            
    # add points according to the number of a certain suit there are        
    # loop through each VALUE in the suits dictionary, if any value in the dictionary is 4 or 5, add 4 or 5 points respectively
    for suit_count in num_suits.values():
        if suit_count == 4:
            points += 4
        if suit_count == 5:
            points += 5
                
    
    
    
    
    
    
    
    # add points according to straights and 15 count
    
    # create list of values in hand
    for p in range(len(hand)):
        list_hand_values.append(hand[p][1])
    
    # get all combinations of values
    list_hand_values_combos_two = list(combinations(list_hand_values, 2))
    list_hand_values_combos_three = list(combinations(list_hand_values, 3))
    list_hand_values_combos_four = list(combinations(list_hand_values, 4))

    # convert tuples in combinations list to lists
    for y in range(len(list_hand_values_combos_two)):
        list_hand_values_combos_two[y] = list(list_hand_values_combos_two[y])
    for y in range(len(list_hand_values_combos_three)):
        list_hand_values_combos_three[y] = list(list_hand_values_combos_three[y])
    for y in range(len(list_hand_values_combos_four)):
        list_hand_values_combos_four[y] = list(list_hand_values_combos_four[y])
    
    # sort the elements of each nested list to be in ascending order
    for z in range(len(list_hand_values_combos_two)):
        list_hand_values_combos_two[z] = sorted(list_hand_values_combos_two[z])
    for z in range(len(list_hand_values_combos_three)):
        list_hand_values_combos_three[z] = sorted(list_hand_values_combos_three[z])
    for z in range(len(list_hand_values_combos_four)):
        list_hand_values_combos_four[z] = sorted(list_hand_values_combos_four[z])

    list_hand_values = sorted(list_hand_values)

    # set a value to change if there are consecutive numbers in the 5 or 4 number combinations
    condition = 1
    
    # check all 5 values are consecutive, if they are, increase number of points, change value of condition to prevent next if statement from running
    if condition == 1:
        n = list_hand_values[0]
        if (list_hand_values[1] == n+1) and (list_hand_values[2] == n+2) and (list_hand_values[3] == n+3) and (list_hand_values[4] == n+4):
            points += 5
            condition -= 1
        for w in range(len(list_hand_values)):
            if (list_hand_values[w] == 11) or (list_hand_values[w] == 12) or (list_hand_values[w] == 13):
                list_hand_values[w] = 10
                
    # loop through each element in the combinations of 4 numbers list to check of any of them contain consective numbers, if they do, increase the number of points and chaneg value of condition 
    if condition == 1:
        for x in range(len(list_hand_values_combos_four)):
            n = list_hand_values_combos_four[x][0]
            if (list_hand_values_combos_four[x][1] == n+1) and (list_hand_values_combos_four[x][2] == n+2) and (list_hand_values_combos_four[x][3] == n+3):
                points += 4
                condition -= 1
            
            # check if value at position is king queen or jack, change value to 10 if its true to calculate 15 count
            for y in range(len(list_hand_values_combos_four[x])): 
                if (list_hand_values_combos_four[x][y]) == 11 or (list_hand_values_combos_four[x][y]) == 12 or (list_hand_values_combos_four[x][y]) == 13:
                    list_hand_values_combos_four[x][y] = 10
           
    # loop through each element in combinations of 3 numbers list to check oif any of them contain consecutive numbers, increase the number of points accordingly            
    if condition == 1:
        for y in range(len(list_hand_values_combos_three)):
            n = list_hand_values_combos_three[y][0]
            if (list_hand_values_combos_three[y][1] == n+1) and (list_hand_values_combos_three[y][2] == n+2):
                points += 3
                
            # check if value at position is king queen or jack, change value to 10 if its true to calculate 15 count
            for z in range(len(list_hand_values_combos_three[y])):
                if (list_hand_values_combos_three[y][z] == 11) or (list_hand_values_combos_three[y][z] == 12) or (list_hand_values_combos_three[y][z] == 13):
                    list_hand_values_combos_three[y][z] = 10   
    
    for y in range(len(list_hand_values_combos_two)):
        for z in range(len(list_hand_values_combos_two[y])):
            if (list_hand_values_combos_two[y][z] == 11) or (list_hand_values_combos_two[y][z] == 12) or (list_hand_values_combos_two[y][z] == 13):
                list_hand_values_combos_two[y][z] = 10
                
    # loop through each combination of 3, 4, and 5 to see if the sum of values is equal to 15
    for x in list_hand_values_combos_two:
        if sum(x) == 15:
            points += 2
            
    for x in list_hand_values_combos_three:
        if sum(x) == 15:
            points += 2
        
    for y in list_hand_values_combos_four:
        if sum(y) == 15:
            points += 2
        
    if sum(list_hand_values) == 15:
        points += 2
    
    
    
    
    return points


################################
# PART 3 - PLAY
################################

def play(shuffled_deck):
    """
    (list) -> [str, int, int]
    
    Function deals cards to players, computes player scores, and
    determines winner.
    
    Function retuns a three-element list where the first element is a string
    indicating the winner, the second element is an int specifying player\'s
    score, and the third element is an int specifying dealer\'s score.
    """
    player_hand = []
    dealer_hand = []
    
    # add cards to each hand, loop through range 1-10, if number is odd, add to deealer's hand, else add to player's hand
    for card in range(1,11):
        if card % 2 == 0:
            deal_card(shuffled_deck, player_hand)
        else:
            deal_card(shuffled_deck, dealer_hand)
            
    # calculate score using previously defined functions
    player_score = score_hand(player_hand)
    dealer_score = score_hand(dealer_hand)
    
    # check who won by using if else statements and comparing score
    if player_score > dealer_score:
        verdict = "player wins"
    elif player_score == dealer_score:
        verdict = "dealer wins"
    else:
        verdict = "dealer wins"
        
    results = [verdict, player_score, dealer_score]
    
    return results
    
