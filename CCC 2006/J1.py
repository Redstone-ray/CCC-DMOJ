b = [461, 431, 420, 0]
s = [100, 57, 70, 0]
d = [130, 160, 118, 0]
de = [167, 266, 75, 0]
food = [b, s, d, de]
import sys
cal = 0
for i in range(4):
    a = int(input())
    cal += food[i][a - 1]
print("Your total Calorie count is "+str(cal)+".")
sys.exit(0)
