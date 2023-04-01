import pandas as pd
from single_sim import *

# need to run this import before running the play_ball() function
from pregame_utils import *


def play_ball_mlb(matchup_list, lineup_stats, pitching_matchup_stats, game_gambling):

    for game in range(len(matchup_list)):

        game_df = single_simulation(5000, game, matchup_list, lineup_stats, pitching_matchup_stats, game_gambling)
        print(game_df)
