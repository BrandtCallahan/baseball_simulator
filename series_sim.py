import random
from random import uniform
import pandas as pd
from datetime import date
from logzero import logger

from inning_utils import Lineup, AtBat, baserunning
from game_utils import inning, gameboard


# lays the ground work to give us totals on a single game

def truegamesim(game_number, lineup_stats, pitching_matchup_stats):
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

    scoreboard1 = gameboard(game_number, 0, lineup_stats,
                            pitching_matchup_stats)  # runs team 1 gameboard (first 8 innings)
    scoreboard2 = gameboard(game_number, 1, lineup_stats,
                            pitching_matchup_stats)  # runs team 2 gameboard (first 8 innings)

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
    BBtotal1 += [BBt1]
    B1total1 += [B1t1]
    B2total1 += [B2t1]
    B3total1 += [B3t1]
    HRtotal1 += [HRt1]
    LOBt1 = scoreboard1[7]
    LOBtotal1 += [LOBt1]

    Kt1 = scoreboard1[8]
    Ktotal1 += [Kt1]
    GOt1 = scoreboard1[9]
    GOtotal1 += [GOt1]
    FOt1 = scoreboard1[10]
    FOtotal1 += [FOt1]

    PCt1 = scoreboard1[11]
    PCtotal1 += [PCt1]

    # total offensive stats for team 2
    BBt2 = scoreboard2[2]
    B1t2 = scoreboard2[3]
    B2t2 = scoreboard2[4]
    B3t2 = scoreboard2[5]
    HRt2 = scoreboard2[6]
    BBtotal2 += [BBt2]
    B1total2 += [B1t2]
    B2total2 += [B2t2]
    B3total2 += [B3t2]
    HRtotal2 += [HRt2]
    LOBt2 = scoreboard2[7]
    LOBtotal2 += [LOBt2]

    Kt2 = scoreboard2[8]
    Ktotal2 += [Kt2]
    GOt2 = scoreboard2[9]
    GOtotal2 += [GOt2]
    FOt2 = scoreboard2[10]
    FOtotal2 += [FOt2]

    PCt2 = scoreboard2[11]
    PCtotal2 += [PCt2]

    i = 9  # sets an index that will come in play later
    sb = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # sets up our inning list

    hrl1 = inning(game_number, lineup_stats, 0, pitching_matchup_stats, 1, scoreboard1[-1])  # call the inning to run
    ri1 = hrl1[0]  # index out the runs
    r1 = ri1  # makes the road team (first listed) have their 9th AB
    rg1 += [r1]  # adds their runs to the run list
    hi1 = hrl1[1]  # hits from inning
    h1 += [hi1]  # add to hit list

    # team 1 top offensive stats for top of 9th
    BBt1 = hrl1[2]
    B1t1 = hrl1[3]
    B2t1 = hrl1[4]
    B3t1 = hrl1[5]
    HRt1 = hrl1[6]
    BBtotal1 += [BBt1]
    B1total1 += [B1t1]
    B2total1 += [B2t1]
    B3total1 += [B3t1]
    HRtotal1 += [HRt1]
    LOBt1 = hrl1[7]
    LOBtotal1 += [LOBt1]

    Kt1 = hrl1[8]
    Ktotal1 += [Kt1]
    GOt1 = hrl1[9]
    GOtotal1 += [GOt1]
    FOt1 = hrl1[10]
    FOtotal1 += [FOt1]

    PCt1 = hrl1[11]
    PCtotal1 += [PCt1]

    # runs if needed
    if sum(rg1) >= sum(rg2):  # keeps the bottom of 9th optional
        hrl2 = inning(game_number, lineup_stats, 1, pitching_matchup_stats, 0,
                      scoreboard2[-1])  # call the inning for team two
        ri2 = hrl2[0]  # index out the runs
        r2 = ri2  # if played runs the 9th for team 2 (home team)
        rg2 += [r2]  # adds their runs to the runs list
        hi2 = hrl2[1]  # hits from inning
        h2 += [hi2]  # add to hit list

        # team 2 offensive statistics
        BBt2 = hrl2[2]
        B1t2 = hrl2[3]
        B2t2 = hrl2[4]
        B3t2 = hrl2[5]
        HRt2 = hrl2[6]
        BBtotal2 += [BBt2]
        B1total2 += [B1t2]
        B2total2 += [B2t2]
        B3total2 += [B3t2]
        HRtotal2 += [HRt2]
        LOBt2 = hrl2[7]
        LOBtotal2 += [LOBt2]

        Kt2 = hrl2[8]
        Ktotal2 += [Kt2]
        GOt2 = hrl2[9]
        GOtotal2 += [GOt2]
        FOt2 = hrl2[10]
        FOtotal2 += [FOt2]

        PCt2 = hrl2[11]
        PCtotal2 += [PCt2]

    # runs as long as run totals are equal
    while sum(rg1) == sum(rg2):  # creates an extra inning parameter
        i += 1  # index that adds 1 to the already made inning list
        hrl1 = inning(game_number, lineup_stats, 0, pitching_matchup_stats, 1,
                      scoreboard2[-1])  # an extra inning for team 1
        hrl2 = inning(game_number, lineup_stats, 1, pitching_matchup_stats, 0,
                      scoreboard2[-1])  # an extra inning for team 2
        ri1 = hrl1[0]  # index runs for team 1
        ri2 = hrl2[0]  # index runs for team 2
        r1 = ri1
        r2 = ri2
        rg1 += [r1]  # adds the runs to the run list for both teams
        rg2 += [r2]
        sb += [i]  # adds to the inning list

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
        BBtotal1 += [BBt1]
        B1total1 += [B1t1]
        B2total1 += [B2t1]
        B3total1 += [B3t1]
        HRtotal1 += [HRt1]
        LOBt1 = hrl1[7]
        LOBtotal1 += [LOBt1]
        Kt1 = hrl1[8]
        Ktotal1 += [Kt1]
        GOt1 = hrl1[9]
        GOtotal1 += [GOt1]
        FOt1 = hrl1[10]
        FOtotal1 += [FOt1]
        PCt1 = hrl1[11]
        PCtotal1 += [PCt1]

        BBt2 = hrl2[2]
        B1t2 = hrl2[3]
        B2t2 = hrl2[4]
        B3t2 = hrl2[5]
        HRt2 = hrl2[6]
        BBtotal2 += [BBt2]
        B1total2 += [B1t2]
        B2total2 += [B2t2]
        B3total2 += [B3t2]
        HRtotal2 += [HRt2]
        LOBt2 = hrl2[7]
        LOBtotal2 += [LOBt2]
        Kt2 = hrl2[8]
        Ktotal2 += [Kt2]
        GOt2 = hrl2[9]
        GOtotal2 += [GOt2]
        FOt2 = hrl2[10]
        FOtotal2 += [FOt2]
        PCt2 = hrl2[11]
        PCtotal2 += [PCt2]

    # gives us a returnable value to analyze over multiple games
    if sum(rg1) > sum(rg2):  # team 1 win
        tw = [1, sum(rg1), sum(BBtotal1), sum(B1total1), sum(B2total1), sum(B3total1), sum(HRtotal1), sum(LOBtotal1),
              sum(Ktotal1), sum(GOtotal1), sum(FOtotal1), sum(PCtotal1), sum(rg2), sum(BBtotal2), sum(B1total2),
              sum(B2total2), sum(B3total2), sum(HRtotal2), sum(LOBtotal2), sum(Ktotal2), sum(GOtotal2), sum(FOtotal2),
              sum(PCtotal2)]
    else:  # team 2 win
        tw = [2, sum(rg1), sum(BBtotal1), sum(B1total1), sum(B2total1), sum(B3total1), sum(HRtotal1), sum(LOBtotal1),
              sum(Ktotal1), sum(GOtotal1), sum(FOtotal1), sum(PCtotal1), sum(rg2), sum(BBtotal2), sum(B1total2),
              sum(B2total2), sum(B3total2), sum(HRtotal2), sum(LOBtotal2), sum(Ktotal2), sum(GOtotal2), sum(FOtotal2),
              sum(PCtotal2)]

    return tw


