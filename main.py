home={}
away={}
def addplayer(team):
    name=input('ENTER NAME')
    team[name]={'points':0,'assists':0,'FGA':0,'FGM':0,'3PA':0,'3PM':0}


def FGp(team,player):#returns Field goal % as float
    if (team[player]['FGA'])==0:
        return 0
    fgp=((team[player]['FGM'])/(team[player]['FGA']))*100
    return fgp

def points(team,player):#returns the points scored by the player as a float
    return team[player]['points']
    
def assists(team,player):#returns the assists scored by the player as a float
    return team[player]['assists']

def TSp(team,player): #returns True Shooting % as float
    tsp=((team[player]['points'])/(2*team[player]['FGA']))*100
    return tsp
def Thrp(team,player):#returns 3 pointers made % as float
    if (team[player]['3PM'])==0:
        return 0
    tpm=((team[player]['3PM'])/(team[player]['3PA']))*100
    return tpm


def teamFGp(team):    #Returns Team FG % as float
    teamFGA=0
    teamFGM=0
    for i in team:
        teamFGA+=team[i]['FGA']
        teamFGM+=team[i]['FGM']
    return (teamFGM/teamFGA)


def team3Pp(team):    # Returns Team 3P % as float
    team3PA=0
    team3PM=0
    for i in team:
        team3PA+=team[i]['3PA']
        team3PM+=team[i]['3PM']
    return (team3PM/team3PA)

def teamTSp(team):          # returns tream TS % as float
    teamPts=0
    teamFGA=0
    for i in team:
        teamPts+=team[i]['points']
        teamFGA+=team[i]['FGA']
    return (teampts/(2*teamFGA))


def TeamLeadPoints(team):
    return max(team,key=lambda x:team[x]['points'])

def TeamLeadAssists(team):
    return max(team,key=lambda x:team[x]['assists'])





#d={'ullas':{'points':10,'assists':0,'FGA':0,'FGM':0,'3PA':0,'3PM':0},'tanmay':{'points':5,'assists':0,'FGA':0,'FGM':0,'3PA':0,'3PM':0},'vihaan':{'points':0,'assists':0,'FGA':0,'FGM':0,'3PA':0,'3PM':0}}
