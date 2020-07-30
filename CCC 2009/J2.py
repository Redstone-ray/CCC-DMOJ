import sys
# Speed up input
input = sys.stdin.readline
# Initialize variables
a, b, c, d = int(input()), int(input()), int(input()), int(input())
#set counter
count = 0
# For i in range every possible solution
for i in range(d // a + 1):
    # For i in range every possible solution
    for j in range(d // b + 1):
        # For i in range every possible solution
        for k in range(d // c + 1):
            # If the total points are with in range and the solution is not 0
            # here i, j, k are the number of each type of fish possible
            if (a * i) + (b * j) + (c * k) <= d and i + j + k > 0:
                # print out the number of fish possible
                print(f"{i} Brown Trout, {j} Northern Pike, {k} Yellow Pickerel")
                # add one to counter
                count += 1
# sysout the number of ways possible
print('Number of ways to catch fish:', count)