# runs the simulation n number of times
def simulation(n, game_number, lineup_stats, pitching_matchup_stats):
    team1name = lineup_stats[0][0][0]
    team2name = lineup_stats[1][0][0]

    RUNtotal1 = []
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

    RUNtotal2 = []
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

    tt1w = 0  # team 1 win total
    tt2w = 0  # team 2 win total

    for w in range(n):  # run as many times as the user wants with n (inputted in function call)

        tw1 = 0  # team 1 win
        tw2 = 0  # team 2 win

        g = truegamesim(game_number, lineup_stats, pitching_matchup_stats)  # assign function truegame to variable g
        # run g (truegamesim function)

        # team 1 stats per game
        RUNt1 = g[1]
        BBt1 = g[2]
        B1t1 = g[3]
        B2t1 = g[4]
        B3t1 = g[5]
        HRt1 = g[6]
        LOBt1 = g[7]
        Kt1 = g[8]
        GOt1 = g[9]
        FOt1 = g[10]
        PCt1 = g[11]

        # team 2 stats per game
        RUNt2 = g[12]
        BBt2 = g[13]
        B1t2 = g[14]
        B2t2 = g[15]
        B3t2 = g[16]
        HRt2 = g[17]
        LOBt2 = g[18]
        Kt2 = g[19]
        GOt2 = g[20]
        FOt2 = g[21]
        PCt2 = g[22]

        if g[0] == 1:  # if 1 is returned from that run
            tw1 = 1  # then team 1 won so give them 1

        elif g[0] == 2:  # if anything else is returned
            tw2 = 1  # then team 2 won so give them 1

        tt1w = tt1w + tw1  # add up team 1 wins
        tt2w = tt2w + tw2  # add up team 2 wins

        # total team 1 statistics
        RUNtotal1 = RUNtotal1 + [RUNt1]
        BBtotal1 = BBtotal1 + [BBt1]
        B1total1 = B1total1 + [B1t1]
        B2total1 = B2total1 + [B2t1]
        B3total1 = B3total1 + [B3t1]
        HRtotal1 = HRtotal1 + [HRt1]
        LOBtotal1 = LOBtotal1 + [LOBt1]
        Ktotal1 = Ktotal1 + [Kt1]
        GOtotal1 = GOtotal1 + [GOt1]
        FOtotal1 = FOtotal1 + [FOt1]
        PCtotal1 = PCtotal1 + [PCt1]

        # total team 2 statistics
        RUNtotal2 = RUNtotal2 + [RUNt2]
        BBtotal2 = BBtotal2 + [BBt2]
        B1total2 = B1total2 + [B1t2]
        B2total2 = B2total2 + [B2t2]
        B3total2 = B3total2 + [B3t2]
        HRtotal2 = HRtotal2 + [HRt2]
        LOBtotal2 = LOBtotal2 + [LOBt2]
        Ktotal2 = Ktotal2 + [Kt2]
        GOtotal2 = GOtotal2 + [GOt2]
        FOtotal2 = FOtotal2 + [FOt2]
        PCtotal2 = PCtotal2 + [PCt2]

    return [team1name, tt1w, team2name, tt2w, n, int(sum(RUNtotal1) / n), int(sum(RUNtotal2) / n),
            round(float(sum(Ktotal1) / n), 2), round(float(sum(Ktotal2) / n), 2)]


def series_simulation(lineup_stats, pitching_matchup_stats):
    series = []
    for game_num in range(3):
        logger.info(f"Game {game_num + 1} of {lineup_stats[0][0][0]} vs. {lineup_stats[1][0][0]}")
        sim_game = simulation(5000, game_num + 1, lineup_stats, pitching_matchup_stats)

        if sim_game[1] > sim_game[3]:
            print(
                f"{sim_game[0]} won game {game_num + 1} {round(float(sim_game[1] / sim_game[4]), 2) * 100}% of the time.")
            print(f"{pitching_matchup_stats[0][game_num][1]} is the winning pitcher.")
            print(f"{pitching_matchup_stats[1][game_num][1]} is the losing pitcher.")
        else:
            print(
                f"{sim_game[2]} won game {game_num + 1} {round(float(sim_game[3] / sim_game[4]), 2) * 100}% of the time.")
            print(f"{pitching_matchup_stats[1][game_num][1]} is the winning pitcher.")
            print(f"{pitching_matchup_stats[0][game_num][1]} is the losing pitcher.")

        series += [sim_game]

    return series
