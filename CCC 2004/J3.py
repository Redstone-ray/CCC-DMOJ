N = int(input())
M = int(input())
adjectives = [input().strip() for i in range(N)]
nouns = [input().strip() for i in range(M)]
for adjective in adjectives:
    for noun in nouns:
        print(adjective + ' as ' + noun)