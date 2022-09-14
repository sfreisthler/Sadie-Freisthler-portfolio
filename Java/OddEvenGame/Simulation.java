/**
 * This class should run simulations to determine
 * whether or not the Odd-Even game is fair and if
 * not who has the advantage and what is a strategy
 * that will realize that adavantage.
 * 
 * @author srf2156
 */


public class Simulation{ 
    
    public static void main(String[] args){ 
        // found on educative.io
        double maxMin = Integer.MIN_VALUE;
        double player1Ratio = 0;

        for(double i=0; i<1.02; i += 0.02) {
            // found on educative.io
            double rowMin = Integer.MAX_VALUE;
            double currentPlayer1Ratio = i;
            for(double j=0; j<1.02; j += 0.02) {
                Game g = new Game(i,j);
                g.play(100000);
                double currentMin = g.getP1Score() / 100000.0;
                if (currentMin < rowMin) {
                    rowMin = currentMin;
                }
            }

            if (rowMin > maxMin) {
                maxMin = rowMin;
                player1Ratio = currentPlayer1Ratio;
            }
        }
        if (maxMin > 0) {
            System.out.println("Player 1 (odd) has an advantage!");
            System.out.println(player1Ratio);
        }

    }
}
