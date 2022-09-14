/**
 * This class represents the Odd-Even game
 * 
 * @author srf2156
 */
import java.util.Scanner;

public class Game{
    private boolean p1IsHuman; 
    private boolean p2IsHuman;
    private int p1Score;
    private int p2Score;
    private Scanner scanner;
    private ComputerPlayer p1;
    private ComputerPlayer p2;
    private int total;
    private int humanPlay;
    private int computerPlay;
    private boolean run = true;
    
/* this version of the game constructor is for Part 1
 * it takes no parameters */
    public Game(){
        assignPlayer();
        play();
        announceWinner();
    }

    
/* this version of the game constructor is for Part 2
 * It requires two doubles as parameters. You will use 
 * these to set the initial thresholds for you computer players */
    public Game (double t1, double t2){
        p1 = new ComputerPlayer(t1);
        p1IsHuman = false;
        p2 = new ComputerPlayer(t2);
        p2IsHuman = false;

    }
    
/* this version of the play method is for Part 1
 * It takes no parameters and should play the interactive
 * version of the game */
    public void play(){
        while (run == true) {
            playHuman();
            if (humanPlay == 1 || humanPlay == 2) {
                if (p1IsHuman) {
                    p2.playComputer();
                    computerPlay = p2.computerPlay;
                } else {
                    p1.playComputer();
                    computerPlay = p1.computerPlay;
                }

                int total = humanPlay + computerPlay;
                if (total % 2 == 0) {
                    addP2Score(total);
                } else {
                    addP1Score(total);
                }
            } else {
                run = false;
            }
        }
    }
    
    
/** this version of the play method is for Part 2
 * It takes a single int as a parameter which is the
 * number of computer vs. computer games that should be played */
    public void play(int games){
        int i = 0;
        while (i < games) {
            p1.playComputer();
            p2.playComputer();
            int total = p1.computerPlay + p2.computerPlay;
            
            if(total % 2 == 0) {
                p2.addScore(total);
                p1.subtractScore(total);
            } else {
                p2.subtractScore(total);
                p1.addScore(total);
            }
            i += 1;

        }

    }

/* this method should return the current score (number of tokens)
 * that player 1 has */
    public int getP1Score(){
        if (p1IsHuman) {
            return p1Score;
        } else {
            return p1.getScore();
        }    
    }
    
/* this method should return the current score (number of tokens)
 * that player 2 has */
    public int getP2Score(){
        if (p2IsHuman) {
            return p2Score;
        } else {
            return p2.getScore();
        } 
    }  
    private void addP1Score(int total) {
        
        if (p1IsHuman == false) {
            p1.addScore(total);
            p2Score = p2Score - total;
        } else {
            p1Score = p1Score + total;
            p2.subtractScore(total);
        }

    }

    private void addP2Score(int total) {
        if (p1IsHuman == false) {
            p2Score = p2Score + total;
            p1.subtractScore(total);
        } else {
            p2.addScore(total);
            p1Score = p1Score - total;
        }

    }
    
    
    // you may or may not want more methods here:

/* this method assigns player numbers*/
    public void assignPlayer() {
        p1IsHuman = false;
        p2IsHuman = false;
        // take user input to determine their player
        System.out.println("Please choose a player by entering 1 or 2.");
        scanner = new Scanner(System.in);
        int playerNumber = scanner.nextInt();

        // assign the computer to whichever player the user doesn't want
        if (playerNumber == 1) {
            p2 = new ComputerPlayer(0.5);
            p1IsHuman = true;
            p1Score = 0;
        } 
        if (playerNumber == 2) {
            p1 = new ComputerPlayer(0.5);
            p2IsHuman = true;
            p2Score = 0;
        }
    }

    public void playHuman() {
        System.out.println("Hi human! Would you like to play a 1 or a 2?");
        scanner = new Scanner(System.in);
        humanPlay = scanner.nextInt();
    }

    public void announceWinner() {
        System.out.println("Player 1: " + getP1Score());
        System.out.println("Player 2: " + getP2Score());

        if (getP1Score() > getP2Score()) {
            System.out.println("Player 1 wins!");
        } else if (getP1Score() < getP2Score()){
            System.out.println("Player 2 wins!");
        } else {
            System.out.println("It's a draw!");
        }
    }
    
    
}
