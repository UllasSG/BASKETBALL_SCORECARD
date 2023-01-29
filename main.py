
######################################################################################################################

from tkinter import *
window=Tk()



home={}
away={}
homepoints=0
awaypoints=0
d={'Tuesday':{'points':10,'assists':5,'FGA':5,'FGM':3,'3PA':0,'3PM':8},'tanmay':{'points':60,'assists':50,'FGA':5,'FGM':0,'3PA':7,'3PM':0},'vihaan':{'points':45,'assists':0,'FGA':0,'FGM':0,'3PA':0,'3PM':0}}
def addplayer(team):
    name=input('ENTER NAME')
    team[name]={'points':0,'assists':0,'FGA':0,'FGM':0,'3PA':0,'3PM':0}



def FGp(team,player):#returns Field goal % as float
    if (team[player]['FGA'])==0:
        return 0
    fgp=((team[player]['FGM'])/(team[player]['FGA']))*100
    return round(fgp,2)

def points(team,player):#returns the points scored by the player as a float
    return team[player]['points']
    
def assists(team,player):#returns the assists scored by the player as a float
    return team[player]['assists']

def TSp(team,player): #returns True Shooting % as float
    tsp=((team[player]['points'])/(2*team[player]['FGA']))*100
    return round(tsp,2)
def Thrp(team,player):#returns 3 pointers made % as float
    if (team[player]['3PM'])==0:
        return 0
    tpm=((team[player]['3PM'])/(team[player]['3PA']))*100
    return round(tpm,2)


def teamFGp(team):    #Returns Team FG % as float
    teamFGA=0
    teamFGM=0
    for i in team:
        teamFGA+=team[i]['FGA']
        teamFGM+=team[i]['FGM']
    print('teamFGA',teamFGA)
    if teamFGA==0:
        return 0
    else:
        return round(((teamFGM/(teamFGA))*100),2)


def team3Pp(team):    # Returns Team 3P % as float
    team3PA=0
    team3PM=0
    for i in team:
        team3PA+=team[i]['3PA']
        team3PM+=team[i]['3PM']
    if team3PA==0:
        return 0
    else:
        return round(((team3PM/team3PA)*100),2)

def teamTSp(team):          # returns tream TS % as float
    teamPts=0
    teamFGA=0
    for i in team:
        teamPts+=team[i]['points']
        teamFGA+=team[i]['FGA']
    if teamFGA==0:
        return 0
    else :
        return round(((teamPts/(2*teamFGA))*100),2)


def TeamLeadPoints(team):
    return max(team,key=lambda x:team[x]['points'])

def TeamLeadAssists(team):
    return max(team,key=lambda x:team[x]['assists'])


################## INPUT PLAYS   ####################

#play=(team,player,2p/3p,made/miss,assisted,teamtotal)
play=(d,'vihaan',3,'Made','tanmay',homepoints)

def newplay(p):
    global homepoints
    p[0][p[1]]['FGA']+=1
    if p[3]=='Made':
        p[0][p[1]]['points']+=int(p[2])
        p[5].set(int(int(p[5].get())+int(p[2])))
        p[0][p[1]]['FGM']+=1
        p[0][p[4]]['assists']+=1
    if p[2]=='3':
        p[0][p[1]]['3PA']+=1
        if p[3]=='Made':
            p[0][p[1]]['3PM']+=1

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

homeTeam=[]
awayTeam=[]
#Define the submit button callback function
def submit_names(home_names,away_names):
    global home
    global away
    #Get the names from the entry widgets
    home_names = (home_player1.get(), home_player2.get(), home_player3.get(), home_player4.get(), home_player5.get())
    away_names = (away_player1.get(), away_player2.get(), away_player3.get(), away_player4.get(), away_player5.get())
    for i in home_names:
        home[i]={'points':0,'assists':0,'FGA':0,'FGM':0,'3PA':0,'3PM':0}
    for k in away_names:
        away[k]={'points':0,'assists':0,'FGA':0,'FGM':0,'3PA':0,'3PM':0}
    #Print the team names
    #print(f"Home team: ",home_names)
    #print(f"Away team: ",away_names)
    window.destroy()

#Create the button to submit the names
submit_button = Button(window, text="Submit",command =lambda :submit_names(homeTeam,awayTeam),width=20,height=2)
submit_button.grid()
submit_button.place(relx=0.45,rely=0.9)


window.attributes('-fullscreen',True)

