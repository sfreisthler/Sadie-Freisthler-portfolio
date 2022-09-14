## Odd/Even Game

### Description
This is a two player game. Each player simultaneously declares "one" or "two". Player 1 wins if the sum of the two numbers is odd and Player 2 wins if the sum of the two numbers is even. In either case the loswer is obligated to pay the winner (in tokens) the sum of the two declared numbers. Scores are cumulative across rounds.

### Classes

**ComputerPlayer:**

**Simulation:**

**Game:**

@author srf2156

Part 1:

Game

In the Game class I added a number of extra methods on top of the ones given in the template for the project.
I created a method called assignPlayer() that allows the user to choose if they want to be odd or even and 
assigns the computer to be the other player. This method uses a two boolean variable and sets either p1IsHuman
or p2IsHuman to true depending on which player the user chooses. This boolean variable is then used in other
methods to determine what method to use or variable to reference in order to determine the scores of the players.
The method announceWinner() gets both p1 and p2's scores, determines who the winner is and prints the winner to the
console.  

ComputerPlayer

In the ComputerPlayer class, I created several methods to govern the computer's game play actions. 
There are methods to add and subtract tokens from the computer's score as well as a method to retrieve the current 
token total. In the play method, I used Math.random() to generate a random double and had the computer either throw 
a one or a two depending on the given threshold.


Part 2:

Simulation

In the simulation I used two for loops to iterate over doubles for the ratio of ones to twos thrown by the computer.
Player 1's ratio is represented by the variable i and is incremented by 0.02 each pass. Player 2's ratio is represented
by variable j and is incremented by 0.02 each pass. For each value of i, I increment through all of the possible values
of j and assign the lowest value in that row to the variable rowmin. This is then compared to the variable maxmin and 
if rowmin is larger than maxmin maxmin = rowmin. This is done for every value of i. If the maxmin is a positive value,
this tells me that player 1 will always win at the value of i where this maxmin occurred. 

After running my simulation, I have determined that player 1 has the advantage at a threshold t value of 0.58.
