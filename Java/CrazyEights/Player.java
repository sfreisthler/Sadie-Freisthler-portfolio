/** Player.java
*   Author: Sadie Freisthler
*   
*   Player class as part of Crazy Eights
*   To be used with Game, Card, Deck classes
*
*/

import java.util.ArrayList;
import java.util.Scanner;

class Player{
    
    private ArrayList<Card> hand; // the player's hand
    private Scanner input;

    public Player(){
        hand = new ArrayList<Card>();
        input = new Scanner(System.in);

    }

    // Adds a card to the player's hand
    public void addCard(Card c){
        hand.add(c);
    }
   
    // Covers all the logic regarding a human player's turn
    // public so it may be called by the Game class
    public Card playsTurn(Deck deck, Card faceup, char suit){
        Card cardPlayed = null;
        String printableSuit = printableSuit(suit);

        System.out.println(directions(faceup, printableSuit));
        String userInput = input.nextLine();

        while (userInput.equals("draw") && deck.canDeal() == true) {
            // draws a card
            addCard(deck.deal());

            System.out.println(directions(faceup, printableSuit));
            userInput = input.nextLine();
        }

        if (deck.canDeal() == false) {
            cardPlayed = null;
        } else {
            int index = Integer.parseInt(userInput);
            cardPlayed = hand.get(index-1);
            while (canPlay(faceup, suit, cardPlayed) == false) {
                System.out.println("You cannot play that card, please try again.");
                System.out.println(directions(faceup, printableSuit));
                userInput = input.nextLine();

                while (userInput.equals("draw") && deck.canDeal() == true) {
                    addCard(deck.deal());
                    System.out.println(directions(faceup, printableSuit));
                    userInput = input.nextLine();
                }
                index = Integer.parseInt(userInput);
                cardPlayed = hand.get(index-1);
            }

            removeCard(index-1); 
        }

        return cardPlayed;
    }

    
    // Accessor for the players hand
    public ArrayList<Card> getHand(){
        return hand;
    }

    // Returns a printable string representing the player's hand
    public String handToString(){
        String handDescription = "";
        for (int i = 0; i < hand.size(); i++) {
            String s = Integer.toString(i+1);
            handDescription += s;
            handDescription += "\t";
            handDescription += hand.get(i).toString();
            handDescription += "\n";
        }
        return handDescription;
    }

    // removes card from player hand
    public void removeCard(int i) {
        hand.remove(i);
    }

    // deals player hand
    public void dealHand(Deck deck) {
        for (int i = 0; i < 7; i++) {
            addCard(deck.deal());
        }
    }

    // makes suit into printable format
    public String printableSuit(char suit) {
        String suitString = "";
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
        return suitString;
    }

    private boolean canPlay(Card faceup, char suit, Card play) {
        boolean canPlay = true;
        if (play.getRank() == faceup.getRank() || play.getSuit() == suit || play.getRank() == 8) {
            canPlay = true;
        } else {
            canPlay = false;
        }

        return canPlay;
    }
    
    private String directions(Card faceup, String printableSuit) {
        String directions = "";
        directions += "\n";
        directions += handToString();
        directions += "\n---------- The 'up' card is a " + faceup + " ----------";
        directions += "\nThe current suit is " + printableSuit + ".\n";
        directions += "Type 'draw' to draw a card or type the corresponding number of the card you would like to play!";

        return directions;
    }

    


// you will likely wish to have several more helper methods to simplify
// and shorten the methods above.

} // end
