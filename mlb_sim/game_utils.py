from random import uniform

from inning_utils import Lineup, baserunning


# now we set the groundwork for an inning to take place
def inning(game_number,
           matchup_list,
           lineup_stats,
           away_home_lineup,
           pitching_matchup_stats,
           away_home_pitcher,
           batter=None):

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

        # player SLG %
        single_num = (lineup_stats[game_number][away_home_lineup][batter][3])
        double_num = (lineup_stats[game_number][away_home_lineup][batter][4] + single_num)
        triple_num = (lineup_stats[game_number][away_home_lineup][batter][5] + (double_num))
        homer_num = (lineup_stats[game_number][away_home_lineup][batter][6] + (triple_num))
        total_hits = 0
        for i in range(3, 7):
            total_hits += lineup_stats[game_number][away_home_lineup][batter][i]
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

        # at bat: strikeout,groundout,flyout,walk,hit,pitchcount, batter num
        pitchnum = AB[5]

        abSLG = uniform(0, 1)  # create the SLG % value

        atbat = [AB[3], AB[4], abSLG]  # pairs up the OBP (hit/no hit) and SLG (hit type)
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
              pitching_matchup_stats,):
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

    return board
