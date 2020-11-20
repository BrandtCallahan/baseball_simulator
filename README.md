# Baseball_Simulator

The simulator works with an inputted on-base percentage (OBP). Nowadays OBP can be seen as a promising offensive stat because it follows what was learned through "Moneyball" in that in order to win games you need to score runs and in order to score runs you need to get on base. The single game simulator is composed of three initial parts (functions). 

## Baserunning()
The first function is a baserunning function where it lays out all of the possible options runners have to be on base. It also accounts for how runners react to the different hits. For now, it has runners on second scoring on every hit possible from a single to a homerun (obviously). THe inputs for the function are aPOSlist and SLG. The input of aPOSlist is a list of 3 values (0's and 1's) which tell the function where runners currently are. Within the list, 0's mean no one is currently on that base and 1's mean there is someone on that base. The positions within the list represent the bases with the first position being first, second being second, and third being third. An example is [0,1,0] representing a man on second. 

## Inning()
Secondly, we have the inning function which runs through an entire inning of baseball. It begins with a while statement which sets it up to run as long as outs (o) is less than 3. This is because an inning of baseball will continue until the defense records 3 outs. 
