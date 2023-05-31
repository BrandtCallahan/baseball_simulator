from random import uniform


# run through the lineup
def Lineup(game_number,
           matchup_list,
           lineup_stats,
           away_home_lineup,
           pitching_matchup_stats,
           away_home_pitcher,
           batter,
           pitchcount):
    """

    Parameters
    ----------
    game_number: int
        Integer used as an index for the matchup, lineups, and pitchers
    matchup_list: list
        List of team matchups (i.e. [ATL, LAD]
    lineup_stats: list
        Team batting lineups with batter statistics
    away_home_lineup: int
        Integer that signifies away or home lineup (0 = away lineup, 1 = home lineup)
    pitching_matchup_stats: list
        Team pitching matchups with pitcher statistics
    away_home_pitcher: int
        Integer that signifies away or home pitcher (0 = away pitcher, 1 = home pitcher)
    batter: int
        Integer that signifies what batter is up, will be index for statistics to use
    pitchcount: int
        Number of pitches the pitcher has thrown so far in the game

    Returns
    -------
    list[int, int, int, int, int, int, int, int]
    list[strikeout (0/1), groundout (0/1), flyout (0/1), walk (0/1), hit (0/1), abpitchcount, batter index, starter/relief index]

    """

    game = lineup_stats
    matchup = [matchup_list[game_number][0], matchup_list[game_number][1]]
    lineup = game[game_number][away_home_lineup]
    pitching_matchup = [pitching_matchup_stats[game_number][away_home_lineup][0][0],
                        pitching_matchup_stats[game_number][away_home_pitcher][0][0]]
    team = matchup[away_home_pitcher]
    pitcher = pitching_matchup_stats[game_number][away_home_pitcher][0]

    if pitchcount <= 80:
        atbat = AtBat(lineup[batter][1], pitcher[1]) + [batter] + [0]  # starter
    else:
        atbat = AtBat(lineup[batter][1], pitcher[3]) + [batter] + [1]  # relief (median of bullpen WHIP)

    return atbat


