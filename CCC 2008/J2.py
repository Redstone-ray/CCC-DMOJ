import sys
def first_to_end():
    play_list.append(play_list[0])
    play_list.remove(play_list[0])
def swap():
    play_list[0], play_list[1] = play_list[1], play_list[0]
def end_to_first():
    play_list.insert(0, play_list.pop(4))
play_list = ["A", "B", "C", "D", "E"]
while True:
    a=int(input())
    b=int(input())
    if a==1:
        for i in range (b):
            first_to_end()
    elif a==2:
        for i in range (b):
            end_to_first()
    elif a==3:
        for i in range (b):
            swap()
    else:
        print(play_list[0],play_list[1],play_list[2],play_list[3],play_list[4])
        sys.exit(0)

