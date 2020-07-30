a=input()
import sys
chars = ["I", "O", "S", "H", "Z", "X", "N"]
for i in range (len(a)):
    if a[i] in chars:
        pass
    else:
        print("NO")
        sys.exit(0)
print("YES")