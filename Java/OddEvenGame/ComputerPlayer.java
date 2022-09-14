/**
 * This class represents a computer
 * player in the Odd-Even game
 * 
 *  @author srf2156
 */

public class ComputerPlayer{
    private double t;
    private int tokenBalance;
    public int computerPlay;
    private double randomDouble;
    
    public ComputerPlayer(double threshold){
        t=threshold;
        tokenBalance=0;
    }

// this class returns the computer's token balance
    public int getScore() {
        return tokenBalance;
    }

    public void playComputer() {
        randomDouble = Math.random();
        if (randomDouble <= t) {
            computerPlay = 1;
        } else {
            computerPlay = 2;
        }
    }  

    public void addScore(int tokens) {
        tokenBalance = tokens + tokenBalance;
    }

    public void subtractScore(int tokens) {
        tokenBalance = tokenBalance - tokens;
    }
}
