
/** Card.java
*   Author: Sadie Freisthler
*   
*   
*   Models a typical playing card
*
*/

class Card{
    
    private char suit;
    private int rank;

    // Initializes a card instance
    public Card(char suit, int rank){
        this.suit = suit;
        this.rank = rank;
    }

    // Accessor for suit
    public char getSuit(){
        return suit;
    }

    
    // Accessor for rank
    public int getRank(){
        return rank;
    }

    // Returns a human readable form of the card (eg. King of Diamonds)
    public String toString(){
        String suitString = "";
        String[] rankString = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"};

        // Use switch statement to assign respective suits to suitString
        switch(suit) {
            case 's': suitString = "Spades";
                    break;
            case 'h': suitString = "Hearts";
                    break;
            case 'd': suitString = "Diamonds";
                    break;
            case 'c': suitString = "Clubs";
                    break;
        }

        String cardDescription = rankString[rank-1] + " of " + suitString;
        return cardDescription;
    }
}
