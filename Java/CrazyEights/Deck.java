/** Deck.java
*   Author: Sadie Freisthler
*   
*   Models a typical deck of playing cards
*   To be used with Card class
*
*/ 
import java.lang.Math;

class Deck{

    private Card[] deck; // contains the cards to play with
    private int top = 0; // controls the "top" of the deck to deal from
    public static char[] suits = {'c', 'd', 'h', 's'};

    // constructs a default Deck
    public Deck(){
        // Nested for loops to increment suit and rank to populate deck with all cards
        int count = 0;
        deck = new Card[52];
        for (int i = 1; i < 14; i++) {
            for (int j = 0; j < 4; j++) {
                deck[count] = new Card(suits[j],i);
                count++;
            }
        }
    }

    // Deals the top card off the deck
    public Card deal(){
        top++;
        return deck[top-1];
        
        // your code here
        // increment top, return top-1
    }


    // returns true provided there is a card left in the deck to deal
    public boolean canDeal(){
        if (top < 52) {
            return true;
        } else {
            return false;
        }
    }

    // Shuffles the deck
    public void shuffle(){
        for (int i = 0; i <= 1000; i++) {
            // Generate two random numbers
            double randDub1 = Math.random() * 52;
            int randNum1 = (int)randDub1;

            double randDub2 = Math.random() *52;
            int randNum2 = (int)randDub2;

            Card temp = deck[randNum1];
            deck[randNum1] = deck[randNum2];
            deck[randNum2] = temp;
        }
    }

    // Returns a string representation of the whole deck
    public String toString(){
       String deckDescription = "";
       for (int i = 0; i < 52; i++) {
           deckDescription += deck[i].toString();
           deckDescription += "\n";
       }

       return deckDescription;
    }

    // you may wish to have more helper methods to simplify
    // and shorten the methods above.
}