# this function lays out the groundwork for an atbat to take place
def AtBat(obp, whip):
    """

    Parameters
    ----------
    obp: float
        Hitter's On-Base Percentage
    whip: float
        Pitcher's Walks and Hits per Innings Pitched

    Returns
    -------
    list[int, int, int, int, int, int]
    list[strikeout, groundout, flyout, walk, hit, abpitchcount]

    """
    strike = 0
    ball = 0
    out = 0
    ob = 0
    count = [ball] + [strike]
    abpitchcount = 0
    strikeout = 0
    groundout = 0
    flyout = 0
    walk = 0
    hit = 0

    pitchlist = []
    swinglist = []
    contactlist = []
    fairlist = []
    outcomelist = []

    aboutcome = []

    while (ball < 4 and strike < 3) and (out < 1 and ob < 1):
        pitch = (uniform(0, 3))  # ball/strike
        swing = (uniform(0, 1))  # swing/no swing
        contact = (uniform(0, 1))  # contact/miss
        fair = (uniform(0, 1))  # fair/foul
        outcome = uniform(0, 1)  # hit/out

        umperror = 0.05

        # These percentages were found online
        # https://www.beyondtheboxscore.com/2014/6/4/5776990/swing-rate-ball-strike-counts-swinging-strikes
        count_dict = {
            "count00": {
                "noswing": 0.75,  # no swing perc.
                "whiff": 0.05,  # swing and miss perc.
                "contact": 0.39,  # foul perc.
            },
            "count01": {
                "noswing": 0.53,
                "whiff": 0.10,
                "contact": 0.38,
            },
            "count02": {
                "noswing": 0.5,
                "whiff": 0.12,
                "contact": 0.39,
            },
            "count10": {
                "noswing": 0.59,
                "whiff": 0.07,
                "contact": 0.39,
            },
            "count11": {
                "noswing": 0.47,
                "whiff": 0.10,
                "contact": 0.39,
            },
            "count12": {
                "noswing": 0.42,
                "whiff": 0.13,
                "contact": 0.39,
            },
            "count20": {
                "noswing": 0.61,
                "whiff": 0.06,
                "contact": 0.4,
            },
            "count21": {
                "noswing": 0.41,
                "whiff": 0.10,
                "contact": 0.4,
            },
            "count22": {
                "noswing": 0.34,
                "whiff": 0.12,
                "contact": 0.4,
            },
            "count30": {
                "noswing": 0.94,
                "whiff": 0.008,
                "contact": 0.41,
            },
            "count31": {
                "noswing": 0.45,
                "whiff": 0.08,
                "contact": 0.4,
            },
            "count32": {
                "noswing": 0.26,
                "whiff": 0.11,
                "contact": 0.41,
            },
        }

        pitchnum = 1

        # new_pitch = Pitch(count, pitch, whip, obp, swing, contact, fair, outcome, umperror, count_dict)
        count_var = f"{ball}{strike}"

        if pitch < whip:  # ball
            if swing <= umperror:  # ump calls ball strike
                strike += 1
            elif swing > umperror and swing < count_dict[f"count{count_var}"]["noswing"]:  # no swing
                ball += 1
            elif swing > umperror and swing >= count_dict[f"count{count_var}"]["noswing"]:  # swing
                if contact < count_dict[f"count{count_var}"]["whiff"]:  # miss
                    strike += 1
                elif contact >= count_dict[f"count{count_var}"]["whiff"]:  # contact
                    if fair < count_dict[f"count{count_var}"]["contact"]:  # foul
                        if count[1] < 2:
                            strike += 1
                        elif count[1] == 2:
                            strike += 0
                    elif fair >= count_dict[f"count{count_var}"]["contact"]:  # fair
                        if outcome > obp:
                            out = 1
                            ob = 0
                        if outcome <= obp:
                            out = 0
                            ob = 1

        elif pitch >= whip:  # strike
            if swing <= umperror:  # ump calls strike ball
                ball += 1
            elif swing > umperror and swing < count_dict[f"count{count_var}"]["noswing"]:  # no swing
                strike += 1
            elif swing > umperror and swing >= count_dict[f"count{count_var}"]["noswing"]:  # swing
                if contact < count_dict[f"count{count_var}"]["whiff"]:  # miss
                    strike += 1
                elif contact >= count_dict[f"count{count_var}"]["whiff"]:  # contact
                    if fair < count_dict[f"count{count_var}"]["contact"]:  # foul
                        if count[1] < 2:
                            strike += 1
                        elif count[1] == 2:
                            strike += 0
                    elif fair >= count_dict[f"count{count_var}"]["contact"]:  # fair
                        if outcome > obp:
                            out = 1
                            ob = 0
                        if outcome <= obp:
                            out = 0
                            ob = 1

        count = [ball] + [strike]

        pitchlist += [pitch]
        swinglist += [swing]
        contactlist += [contact]
        fairlist += [fair]
        outcomelist += [outcome]

        abpitchcount += pitchnum

        aboutcome = [out, ob]

    if count[1] == 3:
        strikeout = 1
        out = 1
    elif count[1] < 3 and aboutcome[0] == 1:
        outtype = int(uniform(0, 11))
        if outtype <= 6:
            groundout = 1
            out = 1
        elif outtype > 6:
            flyout = 1
            out = 1
    elif count[0] == 4:
        walk = 1
        ob = 1
    elif aboutcome[1] == 1:
        hit = 1
        ob = 1

    ab = [strikeout, groundout, flyout, walk, hit, abpitchcount]

    return ab


# this lays the groundwork for baserunners moving around the bases
# it is atbat specific