window.mainloop()
print(homeTeam)
##################################################################
import tkinter as tk



root = tk.Tk()
root.title("Basketball Scorecard")

scoreFrame=Frame(root,bg='black')

possesion=['none']


def open_new_window():
    ###################################tany########################



    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    testlabel=tk.Label(new_window,text='add play')
    testlabel.grid()
    new_window.geometry("500x200")
  
    # Dropdown menu options
    playernames = [j for j in home]+[r for r in away]
  
    # datatype of menu text
    playerclicked = StringVar()
  
    # initial menu text
    playerclicked.set( "player name" )
  
    # Create Dropdown menu
    playerdrop = OptionMenu( new_window , playerclicked , *playernames )

    # Dropdown menu options
    shottype = [2,3]
    shotypeclicked = StringVar()
    shotypeclicked.set('Shot type')
    shottypedrop = OptionMenu( new_window , shotypeclicked , *shottype )

    result=['Made','Missed']
    resultclicked=StringVar()
    resultclicked.set('Result')
    resultdrop=OptionMenu(new_window,resultclicked,*result)

    assisted=[w for w in home]+[y for y in away]
    
    assistedclicked=StringVar()
    assistedclicked.set('Assisted by')
    assisteddrop=OptionMenu(new_window,assistedclicked,*assisted)
    #print('in open1',w)
    attemptLabel=Label(new_window,text='attempts a')
    assistedbyLabel=Label(new_window,text='assisted by')

    Team=['home','away']
    Teamclicked=StringVar()
    Teamclicked.set('Team')
    Teamdrop=OptionMenu(new_window,Teamclicked,*Team)
    def subPlay():
        global homepoints
        print(homepoints)
        pz=[playerclicked.get(),shotypeclicked.get(),resultclicked.get(),assistedclicked.get()]
        print(pz)
        if Teamclicked.get()=='home':
            pz.insert(0,home)
            pz.append(home_score)
        else:
            pz.insert(0,away)
            pz.append(away_score)
        
        newplay(pz)
        #home_score.set(home_score.get() + 2)
        #home_score_label.config(Text='fdsf')
        print(home)
        print(teamFGp(home))
        hfgpVar.set(str(teamFGp(home))+'%')
        afgpVar.set(str(teamFGp(away))+'%')
        htppVar.set(str(team3Pp(home))+'%')
        atppVar.set(str(team3Pp(away))+'%')
        htspVar.set(str(teamTSp(home))+'%')
        atspVar.set(str(teamTSp(away))+'%')
        hplVar.set(TeamLeadPoints(home)+' - '+str(points(home,TeamLeadPoints(home))))
        aplVar.set(TeamLeadPoints(away)+' - '+str(points(home,TeamLeadPoints(away))))    
        new_window.destroy()
        

        
        
    subBtn=Button(new_window,text='SUBMIT',command=subPlay)
    Teamdrop.grid(row=1,column=0)
    playerdrop.grid(row=1,column=1)
    attemptLabel.grid(row=1,column=2)
    shottypedrop.grid(row=1,column=3)
    resultdrop.grid(row=1,column=4)
    assistedbyLabel.grid(row=1,column=5)
    assisteddrop.grid(row=1,column=6)
    subBtn.grid()
      ###################################tany########################
    
    new_window.mainloop()
    
print(homepoints)

addplaybtn=tk.Button(scoreFrame,bg='white',fg='green',text=' + ',font=("Arial", 20),command=open_new_window)
addplaybtn.grid()
addplaybtn.place(relx=0.48,rely=0.55)



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
################tanmay#################
statsFrame=Frame(root,bg='white',background='black')
#statsFrame.config(width=500,height=100)
#statsFrame.place(relx=0.5,rely=0.9)

statsFrame.pack(padx=10,pady=10)
############################
hfgpVar=tk.StringVar()
hfgpVar.set(str(teamFGp(home))+'%')
afgpVar=tk.IntVar()
afgpVar.set(str(teamFGp(away))+'%')
htppVar=tk.IntVar()
htppVar.set(str(team3Pp(home))+'%')
atppVar=tk.StringVar()
atppVar.set(str(team3Pp(away))+'%')
htspVar=tk.StringVar()
htspVar.set(str(teamTSp(home))+'%')
atspVar=tk.StringVar()
atspVar.set(str(teamTSp(away))+'%')



