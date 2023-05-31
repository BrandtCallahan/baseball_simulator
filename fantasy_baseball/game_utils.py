from random import uniform

from inning_utils import Lineup, baserunning


# now we set the groundwork for an inning to take place
def inning(
        game_number,
        matchup_list,
        lineup_stats,
        away_home_lineup,
        pitching_matchup_stats,
        away_home_pitcher,
        batter_stats,
        pitcher_stats,
        batter=None,
):
    o = 0  # outs start at 0
    aPOSlist = [0, 0, 0]  # start with nobody on
    POSLIST = []  # list of runners moving around bases

    ht = 0  # hit total
    rt = 0  # run total
    rs = 0  # run scored
    rlist = []  # list of runs and when/how scored
    LOB = 0  # men left on base

    walkt = 0  # walk total
    singlet = 0  # single total
    doublet = 0  # double total
    triplet = 0  # triple total
    homerunt = 0  # homerun total

    strikeoutt = 0  # strikeout total
    groundoutt = 0  # groundout total
    flyoutt = 0  # flyout total

    pitchcount = 0
    atbatlist = []  # list the atbat outcomes in order

    if batter is None:
        batter = 0

    while o < 3:  # inning continues as long as there are less than 3 outs

        # logger.info(f"{lineup_stats[away_home_lineup][batter][1]} is now batting with {o} outs")

        # player SLG
        single_num = (lineup_stats[game_number][away_home_lineup][batter][3])
        double_num = (lineup_stats[game_number][away_home_lineup][batter][4] + single_num)
        triple_num = (lineup_stats[game_number][away_home_lineup][batter][5] + (double_num))
        homer_num = (lineup_stats[game_number][away_home_lineup][batter][6] + (triple_num))
        total_hits = 0
        for i in range(3, 7):
            total_hits += lineup_stats[game_number][away_home_lineup][batter][i]
        if total_hits == 0:
            single = 0.65
            double = single + 0.2
            triple = double + 0.02
            homer = triple + 0.13
        else:
            single = (lineup_stats[game_number][away_home_lineup][batter][3]) / total_hits
            double = (lineup_stats[game_number][away_home_lineup][batter][4] + single_num) / total_hits
            triple = (lineup_stats[game_number][away_home_lineup][batter][5] + (double_num)) / total_hits
            homer = (lineup_stats[game_number][away_home_lineup][batter][6] + (triple_num)) / total_hits

        AB = Lineup(game_number,
                    matchup_list,
                    lineup_stats,
                    away_home_lineup,
                    pitching_matchup_stats,
                    away_home_pitcher,
                    batter,
                    pitchcount)

        # at bat: strikeout, groundout, flyout, walk, hit, pitchcount, batter num
        pitchnum = AB[5]

        abSLG = uniform(0, 1)  # create the SLG % value

        atbat = [AB[3], AB[4], abSLG]  # pairs up the OBP (hit/no hit) and SLG (hit type)
        # abl += [atbat] # list the hits in order of occurance
        abWALK = atbat[0]
        abHIT = atbat[1]
        SLG = atbat[2]

        if abWALK == 1:
            y = 0
            h = 0  # walk(BB)/HBP
            walkt += 1
            atbatlist += ["walk"]
            # aPOSlist=[1,0,0]
        elif abHIT == 1:
            if SLG <= single:  # single liklihood
                y = 0
                h = 1  # single
                singlet += 1
                atbatlist += ["single"]
                # aPOSlist=[1,0,0]
            elif (SLG > single) or (SLG <= double):  # double liklihood
                y = 0
                h = 1  # double
                doublet += 1
                atbatlist += ["double"]
                # aPOSlist=[0,1,0]
            elif (SLG > double) or (SLG <= triple):  # triple liklihood
                y = 0
                h = 1  # triple
                triplet += 1
                atbatlist += ["triple"]
                # aPOSlist=[0,0,1]
            elif (SLG > triple) or (SLG <= homer):  # homerun liklihood
                y = 0
                h = 1
                atbatlist += ["homerun"]
                # aPOSlist=[0,0,0]
                homerunt += 1
        elif abWALK == 0 and abHIT == 0:  # obp is set up outside of the loop
            h = 0  # since out, no hit
            if AB[0] == 1:
                y = 1  # add an out
                strikeoutt += 1
                atbatlist += ['strikeout']
                if POSLIST == []:
                    aPOSlist = [0, 0, 0]
                    rs = 0
                else:
                    aPOSlist = POSLIST[-1]  # return the previous baserunner list
                    rs = 0
            elif AB[1] == 1:
                y = 1  # add an out
                groundoutt = groundoutt + 1
                atbatlist = atbatlist + ['groundout']
                if POSLIST == []:
                    aPOSlist = [0, 0, 0]
                    rs = 0
                else:
                    aPOSlist = POSLIST[-1]  # return the previous baserunner list
                    rs = 0
            elif AB[2] == 1:
                y = 1  # add an out
                flyoutt = flyoutt + 1
                atbatlist = atbatlist + ['flyout']
                if POSLIST == []:
                    aPOSlist = [0, 0, 0]
                    rs = 0
                else:
                    aPOSlist = POSLIST[-1]  # return the previous baserunner list
                    rs = 0

        if abWALK == 1 or abHIT == 1:
            baserun = baserunning(game_number, lineup_stats, aPOSlist, atbat, batter, away_home_lineup)
            aPOSlist = baserun[
                0]  # index out where players are on base shown in list form (i.e. [1,0,0] = man on first)
            rs = baserun[1]  # index out the runs scored

        POSLIST = POSLIST + [aPOSlist]  # creates a list to keep track of where runners are on base after each new atbat

        rlist = rlist + [rs]  # list of runs scoring
        LOB = sum(POSLIST[-1])
        rt = rt + rs  # run total
        ht = ht + h  # hit total
        o = o + y  # out total
        pitchcount = pitchcount + pitchnum

        # batting stats: K, GO, FO, BB, 1B, 2B, 3B, HR, RBI
        ab_outcome = atbatlist.pop(0)
        batter_stat = batter_stats[lineup_stats[game_number][away_home_lineup][batter][0]]
        pitcher_stat = pitcher_stats[pitching_matchup_stats[game_number][away_home_pitcher][0][0]]

        B_K = batter_stat[0]
        B_GO = batter_stat[1]
        B_FO = batter_stat[2]
        B_BB = batter_stat[3]
        B_B1 = batter_stat[4]
        B_B2 = batter_stat[5]
        B_B3 = batter_stat[6]
        B_HR = batter_stat[7]
        B_RBI = batter_stat[8]

        P_K = pitcher_stat[0]
        P_BB = pitcher_stat[1]
        P_B1 = pitcher_stat[2]
        P_B2 = pitcher_stat[3]
        P_B3 = pitcher_stat[4]
        P_HR = pitcher_stat[5]
        P_RA = pitcher_stat[6]
        P_ER = pitcher_stat[7]
        P_IP = pitcher_stat[8]

        if ab_outcome == "strikeout":
            B_K += 1
            P_K += 1
        elif ab_outcome == "groundout":
            B_GO += 1
        elif ab_outcome == "flyout":
            B_FO += 1
        elif ab_outcome == "walk":
            B_BB += 1
            P_BB += 1
        elif ab_outcome == "single":
            B_B1 += 1
            P_B1 += 1
        elif ab_outcome == "double":
            B_B2 += 1
            P_B2 += 1
        elif ab_outcome == "triple":
            B_B3 += 1
            P_B3 += 1
        elif ab_outcome == "homerun":
            B_HR += 1
            P_HR += 1

        if rs > 0:
            B_RBI += rs
            P_ER += rs  # right now all runs allowed are earned (haven't yet included errors)
            P_RA += rs
        else:
            B_RBI += 0
            P_ER += 0
            P_RA += 0

        if y == 1:
            if AB[7] == 0:
                P_IP += 0.333
            else:
                P_IP += 0
        else:
            P_IP += 0

        batter_stat_line = [B_K, B_GO, B_FO, B_BB, B_B1, B_B2, B_B3, B_HR, B_RBI]
        batter_stats[f"{lineup_stats[game_number][away_home_lineup][batter][0]}"] = batter_stat_line

        pitcher_stat_line = [P_K, P_BB, P_B1, P_B2, P_B3, P_HR, P_RA, P_ER, round(P_IP, 3)]
        pitcher_stats[f"{pitching_matchup_stats[game_number][away_home_pitcher][0][0]}"] = pitcher_stat_line

        if batter < 8:
            batter = batter + 1
        elif batter == 8:
            batter = 0

    off = [rt, ht, walkt, singlet, doublet, triplet, homerunt, LOB, strikeoutt, groundoutt, flyoutt, pitchcount, batter]

    return off


