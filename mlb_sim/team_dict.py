import bidict

# Two-way dictionary
rotowire_team_dict = bidict.bidict(
    ARI="Arizona Diamondbacks",
    ATL="Atlanta Braves",
    BAL="Baltimore Orioles",
    BOS="Boston Red Sox",
    CHC="Chicago Cubs",
    CWS="Chicago White Sox",
    CIN="Cincinnati Reds",
    CLE="Cleveland Indians",
    COL="Colorado Rockies",
    DET="Detroit Tigers",
    HOU="Houston Astros",
    KC="Kansas City Royals",
    LAA="Los Angeles Angels",
    LAD="Los Angeles Dodgers",
    MIA="Miami Marlins",
    MIL="Milwaukee Brewers",
    MIN="Minnesota Twins",
    NYM="New York Mets",
    NYY="New York Yankees",
    OAK="Oakland Athletics",
    ATH='Athletics',
    PHI="Philadelphia Phillies",
    PIT="Pittsburgh Pirates",
    SD="San Diego Padres",
    SEA="Seattle Mariners",
    SF="San Francisco Giants",
    STL="St. Louis Cardinals",
    TB="Tampa Bay Rays",
    TEX="Texas Rangers",
    TOR="Toronto Blue Jays",
    # WAS="Washington Nationals",
    WSH='Washington Nationals',
)

# Two-way dictionary
baseball_reference_team_dict = bidict.bidict(
    ARI="Arizona Diamondbacks",
    ATL="Atlanta Braves",
    BAL="Baltimore Orioles",
    BOS="Boston Red Sox",
    CHC="Chicago Cubs",
    CHW="Chicago White Sox",
    CIN="Cincinnati Reds",
    CLE="Cleveland Indians",
    COL="Colorado Rockies",
    DET="Detroit Tigers",
    HOU="Houston Astros",
    KCR="Kansas City Royals",
    LAA="Los Angeles Angels of Anaheim",
    # LAA="Los Angeles Angels",
    LAD="Los Angeles Dodgers",
    MIA="Miami Marlins",
    MIL="Milwaukee Brewers",
    MIN="Minnesota Twins",
    NYM="New York Mets",
    NYY="New York Yankees",
    OAK="Oakland Athletics",
    ATH='Athletics',
    PHI="Philadelphia Phillies",
    PIT="Pittsburgh Pirates",
    SDP="San Diego Padres",
    SEA="Seattle Mariners",
    SFG="San Francisco Giants",
    STL="St. Louis Cardinals",
    TBR="Tampa Bay Rays",
    TEX="Texas Rangers",
    TOR="Toronto Blue Jays",
    # WSN="Washington Nationals",
    WSH='Washington Nationals',
)

# rotowire to baseball reference
team_dict = {
    "ARI": "ARI",
    "ATL": "ATL",
    "BAL": "BAL",
    "BOS": "BOS",
    "CHC": "CHC",
    "CWS": "CHW",
    "CIN": "CIN",
    "CLE": "CLE",
    "COL": "COL",
    "DET": "DET",
    "HOU": "HOU",
    "KC": "KCR",
    "LAA": "LAA",
    "LAD": "LAD",
    "MIA": "MIA",
    "MIL": "MIL",
    "MIN": "MIN",
    "NYM": "NYM",
    "NYY": "NYY",
    "OAK": "OAK",
    "ATH": "OAK",
    "PHI": "PHI",
    "PIT": "PIT",
    "SD": "SDP",
    "SEA": "SEA",
    "SF": "SFG",
    "STL": "STL",
    "TB": "TBR",
    "TEX": "TEX",
    "TOR": "TOR",
    "WAS": "WSN",
    'WSH': "WSN",
}

team_name_dict = {
    "Arizona Diamondbacks": "ARI",
    "Atlanta Braves": "ATL",
    "Baltimore Orioles": "BAL",
    "Boston Red Sox": "BOS",
    "Chicago Cubs": "CHC",
    "Chicago White Sox": "CWS",
    "Cincinnati Reds": "CIN",
    "Cleveland Guardians": "CLE",
    "Colorado Rockies": "COL",
    "Detroit Tigers": "DET",
    "Houston Astros": "HOU",
    "Kansas City Royals": "KCR",
    "Los Angeles Angels": "LAA",
    "Los Angeles Dodgers": "LAD",
    "Miami Marlins": "MIA",
    "Milwaukee Brewers": "MIL",
    "Minnesota Twins": "MIN",
    "New York Mets": "NYM",
    "New York Yankees": "NYY",
    "Oakland Athletics": "OAK",
    "Athletics": "OAK",
    "Philadelphia Phillies": "PHI",
    "Pittsburgh Pirates": "PIT",
    "San Diego Padres": "SDP",
    "Seattle Mariners": "SEA",
    "San Francisco Giants": "SFG",
    "St. Louis Cardinals": "STL",
    "Tampa Bay Rays": "TBR",
    "Texas Rangers": "TEX",
    "Toronto Blue Jays": "TOR",
    "Washington Nationals": "WSN",
}


def get_baseball_reference_team(full_team_name):
    """
    Get the Baseball Reference abbreviation from the Rotowire abbreviation
    :param full_team_name: team name in the Rotowire dictionary
    :return: Baseball Reference team abbreviation
    """
    if rotowire_team_dict[full_team_name] == "Los Angeles Angels":
        team = baseball_reference_team_dict.inv["Los Angeles Angels of Anaheim"]
    else:
        team = baseball_reference_team_dict.inv[rotowire_team_dict[full_team_name]]
    # team = team_name_dict[full_team_name]

    return team
