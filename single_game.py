from game_utils import inning, gameboard


# this function sets up for two teams to play against each other
def truegame(game_number, lineup_stats, pitching_matchup_stats):
    team1name = lineup_stats[0][0][0]
    team2name = lineup_stats[1][0][0]

    BBtotal1 = []
    B1total1 = []
    B2total1 = []
    B3total1 = []
    HRtotal1 = []
    LOBtotal1 = []
    Ktotal1 = []
    GOtotal1 = []
    FOtotal1 = []
    PCtotal1 = []

    BBtotal2 = []
    B1total2 = []
    B2total2 = []
    B3total2 = []
    HRtotal2 = []
    LOBtotal2 = []
    Ktotal2 = []
    GOtotal2 = []
    FOtotal2 = []
    PCtotal2 = []

    r1 = 0  # team 1 runs
    r2 = 0  # team 2 runs

    scoreboard1 = gameboard(game_number, 0, lineup_stats, pitching_matchup_stats)  # runs team 1 gameboard (first 8 innings)
    scoreboard2 = gameboard(game_number, 1, lineup_stats, pitching_matchup_stats)  # runs team 2 gameboard (first 8 innings)

    rg1 = scoreboard1[0]  # runs for team 1
    rg2 = scoreboard2[0]  # runs for team 2
    h1 = scoreboard1[1]  # hits team 1
    h2 = scoreboard2[1]  # hits team 2

    # total up offensive stats for team 1
    BBt1 = scoreboard1[2]
    B1t1 = scoreboard1[3]
    B2t1 = scoreboard1[4]
    B3t1 = scoreboard1[5]
    HRt1 = scoreboard1[6]
    BBtotal1 = BBtotal1 + [BBt1]
    B1total1 = B1total1 + [B1t1]
    B2total1 = B2total1 + [B2t1]
    B3total1 = B3total1 + [B3t1]
    HRtotal1 = HRtotal1 + [HRt1]
    LOBt1 = scoreboard1[7]
    LOBtotal1 = LOBtotal1 + [LOBt1]

    Kt1 = scoreboard1[8]
    Ktotal1 = Ktotal1 + [Kt1]
    GOt1 = scoreboard1[9]
    GOtotal1 = GOtotal1 + [GOt1]
    FOt1 = scoreboard1[10]
    FOtotal1 = FOtotal1 + [FOt1]

    PCt1 = scoreboard1[11]
    PCtotal1 = PCtotal1 + [PCt1]

    # total offensive stats for team 2
    BBt2 = scoreboard2[2]
    B1t2 = scoreboard2[3]
    B2t2 = scoreboard2[4]
    B3t2 = scoreboard2[5]
    HRt2 = scoreboard2[6]
    BBtotal2 = BBtotal2 + [BBt2]
    B1total2 = B1total2 + [B1t2]
    B2total2 = B2total2 + [B2t2]
    B3total2 = B3total2 + [B3t2]
    HRtotal2 = HRtotal2 + [HRt2]
    LOBt2 = scoreboard2[7]
    LOBtotal2 = LOBtotal2 + [LOBt2]

    Kt2 = scoreboard2[8]
    Ktotal2 = Ktotal2 + [Kt2]
    GOt2 = scoreboard2[9]
    GOtotal2 = GOtotal2 + [GOt2]
    FOt2 = scoreboard2[10]
    FOtotal2 = FOtotal2 + [FOt2]

    PCt2 = scoreboard2[11]
    PCtotal2 = PCtotal2 + [PCt2]

    i = 9  # sets an index that will come in play later
    sb = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # sets up our inning list

    hrl1 = inning(game_number, lineup_stats, 0, pitching_matchup_stats, 1, scoreboard1[-1])  # call the inning to run
    ri1 = hrl1[0]  # index out the runs
    r1 = ri1  # makes the road team (first listed) have their 9th AB
    rg1 = rg1 + [r1]  # adds their runs to the run list
    hi1 = hrl1[1]  # hits from inning
    h1 = h1 + [hi1]  # add to hit list

    # team 1 top offensive stats for top of 9th
    BBt1 = hrl1[2]
    B1t1 = hrl1[3]
    B2t1 = hrl1[4]
    B3t1 = hrl1[5]
    HRt1 = hrl1[6]
    BBtotal1 = BBtotal1 + [BBt1]
    B1total1 = B1total1 + [B1t1]
    B2total1 = B2total1 + [B2t1]
    B3total1 = B3total1 + [B3t1]
    HRtotal1 = HRtotal1 + [HRt1]
    LOBt1 = hrl1[7]
    LOBtotal1 = LOBtotal1 + [LOBt1]

    Kt1 = hrl1[8]
    Ktotal1 = Ktotal1 + [Kt1]
    GOt1 = hrl1[9]
    GOtotal1 = GOtotal1 + [GOt1]
    FOt1 = hrl1[10]
    FOtotal1 = FOtotal1 + [FOt1]

    PCt1 = hrl1[11]
    PCtotal1 = PCtotal1 + [PCt1]

    # runs if needed
    if sum(rg1) >= sum(rg2):  # keeps the bottom of 9th optional
        hrl2 = inning(game_number, lineup_stats, 1, pitching_matchup_stats, 0, scoreboard2[-1])  # call the inning for team two
        ri2 = hrl2[0]  # index out the runs
        r2 = ri2  # if played runs the 9th for team 2 (home team)
        rg2 = rg2 + [r2]  # adds their runs to the runs list
        hi2 = hrl2[1]  # hits from inning
        h2 = h2 + [hi2]  # add to hit list

        # team 2 offensive statistics
        BBt2 = hrl2[2]
        B1t2 = hrl2[3]
        B2t2 = hrl2[4]
        B3t2 = hrl2[5]
        HRt2 = hrl2[6]
        BBtotal2 = BBtotal2 + [BBt2]
        B1total2 = B1total2 + [B1t2]
        B2total2 = B2total2 + [B2t2]
        B3total2 = B3total2 + [B3t2]
        HRtotal2 = HRtotal2 + [HRt2]
        LOBt2 = hrl2[7]
        LOBtotal2 = LOBtotal2 + [LOBt2]

        Kt2 = hrl2[8]
        Ktotal2 = Ktotal2 + [Kt2]
        GOt2 = hrl2[9]
        GOtotal2 = GOtotal2 + [GOt2]
        FOt2 = hrl2[10]
        FOtotal2 = FOtotal2 + [FOt2]

        PCt2 = hrl2[11]
        PCtotal2 = PCtotal2 + [PCt2]

    # runs as long as run totals are equal
    while sum(rg1) == sum(rg2):  # creates an extra inning parameter
        i = i + 1  # index that adds 1 to the already made inning list
        hrl1 = inning(game_number, lineup_stats, 0, pitching_matchup_stats, 1, hrl1[-1])  # an extra inning for team 1
        hrl2 = inning(game_number, lineup_stats, 1, pitching_matchup_stats, 0, hrl2[-1])  # an extra inning for team 2
        ri1 = hrl1[0]  # index runs for team 1
        ri2 = hrl2[0]  # index runs for team 2
        r1 = ri1
        r2 = ri2
        rg1 = rg1 + [r1]  # adds the runs to the run list for both teams
        rg2 = rg2 + [r2]
        sb = sb + [i]  # adds to the inning list

        hi1 = hrl1[1]  # takes the index for hits team 1
        h1 = h1 + [hi1]  # extra inning hits team 1 (adds to list)
        hi2 = hrl2[1]  # takes the index hits team 2
        h2 = h2 + [hi2]  # extra inning hits team 2 (adds to list)

        # total up statistics for each team
        BBt1 = hrl1[2]
        B1t1 = hrl1[3]
        B2t1 = hrl1[4]
        B3t1 = hrl1[5]
        HRt1 = hrl1[6]
        BBtotal1 = BBtotal1 + [BBt1]
        B1total1 = B1total1 + [B1t1]
        B2total1 = B2total1 + [B2t1]
        B3total1 = B3total1 + [B3t1]
        HRtotal1 = HRtotal1 + [HRt1]
        LOBt1 = hrl1[7]
        LOBtotal1 = LOBtotal1 + [LOBt1]
        Kt1 = hrl1[8]
        Ktotal1 = Ktotal1 + [Kt1]
        GOt1 = hrl1[9]
        GOtotal1 = GOtotal1 + [GOt1]
        FOt1 = hrl1[10]
        FOtotal1 = FOtotal1 + [FOt1]
        PCt1 = hrl1[11]
        PCtotal1 = PCtotal1 + [PCt1]

        BBt2 = hrl2[2]
        B1t2 = hrl2[3]
        B2t2 = hrl2[4]
        B3t2 = hrl2[5]
        HRt2 = hrl2[6]
        BBtotal2 = BBtotal2 + [BBt2]
        B1total2 = B1total2 + [B1t2]
        B2total2 = B2total2 + [B2t2]
        B3total2 = B3total2 + [B3t2]
        HRtotal2 = HRtotal2 + [HRt2]
        LOBt2 = hrl2[7]
        LOBtotal2 = LOBtotal2 + [LOBt2]
        Kt2 = hrl2[8]
        Ktotal2 = Ktotal2 + [Kt2]
        GOt2 = hrl2[9]
        GOtotal2 = GOtotal2 + [GOt2]
        FOt2 = hrl2[10]
        FOtotal2 = FOtotal2 + [FOt2]
        PCt2 = hrl2[11]
        PCtotal2 = PCtotal2 + [PCt2]

    # puts the dash in for the home team's final inning since it wasn't played
    if sb[-1] == 9 and sum(rg2[0:8]) > sum(rg1):
        rg2 = rg2 + ["-"]

    # sums up the teams' runs
    if sum(sb) == 45 and rg2[8] == "-":
        rg1 = rg1 + [sum(rg1), sum(h1), sum(LOBtotal1)]
        rg2 = rg2 + [sum(rg2[0:-1]), sum(h2), sum(LOBtotal2)]

    # sums up the teams' runs
    if sum(sb) == 45 and rg2[8] != "-":
        rg1 = rg1 + [sum(rg1), sum(h1), sum(LOBtotal1)]
        rg2 = rg2 + [sum(rg2), sum(h2), sum(LOBtotal2)]

    # sums up the teams' runs
    if sum(sb) > 45:
        rg1 = rg1 + [sum(rg1), sum(h1), sum(LOBtotal1)]
        rg2 = rg2 + [sum(rg2), sum(h2), sum(LOBtotal2)]

    # creates the run total, hit total, and LOB total in the scoreboard
    sb = sb + ["R", "H", "LOB"]

    # TODO: edit this to accomodate gambling odds for games
    # # game favorite
    # betting_info = game_gambling[game_number]
    # game_fav = betting_info[1]
    # over_under = betting_info[3]
    #
    # # money line
    # if rg1[-3] > rg2[-3]:
    #     winner = team1name
    # elif rg2[-3] > rg1[-3]:
    #     winner = team2name
    #
    # if winner == game_fav:
    #     moneyline = "fav"
    # else:
    #     moneyline = "underdog"
    #
    # # over/under
    # total_runs = (rg1[-3] + rg2[-3])
    #
    # if total_runs > over_under:
    #     o_u = "over"
    # elif total_runs < over_under:
    #     o_u = "under"
    # else:
    #     o_u = "push"

    # creates the neat scoreboard output
    for i in range(len(sb)): print(sb[i], end=" ")
    print("")

    for r in range(len(rg1)): print(rg1[r], end=" ")
    print("")

    for r in range(len(rg2)): print(rg2[r], end=" ")
    print("")

    if rg1[-3] > rg2[-3]:
        print(f"{team1name} won", rg1[-3], "to", rg2[-3])

    if rg2[-3] > rg1[-3]:
        print(f"{team2name} won", rg2[-3], "to", rg1[-3])

    # prints out the teams' stat totals

    print(team1name, "totaled:", sum(BBtotal1), "walks,", sum(B1total1), "singles,", sum(B2total1), "doubles,",
          sum(B3total1), "triples, and", sum(HRtotal1), "home runs. Team 1 left", sum(LOBtotal1),
          "men on base. Team 1 struck out", sum(Ktotal1), "times, grounded out", sum(GOtotal1), "times, and flew out",
          sum(FOtotal1), "times. Team 1 threw", sum(PCtotal1), "pitches.")
    print(team2name, "totaled:", sum(BBtotal2), "walks,", sum(B1total2), "singles,", sum(B2total2), "doubles,",
          sum(B3total2), "triples, and", sum(HRtotal2), "home runs. Team 2 left", sum(LOBtotal2),
          "men on base. Team 2 struck out", sum(Ktotal2), "times, grounded out", sum(GOtotal2), "times, and flew out",
          sum(FOtotal2), "times. Team 2 threw", sum(PCtotal2), "pitches.")
