win=0
for i in range (6):
    if input()=="W":
        win=win+1
if win== 1 or win == 2:
    print(3)
elif win == 3 or win ==4:
    print(2)
elif win ==5 or win == 6:
    print(1)
else:
    print(-1)