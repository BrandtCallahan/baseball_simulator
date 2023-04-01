import pandas as pd
from game_utils import *
from inning_utils import *
from simulation import *
from series_simulation import *
from single_game import truegame

# need to run this import before running the play_ball() function
from pregame_utils import *


def play_ball(sim_type):

    lineup_stats = offense()
    pitching_matchup_stats = pitching()

    if sim_type == 'single_game':
        game_number = 1  # set the specific game you want to run (specific for pitching matchup)

        game_df = truegame(game_number, lineup_stats, pitching_matchup_stats)

    if sim_type == 'game_sim':
        n = 500  # set the number of times to run each game
        game_number = 1  # set the specific game you want to run (specific for pitching matchup)

        game_df = single_simulation(n, game_number, lineup_stats)

    if sim_type == 'series_sim':
        n = 500  # set the number of times to run each game
        series_len = 3  # set series length

        game_df = series_simulation(n, series_len, lineup_stats, pitching_matchup_stats)

    return game_df
