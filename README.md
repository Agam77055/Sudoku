# Sudoku Game

### Video Demo:  https://youtu.be/RHRz-WfbIp4

## Description:

The Sudoku Game Project is an interactive application designed to generate, display, and solve Sudoku puzzles. The core objective is to fill a 9x9 grid with digits from 1 to 9, ensuring that each digit appears only once in each row, column, and 3x3 subgrid. This project includes features for generating random puzzles of varying difficulty, providing hints to players, and validating the correctness of the player's solution in real-time. The game offers a user-friendly interface, making it accessible for both beginners and experienced Sudoku enthusiasts. Additionally, the project incorporates an efficient backtracking algorithm to ensure that every generated puzzle is solvable, and it includes comprehensive testing to verify the correctness of the Sudoku logic.

As per the minimum requirements, 3 functions have been created:

```zsh
is_valid(board, num, row, col)
is_game_over(board)
empty_cells(board)
```
## Function Descriptions:

### is_valid(board, num, row, col)
This function checks whether placing a given number in a specific row and column on the board is valid according to Sudoku rules.

### Parameters:

board: 2D list representing the Sudoku board.
num: The number to be placed (1-9).
row: The row index where the number is to be placed.
col: The column index where the number is to be placed.

Returns:

True if the placement is valid, False otherwise.

### is_game_over(board)
This function checks if the Sudoku game is over, meaning all cells are filled with valid numbers.

#### Parameters:

board: 2D list representing the Sudoku board.

Returns:

True if the game is over, False otherwise.

### empty_cells(board)
This function finds the first empty cell (with a value of 0) on the board.

#### Parameters:

board: 2D list representing the Sudoku board.

Returns:

Tuple of the row and column index of the first empty cell, or None if there are no empty cells.

---
Which are accompanied by their own unit test in test_project.py

```zsh
test_is_valid()
test_is_game_over()
test_empty_cells()
```

#### In requirements.txt, the command used to install the required library, tkinter, is shown

```zsh
pip install -r requirements.txt
```

### To run the program:
Use the following,
```zsh
python project.py
```

### To run the pytest program:
Use the following,

```zsh
pytest test_project.py
```

### Features:

- Random Puzzle Generation: Generates Sudoku puzzles with varying levels of difficulty.

- Real-Time Validation: Checks the correctness of the player's solution as numbers are entered.

- User-Friendly Interface: Designed to be intuitive and accessible for users of all skill levels.

- Backtracking Algorithm: Ensures every puzzle generated is solvable.

- Comprehensive Testing: Includes unit tests for key functions to ensure the reliability and correctness of the game logic.

## The sudoku game will open up like the following:
![alt text](<Sudoku board.png>)


## You can use the arrow keys to select a box like this:
![alt text](<Sudoku select.png>)

## Use numerics 1-9 to input the number, and use backspace to remove the inputted number
![alt text](<Sudoku input.png>)
