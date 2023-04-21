import pandas as pd


def stats_data(type):

    if type == "batting":
        # urls for batting and pitching rosters/stats
        url = input(f"Please enter the directory to your batting data .csv\n")
        # "~/Downloads/Baseball DB - batting.csv"

        df = pd.read_csv(url)
        df["Player"] = df["Player"].str.lower().str.replace(".", "")

    elif type == "pitching":
        url = input(f"Please enter the directory to your pitching data .csv\n")
        # ~/Downloads/Baseball DB - pitching.csv

        # pitching df
        df = pd.read_csv(url)
        df["WHIP"] = (df["BB"] + df["H"]) / df["IP"]
        df["Player"] = df["Player"].str.lower().str.replace(".", "")

    else:
        raise Exception(f"Please enter a valid type. Either 'batting' or 'pitching'.")

    return df


def offense():
    # lineup creation
    away_team = input(f"Who is the away team?\n")
    home_team = input(f"Who is the home team?\n")

    # matchup
    matchup = [away_team, home_team]
    batting_df = stats_data("batting")

    # setting up lineup and pitching rotation
    away_team_lineup = []
    for player in range(1, 10):
        away_team_lineup += [input(f"Enter {away_team}'s #{player} batter's name: \n")]

    home_team_lineup = []
    for player in range(1, 10):
        home_team_lineup += [input(f"Enter {home_team}'s #{player} batter's name: \n")]

    away_lineup = pd.DataFrame()
    away_lineup_stats = []
    for n, player in enumerate(away_team_lineup):
        temp = batting_df[(batting_df["Player"] == player.lower()) & (batting_df["Team"] == away_team)][
            ["Team", "Player", "OBP", "SLG", "1B", "2B", "3B", "HR"]]
        away_lineup = pd.concat([away_lineup, temp]).reset_index(drop=True)

        away_lineup_stats += [[
            away_lineup["Team"][n],
            away_lineup["Player"][n],
            away_lineup["OBP"][n],
            away_lineup["SLG"][n],
            away_lineup["1B"][n],
            away_lineup["2B"][n],
            away_lineup["3B"][n],
            away_lineup["HR"][n],
        ]]

    home_lineup = pd.DataFrame()
    home_lineup_stats = []
    for n, player in enumerate(home_team_lineup):
        temp = batting_df[(batting_df["Player"] == player.lower()) & (batting_df["Team"] == home_team)][
            ["Team", "Player", "OBP", "SLG", "1B", "2B", "3B", "HR"]]
        home_lineup = pd.concat([home_lineup, temp]).reset_index(drop=True)

        home_lineup_stats += [[
            home_lineup["Team"][n],
            home_lineup["Player"][n],
            home_lineup["OBP"][n],
            home_lineup["SLG"][n],
            home_lineup["1B"][n],
            home_lineup["2B"][n],
            home_lineup["3B"][n],
            home_lineup["HR"][n],
        ]]

    lineup_stats = []
    lineup_stats += [away_lineup_stats]
    lineup_stats += [home_lineup_stats]

    return lineup_stats


def pitching():
    # lineup creation
    away_team = input(f"Who is the away team?\n")
    home_team = input(f"Who is the home team?\n")

    games = input(f"How many games are being played?\n")
    pitching_df = stats_data("pitching")

    away_team_pitcher = []
    for player in range(1, int(games)+1):
        away_team_pitcher += [input(f"Enter {away_team}'s #{player} pitcher's name: \n")]

    home_team_pitcher = []
    for player in range(1, int(games)+1):
        home_team_pitcher += [input(f"Enter {home_team}'s #{player} pitcher's name: \n")]

    away_pitcher = pd.DataFrame()
    away_pitcher_stats = []
    for n, player in enumerate(away_team_pitcher):
        temp = pitching_df[(pitching_df["Player"] == player.lower()) & (pitching_df["Team"] == away_team)][
            ["Team", "Player", "ERA", "WHIP"]].reset_index(drop=True)
        away_pitcher = pd.concat([away_pitcher, temp]).reset_index(drop=True)

        away_pitcher_stats += [[away_pitcher["Team"][n],
                               away_pitcher["Player"][n],
                               away_pitcher["ERA"][n],
                               away_pitcher["WHIP"][n],
                               pitching_df[(pitching_df["Team"] == away_team)
                                           & (pitching_df["GS"] < pitching_df["GS"].quantile(0.75))].WHIP.median()
                               ]]


    home_pitcher = pd.DataFrame()
    home_pitcher_stats = []
    for n, player in enumerate(home_team_pitcher):
        temp = pitching_df[(pitching_df["Player"] == player.lower()) & (pitching_df["Team"] == home_team)][
            ["Team", "Player", "ERA", "WHIP"]].reset_index(drop=True)
        home_pitcher = pd.concat([home_pitcher, temp]).reset_index(drop=True)

        home_pitcher_stats += [[home_pitcher["Team"][n],
                               home_pitcher["Player"][n],
                               home_pitcher["ERA"][n],
                               home_pitcher["WHIP"][n],
                               pitching_df[(pitching_df["Team"] == home_team)
                                           & (pitching_df["GS"] < pitching_df["GS"].quantile(0.75))].WHIP.median()
                               ]]

    pitching_matchup_stats = []
    pitching_matchup_stats += [away_pitcher_stats]
    pitching_matchup_stats += [home_pitcher_stats]

    return pitching_matchup_stats

# gambling odds
