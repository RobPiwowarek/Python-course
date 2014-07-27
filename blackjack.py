# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
wins = 0
loses = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.list = []

    def __str__(self):
        string = ""
        i = 0
        while i < len(self.list):
            string += str(self.list[i].get_suit()) + str(self.list[i].get_rank()) + " "
            i += 1
            
        return string

    def add_card(self, card):
        self.list.append(card)

    def get_value(self):
        hand_score = 0
        for i in self.list:
            if i.get_rank() != 'A':
                hand_score += VALUES[i.get_rank()]
            else:
                hand_score += VALUES[i.get_rank()]
                
        for i in self.list:
            if i.get_rank() == 'A':
                if hand_score + 10 <= 21:
                    hand_score += 10
                
        return hand_score
   
    def draw(self, canvas, pos):
        j = 0
        for i in self.list:
            i.draw(canvas,(pos[0]+j,pos[1]))
            j += 73
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                c = Card(suit,rank)
                self.deck.append(c)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop(0)
    
    def __str__(self):
        string = ""
        for i in self.deck:
            string += str(i.get_suit)+str(i.get_rank)+" "
            
        return string

#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, loses, score
    i = 0
    
    if in_play == True:
        outcome = "New deal while game in progress. Player Loses" 
        loses += 1
        score = wins - loses
        in_play = False
    
    deck = Deck()
    deck.shuffle()
    dealer_hand = Hand()
    player_hand = Hand()
    
    while i < 2:
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        i += 1
    
    in_play = True

def hit():
    global in_play, wins, loses, score, outcome
    if in_play == True:
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())
            if player_hand.get_value() > 21:
                outcome = "You have busted!"
                loses += 1
                in_play = False
                score = wins - loses
       
def stand():
    global wins, loses, score, in_play, outcome
    if in_play == False:
        pass
    else:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())    
        
        if player_hand.get_value() <= dealer_hand.get_value():
            if dealer_hand.get_value() > 21:
                outcome =  "Player wins!"
                in_play = False
                wins += 1
            else:
                outcome =  "Dealer wins!"
                loses += 1
                in_play = False
        else:
            if player_hand.get_value() > 21:
                outcome =  "Dealer wins!"
                loses += 1
                in_play = False
            else:
                outcome = "Player wins!"
                wins += 1
                in_play = False

    score = wins - loses
    
# draw handler    
def draw(canvas):
    player_hand.draw(canvas, (100,400))
    dealer_hand.draw(canvas, (100,75))
    canvas.draw_text("Blackjack", (225, 50), 40, "Black")
    if in_play == False:
        canvas.draw_text(outcome, (225, 250), 30, "White")
        canvas.draw_text("New deal?", (225, 300), 30, "Black")
    else:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (100+CARD_BACK_CENTER[0],75+CARD_BACK_CENTER[1]), CARD_BACK_SIZE)
        canvas.draw_text("Hit or stand?", (225, 300), 30, "Black")
        
    canvas.draw_text("Score: " + str(score), (425, 300), 30, "Black")
        
player_hand = Hand()
dealer_hand = Hand()
deck = Deck()
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()