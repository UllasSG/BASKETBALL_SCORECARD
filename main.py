
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
homeFrame.place(relx=0.08,rely=0.6,anchor=W)
awayFrame=Frame(window,width=230,bg='black',height=100)
awayFrame.grid()
awayFrame.place(relx=0.68,rely=0.6,anchor=W)
#Pack the widgets in the home frame
home_label = Label(homeFrame, text="Team 1",font=("arial", 20))
home_label.grid(row=0, column=0,pady=20)
home_player1 = Entry(homeFrame,font=("arial", 20))
home_player1.grid(row=1, column=0,pady=10)
home_player2 = Entry(homeFrame,font=("arial", 20))
home_player2.grid(row=2, column=0,pady=10)
home_player3 = Entry(homeFrame,font=("arial", 20))
home_player3.grid(row=3, column=0,pady=10)
home_player4 = Entry(homeFrame,font=("arial", 20))
home_player4.grid(row=4, column=0,pady=10)
home_player5 = Entry(homeFrame,font=("arial", 20))
home_player5.grid(row=5, column=0,pady=10)


away_label = Label(awayFrame, text="Team 2",font=("arial", 20))
away_label.grid(row=0, column=1,pady=20)
away_player1 = Entry(awayFrame,font=("arial", 20))
away_player1.grid(row=1, column=1,pady=10)
away_player2 = Entry(awayFrame,font=("arial", 20))
away_player2.grid(row=2, column=1,pady=10)
away_player3 = Entry(awayFrame,font=("arial", 20))
away_player3.grid(row=3, column=1,pady=10)
away_player4 = Entry(awayFrame,font=("arial", 20))
away_player4.grid(row=4, column=1,pady=10)
away_player5 = Entry(awayFrame,font=("arial", 20))
away_player5.grid(row=5, column=1,pady=10)


#Define the submit button callback function
def submit_names():

#Get the names from the entry widgets
    home_names = (home_player1.get(), home_player2.get(), home_player3.get(), home_player4.get(), home_player5.get())
    away_names = (away_player1.get(), away_player2.get(), away_player3.get(), away_player4.get(), away_player5.get())
    

#Print the team names
    print(f"Home team: ",home_names)
    print(f"Away team: ",away_names)
    window.destroy()

#Create the button to submit the names
submit_button = Button(window, text="Submit",command = submit_names,width=20,height=2)
submit_button.grid()
submit_button.place(relx=0.45,rely=0.9)


window.attributes('-fullscreen',True)

window.mainloop()

##################################################################
import tkinter as tk



root = tk.Tk()
root.title("Basketball Scorecard")

scoreFrame=Frame(root,bg='black')

# Create labels for HOME and AWAY teams
home_label = tk.Label(scoreFrame, text="HOME", font=("Helvetica", 50),bg='black',fg='Blue')
away_label = tk.Label(scoreFrame, text="AWAY", font=("Helvetica", 50),bg='black',fg='Blue')

# Create variables to store score for HOME and AWAY teams
home_score = tk.IntVar()
away_score = tk.IntVar()

# Create label widgets to display score for HOME and AWAY teams
home_score_label = tk.Label(scoreFrame, textvariable=home_score, font=("Helvetica", 30),bg='black',fg='white')
away_score_label = tk.Label(scoreFrame, textvariable=away_score, font=("Helvetica", 30),bg='black',fg='white')

# Create buttons to increment scores for HOME and AWAY teams
home_score_button = tk.Button(scoreFrame, text="+", font=("Helvetica", 20), command=lambda: home_score.set(home_score.get() + 1))
away_score_button = tk.Button(scoreFrame, text="+", font=("Helvetica", 20), command=lambda: away_score.set(away_score.get() + 1))

# Create button to reset the scores
reset_button = tk.Button(scoreFrame, text="Reset", font=("Helvetica", 20), command=lambda: [home_score.set(0), away_score.set(0)])

# Use the grid layout manager to position the widgets
home_label.grid(row=0, column=0, pady=20,padx=100)
home_score_label.grid(row=1, column=0,)
#home_score_button.grid(row=0, column=2)
away_label.grid(row=0, column=1, pady=20,padx=100)
away_score_label.grid(row=1, column=1)
#away_score_button.grid(row=1, column=2)
#reset_button.grid(row=2, column=0, columnspan=3, pady=20)
scoreFrame.pack()

statsFrame=Frame(root,bg='white')
statsFrame.pack()
statsFrame.configure(width=100,height=30)
s=Label(statsFrame,text='TEAM STATS').pack()
root.configure(background='black')
root.attributes('-fullscreen',True)
root.mainloop()


