for j in range(int(input())):
    words = input().split()
    for i,j in enumerate(words):
        if len(j)==4:
            words[i]="****"
    print(*words)