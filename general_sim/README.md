# baseball_simulator

The simulator uses a batter's on-base percentage (OBP) and a pitcher's out percentage to simulate two teams playing against each other. Nowadays OBP can be seen as a promising offensive stat because it follows what was learned through "Moneyball" in that in order to win games you need to score runs and in order to score runs you need to get on base. Just as OBP can be seen as a promising offensive statistic, a pitcher's ability to get outs (out percentage) helps paint the picture for how efficient a pitcher can throw strikes under the assumption that batter's swing at strikes and getting swings either leads to swings and misses or contact leading to the chance for outs.
 

## Pre-Game
#### pregame_utils.py
Currently, the simulator is set up to import two excel files, one including offensive statistics and a second including pitchinig statistics. The user will be prompted to input the names of the two teams playing against each other as well as the batting lineups and pitching matchup for the game. Once the linupes are inputted the dataframes can be built by extracting the needed data for future functions. Those offensive statistics include a batter's OBP, slugging percentage (SLG), singles, doubles, triples, and homeruns. The pitching dataframes work similarly by extracting the appropriate pitcher's statistics of earned run average (ERA), walks, hits, and innings pitched. The pitcher's WHIP is then calculated using the pitcher's walks, hits, and innings pitched. A final stat is added to the pitching dataframe and that is the median WHIP of non-starting pitchers for the respective team. This will be used as the bullpen's WHIP for when the starting pitcher meets a pitch threshold during the simulation. 

## Inning
#### inning_utils.py
There are three functions that live here in order to set up the workings of an inning within the game. The first function is the Lineup() function that will be used to move through the lineup batter by batter and put the batter's statistics against the pitcher's in the simulation. Another feature living within this function is the mechanism that will generate the pitching change after the starting pitcher's pitch count surpasses 85 pitches. The next function is an AtBat() function that generates a random number to be the pitch and compare to the batter's OBP to help determine the batter's atbat outcome pitch by pitch. Other numbers are generated each pitch to compare for ball/strike, swing/no swing, contact/whiff, and fair/fould scenarios. Lastly, a baserunning function, baserunning(), is used to move runners on base and incorporates a batter's atbat outcome to move the runners appropriately.

## Game
### game_utils.py
Two functions live here that help create a the workings of a baseball game. The first is the actual playing of an inning with batters coming up to face the pitcher and having an outcome from each atbat. Offensive stats and atbat outcomes are tracked in order for box score stats to be tallied at the conclusion of the game. The inning will also keep track of the batter and who has made the last out in order to keep the correct order of atbats throughout the game. The gameboard() function is one that will run the inning() function and start to shape the scoreboard of the game. It works as a tracking mechanism for just one team's innings so two will have to be used for the course of a game. 

## Simulations
### single_game.py, sim_utils.py, series_simulation.py
There are three options for running through the simulator. 
1. The first is just a single game where the output is a true scoreboard with inning totals on runs and total team run totals, hit totals, and runners left on base throughout the game. Also in the output are totals for walks, singles, doubles, triples, homeruns, and out totals detailed as strikeouts, groundouts and flyouts. 
2. The next type of simulator run is a multi-run of single game. This will run the data given for the single game n number of times and that is defined in the function simulation(). The output here is similar to the true single game but will give averages based on the number of games played. Also in the output will be the number of games won by each team.
3. Lastly, we have a series simulator that will allow the user to set up any number of games series, i.e. 3 game, 5 game, or 7 game, and run the simulator to learn who is likely to win the series. The output here will give a game by game likelihood of winners and tell you the winning pitcher for each game. 
