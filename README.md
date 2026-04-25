
# 🎲 Dice Rolling Game (Python)

## 📌 Project Overview

This is a simple Python-based dice rolling game. The program simulates rolling two dice based on user input. It continuously asks the user whether they want to roll the dice or exit the game.

## ⚙️ How the Program Works (Step-by-Step)

1. **Import Module**

   * The program starts by importing the `random` module.
   * This module is used to generate random numbers for dice rolls.

2. **Infinite Loop**

   * A `while True` loop is used to keep the game running continuously until the user decides to quit.

3. **User Input**

   * The user is asked:

     Roll the dice (y/n):
     
   * Input is converted to lowercase using `.lower()` to handle both uppercase and lowercase inputs.

4. **Rolling the Dice**

   * If the user enters `"y"`:

     * Two random numbers are generated using:

       random.randint(1,6)
       
     * These represent the values of two dice.
     * The result is displayed as a tuple:

       (die1, die2)

5. **Exit Condition**

   * If the user enters `"n"`:

     * The program prints:

       Thanks for Playing
       
     * The loop breaks and the program ends.

6. **Invalid Input Handling**

   * If the user enters anything other than `"y"` or `"n"`:

     * The program displays:

       Invalid choice!

## ▶️ How to Run the Program

1. Make sure Python is installed
2. Save the file as `main.py`
3. Run the program using:

   ```bash
   python main.py
## 📊 Example Output

```
Roll the dice (y/n): y
(3, 5)

Roll the dice (y/n): y
(1, 6)

Roll the dice (y/n): n
Thanks for Playing

## 🛠️ Technologies Used

* Python
* Random Module

## 🎯 Key Concepts Used

* Loops (`while`)
* Conditional Statements (`if-elif-else`)
* User Input (`input()`)
* Random Number Generation


## 🚀 Future Improvements

* Add score tracking
* Create a GUI version
* Add multiplayer mode

* Turn this into a **mini game project (portfolio level)**
