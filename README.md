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

The current AI implementation is quite strong, and I have personally found it challenging to win or even draw against it. 
In terms of evaluation function [this tutorial](https://medium.com/analytics-vidhya/artificial-intelligence-at-play-connect-four-minimax-algorithm-explained-3b5fc32e4a4f) helped quite a lot

## Contribution
Feel free to fork this repository and submit pull requests. Improvements to the evaluation function or any other part of the AI are particularly welcome.
