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
def pointsss

