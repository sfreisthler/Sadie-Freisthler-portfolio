Card class

The card class has accessor methods getRank() and getSuit() which returns the respective rank or suit of
the card on which the method is called. There is also a toString() method which returns a human readable 
version of the card. I used a switch statement to assign the names of the suit based on the char in the suit 
variable. I used an array with all of the different card rank values and indexed this array to get the human
readable versions of the suits. 


Deck class

The deck class starts by instantiating the variable for deck, char, and suits. Then I populated the deck
with all of the cards using nested for loops to iterate through all of the possible suits and ranks. The deal()
method deals the top card of the deck by first increasing the variable top by one and then returning the top card
of the deck. The method canDeal() returns a boolean that states whether or not there are cards left in the deck 
to deal. The method shuffle() shuffles the deck by switching two random cards in the deck one thousand times.
Finally, the toString() method makes sure that the deck is in human readable format by iterating through all of
the cards in the deck and adding them to a string for deck description. This string is then returned.


Player class

The addCard() method adds a card to the hand. In the playsTurn() method, the Card, cardPlayed, is instantiated
and the method directions() is called to print the current card and suit. User input is then taken. While the 
user's input is equal to "draw" cards are added to the player's hand. After this while loop is broken, if the 
deck is out of cards the variable cardPlayed is set equal to null. Else, the user's input is converted to an 
integer and the cardPlayed is set equal to the card at that index of the player's hand. I used a method canPlay()
to check whether the card is a valid play. While canPLay() is equal to false. The player is told that they 
cannot play that card and they are then prompted to choose another card. While this input is equal to "draw"
cards are added to the player's hand. Finally when they input a valid play, the card is removed from their hand
and returned. 



Game class

The game class starts by instantiating the variables for the player hand, computer hand, deck, and scanner. 
Then the cards are shuffled and the player and computer hands are dealt. The faceup and currentSuit variables
are also assigned. The play() method contains the code required to play a round of crazy eights and returns a 
boolean that controls if another round is played in CrazyEights.java. First there is a method rules() which 
prints out the rules of the game. The while the method end() is equal to false, the following occurs. The faceup 
variable is assigned to the value of the card returned from the player's turn. If this value does not equal
null, then the current suit is set to the suit of the card the player played. Here, the method checks to see if
the rank of the player's card is an 8, if so it prompts them to choose a suit. Then the computerTurn() method is
called and the computer plays. Finally this method returns the playAgain() method which returns a boolean based off
of player input.

In the computerTurn() method I instantiated variables for playableCard, currentCard, and i. I then iterated
through the computer's cards and as soon as one of the cards was playable I set playableCard equal to true
which breaks the while loop. The variables faceup and currentSuit are then set to their respective values. If 
this card is an 8 I used another method called generateSuit() to generate a random suit. If the deck runs out of
cards I set the variable currentCard to null. Finally, if the computer doesn't have any playable cards it draws
until it gets a card it can play. 

The playAgain() method controls whether or not the user plays again. When called, the user is prompted to 
enter 'q' to quit. If the user inputs 'q' playAgain() is set to false and the game is over. If anything else
is entered the user plays again. 

The end() method is a method that controls the ending conditions for a game. It returns a boolean true or false.
If any of the end conditions are met for crazy eights it returns false. For example, if either of the players' hands
have 0 cards or the deck is out of cards false is returned.