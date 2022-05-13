import random
from random import uniform
import pandas as pd
from datetime import date

# this function lays out the groundwork for an atbat to take place

def AtBat(obp,whip):
    
    strike=0
    ball=0
    pitchnum=0
    out=0
    ob=0
    count=[ball]+[strike]
    abpitchcount=0
    strikeout=0
    groundout=0
    flyout=0
    walk=0
    hit=0
    
    pitchlist=[]
    swinglist=[]
    contactlist=[]
    fairlist=[]
    outcomelist=[]
    
    ab=[]
    aboutcome=[]
    
    while (ball < 4 and strike < 3) and (out < 1 and ob < 1):
    
        pitch=(uniform(0,3)) #ball/strike
        swing=(uniform(0,1)) #swing/no swing
        contact=(uniform(0,1)) #contact/miss
        fair=(uniform(0,1)) #fair/foul
        outcome=uniform(0,1) #hit/out
        
        #need to adjust for counts
        
        umperror=0.1
        
        #These percentages were found online
        
        bat=0.75 #no swing perc.
        whiff=0.2 #swing and miss perc.
        inplay=0.39 #foul perc.
        
        bat01=0.53 #no swing perc.
        whiff01=0.22 #swing and miss perc.
        inplay01=0.38 #foul perc.
        
        bat02=0.5 #no swing perc.
        whiff02=0.25 #swing and miss perc.
        inplay02=0.39 #foul perc.
        
        bat10=0.59 #no swing perc.
        whiff10=0.19 #swing and miss perc.
        inplay10=0.39 #foul perc.
        
        bat11=0.47 #no swing perc.
        whiff11=0.2 #swing and miss perc.
        inplay11=0.39 #foul perc.
        
        bat12=0.42 #no swing perc.
        whiff12=0.22 #swing and miss perc.
        inplay12=0.39 #foul perc.
        
        bat20=0.61 #no swing perc.
        whiff20=0.15 #swing and miss perc.
        inplay20=0.4 #foul perc.
        
        bat21=0.41 #no swing perc.
        whiff21=0.17 #swing and miss perc.
        inplay21=0.4 #foul perc.
        
        bat22=0.34 #no swing perc.
        whiff22=0.19 #swing and miss perc.
        inplay22=0.4 #foul perc.
        
        bat30=0.94 #no swing perc.
        whiff30=0.12 #swing and miss perc.
        inplay30=0.41 #foul perc.
        
        bat31=0.45 #no swing perc.
        whiff31=0.13 #swing and miss perc.
        inplay31=0.4 #foul perc.
        
        bat32=0.26 #no swing perc.
        whiff32=0.15 #swing and miss perc.
        inplay32=0.41 #foul perc.
        
        pitchnum=1
        
        if count == [0,0]:
            if pitch < whip: #ball
                if swing <= umperror: #ump calls ball strike
                    strike=strike+1
                elif swing > umperror and swing < bat: #no swing
                    ball=ball+1
                elif swing > umperror and swing >= bat: #swing
                    if contact < whiff: #miss
                        strike=strike+1
                    elif contact >= whiff: #contact
                        if fair < inplay: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1

            elif pitch >= whip: #strike
                if swing <= umperror: #ump calls strike ball
                    ball=ball+1
                elif swing > umperror and swing < bat: #no swing
                    strike=strike+1
                elif swing > umperror and swing >= bat: #swing
                    if contact < whiff: #miss
                        strike=strike+1
                    elif contact >= whiff: #contact
                        if fair < inplay: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1
        
        if count == [0,1]:
            if pitch < whip: #ball
                if swing <= umperror: #ump calls ball strike
                    strike=strike+1
                elif swing > umperror and swing < bat01: #no swing
                    ball=ball+1
                elif swing > umperror and swing >= bat01: #swing
                    if contact < whiff01: #miss
                        strike=strike+1
                    elif contact >= whiff01: #contact
                        if fair < inplay01: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay01: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1

            elif pitch >= whip: #strike
                if swing <= umperror: #ump calls strike ball
                    ball=ball+1
                elif swing > umperror and swing < bat01: #no swing
                    strike=strike+1
                elif swing > umperror and swing >= bat01: #swing
                    if contact < whiff01: #miss
                        strike=strike+1
                    elif contact >= whiff01: #contact
                        if fair < inplay01: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay01: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1
            
        if count == [0,2]:
            if pitch < whip: #ball
                if swing <= umperror: #ump calls ball strike
                    strike=strike+1
                elif swing > umperror and swing < bat02: #no swing
                    ball=ball+1
                elif swing > umperror and swing >= bat02: #swing
                    if contact < whiff02: #miss
                        strike=strike+1
                    elif contact >= whiff02: #contact
                        if fair < inplay02: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay02: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1

            elif pitch >= whip: #strike
                if swing <= umperror: #ump calls strike ball
                    ball=ball+1
                elif swing > umperror and swing < bat02: #no swing
                    strike=strike+1
                elif swing > umperror and swing >= bat02: #swing
                    if contact < whiff02: #miss
                        strike=strike+1
                    elif contact >= whiff02: #contact
                        if fair < inplay02: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay02: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1
        
        if count == [1,0]:
            if pitch < whip: #ball
                if swing <= umperror: #ump calls ball strike
                    strike=strike+1
                elif swing > umperror and swing < bat10: #no swing
                    ball=ball+1
                elif swing > umperror and swing >= bat10: #swing
                    if contact < whiff10: #miss
                        strike=strike+1
                    elif contact >= whiff10: #contact
                        if fair < inplay10: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay10: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1

            elif pitch >= whip: #strike
                if swing <= umperror: #ump calls strike ball
                    ball=ball+1
                elif swing > umperror and swing < bat10: #no swing
                    strike=strike+1
                elif swing > umperror and swing >= bat10: #swing
                    if contact < whiff10: #miss
                        strike=strike+1
                    elif contact >= whiff10: #contact
                        if fair < inplay10: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay10: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1
            
        if count == [1,1]:
            if pitch < whip: #ball
                if swing <= umperror: #ump calls ball strike
                    strike=strike+1
                elif swing > umperror and swing < bat11: #no swing
                    ball=ball+1
                elif swing > umperror and swing >= bat11: #swing
                    if contact < whiff11: #miss
                        strike=strike+1
                    elif contact >= whiff11: #contact
                        if fair < inplay11: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay11: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1

            elif pitch >= whip: #strike
                if swing <= umperror: #ump calls strike ball
                    ball=ball+1
                elif swing > umperror and swing < bat11: #no swing
                    strike=strike+1
                elif swing > umperror and swing >= bat11: #swing
                    if contact < whiff11: #miss
                        strike=strike+1
                    elif contact >= whiff11: #contact
                        if fair < inplay11: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay11: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1
        
        if count == [1,2]:
            if pitch < whip: #ball
                if swing <= umperror: #ump calls ball strike
                    strike=strike+1
                elif swing > umperror and swing < bat12: #no swing
                    ball=ball+1
                elif swing > umperror and swing >= bat12: #swing
                    if contact < whiff12: #miss
                        strike=strike+1
                    elif contact >= whiff12: #contact
                        if fair < inplay12: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay12: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1

            elif pitch >= whip: #strike
                if swing <= umperror: #ump calls strike ball
                    ball=ball+1
                elif swing > umperror and swing < bat12: #no swing
                    strike=strike+1
                elif swing > umperror and swing >= bat12: #swing
                    if contact < whiff12: #miss
                        strike=strike+1
                    elif contact >= whiff12: #contact
                        if fair < inplay12: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay12: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1
        
        if count == [2,0]:
            if pitch < whip: #ball
                if swing <= umperror: #ump calls ball strike
                    strike=strike+1
                elif swing > umperror and swing < bat20: #no swing
                    ball=ball+1
                elif swing > umperror and swing >= bat20: #swing
                    if contact < whiff20: #miss
                        strike=strike+1
                    elif contact >= whiff20: #contact
                        if fair < inplay20: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay20: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1

            elif pitch >= whip: #strike
                if swing <= umperror: #ump calls strike ball
                    ball=ball+1
                elif swing > umperror and swing < bat20: #no swing
                    strike=strike+1
                elif swing > umperror and swing >= bat20: #swing
                    if contact < whiff20: #miss
                        strike=strike+1
                    elif contact >= whiff20: #contact
                        if fair < inplay20: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay20: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1
        
        if count == [2,1]:
            if pitch < whip: #ball
                if swing <= umperror: #ump calls ball strike
                    strike=strike+1
                elif swing > umperror and swing < bat21: #no swing
                    ball=ball+1
                elif swing > umperror and swing >= bat21: #swing
                    if contact < whiff21: #miss
                        strike=strike+1
                    elif contact >= whiff21: #contact
                        if fair < inplay21: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay21: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1

            elif pitch >= whip: #strike
                if swing <= umperror: #ump calls strike ball
                    ball=ball+1
                elif swing > umperror and swing < bat21: #no swing
                    strike=strike+1
                elif swing > umperror and swing >= bat21: #swing
                    if contact < whiff21: #miss
                        strike=strike+1
                    elif contact >= whiff21: #contact
                        if fair < inplay21: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay21: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1
        
        if count == [2,2]:
            if pitch < whip: #ball
                if swing <= umperror: #ump calls ball strike
                    strike=strike+1
                elif swing > umperror and swing < bat22: #no swing
                    ball=ball+1
                elif swing > umperror and swing >= bat22: #swing
                    if contact < whiff22: #miss
                        strike=strike+1
                    elif contact >= whiff22: #contact
                        if fair < inplay22: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay22: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1

            elif pitch >= whip: #strike
                if swing <= umperror: #ump calls strike ball
                    ball=ball+1
                elif swing > umperror and swing < bat22: #no swing
                    strike=strike+1
                elif swing > umperror and swing >= bat22: #swing
                    if contact < whiff22: #miss
                        strike=strike+1
                    elif contact >= whiff22: #contact
                        if fair < inplay22: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay22: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1
            
        if count == [3,0]:
            if pitch < whip: #ball
                if swing <= umperror: #ump calls ball strike
                    strike=strike+1
                elif swing > umperror and swing < bat30: #no swing
                    ball=ball+1
                elif swing > umperror and swing >= bat30: #swing
                    if contact < whiff30: #miss
                        strike=strike+1
                    elif contact >= whiff30: #contact
                        if fair < inplay30: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay30: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1

            elif pitch >= whip: #strike
                if swing <= umperror: #ump calls strike ball
                    ball=ball+1
                elif swing > umperror and swing < bat30: #no swing
                    strike=strike+1
                elif swing > umperror and swing >= bat30: #swing
                    if contact < whiff30: #miss
                        strike=strike+1
                    elif contact >= whiff30: #contact
                        if fair < inplay30: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay30: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1
        
        if count == [3,1]:
            if pitch < whip: #ball
                if swing <= umperror: #ump calls ball strike
                    strike=strike+1
                elif swing > umperror and swing < bat31: #no swing
                    ball=ball+1
                elif swing > umperror and swing >= bat31: #swing
                    if contact < whiff31: #miss
                        strike=strike+1
                    elif contact >= whiff31: #contact
                        if fair < inplay31: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay31: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1

            elif pitch >= whip: #strike
                if swing <= umperror: #ump calls strike ball
                    ball=ball+1
                elif swing > umperror and swing < bat31: #no swing
                    strike=strike+1
                elif swing > umperror and swing >= bat31: #swing
                    if contact < whiff31: #miss
                        strike=strike+1
                    elif contact >= whiff31: #contact
                        if fair < inplay31: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay31: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1
        
        if count == [3,2]:
            if pitch < whip: #ball
                if swing <= umperror: #ump calls ball strike
                    strike=strike+1
                elif swing > umperror and swing < bat32: #no swing
                    ball=ball+1
                elif swing > umperror and swing >= bat32: #swing
                    if contact < whiff32: #miss
                        strike=strike+1
                    elif contact >= whiff32: #contact
                        if fair < inplay32: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay32: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1

            elif pitch >= whip: #strike
                if swing <= umperror: #ump calls strike ball
                    ball=ball+1
                elif swing > umperror and swing < bat32: #no swing
                    strike=strike+1
                elif swing > umperror and swing >= bat32: #swing
                    if contact < whiff32: #miss
                        strike=strike+1
                    elif contact >= whiff32: #contact
                        if fair < inplay32: #foul
                            if count[1] < 2:
                                strike=strike+1
                            elif count[1] == 2:
                                strike=strike+0
                        elif fair >= inplay32: #fair
                            if outcome > obp:
                                out=1
                                ob=0
                            if outcome <= obp:
                                out=0
                                ob=1
        
        count=[ball]+[strike]
        
        pitchlist=pitchlist+[pitch]
        swinglist=swinglist+[swing]
        contactlist=contactlist+[contact]
        fairlist=fairlist+[fair]
        outcomelist=outcomelist+[outcome]
        
        abpitchcount=abpitchcount+pitchnum
        
        aboutcome=[out,ob]
        
    if count[1] == 3:
        strikeout = 1
        out = 1
    elif count[1] < 3 and aboutcome[0] == 1:
        outtype=int(uniform(0,11))
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
        
    aboutcome=[out,ob]

    ab=[strikeout,groundout,flyout,walk,hit,abpitchcount]
    
    return ab
  
  # this lays the groundwork for baserunners moving around the bases
  # it is atbat specific
  
  def baserunning(aPOSlist,atbat):

    #atbat=[walk,hit,abSLG]
    single=0.62
    double=0.82
    triple=0.84
    homer=1
    basesruns=[]
    atbat=atbat
    SLG=atbat[2]

    if aPOSlist==[0,0,0]:
        if atbat[0] == 1:
            POSlist=[1,0,0]
            rs=0
        elif atbat[1] == 1:
            if SLG<=single: #nobody on and a single/walk
                POSlist=[1,0,0]
                rs=0
            elif SLG<=double and SLG>single: #nobody on and a double
                POSlist=[0,1,0]
                rs=0
            elif SLG<=triple and SLG>double: #nobody on and a triple
                POSlist=[0,0,1]
                rs=0
            elif SLG<=homer and SLG>triple: #nobody on and a homerun
                POSlist=[0,0,0]
                rs=1

    elif aPOSlist==[1,0,0]:
        if atbat[0] == 1:
            POSlist=[1,1,0]
            rs=0
        elif atbat[1] == 1:
            if SLG<=single: #man on first and single/walk
                POSlist=[1,1,0]
                rs=0
            elif SLG<=double and SLG>single: #man on first and double
                POSlist=[0,1,1]
                rs=0
            elif SLG<=triple and SLG>double: #man on first and triple
                POSlist=[0,0,1]
                rs=1
            elif SLG<=homer and SLG>triple: #man on first and homerun
                POSlist=[0,0,0]
                rs=2

    elif aPOSlist==[1,1,0]:
        if atbat[0] == 1: #man on first and second and walk
            POSlist=[1,1,1]
            rs=0
        elif atbat[1] == 1:
            if SLG<=single: #man on first and second and single
                POSlist=[1,1,0]
                rs=1
            elif SLG<=double and SLG>single: #man on first and second and double
                POSlist=[0,1,1]
                rs=1
            elif SLG<=triple and SLG>double: #man on first and second and triple
                POSlist=[0,0,1]
                rs=2
            elif SLG<=homer and SLG>triple: #man on first and second and homerun
                POSlist=[0,0,0]
                rs=3

    elif aPOSlist==[1,0,1]:
        if atbat[0] == 1: #man on first and third and walk
            POSlist=[1,1,1]
            rs=0
        elif atbat[1] == 1:
            if SLG<=single: #man on first and third and single
                POSlist=[1,1,0]
                rs=1
            elif SLG<=double and SLG>single: #man on first and third and double
                POSlist=[0,1,1]
                rs=1
            elif SLG<=triple and SLG>double: #man on first and third and triple
                POSlist=[0,0,1]
                rs=2
            elif SLG<=homer and SLG>triple: #man on first and third and homerun
                POSlist=[0,0,0]
                rs=3

    elif aPOSlist==[0,1,0]:
        if atbat[0] == 1: #man on second and walk
            POSlist=[1,1,0]
            rs=0
        elif atbat[1] == 1:
            if SLG<=single: #man on second and single
                POSlist=[1,0,1]
                rs=0
            elif SLG<=double and SLG>single: #man on second and double
                POSlist=[0,1,0]
                rs=1
            elif SLG<=triple and SLG>double: #man on second and triple
                POSlist=[0,0,1]
                rs=2
            elif SLG<=homer and SLG>triple: #man on second and homerun
                POSlist=[0,0,0]
                rs=3

    elif aPOSlist==[0,1,1]:
        if atbat[0] == 1: #man on second and third and walk
            POSlist=[1,1,1]
            rs=0
        elif atbat[1] == 1:
            if SLG<=single: #man on second and third and single
                POSlist=[1,0,1]
                rs=1
            elif SLG<=double and SLG>single: #man on second and third and double
                POSlist=[0,1,0]
                rs=2
            elif SLG<=triple and SLG>double: #man on second and third and triple
                POSlist=[0,0,1]
                rs=2
            elif SLG<=homer and SLG>triple: #man on second and third and homerun
                POSlist=[0,0,0]
                rs=3

    if aPOSlist==[0,0,1]:
        if atbat[0] == 1: #man on third and walk
            POSlist=[1,0,1]
            rs=0
        elif atbat[1] == 1:
            if SLG<=single: #man on third and single
                POSlist=[1,0,0]
                rs=1
            elif SLG<=double and SLG>single: #man on third and double
                POSlist=[0,1,0]
                rs=1
            elif SLG<=triple and SLG>double: #man on third and triple
                POSlist=[0,0,1]
                rs=1
            elif SLG<=homer and SLG>triple: #man on third and homerun
                POSlist=[0,0,0]
                rs=2

    if aPOSlist==[1,1,1]:
        if atbat[0] == 1: #bases loaded and walk
            POSlist=[1,1,1]
            rs=1
        elif atbat[1] == 1:
            if SLG<=single: #bases loaded and single
                POSlist=[1,1,0]
                rs=2
            elif SLG<=double and SLG>single: #bases loaded and double
                POSlist=[0,1,1]
                rs=2
            elif SLG<=triple and SLG>double: #bases loaded and triple
                POSlist=[0,0,1]
                rs=3
            elif SLG<=homer and SLG>triple: #bases loaded and homerun
                POSlist=[0,0,0]
                rs=4

    basesruns=[POSlist,rs]
    return basesruns
  
  # now we set the groundwork for an inning to take place
  
  def inning(obp,whip):

    #obp=team[0]
    #whip=team[1]
    
    o=0 #outs start at 0
    atbat=[] #ties together the OBP and SLG into a pair to represent each hitter
    abl=[] #atbat list

    aPOSlist=[0,0,0] #start with nobody on
    POSLIST=[] #list of runners moving around bases
    SLGlist=[] #list of random SLG values for each hitter
    obplist=[] #list of random OBP values for each hitter

    #percantages of occurance of each type of hit
    
    #single=0.62   #83%  62%(MLB)
    #double=0.82   #11%  20%
    #triple=0.84   #2%   2%
    #homer=1       #4%   16%
    
    #if you want random intervals for types of hits
    single1=0.24
    triple1=0.25
    double1=0.34
    single2=0.56
    homer1=0.62
    single3=0.74
    triple2=0.75
    homer2=0.85
    double2=0.96
    single4=1
    

    ht=0 #hit total
    rt=0 #run total
    rs=0 #run scored
    rlist=[] #list of runs and when/how scored
    LOB=0 #men left on base

    walkt=0 #walk total
    singlet=0 #single total
    doublet=0 #double total
    triplet=0 #triple total
    homerunt=0 #homerun total
    
    strikeoutt=0 #strikeout total
    groundoutt=0 #groundout total
    flyoutt=0 #flyout total

    pitchcount=0
    atbatlist=[] #list the atbat outcomes in order
    off=[] #list of offensive stats

    while o < 3: #inning continues as long as there are less than 3 outs

        AB=AtBat(obp,whip) #at bat strikeout,groundout,flyout,walk,hit,pitchcount
        pitchnum=AB[5]
        
        #x=uniform(0,1) #create the comparable OBP value
        abSLG=uniform(0,1) #create the SLG % value

        atbat=[AB[3],AB[4],abSLG] #pairs up the OBP (hit/no hit) and SLG (hit type)
        #abl=abl+[atbat] #list the hits in order of occurance
        abWALK=atbat[0]
        abHIT=atbat[1]
        SLG=atbat[2]

        aPOSlist #return the previous baserunner list

        if abWALK == 1:
            y=0
            h=0 #walk(BB)/HBP
            walkt=walkt+1
            atbatlist=atbatlist+["walk"]
            #aPOSlist=[1,0,0]
        elif abHIT == 1:
            if (SLG <= single1) or (SLG > double1 and SLG <= single2) or (SLG > homer1 and SLG <= single3) or (SLG > homer2) : #single liklihood
                y=0
                h=1 #single
                singlet=singlet+1
                atbatlist=atbatlist+["single"]
                #aPOSlist=[1,0,0]
            elif (SLG > triple1 and SLG <= double1) or (SLG > homer2 and SLG <= double2): #double liklihood
                y=0
                h=1 #double
                doublet=doublet+1
                atbatlist=atbatlist+["double"]
                #aPOSlist=[0,1,0]
            elif (SLG > single1 and SLG <= triple1) or (SLG > single3 and SLG <= triple2): #triple liklihood
                y=0
                h=1 #triple
                triplet=triplet+1
                atbatlist=atbatlist+["triple"]
                #aPOSlist=[0,0,1]
            elif (SLG > single2 and SLG <= homer1) or (SLG > triple2 and SLG <= homer2): #homerun liklihood
                y=0
                h=1
                atbatlist=atbatlist+["homerun"]
                #aPOSlist=[0,0,0]
                homerunt=homerunt+1
        elif abWALK == 0 and abHIT == 0: #obp is set up outside of the loop
            h = 0 #since out, no hit
            if AB[0] == 1:
                y = 1 #add an out
                strikeoutt=strikeoutt+1
                atbatlist=atbatlist+['strikeout']
                if POSLIST==[]:
                    aPOSlist=[0,0,0]
                    rs=0
                else:
                    aPOSlist=POSLIST[-1] #return the previous baserunner list
                    rs=0
            elif AB[1] == 1:
                y = 1 #add an out
                groundoutt=groundoutt+1
                atbatlist=atbatlist+['groundout']
                if POSLIST==[]:
                    aPOSlist=[0,0,0]
                    rs=0
                else:
                    aPOSlist=POSLIST[-1] #return the previous baserunner list
                    rs=0
            elif AB[2] == 1:
                y = 1 #add an out
                flyoutt=flyoutt+1
                atbatlist=atbatlist+['flyout']
                if POSLIST==[]:
                    aPOSlist=[0,0,0]
                    rs=0
                else:
                    aPOSlist=POSLIST[-1] #return the previous baserunner list
                    rs=0

        if abWALK == 1 or abHIT == 1:
            baserun=baserunning(aPOSlist,atbat)
            aPOSlist=baserun[0] #index out where players are on base shown in list form (i.e. [1,0,0] = man on first)
            rs=baserun[1] #index out the runs scored

        POSLIST=POSLIST+[aPOSlist] #creates a list to keep track of where runners are on base after each new atbat


        rlist=rlist+[rs] #list of runs scoring
        LOB=sum(POSLIST[-1])
        rt=rt+rs #run total
        ht=ht+h #hit total
        o=o+y #out total
        pitchcount=pitchcount+pitchnum

    off=[rt,ht,walkt,singlet,doublet,triplet,homerunt,LOB,strikeoutt,groundoutt,flyoutt,pitchcount]

    return off
  
  # now the scoreboard to keep track of runs and the inning
  # this function only sets up one teams "scoreboard" though
  
  def gameboard(obp,whip):
    
    sbi=[] #scoreboard inning
    sbr=[] #scoreboard runs
    sbh=[] #scoreboard on base
    board=[] #final output
    tr=0 #total runs
    th=0 #total hits

    BB=[]
    B1=[]
    B2=[]
    B3=[]
    HR=[]
    LOB=[]
    K=[]
    GO=[]
    FO=[]
    PC=[]

    BBtotal=0
    B1total=0
    B2total=0
    B3total=0
    HRtotal=0
    LOBtotal=0
    Ktotal=0
    GOtotal=0
    FOtotal=0
    PCtotal=0

    for i in range(1,9):
        hrl=inning(obp,whip) #hrl = hit/run list
        r=hrl[0] #index the runs
        h=hrl[1] #index the amount on base

        #types of hits (index out)
        bb=hrl[2]
        b1=hrl[3]
        b2=hrl[4]
        b3=hrl[5]
        hr=hrl[6]
        
        #runners left on base (index out)
        lob=hrl[7]
        
        #types of outs
        k=hrl[8]
        go=hrl[9]
        fo=hrl[10]
        
        #pitch count
        pc=hrl[11]

        #list of stats
        BB=BB+[bb]
        B1=B1+[b1]
        B2=B2+[b2]
        B3=B3+[b3]
        HR=HR+[hr]
        LOB=LOB+[lob]
        K=K+[k]
        GO=GO+[go]
        FO=FO+[fo]
        PC=PC+[pc]

        #total up the lists of stats
        BBtotal=sum(BB)
        B1total=sum(B1)
        B2total=sum(B2)
        B3total=sum(B3)
        HRtotal=sum(HR)
        LOBtotal=sum(LOB)
        Ktotal=sum(K)
        GOtotal=sum(GO)
        FOtotal=sum(FO)
        PCtotal=sum(PC)

        tr=tr+r #totals up how many runs scored
        th=th+h #totals up hits
        sbi=sbi+[i] #inning list to get horizontal
        sbr=sbr+[r] #run list to get horizontal
        sbh=sbh+[h] #hit list
        board=[sbr,sbh,BBtotal,B1total,B2total,B3total,HRtotal,LOBtotal,Ktotal,GOtotal,FOtotal,PCtotal]
        
    return board
  
  # this function sets up for two teams to play against each other
  
  def truegame(team1,team2):
    
    team1name=team1[2]
    team2name=team2[2]
    
    obp1=team1[0]
    whip1=team1[1]
    obp2=team2[0]
    whip2=team2[1]
    
    BBtotal1=[]
    B1total1=[]
    B2total1=[]
    B3total1=[]
    HRtotal1=[]
    LOBtotal1=[]
    Ktotal1=[]
    GOtotal1=[]
    FOtotal1=[]
    PCtotal1=[]

    BBtotal2=[]
    B1total2=[]
    B2total2=[]
    B3total2=[]
    HRtotal2=[]
    LOBtotal2=[]
    Ktotal2=[]
    GOtotal2=[]
    FOtotal2=[]
    PCtotal2=[]

    r1=0 #team 1 runs
    r2=0 #team 2 runs

    scoreboard1=gameboard(obp1,whip2) #runs team 1 gameboard (first 8 innings)
    scoreboard2=gameboard(obp2,whip1) #runs team 2 gameboard (first 8 innings)

    rg1=scoreboard1[0] #runs for team 1
    rg2=scoreboard2[0] #runs for team 2
    h1=scoreboard1[1] #hits team 1
    h2=scoreboard2[1] #hits team 2

    #total up offensive stats for team 1
    BBt1=scoreboard1[2]
    B1t1=scoreboard1[3]
    B2t1=scoreboard1[4]
    B3t1=scoreboard1[5]
    HRt1=scoreboard1[6]
    BBtotal1=BBtotal1+[BBt1]
    B1total1=B1total1+[B1t1]
    B2total1=B2total1+[B2t1]
    B3total1=B3total1+[B3t1]
    HRtotal1=HRtotal1+[HRt1]
    LOBt1=scoreboard1[7]
    LOBtotal1=LOBtotal1+[LOBt1]
    
    Kt1=scoreboard1[8]
    Ktotal1=Ktotal1+[Kt1]
    GOt1=scoreboard1[9]
    GOtotal1=GOtotal1+[GOt1]
    FOt1=scoreboard1[10]
    FOtotal1=FOtotal1+[FOt1]
    
    PCt1=scoreboard1[11]
    PCtotal1=PCtotal1+[PCt1]

    #total offensive stats for team 2
    BBt2=scoreboard2[2]
    B1t2=scoreboard2[3]
    B2t2=scoreboard2[4]
    B3t2=scoreboard2[5]
    HRt2=scoreboard2[6]
    BBtotal2=BBtotal2+[BBt2]
    B1total2=B1total2+[B1t2]
    B2total2=B2total2+[B2t2]
    B3total2=B3total2+[B3t2]
    HRtotal2=HRtotal2+[HRt2]
    LOBt2=scoreboard2[7]
    LOBtotal2=LOBtotal2+[LOBt2]
    
    Kt2=scoreboard2[8]
    Ktotal2=Ktotal2+[Kt2]
    GOt2=scoreboard2[9]
    GOtotal2=GOtotal2+[GOt2]
    FOt2=scoreboard2[10]
    FOtotal2=FOtotal2+[FOt2]
    
    PCt2=scoreboard2[11]
    PCtotal2=PCtotal2+[PCt2]

    tw1=0 #total wins team 1
    tw2=0 #total wins team 2

    i=9 #sets an index that will come in play later
    sb=[1,2,3,4,5,6,7,8,9] #sets up our inning list

    hrl1=inning(obp1,whip2) #call the inning to run
    ri1=hrl1[0] #index out the runs
    r1=ri1 #makes the road team (first listed) have their 9th AB
    rg1=rg1+[r1] #adds their runs to the run list
    hi1=hrl1[1] #hits from inning
    h1=h1+[hi1] #add to hit list

    #team 1 top offensive stats for top of 9th
    BBt1=hrl1[2]
    B1t1=hrl1[3]
    B2t1=hrl1[4]
    B3t1=hrl1[5]
    HRt1=hrl1[6]
    BBtotal1=BBtotal1+[BBt1]
    B1total1=B1total1+[B1t1]
    B2total1=B2total1+[B2t1]
    B3total1=B3total1+[B3t1]
    HRtotal1=HRtotal1+[HRt1]
    LOBt1=hrl1[7]
    LOBtotal1=LOBtotal1+[LOBt1]
    
    Kt1=hrl1[8]
    Ktotal1=Ktotal1+[Kt1]
    GOt1=hrl1[9]
    GOtotal1=GOtotal1+[GOt1]
    FOt1=hrl1[10]
    FOtotal1=FOtotal1+[FOt1]
    
    PCt1=hrl1[11]
    PCtotal1=PCtotal1+[PCt1]

    #runs if needed
    if sum(rg1)>=sum(rg2): #keeps the bottom of 9th optional
        hrl2=inning(obp2,whip1) #call the inning for team two
        ri2=hrl2[0] #index out the runs
        r2=ri2 #if played runs the 9th for team 2 (home team)
        rg2=rg2+[r2] #adds their runs to the runs list
        hi2=hrl2[1] #hits from inning
        h2=h2+[hi2] #add to hit list

        #team 2 offensive statistics
        BBt2=hrl2[2]
        B1t2=hrl2[3]
        B2t2=hrl2[4]
        B3t2=hrl2[5]
        HRt2=hrl2[6]
        BBtotal2=BBtotal2+[BBt2]
        B1total2=B1total2+[B1t2]
        B2total2=B2total2+[B2t2]
        B3total2=B3total2+[B3t2]
        HRtotal2=HRtotal2+[HRt2]
        LOBt2=hrl2[7]
        LOBtotal2=LOBtotal2+[LOBt2]
        
        Kt2=hrl2[8]
        Ktotal2=Ktotal2+[Kt2]
        GOt2=hrl2[9]
        GOtotal2=GOtotal2+[GOt2]
        FOt2=hrl2[10]
        FOtotal2=FOtotal2+[FOt2]
        
        PCt2=hrl2[11]
        PCtotal2=PCtotal2+[PCt2]

    #runs as long as run totals are equal
    while sum(rg1) == sum(rg2): #creates an extra inning parameter
        i=i+1 #index that adds 1 to the already made inning list
        hrl1=inning(obp1,whip2) #an extra inning for team 1
        hrl2=inning(obp2,whip1) #an extra inning for team 2
        ri1=hrl1[0] #index runs for team 1
        ri2=hrl2[0] #index runs for team 2
        r1=ri1
        r2=ri2
        rg1=rg1+[r1] #adds the runs to the run list for both teams
        rg2=rg2+[r2]
        sb=sb+[i] #adds to the inning list

        hi1=hrl1[1] #takes the index for hits team 1
        h1=h1+[hi1] #extra inning hits team 1 (adds to list)
        hi2=hrl2[1] #takes the index hits team 2
        h2=h2+[hi2] #extra inning hits team 2 (adds to list)

        #total up statistics for each team
        BBt1=hrl1[2]
        B1t1=hrl1[3]
        B2t1=hrl1[4]
        B3t1=hrl1[5]
        HRt1=hrl1[6]
        BBtotal1=BBtotal1+[BBt1]
        B1total1=B1total1+[B1t1]
        B2total1=B2total1+[B2t1]
        B3total1=B3total1+[B3t1]
        HRtotal1=HRtotal1+[HRt1]
        LOBt1=hrl1[7]
        LOBtotal1=LOBtotal1+[LOBt1]
        Kt1=hrl1[8]
        Ktotal1=Ktotal1+[Kt1]
        GOt1=hrl1[9]
        GOtotal1=GOtotal1+[GOt1]
        FOt1=hrl1[10]
        FOtotal1=FOtotal1+[FOt1]
        PCt1=hrl1[11]
        PCtotal1=PCtotal1+[PCt1]

        BBt2=hrl2[2]
        B1t2=hrl2[3]
        B2t2=hrl2[4]
        B3t2=hrl2[5]
        HRt2=hrl2[6]
        BBtotal2=BBtotal2+[BBt2]
        B1total2=B1total2+[B1t2]
        B2total2=B2total2+[B2t2]
        B3total2=B3total2+[B3t2]
        HRtotal2=HRtotal2+[HRt2]
        LOBt2=hrl2[7]
        LOBtotal2=LOBtotal2+[LOBt2]
        Kt2=hrl2[8]
        Ktotal2=Ktotal2+[Kt2]
        GOt2=hrl2[9]
        GOtotal2=GOtotal2+[GOt2]
        FOt2=hrl2[10]
        FOtotal2=FOtotal2+[FOt2]
        PCt2=hrl2[11]
        PCtotal2=PCtotal2+[PCt2]

    #puts the dash in for the home team's final inning since it wasn't played
    if sb[-1] == 9 and sum(rg2[0:8])>sum(rg1):
        rg2=rg2+["-"]

    #sums up the teams' runs
    if sum(sb) == 45 and rg2[8] == "-":
        rg1=rg1+[sum(rg1),sum(h1),sum(LOBtotal1)]
        rg2=rg2+[sum(rg2[0:-1]),sum(h2),sum(LOBtotal2)]

    #sums up the teams' runs
    if sum(sb) == 45 and rg2[8] != "-":
        rg1=rg1+[sum(rg1),sum(h1),sum(LOBtotal1)]
        rg2=rg2+[sum(rg2),sum(h2),sum(LOBtotal2)]

    #sums up the teams' runs
    if sum(sb) > 45:
        rg1=rg1+[sum(rg1),sum(h1),sum(LOBtotal1)]
        rg2=rg2+[sum(rg2),sum(h2),sum(LOBtotal2)]

    #creates the run total, hit total, and LOB total in the scoreboard
    sb=sb+["R","H","LOB"]

    #creates the neat scoreboard output
    for i in range(len(sb)): print(sb[i], end=" ")
    print("")

    for r in range(len(rg1)): print(rg1[r], end=" ")
    print("")

    for r in range(len(rg2)): print(rg2[r], end=" ")
    print("")

    if rg1[-3] > rg2[-3]:
        print("Visitors win",rg1[-3],"to",rg2[-3])
        
    if rg2[-3] > rg1[-3]:
        print("Home team wins",rg2[-3],"to",rg1[-3])
    
    #prints out the teams' stat totals
    
    print(team1name, "totaled:", sum(BBtotal1),"walks,",sum(B1total1),"singles,",sum(B2total1),"doubles,",sum(B3total1),"triples, and",sum(HRtotal1),"home runs. Team 1 left",sum(LOBtotal1),"men on base. Team 1 struck out",sum(Ktotal1),"times, grounded out",sum(GOtotal1),"times, and flew out",sum(FOtotal1),"times. Team 1 threw",sum(PCtotal1),"pitches.")
    print(team2name, "totaled:", sum(BBtotal2),"walks,",sum(B1total2),"singles,",sum(B2total2),"doubles,",sum(B3total2),"triples, and",sum(HRtotal2),"home runs. Team 2 left",sum(LOBtotal2),"men on base. Team 2 struck out",sum(Ktotal2),"times, grounded out",sum(GOtotal2),"times, and flew out",sum(FOtotal2),"times. Team 2 threw",sum(PCtotal2),"pitches.")

   
