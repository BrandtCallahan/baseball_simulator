"""
Use the get_game_matchups() and get_game_lineups() from game_schedule.py

"""

from beautiful_soup_helper import get_soup_from_url
from pregame_utils import get_game_matchups, get_game_lineups, get_game_gambling
from mlb_stats import player_bat_df, player_pitch_df
from unidecode import unidecode
# from team_dict import team_dict
from datetime import datetime


today = datetime.now().strftime("%Y-%m-%d")

# Set up matchups
matchups = get_game_matchups(game_date=today)
matchup_list = []
for matchup in range(len(matchups)):
    away_team = matchups[matchup].away_team
    home_team = matchups[matchup].home_team
    game_date = matchups[matchup].game_date

    matchup_list.append([f"{team_dict[away_team]}", f"{team_dict[home_team]}"])

# Set up each games' lineups and pitchers
lineups = get_game_lineups(game_date=today)

matchup_lineup = []
matchup_pitcher = []
for team_lineup in range(len(lineups)):
    away_lineup = []
    home_lineup = []
    away_lineup_struct = lineups[team_lineup].away_lineup
    for player in range(len(away_lineup_struct)):
        away_player = away_lineup_struct[player].name
        away_lineup.append(f"{away_player}")
    home_lineup_struct = lineups[team_lineup].home_lineup
    for player in range(len(home_lineup_struct)):
        home_player = home_lineup_struct[player].name
        home_lineup.append(f"{home_player}")
    away_pitcher = lineups[team_lineup].away_pitcher.name
    home_pitcher = lineups[team_lineup].home_pitcher.name
    game_date = lineups[team_lineup].game_date

    matchup_lineup.append([away_lineup, home_lineup])
    matchup_pitcher.append([away_pitcher, home_pitcher])

# Set up each games' gambling lines
gambling_lines = get_game_gambling(game_date=today)
game_gambling = []
for game in range(len(gambling_lines)):
    favorite = team_dict[gambling_lines[game].favorite]
    moneyline = int(gambling_lines[game].money_line)
    over_under = float(gambling_lines[game].over_under)
    team_match = matchup_list[game]

    game_gambling.append([team_match, favorite, moneyline, over_under])

# Set up the players with their stats
# TODO: adjust the missing player from stats df. right now using team median but want to try and re-search the df for player
# if player doesn't have full name re-search for last name, first initial
player_bat_df["Name"] = player_bat_df["Name"].apply(unidecode)
player_pitch_df["Name"] = player_pitch_df["Name"].apply(unidecode)

