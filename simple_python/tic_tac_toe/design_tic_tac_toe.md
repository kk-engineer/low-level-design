# Design Tic Tac Toe

## What is Tic Tac Toe ?
TicTacToe is a 2 player game played on a 3 x 3 board. Each player is allotted a symbol (one X and one O). Initially, the board is empty. Alternatively, each player takes a turn and puts their symbol at any empty slot. The first player to get their symbol over a complete row OR a complete column OR a diagonal wins.

You can play the game in Google Search by just searching for “tictactoe”!

## Requirements
* Board can be of NxN size.
* There can be two or more players players.
* Each (N-1) player will be allotted a different symbol.
* The symbol can be one of O, X, ... (N-1) etc.
* The players can be either humans or bots.
* Each human player will have a name, email and profile image.
* Each bot player will have a difficulty level.
* Any random player can start the game.
* Then the players will take turns sequentially.
* The player with any consecutive N symbols in a row, column or diagonal wins.
* If the board is full and no player has won, the game is a draw.
* Provision to "undo" last move.

## Extra requirements
* Tournament.
* Leaderboard.
* Replay moves/ Rewatch game.
* Pause/Resume game.

## Entities and Attributes
* Game
  * Board
  * Players
* Board
  * Cells
* Cell
  * Row
  * Column
  * Symbol
* Human Player
  * Name
  * Email
  * Profile Image
* Bot Player
  * Difficulty Level

## Class Diagram 

```mermaid
classDiagram
  class Game {
    - Board board
    - Player[] players
    - WinningStrategy winningStrategy
    - GameState gameState
    +startGame(Player[], int)
    +makeMove(PlayerId, int, int)
    +checkWinner(Board, Player[]) Player
    +registerPlayer(Player)
  }

  class GameState {
    <<Enumeration>>
    - IN_PROGRESS
    - DRAW
    - WINNER
  }

    class Board {
    -Cell[][] cells
    +Board(int size) : Board
  }

  class Cell {
    -int row
    -int column
    -Player player
  }

  class Symbol {
    -String name
    -Byte[] symbolImage
  }

  class Player {
    <<abstract>>
    -Symbol symbol
    +play(Board) BoardCell
  }

  class HumanPlayer {
    -User user
    +play(Board) BoardCell
  }

  class User {
    -String name
    -String email
    -Byte[] profileImage
  }

  class BotPlayer {
    -Level difficultyLevel
    -MoveStrategy moveStrategy
    +play(Board) BoardCell
  }

    class MoveStrategy {
        <<interface>>
        +makeMove(Board) BoardCell
    }

    class EasyMoveStrategy {
        +makeMove(Board) BoardCell
    }

    class MediumMoveStrategy {
        +makeMove(Board) BoardCell
    }

    class HardMoveStrategy {
        +makeMove(Board) BoardCell
    }

  Game "1" --* "*" Player
  Game "*" --o "1" GameState
    Game "1" --* "1" Board
    Board "1" --* "*" Cell
    Cell "1" --o "1" Player
    Player "1" --o "1" Symbol
  HumanPlayer "*" --o "1" User
  Player <|-- HumanPlayer
  Player <|-- BotPlayer
  BotPlayer "*" --o "1" MoveStrategy
  MoveStrategy <|-- EasyMoveStrategy
  MoveStrategy <|-- MediumMoveStrategy
  MoveStrategy <|-- HardMoveStrategy


  class WinningStrategy {
    <<interface>>
    +checkWinner(Board, Player[]) Player
  }

    class NInARowWinningStrategy {
        +checkWinner(Board, Player[]) Player
    }

    class NInAColumnWinningStrategy {
        +checkWinner(Board, Player[]) Player
    }

    class NInADiagonalWinningStrategy {
        +checkWinner(Board, Player[]) Player
    }

    Game "*" --o "1" WinningStrategy
    WinningStrategy <|-- NInARowWinningStrategy
    WinningStrategy <|-- NInAColumnWinningStrategy
    WinningStrategy <|-- NInADiagonalWinningStrategy

```

## Expectations
* The code should be working and functionally correct
* Good software design practices should be followed:
* Code should be modular, readable, extensible
* Separation of concern should be addressed
* Project structured well across multiple files/ packages
* Write unit tests
* CLI app, no need of GUI