def baserunning(game_number, lineup_stats, aPOSlist, atbat, batter, away_home_lineup):
    """
    Function that aims to provide the work of having baserunners move around the bases on different scenarios

    Parameters
    ----------
    game_number: int
        Integer used as an index for the matchup, lineups, and pitchers
    lineup_stats: list
        Team batting lineups with batter statistics
    aPOSlist: list
        List of where runners are on base (i.e. [0, 1, 0] is a runner on second)
    atbat: list
        List returning the result of the at-bat (i.e. hit, walk, or out)
    batter: int
        Integer that signifies what batter is up, will be index for statistics to use
    away_home_lineup: int
        Integer that signifies away or home lineup (0 = away lineup, 1 = home lineup)

    Returns
    -------
    list[list, int]

    """

    single = lineup_stats[game_number][away_home_lineup][batter][3]
    double = lineup_stats[game_number][away_home_lineup][batter][4] + single
    triple = lineup_stats[game_number][away_home_lineup][batter][5] + (single + double)
    homer = lineup_stats[game_number][away_home_lineup][batter][6] + (single + double + triple)
    basesruns = []
    SLG = atbat[2]

    if aPOSlist == [0, 0, 0]:
        if atbat[0] == 1:
            POSlist = [1, 0, 0]
            rs = 0
        elif atbat[1] == 1:
            if SLG <= single:  # nobody on and a single/walk
                POSlist = [1, 0, 0]
                rs = 0
            elif SLG <= double and SLG > single:  # nobody on and a double
                POSlist = [0, 1, 0]
                rs = 0
            elif SLG <= triple and SLG > double:  # nobody on and a triple
                POSlist = [0, 0, 1]
                rs = 0
            elif SLG <= homer and SLG > triple:  # nobody on and a homerun
                POSlist = [0, 0, 0]
                rs = 1

    elif aPOSlist == [1, 0, 0]:
        if atbat[0] == 1:
            POSlist = [1, 1, 0]
            rs = 0
        elif atbat[1] == 1:
            if SLG <= single:  # man on first and single/walk
                POSlist = [1, 1, 0]
                rs = 0
            elif SLG <= double and SLG > single:  # man on first and double
                POSlist = [0, 1, 1]
                rs = 0
            elif SLG <= triple and SLG > double:  # man on first and triple
                POSlist = [0, 0, 1]
                rs = 1
            elif SLG <= homer and SLG > triple:  # man on first and homerun
                POSlist = [0, 0, 0]
                rs = 2

    elif aPOSlist == [1, 1, 0]:
        if atbat[0] == 1:  # man on first and second and walk
            POSlist = [1, 1, 1]
            rs = 0
        elif atbat[1] == 1:
            if SLG <= single:  # man on first and second and single
                POSlist = [1, 1, 0]
                rs = 1
            elif SLG <= double and SLG > single:  # man on first and second and double
                POSlist = [0, 1, 1]
                rs = 1
            elif SLG <= triple and SLG > double:  # man on first and second and triple
                POSlist = [0, 0, 1]
                rs = 2
            elif SLG <= homer and SLG > triple:  # man on first and second and homerun
                POSlist = [0, 0, 0]
                rs = 3

    elif aPOSlist == [1, 0, 1]:
        if atbat[0] == 1:  # man on first and third and walk
            POSlist = [1, 1, 1]
            rs = 0
        elif atbat[1] == 1:
            if SLG <= single:  # man on first and third and single
                POSlist = [1, 1, 0]
                rs = 1
            elif SLG <= double and SLG > single:  # man on first and third and double
                POSlist = [0, 1, 1]
                rs = 1
            elif SLG <= triple and SLG > double:  # man on first and third and triple
                POSlist = [0, 0, 1]
                rs = 2
            elif SLG <= homer and SLG > triple:  # man on first and third and homerun
                POSlist = [0, 0, 0]
                rs = 3

    elif aPOSlist == [0, 1, 0]:
        if atbat[0] == 1:  # man on second and walk
            POSlist = [1, 1, 0]
            rs = 0
        elif atbat[1] == 1:
            if SLG <= single:  # man on second and single
                POSlist = [1, 0, 1]
                rs = 0
            elif SLG <= double and SLG > single:  # man on second and double
                POSlist = [0, 1, 0]
                rs = 1
            elif SLG <= triple and SLG > double:  # man on second and triple
                POSlist = [0, 0, 1]
                rs = 2
            elif SLG <= homer and SLG > triple:  # man on second and homerun
                POSlist = [0, 0, 0]
                rs = 3

    elif aPOSlist == [0, 1, 1]:
        if atbat[0] == 1:  # man on second and third and walk
            POSlist = [1, 1, 1]
            rs = 0
        elif atbat[1] == 1:
            if SLG <= single:  # man on second and third and single
                POSlist = [1, 0, 1]
                rs = 1
            elif SLG <= double and SLG > single:  # man on second and third and double
                POSlist = [0, 1, 0]
                rs = 2
            elif SLG <= triple and SLG > double:  # man on second and third and triple
                POSlist = [0, 0, 1]
                rs = 2
            elif SLG <= homer and SLG > triple:  # man on second and third and homerun
                POSlist = [0, 0, 0]
                rs = 3

    if aPOSlist == [0, 0, 1]:
        if atbat[0] == 1:  # man on third and walk
            POSlist = [1, 0, 1]
            rs = 0
        elif atbat[1] == 1:
            if SLG <= single:  # man on third and single
                POSlist = [1, 0, 0]
                rs = 1
            elif SLG <= double and SLG > single:  # man on third and double
                POSlist = [0, 1, 0]
                rs = 1
            elif SLG <= triple and SLG > double:  # man on third and triple
                POSlist = [0, 0, 1]
                rs = 1
            elif SLG <= homer and SLG > triple:  # man on third and homerun
                POSlist = [0, 0, 0]
                rs = 2

    if aPOSlist == [1, 1, 1]:
        if atbat[0] == 1:  # bases loaded and walk
            POSlist = [1, 1, 1]
            rs = 1
        elif atbat[1] == 1:
            if SLG <= single:  # bases loaded and single
                POSlist = [1, 1, 0]
                rs = 2
            elif SLG <= double and SLG > single:  # bases loaded and double
                POSlist = [0, 1, 1]
                rs = 2
            elif SLG <= triple and SLG > double:  # bases loaded and triple
                POSlist = [0, 0, 1]
                rs = 3
            elif SLG <= homer and SLG > triple:  # bases loaded and homerun
                POSlist = [0, 0, 0]
                rs = 4

    basesruns = [POSlist, rs]
    return basesruns