###########################
s=Label(statsFrame,text='TEAM STATS',font=("Helvetica",40),fg='white',bg='black')
s.grid(row=0,column=1)
homeLabel=Label(statsFrame,text='HOME',font=("Helvetica", 30),fg='white',bg='black')
awayLabel=Label(statsFrame,text='AWAY',font=("Helvetica", 30),fg='white',bg='black')
FGLabel=Label(statsFrame,text="FG%",font=("Helvetica", 30),fg='white',bg='black')
TPLabel=Label(statsFrame,text="3P%",font=("Helvetica", 30),fg='white',bg='black')
TSLabel=Label(statsFrame,text="TS%",font=("Helvetica", 30),fg='white',bg='black')
hfgp=Label(statsFrame,textvariable=hfgpVar,font=("Helvetica", 30),fg='white',bg='black')
htpp=Label(statsFrame,textvariable=htppVar,font=("Helvetica", 30),fg='white',bg='black')
htsp=Label(statsFrame,textvariable=htspVar,font=("Helvetica", 30),fg='white',bg='black')
afgp=Label(statsFrame,textvariable=afgpVar,font=("Helvetica", 30),fg='white',bg='black')
atpp=Label(statsFrame,textvariable=atppVar,font=("Helvetica", 30),fg='white',bg='black')
atsp=Label(statsFrame,textvariable=atspVar,font=("Helvetica", 30),fg='white',bg='black')
homeLabel.grid(row=1,column=1,padx=10,pady=10)
awayLabel.grid(row=1,column=2,padx=10,pady=10)
FGLabel.grid(row=2,column=0,padx=10,pady=10)
TPLabel.grid(row=3,column=0,padx=10,pady=10)
TSLabel.grid(row=4,column=0,padx=10,pady=10)
hfgp.grid(row=2,column=1,padx=10,pady=10)
htpp.grid(row=3,column=1,padx=10,pady=10)
htsp.grid(row=4,column=1,padx=10,pady=10)
afgp.grid(row=2,column=2,padx=10,pady=10)
atpp.grid(row=3,column=2,padx=10,pady=10)
atsp.grid(row=4,column=2,padx=10,pady=10)
########################
hplVar=tk.StringVar()
aplVar=tk.StringVar()
halVar=tk.StringVar()
aalVar=tk.StringVar()
hplVar.set(TeamLeadPoints(home)+' - '+str(points(home,TeamLeadPoints(home))))
aplVar.set(TeamLeadPoints(away)+' - '+str(points(home,TeamLeadPoints(away))))        


##########################33
teamleaderFrame=Frame(root,bg='white',background='black')

teamleaderFrame.pack()

teamleaderLabel=Label(teamleaderFrame,text='TEAM LEADERS',font=("Helvetica", 30),fg='white',bg='black')
teamleaderLabel.grid(row=0,column=1)
home_label = tk.Label(teamleaderFrame, text="Home",font=("Helvetica", 30),fg='white',bg='black')
home_label.grid(row=1, column=1,padx=10,pady=8)

away_label = tk.Label(teamleaderFrame, text="Away",font=("Helvetica", 30),fg='white',bg='black')
away_label.grid(row=1, column=2,padx=10,pady=8)

home_points_label = tk.Label(teamleaderFrame, textvariable=hplVar,font=("Helvetica", 30),fg='white',bg='black')
home_points_label.grid(row=2, column=1,padx=10,pady=8)

home_assists_label = tk.Label(teamleaderFrame, text="bbb-2",font=("Helvetica", 30),fg='white',bg='black')
home_assists_label.grid(row=3, column=1,padx=10,pady=8)



away_points_label = tk.Label(teamleaderFrame, text="ddd-4",font=("Helvetica", 30),fg='white',bg='black')
away_points_label.grid(row=2, column=2,padx=10,pady=8)

away_assists_label = tk.Label(teamleaderFrame, text="eee-30",font=("Helvetica", 30),fg='white',bg='black')
away_assists_label.grid(row=3, column=2,padx=10,pady=8)


points_label = tk.Label(teamleaderFrame, text="Points",font=("Helvetica", 30),fg='white',bg='black')
points_label.grid(row=2, column=0,padx=10,pady=10)

assists_label = tk.Label(teamleaderFrame, text="Assists",font=("Helvetica", 30),fg='white',bg='black')
assists_label.grid(row=3, column=0,padx=10,pady=10)


###############
root.configure(background='black')
root.attributes('-fullscreen',True)

root.mainloop()


