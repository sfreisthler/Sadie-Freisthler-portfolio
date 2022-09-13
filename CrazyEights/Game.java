/** Game.java
*   Author: Sadie Freisthler
*   
*   
*   Game class for playing crazy eights in commandline
*   To be used with Player, Card, Deck classes
*
*/


import java.util.Scanner;
import java.util.ArrayList;

class Game{

    private char currentSuit; // need in case an 8 is played
    private Card faceup; 
    private Scanner input;
    private Player p1;
    private ArrayList<Card> compHand;
    private Deck cards;
    
    // sets up the Game object for play
    public Game(){
        p1 = new Player();
        compHand = new ArrayList<Card>();
        cards = new Deck();
        input = new Scanner(System.in);

        // shuffle cards
        cards.shuffle();

        // deal comp hand
        for (int i = 0; i < 7; i++) {
            compHand.add(cards.deal());
        }

        // deal player hand
        p1.dealHand(cards);

        // set faceup
        faceup = cards.deal();

        // set the current suit
        currentSuit = faceup.getSuit();
    }

   

    // Plays a game of crazy eights. 
    // Returns true to continue playing and false to stop playing
    public boolean play(){
        rules();
        while (end(cards, p1) == false) {
            faceup = p1.playsTurn(cards, faceup, currentSuit);

            // set the current suit
            if (faceup != null) {
                currentSuit = faceup.getSuit();

                // if the player plays an 8, prompt them to change the suit
                if (faceup.getRank() == 8) {
                    playerSuit();
                }
                computerTurn(cards);
            }
        }
        return playAgain();
        
    }

    /* Naive computer player AI that does one of two actions:
        1) Plays the first card in their hand that is a valid play
        2) If no valid cards, draws until they can play

        You may choose to use a different approach if you wish but
        this one is fine and will earn maximum marks
     */
    private Card computerTurn(Deck deck){
        boolean playableCard = false;
        int i = 0;
        Card currentCard = null;

        while (playableCard == false && i < compHand.size()) {
            currentCard = compHand.get(i);
            if (currentCard.getSuit() == currentSuit || currentCard.getRank() == faceup.getRank()) {
                playableCard = true;
            }
            i++;    
        }

        if (playableCard == true) {
            // reassigns faceup card and removes card from computer hand
            faceup = compHand.get(i-1);
            currentSuit = faceup.getSuit();
            if (currentCard.getRank() == 8) {
                generateSuit();
            }
            compHand.remove(i-1);
        } else if (deck.canDeal() == false) {
            currentCard = null;
        } else {
            // draws card
            compHand.add(cards.deal());
            currentCard = null;
            computerTurn(cards);
        }
        return currentCard;
    }

    // prints out game rules
    private void rules() {

        String rules = "\nWelcome to Crazy Eights! You'll start with 7 cards. \n";
        rules += "Your job is to match a card in your hand with the up card. \n";
        rules += "You can match it by suit or rank. \n";
        rules += "If you play an 8, you can switch the active suit. \n";
        rules += "If you run out of cards, you win! \n";
        rules += "If you make it through the whole deck then whoever has \n";
        rules += "the fewest cards left wins! \n";
        rules += "Good luck!\n";

        System.out.println(rules);
    }

    // generates random suit for when the computer plays an eight
    private void generateSuit() {
        int randomInt = (int) (Math.random() * 4);
        char[] suits = {'c', 'd', 'h', 's'};
        char newSuit = suits[randomInt];
        currentSuit = newSuit;  
    }

    // prompts user to change the suit
    private void playerSuit() {
        System.out.println("You played an 8! Please choose a new suit (c)lubs, (h)earts,(d)iamonds, or (s)pades.");
        char userInput = input.next().charAt(0);
        currentSuit = userInput;
    }

    // asks the user if they want to play again, returns boolean
    private boolean playAgain() {
        boolean playAgain = true;
        // asks user if they would like to play again
        System.out.println("\nWould you like to play again? Type 'q' to quit.");
        String userInput = input.nextLine();
        userInput = input.nextLine();

        // checks user input against different cases and assigns boolean value
        if (userInput.equals("q")) {
            playAgain = false;
        } 
        // why does this sometimes not let the user input and just automatically play a new game?
        return playAgain;

    }

    // Checks to see if any of the end conditions have been met
    private boolean end(Deck deck, Player p1) {
        boolean end = false;
        // returns false if the player hand has 0 cards
        if (p1.getHand().size() == 0) {
            end = true;
            System.out.println("Player wins!");
        // return false if the computer hand has 0 cards
        } else if (compHand.size() == 0) {
            end = true;
            System.out.println("Computer wins!");
        // returns false if the deck is out of cards
        } else if (deck.canDeal() == false) {
            end = true;
            System.out.println("The deck has no cards left.");
            // checks size of computer and player hands to determine winner 
            if (p1.getHand().size() > compHand.size()) {
                System.out.println("Computer Wins!");
            } else if (p1.getHand().size() < compHand.size()) {
                System.out.println("Player Wins!");
            } else {
                System.out.println("It's a tie!");
            }
        }
        return end;
    }

// you will likely wish to have several more helper methods to simplify
// and shorten the methods above.


}