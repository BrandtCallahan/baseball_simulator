# Baseball_Simulator

The simulator works with an inputted on-base percentage (OBP). Nowadays OBP can be seen as a promising offensive stat because it follows what was learned through "Moneyball" in that in order to win games you need to score runs and in order to score runs you need to get on base. The single game simulator is composed of three initial parts (functions). 

## Baserunning()
The first function is a baserunning function where it lays out all of the possible options runners have to be on base. It also accounts for how runners react to the different hits. The inputs for the function are aPOSlist and SLG. The input of aPOSlist is a list of 3 values (0's and 1's) which tell the function where runners currently are. Within the list, 0's mean no one is currently on that base and 1's mean there is someone on that base. The positions within the list represent the bases with the first position being first, second being second, and third being third. An example is [0,1,0] representing a man on second. The SLG input stands for slugging percentage and accounts for the type of hit that has just happened. I have the different types of hits (including walks... and yes I know that a walk is not a hit) split into different percentages of occurancy. To get the number that will represent the hit type I have a random number generator spit out a random number between 0 and 1. For the time being I have the following distributions for the types of hits:
walk: 0-0.15  (15%)
single: 0.16-0.60 (44%)
double: 0.61-0.82 (21%)
triple: 0.83-0.88 (5%)
homerun: 0.89-1 (11%)
The two inputs for the function, aPOSlist and SLG, allow for the function to know where the runners are on base currently as well as what hit has just happened. This will allow the function to output the new positioning of runners due to the past hit. One thing to keep in mind with the function is that I have it made were all hits with a runner on second will score that runner from second. The final output of the function is a list containing the new positioning of the runners and the runs that scored from the past hit. 

## Inning()
Secondly, we have the inning function which runs through an entire inning of baseball. It begins with a while statement which sets it up to run as long as outs (o) are less than 3. This is because an inning of baseball will continue until the defense records 3 outs. There is one input with this function and that is obp (on-base percentage) and should be the team's on-base percentage that you are wanting to use. The first moving part in this function is a random number that will be generated (between 0 and 1) and then compared to the given obp. If the random number is less than the obp, then it counts as a hit and will then be given a respective SLG value which will determine the type of hit, but if the random number is greater than the obp, it is an out and is counted as so. If we have a hit, we then look to its respective SLG for what the hit is. The SLG will be used in the baserunning function to determine the new positioning of baserunners. From this function we can get a list of statistics to use later on. This list will be the final output and includes run total, hit total, walk total, single total, double total, triple total, homerun total, and men left on base total. 

## Gameboard()
The gameboard function gives us the working parts to create a scoreboard. It begins with a for loop that will run through 8 times. It only runs 8 times because the 9th inning can have some variability depending on the score (i.e. if the home team is winning after 8 and 1/2 innings then there is no bottom of the 9th). The loop includes the inning function where it will run through an inning of baseball 8 times to make up 8 innings of scores and stats for one team. The input for this function is also obp and the call to the inning function uses that inputted obp as its comparable measure for each inning and the result of each at bat. This function also creates a list of each offensive stat kept (walks, singles, doubles, triples, homeruns, and left on base (LOB)) for each inning from the loop. 
