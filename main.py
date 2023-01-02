
######################################################################################################################

from tkinter import *
window=Tk()



home={}
away={}
d={'ullas':{'points':10,'assists':5,'FGA':5,'FGM':3,'3PA':0,'3PM':8},'tanmay':{'points':60,'assists':50,'FGA':5,'FGM':0,'3PA':7,'3PM':0},'vihaan':{'points':45,'assists':0,'FGA':0,'FGM':0,'3PA':0,'3PM':0}}
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
    return (teamPts/(2*teamFGA))


def TeamLeadPoints(team):
    return max(team,key=lambda x:team[x]['points'])

def TeamLeadAssists(team):
    return max(team,key=lambda x:team[x]['assists'])


################## INPUT PLAYS   ####################

#play=(team,player,2p/3p,made/miss,assisted)
play=(d,'ullas',3,False,'tanmay')

def newplay(p):
    d[p[1]]['FGA']+=1
    if p[3]==True:
        d[p[1]]['points']+=p[2]
        d[p[1]]['FGM']+=1
        d[p[4]]['assists']+=1
    if p[2]==3:
        d[p[1]]['3PA']+=1
        if p[3]==True:
            d[p[1]]['3PM']+=1

window.configure(bg='black')


header=Label(window,text='BASKETBALL SCORECARD',font=('Arial Black',50),fg='white',padx=50,bg='black')

header.grid(row=0,column=0)

header.place(relx=0.5,rely=0.1,anchor=CENTER)


home_l=Label(window,text='HOME',font=('Arial Black',50),bg='black',fg='Blue')
away_l=Label(window,text='AWAY',font=('Arial Black',50),bg='black',fg='red')
home_l.grid()
away_l.grid()

home_l.place(relx=0.1,rely=0.3,anchor=W)
away_l.place(relx=0.7,rely=0.3,anchor=W)

homeFrame=Frame(window,width=230,bg='black',height=100)
homeFrame.grid()
homeFrame.place(relx=0.1,rely=0.5,anchor=W)
Inputtxt=Text(homeFrame,height=5,width=20,padx=10,pady=10).pack()






window.attributes('-fullscreen',True)

window.mainloop()


