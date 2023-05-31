import pandas as pd
import os
from logzero import logger
from single_sim import single_simulation
from mlb_lineups import pregame_lineups
from datetime import datetime


def play_ball_mlb(stats_years=None):

    logger.info(f"Running: {datetime.now().strftime('%Y-%m-%d')}")
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

    user = "/Users/bcallahan"
    dir_path = f"{user}/Desktop/mlb_simulator/"
    file_path = dir_path + "daily_mlb_games.csv"
    if not os.path.exists(file_path):
        logger.info(f"Creating .csv file")
        os.mkdir(dir_path)
        daily_games.to_csv(file_path)

    elif os.path.exists(file_path):
        logger.info(f"Loading previous data")
        temp_df = pd.read_csv(file_path)
        logger.info(f"Appending today's games: {datetime.now().strftime('%Y-%m-%d')}")
        all_games = pd.concat([temp_df, daily_games]).reset_index(drop=True)
        all_games = all_games[["date",
                               "away_team",
                               "away_pitcher",
                               "away_lineup",
                               "home_team",
                               "home_pitcher",
                               "home_lineup",
                               "favorite",
                               "over_under",
                               "away_team_ml_pct",
                               "home_team_ml_pct",
                               "away_team_spread_pct",
                               "home_team_spread_pct",
                               "fav_ml_pct",
                               "dog_ml_pct",
                               "fav_spread_pct",
                               "dog_ml_pct",
                               "over_pct",
                               "under_pct",
                               "push_pct",
                               ]]
        all_games.to_csv(file_path)

    logger.info(f"Complete")
    return daily_games


def mlb_gambling(file_path):
    logger.info(f"Loading historical simulation results")
    hist_df = pd.read_csv(file_path)

    logger.info(f"Grading gambling predictions")
    logger.info(f"Moneyline")
    # favorite moneyline
    hist_df.loc[hist_df["fav_ml_pct"] >= 0.85, "fav_ml_grade"] = "A"
    hist_df.loc[(hist_df["fav_ml_pct"] < 0.85) & (hist_df["fav_ml_pct"] >= 0.70), "fav_ml_grade"] = "B"
    hist_df.loc[(hist_df["fav_ml_pct"] < 0.70) & (hist_df["fav_ml_pct"] >= 0.60), "fav_ml_grade"] = "C"
    hist_df.loc[(hist_df["fav_ml_pct"] < 0.60) & (hist_df["fav_ml_pct"] >= 0.50), "fav_ml_grade"] = "D"
    hist_df.loc[(hist_df["fav_ml_pct"] < 0.50), "fav_ml_grade"] = "F"
    # underdog moneyline
    hist_df.loc[hist_df["dog_ml_pct"] >= 0.85, "dog_ml_grade"] = "A"
    hist_df.loc[(hist_df["dog_ml_pct"] < 0.85) & (hist_df["dog_ml_pct"] >= 0.70), "dog_ml_grade"] = "B"
    hist_df.loc[(hist_df["dog_ml_pct"] < 0.70) & (hist_df["dog_ml_pct"] >= 0.60), "dog_ml_grade"] = "C"
    hist_df.loc[(hist_df["dog_ml_pct"] < 0.60) & (hist_df["dog_ml_pct"] >= 0.50), "dog_ml_grade"] = "D"
    hist_df.loc[(hist_df["dog_ml_pct"] < 0.50), "dog_ml_grade"] = "F"

    logger.info(f"Spread")
    # favorite spread
    hist_df.loc[hist_df["fav_spread_pct"] >= 0.85, "fav_spread_grade"] = "A"
    hist_df.loc[(hist_df["fav_spread_pct"] < 0.85) & (hist_df["fav_spread_pct"] >= 0.70), "fav_spread_grade"] = "B"
    hist_df.loc[(hist_df["fav_spread_pct"] < 0.70) & (hist_df["fav_spread_pct"] >= 0.60), "fav_spread_grade"] = "C"
    hist_df.loc[(hist_df["fav_spread_pct"] < 0.60) & (hist_df["fav_spread_pct"] >= 0.50), "fav_spread_grade"] = "D"
    hist_df.loc[(hist_df["fav_spread_pct"] < 0.50), "fav_spread_grade"] = "F"
    # underdog spread
    hist_df.loc[hist_df["dog_spread_pct"] >= 0.85, "dog_spread_grade"] = "A"
    hist_df.loc[(hist_df["dog_spread_pct"] < 0.85) & (hist_df["dog_spread_pct"] >= 0.70), "dog_spread_grade"] = "B"
    hist_df.loc[(hist_df["dog_spread_pct"] < 0.70) & (hist_df["dog_spread_pct"] >= 0.60), "dog_spread_grade"] = "C"
    hist_df.loc[(hist_df["dog_spread_pct"] < 0.60) & (hist_df["dog_spread_pct"] >= 0.50), "dog_spread_grade"] = "D"
    hist_df.loc[(hist_df["dog_spread_pct"] < 0.50), "dog_spread_grade"] = "F"

    logger.info(f"Over/Under")
    # over
    hist_df.loc[hist_df["over_pct"] >= 0.85, "over_grade"] = "A"
    hist_df.loc[(hist_df["over_pct"] < 0.85) & (hist_df["over_pct"] >= 0.70), "over_grade"] = "B"
    hist_df.loc[(hist_df["over_pct"] < 0.70) & (hist_df["over_pct"] >= 0.60), "over_grade"] = "C"
    hist_df.loc[(hist_df["overpct"] < 0.60) & (hist_df["over_pct"] >= 0.50), "over_grade"] = "D"
    hist_df.loc[(hist_df["over_pct"] < 0.50), "over_grade"] = "F"
    # under
    hist_df.loc[hist_df["under_pct"] >= 0.85, "under_grade"] = "A"
    hist_df.loc[(hist_df["under_pct"] < 0.85) & (hist_df["under_pct"] >= 0.70), "under_grade"] = "B"
    hist_df.loc[(hist_df["under_pct"] < 0.70) & (hist_df["under_pct"] >= 0.60), "under_grade"] = "C"
    hist_df.loc[(hist_df["under_pct"] < 0.60) & (hist_df["under_pct"] >= 0.50), "under_grade"] = "D"
    hist_df.loc[(hist_df["under_pct"] < 0.50), "under_grade"] = "F"

    return hist_df
