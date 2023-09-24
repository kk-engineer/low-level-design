# Design Tic Tac Toe

## Overview: What is Tic Tac Toe ?
TicTacToe is a 2 player game played on a 3 x 3 board. Each player is allotted a symbol (one X and one O). Initially, the board is empty. Alternatively, each player takes a turn and puts their symbol at any empty slot. The first player to get their symbol over a complete row OR a complete column OR a diagonal wins.

You can play the game in Google Search by just searching for “tictactoe”!

What kind of design ?
* Object entity
* Interactive application (Desktop application), with no data persistence.
* Web application (Real world application), with data persistence.

Current design: Interactive application (CLI/Desktop app)

## Requirements
* Board can be of NxN size.
* 2 or more players, upto N-1.
* Each (N-1) player will be allotted a different symbol.
* The symbol can be one of O, X, ... (N-1) etc.
* The players can be either humans or bots, only 1 bot per game.
* Each bot player will have a difficulty level.
* How does a game start ?
  *  Any random player can start the game.
* How does the game proceed ?
  *  Then the players will take turns sequentially.
* How does the game end ?
    * Draw/ No Result
    * Win
        * What are the different ways in which the game can be won ?
          * Row, Col, Diagonal
        * Does the game end when -
          * 1 player wins
          * All (N-2) players win except 1 last player
* Provision to "Undo" last move.
* Provision to rewatch/replay all moves.

## Extra requirements
* Tournament.
* Leaderboard.
* Blocked Cells.
* Pause/Resume game.

## Entities and Attributes
* Game
  * Board
  * List<Player> Players
  * GameStatus
  * Player Winner
  * NextTurnPlayer
  * List<Move> Moves
  * List<GameWinningStrategy> GameWinningStrategies

* Board
  * Dimension
  * Cells

* Cell
  * Row
  * Column
  * Player

* Player
  * Symbol
  * Name
  * PlayerType

* Bot Player
  * DifficultyLevel
  * BotPlayingStrategy

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

