import pandas as pd
from logzero import logger
from single_sim import single_simulation
from mlb_lineups import pregame_lineups
from datetime import datetime


def fantasy_baseball(stats_years=None):

    if stats_years is None:
        stats_years = []
    if len(stats_years) == 0:
        curr_year = datetime.now().year
        stats_years = [curr_year-1, curr_year]

    game_data = pregame_lineups(stats_years)
    matchup_list = game_data[0]
    lineup_stats = game_data[1]
    pitching_matchup_stats = game_data[2]
    game_gambling = game_data[3]

    daily_points = pd.DataFrame()
    for game in range(len(matchup_list)):

        try:
            game_df = single_simulation(5000, game, matchup_list, lineup_stats, pitching_matchup_stats, game_gambling)
            batter_df = game_df[0]
            batter_fantasy_points = batter_df[["team", "player", "fantasy_points"]]
            pitcher_df = game_df[1]
            pitcher_fantasy_points = pitcher_df[["team", "player", "fantasy_points"]]

            daily_points = pd.concat([daily_points, batter_fantasy_points, pitcher_fantasy_points]).reset_index(drop=True)

        except IndexError:
            logger.info(f"Error with {matchup_list[game][0]} vs. {matchup_list[game][1]}")
            continue

    return daily_points
