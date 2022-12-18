n=3
home={}
print('HOME TEAM')
for i in range(n):
    nameh=input('ENTER PLAYER NAME')
    home[nameh]={'points':0,'assists':0,'FGA':0,'FGM':0,'3PA':0,'3PM':0}


away={}
print('AWAY TEAM')
for i in range(n):
    namea=input('ENTER PLAYER NAME')
    away[namea]={'points':0,'assists':0,'FGA':0,'FGM':0,'3PA':0,'3PM':0}

print(home)
print(away)