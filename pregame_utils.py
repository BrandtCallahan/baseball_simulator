import pandas as pd

# urls for batting and pitching rosters/stats
batting_url = f"~/Downloads/Baseball DB - batting.csv"
pitching_url = f"~/Downloads/Baseball DB - pitching.csv"

# batting df
batting_df = pd.read_csv(batting_url)
batting_df["Player"] = batting_df["Player"].str.lower().str.replace(".", "")

# pitching df
pitching_df = pd.read_csv(pitching_url)
pitching_df["WHIP"] = (pitching_df["BB"] + pitching_df["H"]) / pitching_df["IP"]
pitching_df["Player"] = pitching_df["Player"].str.lower().str.replace(".", "")


# lineup creation
away_team = input(f"Who is the away team?\n")
home_team = input(f"Who is the home team?\n")

# matchup
matchup = [away_team, home_team]

# setting up lineup and pitching rotation
away_team_lineup = []
for player in range(1, 10):
    away_team_lineup += [input(f"Enter batter's name: \n")]
away_team_pitcher = []
for player in range(1, 4):
    away_team_pitcher += [input(f"Enter pitcher's name: \n")]

home_team_lineup = []
for player in range(1, 10):
    home_team_lineup += [input(f"Enter batter's name: \n")]
home_team_pitcher = []
for player in range(1, 4):
    home_team_pitcher += [input(f"Enter pitcher's name: \n")]

away_lineup = pd.DataFrame()
away_lineup_stats = []
for n, player in enumerate(away_team_lineup):
    temp = batting_df[(batting_df["Player"] == player) & (batting_df["Team"] == away_team)][
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
    temp = batting_df[(batting_df["Player"] == player) & (batting_df["Team"] == home_team)][
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

away_pitcher = pd.DataFrame()
away_pitcher_stats = []
for n, player in enumerate(away_team_pitcher):
    temp = pitching_df[(pitching_df["Player"] == player) & (pitching_df["Team"] == away_team)][
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
    temp = pitching_df[(pitching_df["Player"] == player) & (pitching_df["Team"] == home_team)][
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
