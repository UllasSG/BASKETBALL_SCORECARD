home={}
away={}
def addplayer(team):
    name=input('ENTER NAME')
    team[name]={'points':0,'assists':0,'FGA':0,'FGM':0,'3PA':0,'3PM':0}


def FGp(team,player):#returns Field goal % as int
    if (team[player]['FGA'])==0:
        return 0
    fgp=((team[player]['FGM'])/(team[player]['FGA']))*100
    return fgp

def points(team,player):#returns the points scored by the player as a integer
    return team[player]['points']
    
def assists(team,player):#returns the assists scored by the player as a integer
    return team[player]['assists']
def TSp(team,player):
    tsp=((team[player]['points'])/(2*team[player]['FGA']))*100
    return tsp
def 3pm%(team,player):#returns 3 pointers made % as int
    if (team[player]['3pm'])==0:
        return 0
    3pm=((team[player]['3PM'])/(team[player]['3pm']))*100
    return 3pm