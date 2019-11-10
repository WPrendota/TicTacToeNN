# The Tic-Tac-Toe game - A Reinforcement Learning example
Version 1.0

---

## Technologies:
### - [Python](https://www.python.org),

---

## Description:
*The Tic-Tac-Toe game: A Reinforcement Learning example.*

You can test yourself with an easy and strong bot (learned by QRL). 

After each game, Q-Table is created and filled with respective values depending on if the QRL Player based on the following equation for loosing:

Q-Value = min(Q-Table) * (1-Learning_rate) - Learning_rate * Discount * Q-Value_next

and winning:

Q-Value = max(Q-Table) * (1-Learning_rate) + Learning_rate * Discount * Q-Value_next

---

## Deployment:
Download the **??.py** file. In the command line use following arguments for desirable action:
* ```-h``` for the help
* ```-e``` for The TicTacToe game: easy bot,
* ```-s``` for The TicTacToe game: strong bot,
* ```-c``` for The data gathering mode: Random Computer Player vs Random Computer Player,
* ```-d``` for The data gathering mode: Random Computer Player vs QRL Player,
* ```-t``` for The data gathering mode: QRL Player vs QRL Player.

The last four commands take an additional two arguments, which corresponds to the chosen numbers.

You can also used them in the notebooks by importing 'tic_tac_toe_running_script.py' and running 'run_script(game_mode, arg_1=0, arg_2=0)'.

Game modes values:

* ```1``` for The TicTacToe game: easy bot,
* ```2``` for The TicTacToe game: strong bot,
* ```3``` for The data gathering mode: Random Computer Player vs Random Computer Player,
* ```4``` for The data gathering mode: Random Computer Player vs QRL Player,
* ```5``` for The data gathering mode: QRL Player vs QRL Player.

The data gathering modes takes two arguments: the 'test' and 'train' games iteration numbers (0 by default).

---

## Results:

The Random Computer Player vs QRL Player:
Learning_rate: 0.1
Discount: 0.9

The Random Computer Player vs Random Computer Player:


The QRL Player vs QRL Player:


---

## Testing
The implemented calculator functions were checked by UnitTests attached in the **TestSimpleCalculator.py** file.

--- 

## Literature and further reading:
### ["Reinforcement Learning — Implement TicTacToe"](https://towardsdatascience.com/reinforcement-learning-implement-tictactoe-189582bea542)


### ["Reinforcement Learning and Deep Reinforcement Learning with Tic Tac Toe"](https://towardsdatascience.com/reinforcement-learning-and-deep-reinforcement-learning-with-tic-tac-toe-588d09c41dda)


### ["Playing Tic Tac Toe using Reinforcement Learning"](https://www.codementor.io/rohitagrawalofficialmail/playing-tic-tac-toe-using-reinforcement-learning-x5rf9xvey)


### ["Reinforcement Learning: Train a bot to play tic-tac-toe"](https://becominghuman.ai/reinforcement-learning-step-by-step-17cde7dbc56c)


### ["Part 3 — Tabular Q Learning, a Tic Tac Toe player that gets better and better"](https://medium.com/@carsten.friedrich/part-3-tabular-q-learning-a-tic-tac-toe-player-that-gets-better-and-better-fa4da4b0892a)


### ["Tic-Tac-Toe and Reinforcement Learning"](https://medium.com/swlh/tic-tac-toe-and-deep-neural-networks-ea600bc53f51)


### ["Tic-Tac-Toe with Tabular Q-Learning"](https://dev.to/nestedsoftware/tic-tac-toe-with-tabular-q-learning-1kdn)

### ["Reinforcement Learning - A Tic Tac Toe Example"](https://www.codeproject.com/Articles/1400011/Reinforcement-Learning-A-Tic-Tac-Toe-Example)

&nbsp;

## Contributor
### Witold Prendota
