## Odd/Even Game

### Description
This is a two player game. Each player simultaneously declares "one" or "two". Player 1 wins if the sum of the two numbers is odd and Player 2 wins if the sum of the two numbers is even. In either case the loswer is obligated to pay the winner (in tokens) the sum of the two declared numbers. Scores are cumulative across rounds.

### Classes

**ComputerPlayer:**
This class models the computer player in the game. It contains mutator methods to alter the score of the computer, addScore() and subtractScore(), and an accessor method, getScore() to return the computer's score. The playComputer() method determines if the computer throws a 1 or a 2 depending on a given threshold using Math.random().

**Simulation:**
The goal of the simulation class is to find which player, even or odd, has an advantage and at which threshold value of t. The result shows that Player 1 (odd) has an advantage at a threshold t value of 0.58.

**Game:**
In the game class, the human player can choose if they want to be even or odd through the assignPlayer() method. The method announceWinner() gets both scores and prints the winner to the console. 
