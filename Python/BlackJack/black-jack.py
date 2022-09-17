#/usr/bin/python
# -*- coding: utf-8 -*-
# srf2156, jno2171
import random

suits = ['♠','♣','♦','♥'] # Feel free to use these symbols to represent the different suits. 
numbers = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]

numbers_to_points = {"two":2, "three": 3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10, "jack":10, "queen":10, "king":10}


class Card(object):  
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank      

    def __str__(self):
        return (f"{self.rank} {self.suit}") 

class CardCollection(object): 

    def __init__(self):
        self.cards = []

    def add_card(self, card): 
        self.cards.append(card)
        return card    

    def draw_card(self): 
        card = self.cards.pop()
        
        return card 
        

    def make_deck(self):
        for suit in range(4):
          for number in range(13):
            new_card = Card(suits[suit], numbers[number])
            self.add_card(new_card)
        random.shuffle(self.cards)
        

    def value(self):
        total = 0
        aces = 0
        for i in range(len(self.cards)):
          card = self.cards[i]
          if card.rank != "ace":
            total += numbers_to_points[card.rank]
        for i in range(len(self.cards)):
          card = self.cards[i]
          if card.rank == "ace":
            aces += 1
        if aces != 0:
          total += (aces - 1)
          if (total + 11) <= 21:
            total += 11
          else:
            total += 1
        return total


def main():
    # initialize a fresh deck 
    deck = CardCollection()
    deck.make_deck()

    player_total = 0
    player_hand = CardCollection()
    card_drawn = player_hand.add_card(deck.draw_card())
    print(f"player draws: {card_drawn}")
    player_total = player_hand.value()
    choice = 1
    while (int(choice) != 2 and player_total < 21):
      print(f"Sum: {player_total}")
      choice = input('Would you like to draw another card (type "1"), or stay (type "2")\n')
      if int(choice) == 1:
        card_drawn = player_hand.add_card(deck.draw_card())
        print(f"player draws: {card_drawn}")
        player_total = player_hand.value()
    
    if player_total == 21:
      print("Congratulations your total is 21 and you have won")
    elif(player_total > 21):
      print(f"Your total is {player_total} and you have lost")
    else:
      dealer_hand = CardCollection()
      dealer_total = dealer_hand.value()
      while dealer_total < 17:
        card_drawn = dealer_hand.add_card(deck.draw_card())
        print(f"dealer draws: {card_drawn}")
        dealer_total = dealer_hand.value()

      # compare dealer and player totals to determine winner
      if dealer_total == 21:
        print("The dealers hand equals 21, dealer wins.")
      elif dealer_total > 21:
        print(f"The dealers hand is {dealer_total} which is greater than 21, player wins.")
      elif dealer_total == player_total:
        print("Dealer and player totals are equal, tie.")
      elif(dealer_total < player_total):
        print(f"The dealers hand is {dealer_total} which is less than the players hand of {player_total}, player wins. ")
      elif (dealer_total > player_total):
        print(f"The dealers hand is {dealer_total} which is greater than the players hand, dealer wins.")
      
      
    
    # complete the main method

if __name__ == "__main__":
    main()