# now the scoreboard to keep track of runs and the inning
# this function only sets up one teams "scoreboard" though
def gameboard(game_number,
              matchup_list,
              away_home_lineup,
              lineup_stats,
              pitching_matchup_stats, ):
    sbi = []  # scoreboard inning
    sbr = []  # scoreboard runs
    sbh = []  # scoreboard on base
    board = []  # final output
    tr = 0  # total runs
    th = 0  # total hits

    BB = []
    B1 = []
    B2 = []
    B3 = []
    HR = []
    LOB = []
    K = []
    GO = []
    FO = []
    PC = []

    if away_home_lineup == 0:
        away_home_pitcher = 1
    elif away_home_lineup == 1:
        away_home_pitcher = 0

    # generate batter stat tracker
    batter_stats = {}
    for batter in lineup_stats[game_number][away_home_lineup]:
        batter_name = batter[0]
        # build dictionary
        batter_stats[f"{batter_name}"] = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # generate pitcher stat tracker
    pitcher_stats = {}
    for pitcher in pitching_matchup_stats[game_number][away_home_pitcher]:
        pitcher_name = pitcher[0]
        # build stats dictionary
        pitcher_stats[f"{pitcher_name}"] = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(1, 9):
        if i == 1:
            batter = 0
        else:
            batter = hrl[12]
        hrl = inning(game_number,
                     matchup_list,
                     lineup_stats,
                     away_home_lineup,
                     pitching_matchup_stats,
                     away_home_pitcher,
                     batter_stats,
                     pitcher_stats,
                     batter)  # hrl = hit/run list
        r = hrl[0]  # index the runs
        h = hrl[1]  # index the amount on base

        # types of hits (index out)
        bb = hrl[2]
        b1 = hrl[3]
        b2 = hrl[4]
        b3 = hrl[5]
        hr = hrl[6]

        # runners left on base (index out)
        lob = hrl[7]

        # types of outs
        k = hrl[8]
        go = hrl[9]
        fo = hrl[10]

        # pitch count
        pc = hrl[11]

        # list of stats
        BB = BB + [bb]
        B1 = B1 + [b1]
        B2 = B2 + [b2]
        B3 = B3 + [b3]
        HR = HR + [hr]
        LOB = LOB + [lob]
        K = K + [k]
        GO = GO + [go]
        FO = FO + [fo]
        PC = PC + [pc]

        # total up the lists of stats
        BBtotal = sum(BB)
        B1total = sum(B1)
        B2total = sum(B2)
        B3total = sum(B3)
        HRtotal = sum(HR)
        LOBtotal = sum(LOB)
        Ktotal = sum(K)
        GOtotal = sum(GO)
        FOtotal = sum(FO)
        PCtotal = sum(PC)

        tr = tr + r  # totals up how many runs scored
        th = th + h  # totals up hits
        sbi = sbi + [i]  # inning list to get horizontal
        sbr = sbr + [r]  # run list to get horizontal
        sbh = sbh + [h]  # hit list
        board = [sbr, sbh, BBtotal, B1total, B2total, B3total, HRtotal, LOBtotal, Ktotal, GOtotal, FOtotal, PCtotal]

    board = board + [hrl[-1]]

    return [board, batter_stats, pitcher_stats]
