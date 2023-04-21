import pandas as pd
import os
from logzero import logger
from single_sim import single_simulation
from mlb_lineups import pregame_lineups
from datetime import datetime


def play_ball_mlb(stats_years=None):

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

    daily_games = pd.DataFrame()
    for game in range(len(matchup_list)):

        try:
            game_df = single_simulation(5000, game, matchup_list, lineup_stats, pitching_matchup_stats, game_gambling)
            daily_games = pd.concat([daily_games, game_df]).reset_index(drop=True)
        except IndexError:
            logger.info(f"Error with {matchup_list[game][0]} vs. {matchup_list[game][1]}")
            continue

    if not os.path.exists(f"/Users/bcallahan/Desktop/mlb_simulator/daily_mlb_games.csv"):
        logger.info(f"Creating .csv file")
        os.mkdir(f"/Users/bcallahan/Desktop/mlb_simulator/")
        daily_games.to_csv(f"~/Desktop/mlb_simulator/daily_mlb_games.csv")

    elif os.path.exists(f"/Users/bcallahan/Desktop/mlb_simulator/daily_mlb_games.csv"):
        logger.info(f"Loading previous data")
        temp_df = pd.read_csv(f"~/Desktop/mlb_simulator/daily_mlb_games.csv")
        logger.info(f"Appending today's games: {datetime.now().strftime('%Y-%m-%d')}")
        all_games = pd.concat([temp_df, daily_games]).reset_index(drop=True)
        all_games.to_csv(f"~/Desktop/mlb_simulator/daily_mlb_games.csv")

    logger.info(f"Complete")
    return daily_games
