import re

import pandas as pd
import requests
from bs4 import BeautifulSoup
from team_dict import team_dict, team_name_dict


# functions for finding and pull tables taken from GitHub
def findTables(url):
    res = requests.get(url)
    # The next two lines get around the issue with comments breaking the parsing.
    comm = re.compile("<!--|-->")
    soup = BeautifulSoup(comm.sub("", res.text), 'lxml')  # 'lxml'
    divs = soup.findAll('div', id="content")
    divs = divs[0].findAll("div", id=re.compile("^all"))
    ids = []
    for div in divs:
        searchme = str(div.findAll("table"))
        x = searchme[searchme.find("id=") + 3: searchme.find(">")]
        x = x.replace("\"", "")
        if len(x) > 0:
            ids.append(x)
    return ids


def pullTable(url, tableID):
    res = requests.get(url)
    # Work around comments
    comm = re.compile("<!--|-->")
    soup = BeautifulSoup(comm.sub("", res.text), 'lxml')  # 'lxml'
    tables = soup.findAll('table', id=tableID)
    data_rows = tables[0].findAll('tr')
    data_header = tables[0].findAll('thead')
    data_header = data_header[0].findAll("tr")
    data_header = data_header[0].findAll("th")
    game_data = [[td.getText() for td in data_rows[i].findAll(['th', 'td'])]
                 for i in range(len(data_rows))
                 ]
    data = pd.DataFrame(game_data)
    header = []
    for i in range(len(data.columns)):
        header.append(data_header[i].getText())
    data.columns = header
    data = data.loc[data[header[0]] != header[0]]
    data = data.reset_index(drop=True)
    return data


# special characters
special_charc = "*#+"

# list of team abbreviations
team_url = f'https://www.baseball-reference.com/about/team_IDs.shtml'
team_id = pd.read_html(team_url, header=0)[0]
curr_teams = (team_id[team_id['Last Year'] == 'Present']).reset_index(drop=True)

# batting stats url
bat_url = f'https://www.baseball-reference.com/leagues/majors/2022-standard-batting.shtml'
find_bat_tables = findTables(bat_url)  # find the associated tables

# player batting
player_bat = pullTable(bat_url, 'players_standard_batting')
player_bat = player_bat[~(player_bat['Rk'] == '')]
for i in player_bat.index:
    player_bat_list = player_bat["Name"][i].split("\xa0")
    player_bat["Name"][i] = player_bat_list[0] + " " + player_bat_list[1]
    for charc in special_charc:
        player_bat["Name"][i] = player_bat["Name"][i].replace(charc, "")

player_bat["OBP"] = player_bat["OBP"].replace("", ".000")
player_bat["SLG"] = player_bat["SLG"].replace("", ".000")
player_bat["AB"] = player_bat["AB"].astype(int)
player_bat["H"] = player_bat["H"].astype(int)
player_bat["2B"] = player_bat["2B"].astype(int)
player_bat["3B"] = player_bat["3B"].astype(int)
player_bat["HR"] = player_bat["HR"].astype(int)
player_bat_df = player_bat.groupby(["Name"]).agg(Tm=("Tm", "last"),
                                                 OBP=("OBP", "median"),
                                                 SLG=("SLG", "median"),
                                                 abs=("AB", "sum"),
                                                 hits=("H", "sum"),
                                                 doubles=("2B", "sum"),
                                                 triples=("3B", "sum"),
                                                 homers=("HR", "sum")).reset_index()
player_bat_df["singles"] = player_bat_df["hits"].astype(int) - (player_bat_df["doubles"].astype(int)
                                                                + player_bat_df["triples"].astype(int)
                                                                + player_bat_df["homers"].astype(int))

player_bat_df["1B"] = player_bat_df["singles"].astype(int) / player_bat_df["hits"].astype(int)
player_bat_df["2B"] = (player_bat_df["doubles"].astype(int) / player_bat_df["hits"].astype(int))
player_bat_df["3B"] = (player_bat_df["triples"].astype(int) / player_bat_df["hits"].astype(int))
player_bat_df["HR"] = (player_bat_df["homers"].astype(int) / player_bat_df["hits"].astype(int))

player_bat_df = player_bat_df.fillna(0)
player_bat_df["1B"] = player_bat_df["1B"].astype(float)
player_bat_df["2B"] = player_bat_df["2B"].astype(float)
player_bat_df["3B"] = player_bat_df["3B"].astype(float)
player_bat_df["HR"] = player_bat_df["HR"].astype(float)

# team batting
team_bat = pullTable(bat_url, 'teams_standard_batting')
team_bat = team_bat[~(team_bat['Tm'] == 'League Average') & ~(team_bat['Tm'] == '')]

# pitching stats url
pitch_url = f'https://www.baseball-reference.com/leagues/majors/2022-standard-pitching.shtml'
find_pitch_tables = findTables(pitch_url)  # find the associated tables

# player pitching
player_pitch = pullTable(pitch_url, 'players_standard_pitching')
player_pitch = player_pitch[~(player_pitch['Rk'] == '')]
for i in player_pitch.index:
    player_pitch_list = player_pitch["Name"][i].split("\xa0")
    player_pitch["Name"][i] = player_pitch_list[0] + " " + player_pitch_list[1]
    for charc in special_charc:
        player_pitch["Name"][i] = player_pitch["Name"][i].replace(charc, "")

player_pitch["WHIP"] = player_pitch["WHIP"].replace("", "0.000")
player_pitch["ERA"] = player_pitch["ERA"].replace("", "0.00")
player_pitch_df = player_pitch.groupby(["Name"]).agg(Tm=("Tm", "last"),
                                                     WHIP=("WHIP", "median"),
                                                     ERA=("ERA", "median")).reset_index()

# team pitching
team_pitch = pullTable(pitch_url, 'teams_standard_pitching')
team_pitch = team_pitch[~(team_pitch['Tm'] == 'League Average') & ~(team_pitch['Tm'] == '')]
team_pitch["Team"] = team_pitch["Tm"].map(team_name_dict)
team_pitch = team_pitch[["Team", "WHIP"]]
