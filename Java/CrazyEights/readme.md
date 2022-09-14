## Crazy Eights

### Description
This folder contains classes necessary to play a command line version of the game Crazy Eights between a human player and a computer. 
In Crazy Eights players take turn playing a card that match either the suit or number of the current faceup card. If the player plays an
eight, they can change the suit. Whoever runs out of cards first wins!

### Classes
**Card:**
 Models a card. Contains accessor methos getRank() and getSuit() that return the respective rank and suit of 
the card on which the method is called. Also has a toString() method which returns a human readable version of the card.

**Deck:**
 Models a deck of cards. First the deck is populated with 52 card objects. Method canDeal() returns a boolean that states 
whether or not there are cards left to deal in the deck. The method shuffle() shuffels the deck by switching two random cards
1000 times. The toString() method displays the cards in the deck in a human readable format.

**Player:**
 Models the human player. The player is prompted to choose a card to play. Error messages are returned if the card is not playable 
until the player plays a playable card. Contains methods to deal hand, remove card from hand, 
and give game directions.

**Game:**
 Models a game of Crazy Eights. The end() method returns a boolean that tells the program if the game is over. The play() method
has all of the functionality necessary to play a game of Crazy Eights. While end() returns false, the computer and player are
prompted to take turns until one of the end conditions are met. 

**CrazyEights:**
 Calls the play() method to play a game of Crazy Eights until the user states they are done playing.

