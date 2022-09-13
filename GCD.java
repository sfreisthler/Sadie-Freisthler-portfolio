/**
 * Class containing methods that find the GCD of two numbers
 * @author Sadie Freisthler
 * @version 1.0
 */

public class GCD {
    /**
     * Returns the GCD of two numbers calculated iteratively.
     * @param m First parameter for GCD
     * @param n Second parameter for GCD
     * @return GCD of two numbers
     */
    public static int iterativeGcd(int m, int n) {

        while ( n != 0) {
            int c = m % n;
            m = n;
            n = c;
        }

        return m;

    }
    /**
     * Returns the GCD of two numbers calculated recursively.
     * @param m First parameter for GCD
     * @param n Second parameter for GCD
     * @return GCD of two numbers
     */
    public static int recursiveGcd(int m, int n) {
        return (n!=0 ? recursiveGcd(n, m % n): m);
    }

    /**
     * Demonstrates iterativeGcd() and recursiveGce()
     * @param args
     *
     */

    public static void main(String[] args) {
        // if the number of arguments given isn't correct print an error
        if (args.length != 2) {
            System.out.println("Usage: java GCD <integer m> <integer n>");
            System.exit(1);
        } else {
            // try to parse the first argument to an integer
            try {
                int arg0 = Integer.parseInt(args[0]);
                // try to parse the second argument to an integer
                try {
                    int arg1 = Integer.parseInt(args[1]);
                    // if both arguments are 0 print an error
                    if (arg0 == 0 & arg1 == 0) {
                        System.out.println("gcd(0, 0) = undefined");
                        System.exit(0);
                    } else {

                        //handle negative numbers and order
                        int m = Math.abs(arg0);
                        int n = Math.abs(arg1);

                        if (n > m) {
                            int c = m;
                            m = n;
                            n = c;
                        }

                        // calculate and print results
                        int iterativeAnswer = iterativeGcd(m, n);
                        int recursiveAnswer = recursiveGcd(m, n);

                        System.out.println("Iterative: gcd(" + arg0 + ", " + arg1 + ") = " + iterativeAnswer);
                        System.out.println("Recursive: gcd(" + arg0 + ", " + arg1 + ") = " + recursiveAnswer);
                        System.exit(0);
                    }
                } catch (NumberFormatException nfe) {
                    System.out.println("Error: The second argument is not a valid integer.");
                    System.exit(1);
                }
            } catch (NumberFormatException nfe) {
                System.out.println("Error: The first argument is not a valid integer.");
                System.exit(1);

            }
        }
    }

}
