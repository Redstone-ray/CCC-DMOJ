a, b = map(int, input().split(":"))
time = a * 60 + b
for i in range(120):
    if 420 <= time < 600 or 900 <= time < 1140:
        time+=2
    else:
        time+=1
print(str(int(time / 60 % 24)).zfill(2) + ":" + str(time % 60).zfill(2))