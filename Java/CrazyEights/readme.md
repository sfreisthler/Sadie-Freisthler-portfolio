## Crazy Eights

### Description
This folder contains classes necessary to play a command line version of the game crazy eights.

### Classes
**Card**
Models a card. Contains accessor methos getRank() and getSuit() that return the respective rank and suit of 
the card on which the method is called. Also has a toString() method which returns a human readable version of the card.

**Deck**
Models a deck of cards. First the deck is populated with 52 card objects. Method canDeal() returns a boolean that states 
whether or not there are cards left to deal in the deck. The method shuffle() shuffels the deck by switching two random cards
1000 times. The toString() method displays the cards in the deck in a human readable format.

**Player**
Models the human player. The player is prompted to choose a card to play. Error messages are returned if the card is not playable 
until the player plays a playable card. Contains methods to deal hand, remove card from hand, 
and give game directions.

**Game**
Models a game of crazy eights. The end() method returns a boolean that tells the program if the game is over. The play() method
has all of the functionality necessary to play a game of crazy eights. While 

**CrazyEights**



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
