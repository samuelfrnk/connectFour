# connectFour

## Introduction 
This is an implementation of the famous game connect four. It provides a UI and a Player versus Computer Mode.
The Computer bot uses an implementation of the minimax algorithm together with alpha beta pruning to 
concentrate on the important parts of the game tree. It considers moves up to a depth of 6. 

## Getting started 

### Dependencies 
- Python 3.x 
- Tkinter 

### Installation and setup

1. Clone this repository 
```console
    gh repo clone samuelfrnk/connectFour
```
2. Navigate to the source directory
```console
    cd src
```
3. Play against the UI (The human player always begins with blue and the Computer follows with red)

```console
    python3 Main.py
```
## How it works 

The AI logic is implemented in the 'AiLogic.py' class, which contains the minimax algorithm with alpha-beta pruning. In the base case of the recursive function, the method calls the static evaluation method in 'Evaluation.py'. This evaluation function assesses the board state to guide the AI's decisions.

## Considerations 

The current AI implementation is quite strong, and I have personally found it challenging to win or even draw against it. However, there are areas for improvement, particularly in the evaluation function. Currently, it heavily weights winning game-over positions, but its performance can be less effective in non-immediate winning scenarios (i.e., positions where no winning move is within the next 6 moves).

For those interested in benchmarking or improving the AI, you can compare it against another AI 4 Connect bot, which has managed to outperform this implementation

## Contribution
Feel free to fork this repository and submit pull requests. Improvements to the evaluation function or any other part of the AI are particularly welcome.