lineup_stats = []
pitching_matchup_stats = []
for lineup in range(len(matchup_lineup)):

    away_player_stat = []
    home_player_stat = []
    away_pitcher_stat = []
    home_pitcher_stat = []
    away_lineup = matchup_lineup[lineup][0]
    home_lineup = matchup_lineup[lineup][1]
    away_pitcher = matchup_pitcher[lineup][0]
    home_pitcher = matchup_pitcher[lineup][1]

    for player in away_lineup:
        try:
            player_name = player_bat_df[player_bat_df["Name"] == player].reset_index().Name[0]
            player_obp = player_bat_df[player_bat_df["Name"] == player].reset_index().OBP[0]
            player_slg = player_bat_df[player_bat_df["Name"] == player].reset_index().SLG[0]
            player_1b = player_bat_df[player_bat_df["Name"] == player].reset_index()["1B"][0]
            player_2b = player_bat_df[player_bat_df["Name"] == player].reset_index()["2B"][0]
            player_3b = player_bat_df[player_bat_df["Name"] == player].reset_index()["3B"][0]
            player_hr = player_bat_df[player_bat_df["Name"] == player].reset_index()["HR"][0]
        except (AttributeError, KeyError):
            player_name = player
            player_team = matchup_list[lineup][0]
            player_obp = player_bat_df[player_bat_df["Tm"] == player_team].OBP.median()
            player_slg = player_bat_df[player_bat_df["Tm"] == player_team].SLG.median()
            player_1b = player_bat_df[player_bat_df["Tm"] == player_team]["1B"].median()
            player_2b = player_bat_df[player_bat_df["Tm"] == player_team]["2B"].median()
            player_3b = player_bat_df[player_bat_df["Tm"] == player_team]["3B"].median()
            player_hr = player_bat_df[player_bat_df["Tm"] == player_team]["HR"].median()

        away_player_stat.append([player_name, player_obp, player_slg, player_1b, player_2b, player_3b, player_hr])

    for player in home_lineup:
        try:
            player_name = player_bat_df[player_bat_df["Name"] == player].reset_index().Name[0]
            player_obp = player_bat_df[player_bat_df["Name"] == player].reset_index().OBP[0]
            player_slg = player_bat_df[player_bat_df["Name"] == player].reset_index().SLG[0]
            player_1b = player_bat_df[player_bat_df["Name"] == player].reset_index()["1B"][0]
            player_2b = player_bat_df[player_bat_df["Name"] == player].reset_index()["2B"][0]
            player_3b = player_bat_df[player_bat_df["Name"] == player].reset_index()["3B"][0]
            player_hr = player_bat_df[player_bat_df["Name"] == player].reset_index()["HR"][0]
        except (AttributeError, KeyError):
            player_name = player
            player_team = matchup_list[lineup][0]
            player_obp = player_bat_df[player_bat_df["Tm"] == player_team].OBP.median()
            player_slg = player_bat_df[player_bat_df["Tm"] == player_team].SLG.median()
            player_1b = player_bat_df[player_bat_df["Tm"] == player_team]["1B"].median()
            player_2b = player_bat_df[player_bat_df["Tm"] == player_team]["2B"].median()
            player_3b = player_bat_df[player_bat_df["Tm"] == player_team]["3B"].median()
            player_hr = player_bat_df[player_bat_df["Tm"] == player_team]["HR"].median()

        home_player_stat.append([player_name, player_obp, player_slg, player_1b, player_2b, player_3b, player_hr])

    lineup_stats.append([away_player_stat, home_player_stat])

    try:
        player_name = player_pitch_df[player_pitch_df["Name"] == away_pitcher].reset_index().Name[0]
        player_whip = player_pitch_df[player_pitch_df["Name"] == away_pitcher].reset_index().WHIP[0]
        player_era = player_pitch_df[player_pitch_df["Name"] == away_pitcher].reset_index().ERA[0]
        player_team = matchup_list[lineup][0]
        team_whip = player_pitch_df[player_pitch_df["Tm"] == player_team].WHIP.median()
    except (AttributeError, KeyError):
        player_name = away_pitcher
        player_team = matchup_list[lineup][0]
        player_whip = player_pitch_df[player_pitch_df["Tm"] == player_team].WHIP.median()
        player_era = player_pitch_df[player_pitch_df["Tm"] == player_team].ERA.median()
        team_whip = player_pitch_df[player_pitch_df["Tm"] == player_team].WHIP.median()

    away_pitcher_stat.append([player_name, player_whip, player_era, team_whip])

    try:
        player_name = player_pitch_df[player_pitch_df["Name"] == home_pitcher].reset_index().Name[0]
        player_whip = player_pitch_df[player_pitch_df["Name"] == home_pitcher].reset_index().WHIP[0]
        player_era = player_pitch_df[player_pitch_df["Name"] == home_pitcher].reset_index().ERA[0]
        player_team = matchup_list[lineup][1]
        team_whip = player_pitch_df[player_pitch_df["Tm"] == player_team].WHIP.median()
    except (AttributeError, KeyError):
        player_name = home_pitcher
        player_team = matchup_list[lineup][1]
        player_whip = player_pitch_df[player_pitch_df["Tm"] == player_team].WHIP.median()
        player_era = player_pitch_df[player_pitch_df["Tm"] == player_team].ERA.median()
        team_whip = player_pitch_df[player_pitch_df["Tm"] == player_team].WHIP.median()

    home_pitcher_stat.append([player_name, player_whip, player_era, team_whip])

    pitching_matchup_stats.append([away_pitcher_stat, home_pitcher_stat])
